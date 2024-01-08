from django.db import models
from app.models import *

# Create your models here.

class Topic(models.Model):
  topic_name=models.CharField(max_length=100,primary_key=True)


class Webpage(models.Model):
  topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)  
  name=models.CharField(max_length=100)
  email=models.EmailField()
  url=models.URLField()


class AccessRecord(models.Model):
  name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
  author=models.CharField(max_length=100)
  date=models.DateField()