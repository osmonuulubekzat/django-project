from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    publishingdate = models.DateTimeField()
    def __str__(self):
        return  self.title
