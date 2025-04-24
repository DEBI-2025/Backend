from rest_framework import serializers
from .models import Field, Level, Topic, Question,Choice,Quiz

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

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Choice
        fields = ['label', 'choice_text']

class QuizSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    field = serializers.PrimaryKeyRelatedField(queryset=Field.objects.all(),write_only=True)
    topic = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(),write_only=True)
    level = serializers.PrimaryKeyRelatedField(queryset=Level.objects.all(),write_only=True)
    answer_reason = serializers.CharField(write_only=True)
    class Meta:
        model=Quiz 
        fields = ['text', 'answer_reason', 'choices','field','topic','level']
    def create(self,validated_data):
        print(validated_data)
        choices_data = validated_data.pop("choices")

        quiz_question=Quiz.objects.create(**validated_data)

        for choice_data in choices_data:
            Choice.objects.create(quiz_question=quiz_question,**choice_data)
        
        return quiz_question
class ReceivedAnswerSerializer(serializers.Serializer):
    choices = ChoiceSerializer()
    #text = serializers.CharField(read_only=True)
    text = serializers.CharField()