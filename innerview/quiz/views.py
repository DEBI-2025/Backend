from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Field, Level, Topic, Question,Quiz,Choice
from .serializers import FieldSerializer, LevelSerializer, TopicSerializer, QuestionSerializer,QuizSerializer,ChoiceSerializer,ReceivedAnswerSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from .geminiAPI import geminiAPI,quizGeminiAPI
import json
# List all available fields
class FieldListView(generics.ListAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated]

# List all available levels
class LevelListView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [IsAuthenticated]

# List topics based on field selection
class TopicListView(generics.ListAPIView):
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        field_id = self.request.query_params.get('field_id')
        if field_id:
            return Topic.objects.filter(field_id=field_id)
        return Topic.objects.all()

class QuizListView(generics.ListAPIView):
    serializer_class=QuizSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        required_params  = ['field', 'topic', 'level']
        missing = [param for param in required_params if not self.request.GET.get(param)]
        if missing:
            raise ValidationError({'error': f"Missing query parameters: {', '.join(missing)}"})
        try :
            field=Field.objects.get(name=self.request.GET.get('field'))
            level=Level.objects.get(name=self.request.GET.get('level'))   
            topic=Topic.objects.get(name=self.request.GET.get('topic'))

        except (Field.DoesNotExist, Level.DoesNotExist, Topic.DoesNotExist) as e:
            raise ValidationError({'error': str(e)})
        
        queryset = Quiz.objects.filter(field__id=field.pk,topic__id=topic.pk,level__id=level.pk)
        if not queryset.exists():
            api_key="AIzaSyDbgILxNKc0RZjgER7LK-SpKVU4X7HFkyI"

            newQs=quizGeminiAPI(api_key,field.name,level.name,topic.name)['questions']
            for newQ in newQs:
                newQ['topic']=topic.pk
                newQ['field']=field.pk
                newQ['level']=level.pk
                serializer = QuizSerializer(data=newQ)
                print(newQ)
                if serializer.is_valid():
                    serializer.save() 
            queryset = Quiz.objects.filter(field_id=field.pk,topic_id=topic.pk,level_id=level.pk)
        
        return queryset
# Fetch questions based on selected field, level, and topic
class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        required_params  = ['field', 'topic', 'level']
        missing = [param for param in required_params if not self.request.GET.get(param)]
        if missing:
            raise ValidationError({'error': f"Missing query parameters: {', '.join(missing)}"})
        
        field=Field.objects.get(name=self.request.GET.get('field'))
        level=Level.objects.get(name=self.request.GET.get('level'))   
        topic=Topic.objects.get(name=self.request.GET.get('topic'))
     
        queryset = Question.objects.filter(field__id=field.pk,topic__id=topic.pk,level__id=level.pk)
        if (queryset.count() ==0):
            api_key="AIzaSyDbgILxNKc0RZjgER7LK-SpKVU4X7HFkyI"

            newQs=geminiAPI(api_key,field.name,level.name,topic.name)['questions']
            for newQ in newQs:
                Question.objects.create(text=newQ['text'],answer=newQ['answer'],field=field,topic=topic,level=level)  
            queryset = Question.objects.filter(field_id=field.pk,topic_id=topic.pk,level_id=level.pk)
        

        return queryset

class GetScore(APIView):

    def post(self,request):
        serializer = ReceivedAnswerSerializer(data=request.data ,many=True)
        if serializer.is_valid():
            
            answers=serializer.validated_data
            score=0
            QuestionsNum=len(answers)
            reponse_data={}
            reponse_data['answers']=[]
            for answer in answers:
                text=answer['text']
                question=Quiz.objects.get(text=text)
                user_choice = question.choices.get(label=answer['choices']['label'])
                if (user_choice.is_correct):
                    score+=1
                reponse_data['answers'].append(
                    {
                        'text': text,
                        'staus': "correct" if user_choice.is_correct else "wrong",
                        'correct_label' : str(question.choices.get(is_correct=True).label),
                        'correct_choice_text' : str(question.choices.get(is_correct=True).choice_text),
                        'answer_reason' : str(question.answer_reason),
                    }
            )
            pct=(score/QuestionsNum)*100
            reponse_data['result'] = "Pased" if  pct > 60 else "Failed"
            reponse_data['Score']= str(pct) + "%"
            return Response(reponse_data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
