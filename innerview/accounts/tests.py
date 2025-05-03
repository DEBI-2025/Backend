from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from .models import UserAccountManager , UserAccount  
# Create your tests here.

class  AuthAPITestCase(APITestCase):
    def setUp(self):
        #return super().setUp()
        pass
    def test_create_user_and_login(self):
        URL= "/auth/users/"
        data= {
            "first_name":"ziad",
            "last_name":"mohamed",
            "email":"ziad.mohamed@gmail.com",
            "date_of_birth":"2000-1-1",
            "phone":"01551343021",
            "password":"Ziad@2000",
            "re_password":"Ziad@2000"
        }
        responce=self.client.post(path=URL,data=data,format='json')
        self.assertEqual(responce.status_code,status.HTTP_201_CREATED)
        self.assertEqual(UserAccount.objects.count(),1)

        login_url="/auth/jwt/create"
        data= {"email":"ziad.mohamed@gmail.com","password":"Ziad@2000"}
        user=UserAccount.objects.get(email="ziad.mohamed@gmail.com")
        user.is_active=True
        user.save()
        response=self.client.post(path=login_url,data=data,format='json')
        #print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        

    def test_create_user_with_missing_data(self):
        URL= "/auth/users/"
        data= {
            "first_name":"ziad",
            "last_name":"mohamed",
            #"email":"ziad.mohamed@gmail.com",
            "date_of_birth":"2000-1-1",
            "phone":"01551343021",
            "password":"Ziad@2000",
            "re_password":"Ziad@2000"
        }
        

        responce=self.client.post(path=URL,data=data,format='json')
        self.assertEqual(responce.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(UserAccount.objects.count(),0)

    # def test_user_login(self):
    #     self.user = UserAccount.objects.create(email="hamdy@gmail.com",first_name="Abdelrhman",last_name="Hamdy",date_of_birth="1997-2-1",phone="01551343021",password="Hello@523")
    #     self.assertEqual(UserAccount.objects.count(),1)
    #     print("User Acyive :   ",UserAccount.objects.get().is_active)
    #     login_url="/auth/jwt/create"
    #     data= {
    #         "email":"hamdy@gmail.com",
    #         "password": "Hello@523"
    #     }
    #     response=self.client.post(path=login_url,data=data,format='json')
    #     print(response.json)
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)
        