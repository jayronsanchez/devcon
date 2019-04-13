from django.db import models
from django.urls import reverse

# Create your models here.
class Jokes(models.Model):  
    joke_title = models.CharField(max_length=256)
    joke = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:create_joke')

    def __str__(self):
        return self.joke_title