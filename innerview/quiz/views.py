from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Field, Level, Topic, Question
from .serializers import FieldSerializer, LevelSerializer, TopicSerializer, QuestionSerializer
from rest_framework.exceptions import ValidationError
from .geminiAPI import geminiAPI
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