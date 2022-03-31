from os import F_OK
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

# class User(AbstractUser):
#     def __repr__(self):
#         return f"<User username={self.username}>"

#     def __str__(self):
#         return self.username

class Movie(models.Model):
    # title = 
    # created = datetime
    # watched = bool
    # user = Fk

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()

class List(models.Model):
    # name = char
    # user = fk

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()

class Category(models.Model):
    # name = char
    # list =fk
    # user = fk

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()