from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from .models import UserAccountManager , UserAccount  
from django.contrib.auth.hashers import make_password
# Create your tests here.

class  AuthAPITestCase(APITestCase):
    def setUp(self):
        self.user = UserAccount.objects.create(email="hamdy@gmail.com",first_name="Abdelrhman",last_name="Hamdy",date_of_birth="1997-2-1",phone="01551343021",password=make_password("Hello@523"))
        self.login_url="/auth/jwt/create"
        self.sign_up_url= "/auth/users/"
        self.create_refresh_token_url="/auth/jwt/refresh/"
        
    def test_create_user_and_login(self):
        data= {
            "first_name":"ziad",
            "last_name":"mohamed",
            "email":"ziad.mohamed@gmail.com",
            "date_of_birth":"2000-1-1",
            "phone":"01551343021",
            "password":"Ziad@2000",
            "re_password":"Ziad@2000"
        }
        response=self.client.post(path=self.sign_up_url,data=data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
 
        self.assertEqual(UserAccount.objects.count(),2)

        data= {"email":"ziad.mohamed@gmail.com","password":"Ziad@2000"}
        response=self.client.post(path=self.login_url,data=data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        

    def test_create_user_with_missing_data(self):
        data= {
            "first_name":"ziad",
            #"last_name":"mohamed",
            "email":"ziad.mohamed@gmail.com",
            "date_of_birth":"2000-1-1",
            "phone":"01551343021",
            "password":"Ziad@2000",
            "re_password":"Ziad@2000"
        }
        

        responce=self.client.post(path=self.sign_up_url,data=data,format='json')
        self.assertEqual(responce.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(UserAccount.objects.count(),1)

    def test_user_login_with_wrong_password(self):
        self.assertEqual(UserAccount.objects.count(),1)
        data= {
            "email":"hamdy@gmail.com",
            "password": "Hello@985"
        }
        response=self.client.post(path=self.login_url,data=data,format='json')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
    
    def test_create_refresh_token(self):        
        data= {
            "email":"hamdy@gmail.com",
            "password": "Hello@523"
        }
        response=self.client.post(path=self.login_url,data=data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        data={
            "refresh": str(response.data['refresh'])
        } 
        response=self.client.post(path=self.create_refresh_token_url,data=data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)