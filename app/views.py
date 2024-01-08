from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse 
# Create your views here.
def insert_topic(request):
  TWFO=TopicForm()
  d={'TWFO':TWFO}
  if request.method=='POST':
    TWO=TopicForm(request.POST)
    if TWO.is_valid():
      tn=TWO.cleaned_data['topic_name']
      TO=Topic.objects.get_or_create(topic_name=tn)[0]
      TO.save()
    return HttpResponse('data inserted successfully')

  return render(request,'insert_topichtml.html',d)    


def insert_webpage(request):
  EWFO=WebpageForm()
  d={'EWFO':EWFO}
  if request.method=='POST':
    WFDO=WebpageForm(request.POST)
    if WFDO.is_valid():
      tn=WFDO.cleaned_data['topic_name']
      TO=Topic.objects.get(topic_name=tn)
      n=WFDO.cleaned_data['name']
      e=WFDO.cleaned_data['email']
      u=WFDO.cleaned_data['url']
      WO=Webpage.objects.get_or_create(topic_name=TO,name=n,email=e,url=u)[0]
      WO.save()
      
      QLWO=Webpage.objects.all()
      d1={'webpages':QLWO}
      return render(request,'webpage_data.html',d1)
  return render(request,'insert_webpagehtml.html',d)  


def insert_access(request):
    ARFO=AccessRecordForm()
    d={'ARFO':ARFO}
    if request.method=='POST':
      ARO=AccessRecordForm(request.POST)
      if ARO.is_valid():
        na=ARO.cleaned_data['name']
        WO=Webpage.objects.get(pk=na)
        a=ARO.cleaned_data['author']
        d=ARO.cleaned_data['date']
        AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
        AO.save()

        
        return HttpResponse("insert_data success")
    return render(request,'insert_accessrecord.html',d)    


   