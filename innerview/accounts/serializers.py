from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta : 
        model = User
        fields = ['id','email','first_name','last_name','date_of_birth','phone','password','level']
        extra_kwargs = {'password': {'write_only': True}} # Prevents password from being exposed in API responses.