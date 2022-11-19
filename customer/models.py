import datetime
from django.db import models
import random
import string
import uuid 
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Random String Generate
random_string = ''.join(random.choices(string.ascii_uppercase +string.digits, k=7))

class CustomerManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Must have a email address.")
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Customer
class Customer(AbstractBaseUser,PermissionsMixin):
    first_name  =   models.CharField(max_length=50,blank=True,null=True)
    last_name   =   models.CharField(max_length=50,blank=True,null=True)
    email       =   models.EmailField(max_length=50,unique=True)
    phone       =   models.IntegerField(unique=True)
    is_active   =   models.BooleanField(default=True)
    is_staff    =   models.BooleanField(default=False)
    is_admin    =   models.BooleanField(default=False)
    unique_id   =   models.CharField(max_length=8,default=uuid.uuid4().hex[:6].upper())
    profile     =   models.ImageField(upload_to='media/profile/',default='media/profile/avatar.png')
    update_at   =   models.DateField(default=datetime.date.today)
    created_at  =   models.DateField(default=datetime.date.today)
    object      =   CustomerManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = ("Customer")


# State
class State(models.Model):
    name            =       models.CharField(max_length=100,blank=True,null=True)
    is_active       =       models.BooleanField(default=True)
    update_at       =       models.DateField(default=datetime.date.today)
    created_at      =       models.DateField(default=datetime.date.today)  

    class Meta:
        verbose_name = ("State")

    def __str__(self):
        return self.name


# Shipping Address
class ShippingAddress(models.Model):
    customer        =       models.ForeignKey(Customer,on_delete=models.CASCADE)
    state           =       models.ForeignKey(State,on_delete=models.CASCADE)
    dist            =       models.CharField(max_length=50)
    address         =       models.CharField(max_length=250)
    pincode         =       models.IntegerField()
    is_active       =       models.BooleanField(default=True)
    update_at       =       models.DateField(default=datetime.date.today)
    created_at      =       models.DateField(default=datetime.date.today) 


    class Meta:
        verbose_name = ("Customer Shipping Address")

    def __str__(self):
        return self.name



#  Token For Forgot Password and Verification
class ValidationToken(models.Model):
    customer        =       models.ForeignKey(Customer,on_delete=models.CASCADE)
    type            =       models.CharField(max_length=50)
    token           =       models.CharField(max_length=50,default=uuid.uuid1().hex[:20])
    is_active       =       models.BooleanField(default=True)
    update_at       =       models.DateField(default=datetime.date.today)
    created_at      =       models.DateField(default=datetime.date.today) 


    class Meta:
        verbose_name = ("Customer Shipping Address")

    def __str__(self):
        return self.name

