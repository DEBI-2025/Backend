from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
import sys
sys.path.append('../accounts')
from accounts.models import UserAccountManager , UserAccount  
from .models import Question, Quiz, Choice , Field, Level, Topic
from django.contrib.auth.hashers import make_password
# Create your tests here.

class FieldTestCase(APITestCase):
    def setUp(self):
        Field.objects.create(name="Software Engineering")
        Field.objects.create(name="Cyber Security")
        self.user = UserAccount.objects.create(email="hamdy@gmail.com",first_name="Abdelrhman",last_name="Hamdy",date_of_birth="1997-2-1",phone="01551343021",password=make_password("Hello@523"))
        self.login_url="/auth/jwt/create"
        self.field_url="/api/fields/"
        data={
            'email':"hamdy@gmail.com",
            'password':"Hello@523"
        }
        response=self.client.post(path=self.login_url,data=data,format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {response.data['access']}')
    def test_get_fields(self):
        self.client.force_login(user=self.user)
        response=self.client.get(path=self.field_url)
        self.assertEqual(len(response.data),2)    
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_get_field_without_authentication(self):
        self.client.credentials()
        response=self.client.get(path=self.field_url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_get_field_after_Deletion(self):
        Field.objects.get(name="Software Engineering").delete()
        response=self.client.get(path=self.field_url)
        self.assertEqual(len(response.data),1)    
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class TopicsTestCase(APITestCase):
    def setUp(self):
        self.field_topic_list=[{"Software Engineering":['DevOps','Front End','Back End']},
        {"Cyber Security":['Security Analyst','Security Engineer','Penetration Tester']},
        {"Data Science":['Data Scientist','Machine Learning Engineer','Data Engineer']}]

        for field_topic in self.field_topic_list:
            field_name=list(field_topic.keys())[0]
            field=Field.objects.create(name=field_name)
            for topic in list(field_topic.values())[0]:
                Topic.objects.create(name=topic,field=field) 
                
        self.user = UserAccount.objects.create(email="hamdy@gmail.com",first_name="Abdelrhman",last_name="Hamdy",date_of_birth="1997-2-1",phone="01551343021",password=make_password("Hello@523"))
        self.login_url="/auth/jwt/create"
        self.topic_url="/api/topics/"
        data={
            'email':"hamdy@gmail.com",
            'password':"Hello@523"
        }
        response=self.client.post(path=self.login_url,data=data,format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {response.data['access']}')

    def test_get_topics(self):
        self.client.force_login(user=self.user)
        response=self.client.get(path=self.topic_url)    
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),9) 
    
    def test_get_topics_with_query_parameter(self):
        self.client.force_login(user=self.user)
        response=self.client.get(self.topic_url,{'field_id': '1'})    
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        for i in range(len(response.data)) :
            self.assertEqual(response.data[i]['name'],self.field_topic_list[0]["Software Engineering"][i])
                
        self.assertEqual(len(response.data),3) 
    
    def test_get_topics_with__wrong_query_parameter(self):
        self.client.force_login(user=self.user)
        response=self.client.get(self.topic_url,{'field_id': '10'})
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_get_topics_without_authentication(self):
        self.client.credentials()
        response=self.client.get(path=self.topic_url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

class LevelsTestCase(APITestCase):
    def setUp(self):
        self.level_names=['Entry','Intermidiate','Advanced']
        for level_name in self.level_names: 
            Level.objects.create(name=level_name)
        self.user = UserAccount.objects.create(email="hamdy@gmail.com",first_name="Abdelrhman",last_name="Hamdy",date_of_birth="1997-2-1",phone="01551343021",password=make_password("Hello@523"))
        self.login_url="/auth/jwt/create"
        self.levels_url="/api/levels/"
        data={
            'email':"hamdy@gmail.com",
            'password':"Hello@523"
        }
        response=self.client.post(path=self.login_url,data=data,format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {response.data['access']}')

    def test_get_levels(self):
        self.client.force_login(user=self.user)
        response=self.client.get(path=self.levels_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),3)
        print(response.data)
        for i in range(3):
            self.assertEqual(self.level_names[i],response.data[i]['name'])

    
    def test_get_levels_without_authentication(self):
        self.client.credentials()
        response=self.client.get(path=self.levels_url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
    
class QuestionsTestCase(APITestCase):
    def setUp(self):
        self.user = UserAccount.objects.create(email="hamdy@gmail.com",first_name="Abdelrhman",last_name="Hamdy",date_of_birth="1997-2-1",phone="01551343021",password=make_password("Hello@523"))
        self.login_url="/auth/jwt/create"
        self.questions_url="/api/questions/"
        data={
            'email':"hamdy@gmail.com",
            'password':"Hello@523"
        }
        response=self.client.post(path=self.login_url,data=data,format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {response.data['access']}')


