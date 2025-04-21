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
        
        
        field_id = self.request.GET.get('field_id')
        topic_id = self.request.GET.get('topic_id')
        level_id = self.request.GET.get('level_id')
        if  (not field_id or not topic_id or not level_id):
            raise ValidationError({'Error': "Missing field or Topic or level query parameter"})
        
        
        queryset = Question.objects.filter(field_id=field_id,topic_id=topic_id,level_id=level_id)
        if (queryset.count() ==0):
            api_key="AIzaSyDbgILxNKc0RZjgER7LK-SpKVU4X7HFkyI"
            field=Field.objects.get(id=field_id)
            level=Level.objects.get(id=level_id)
            topic=Topic.objects.get(id=topic_id)
            newQs=geminiAPI(api_key,field.name,level.name,topic.name)['questions']
            for newQ in newQs:
                Question.objects.create(text=newQ['text'],answer=newQ['answer'],field_id=field_id,topic_id=topic_id,level_id=level_id)  
            queryset = Question.objects.filter(field_id=field_id,topic_id=topic_id,level_id=level_id)
        

        return queryset