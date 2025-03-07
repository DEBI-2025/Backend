from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

User = get_user_model()

class ActivateUserView(APIView):
    def get(self, request, uid, token):
        try:
            uid = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError):
            return Response({"error": "Invalid activation link"}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"message": "Your account has been activated successfully!"}, status=status.HTTP_200_OK)
        
        return Response({"error": "Activation link is invalid or expired"}, status=status.HTTP_400_BAD_REQUEST)
