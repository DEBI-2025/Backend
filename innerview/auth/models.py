from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class  UserAccountManager(BaseUserManager):

    def create_user(self,email,first_name,last_name,date_of_birth,phone,password=None):
        if not email : 
            raise ValueError("Users must have an email address !!")
        email=self.normalize_email(email)
        user = self.model(email=email ,first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,phone=phone)
        user.set_passowrd(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,first_name,last_name,date_of_birth,phone,password=None):
        user=self.create_user(email,first_name,last_name,date_of_birth,phone,password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    date_of_birth= models.DateField()
    phone = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['first_name','last_name','date_of_birth','phone']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return self.last_name
    def __str__(self):
        return self.email
