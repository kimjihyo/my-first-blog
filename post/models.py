from django.db import models
from django.utils import timezone
from django.urls import reverse



class Post(models.Model):
    

    subject = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)

    def get_absolute_url(self):
        return reverse('post:ViewPost', kwargs={'pk': self.pk})

    def __str__(self):
        return  self.subject + " - " + self.author