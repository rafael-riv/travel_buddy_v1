from django.db import models
import re
import datetime
from datetime import date

from django.db.models import deletion

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['name']) < 2:
            errors['firstname_len'] = "nombre debe tener al menos 2 caracteres de largo";

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "correo invalido"

        if not SOLO_LETRAS.match(postData['name']):
            errors['solo_letras'] = "solo letras en nombreporfavor"

        if len(postData['password']) < 8:
            errors['password'] = "contraseña debe tener al menos 8 caracteres";

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "contraseña y confirmar contraseña no son iguales. "

        
        return errors

class TripsManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if datetime.datetime.strptime(postData['start_date'], "%Y-%m-%d").date() <= datetime.date.today():
            errors['wrong_start_date'] = "Travel dates should be future-dated"
        if datetime.datetime.strptime(postData['end_date'], "%Y-%m-%d").date() <= datetime.datetime.strptime(postData['start_date'], "%Y-%m-%d").date():
            errors['wrong_end_date'] = "Travel Date To should not be before the Travel Date From"
        if len(postData['description_plan']) <= 1:
            errors['empty_plan'] = "You should describe your trip plan"
        return errors


class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=CHOICES)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

class Viaje(models.Model):
    destination = models.CharField(max_length=100)
    travel_star = models.DateField()
    travel_end = models.DateField()
    plan = models.CharField(max_length=255)
    owner_user = models.ForeignKey(User, related_name= "own_trips", on_delete= models.CASCADE)
    user = models.ManyToManyField(User, related_name="trip")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripsManager()




