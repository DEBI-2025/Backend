from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()  
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()  
        category = self.request.query_params.get('category')

        if category:
            queryset = queryset.filter(category__iexact=category)

        return queryset
