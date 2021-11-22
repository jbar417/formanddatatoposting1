from django.db import models

# Create your models here.
class CommentData(models.Model):
  name = models.CharField(max_length=30)
  email = models.CharField(max_length=50)
  comment = models.TextField()