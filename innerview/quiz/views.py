from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Field, Level, Topic, Question
from .serializers import FieldSerializer, LevelSerializer, TopicSerializer, QuestionSerializer

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
        field_id = self.request.query_params.get('field_id')
        topic_id = self.request.query_params.get('topic_id')
        level_id = self.request.query_params.get('level_id')

        queryset = Question.objects.all()

        if field_id:
            queryset = queryset.filter(field_id=field_id)
        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)
        if level_id:
            queryset = queryset.filter(level_id=level_id)

        return queryset