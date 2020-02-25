from django.db import models
from django.core.validators import (
    EmailValidator,
    MaxValueValidator,
    MinValueValidator,
    URLValidator,
    validate_slug
)
from main.validators import validate_even_number
# Create your models here.
# every table in database is represented as a class
class Student(models.Model):
    GENDERS = (
        ('f','Female'),
        ('m','Male'),
        ('u','Undisclosed')
    )
    name = models.CharField(max_length = 100)
    roll_number = models.IntegerField(unique = True)
    address = models.TextField(null=True)
    phone_number = models.CharField(max_length = 15,null=True)
    email = models.CharField(max_length=100,null=True,validators = [EmailValidator("Email address is not valid")])
    gender = models.CharField(max_length = 1,choices = GENDERS,null=True)
    age = models.IntegerField(
        null=True,
        validators=[
            MaxValueValidator(150),
            MinValueValidator(0),
            validate_even_number
        ]
    )
    slug = models.CharField(max_length = 100, validators=[validate_slug],null=True)

    def __str__(self):
        return self.name