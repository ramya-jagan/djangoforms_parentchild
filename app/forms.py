from django import forms
from app.models import *

class TopicForm(forms.Form):
  topic_name=forms.CharField()

class WebpageForm(forms.Form):
  tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()] 
  topic_name=forms.ChoiceField(choices=tl) 
  name=forms.CharField()
  email=forms.EmailField()
  url=forms.URLField()

class AccessRecordForm(forms.Form):
  wl=[[wo.pk,wo.name] for wo in Webpage.objects.all()] 
  name=forms.ChoiceField(choices=wl) 
  author=forms.CharField()
  date=forms.DateField()
