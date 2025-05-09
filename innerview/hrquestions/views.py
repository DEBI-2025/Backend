#from rest_framework import viewsets
from rest_framework import generics, viewsets 
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny
import sys,os
sys.path.append('../quiz')
from quiz.geminiAPI import HrQuestionsGeminiAPI
from dotenv import load_dotenv
from rest_framework.response import Response

load_dotenv()
#viewsets.ModelViewSet
class QuestionViewSet(generics.ListAPIView): 
    queryset = Question.objects.all()  
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]  # Change to AllowAny if you want to allow unauthenticated access

    def get_queryset(self):
        queryset = super().get_queryset()  
        category = self.request.query_params.get('category')

        if category and category in ["HR","Behavioral"]:
            queryset = queryset.filter(category__iexact=category)


        return queryset
    def list(self, request, *args, **kwargs):
        queryset= self.get_queryset()
        
        if not queryset.exists():
            generatedHrQuestions=HrQuestionsGeminiAPI(os.getenv("api_key"))
            serializer=self.get_serializer(data=generatedHrQuestions['questions'],many=True)
            if serializer.is_valid():
                serializer.save()
        serializer=self.get_serializer(queryset,many=True)

        return Response(serializer.data)