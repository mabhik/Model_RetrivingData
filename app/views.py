from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topic(request):
    qst=topic.objects.all()
    d={'topics':qst}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    qsw=webpage.objects.all()
    d={'webpage':qsw}
    return render(request,'display_webpage.html',d)

def records(request):
    qsa=accessrecords.objects.all()
    d={'arecords':qsa}
    return render(request,'records.html',d)