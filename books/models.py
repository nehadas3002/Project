from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.utils import timezone
from django.db.models.query_utils import Q
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class User(AbstractUser):
    pass

class NewBook(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    cover = models.URLField(max_length=400)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    synopsis = models.CharField(max_length=400, default=None)
    
    def __str__(self):
        return f"{self.title}, {self.id}"

class Read(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(NewBook, blank=True, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.user}, {self.book.title}"

class Reading(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(NewBook, blank=True, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.user}, {self.book.title}"

class Rating(models.Model):
    book = models.ForeignKey(NewBook, blank=True, on_delete=models.CASCADE, default=None)
    rating = models.IntegerField(default=0, 
        validators=[
            MaxValueValidator(5), 
            MinValueValidator(0)
        ]
    )

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rating}, {self.book.title}, {self.user.username}"

class Comment(models.Model):
    book = models.ForeignKey(NewBook, blank=True, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400, default=None)



    