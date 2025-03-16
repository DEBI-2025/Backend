from rest_framework import serializers
from .models import Field, Level, Topic, Question

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    field = FieldSerializer(read_only=True)
    class Meta:
        model = Topic
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    field = FieldSerializer(read_only=True)
    topic = TopicSerializer(read_only=True)
    level = LevelSerializer(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'