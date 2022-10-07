from tabnanny import verbose
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now = True)
    text = models.TextField()

    def __str__(self):
        return self.title
