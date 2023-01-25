from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    qst=topic.objects.all()
    qst=topic.objects.filter(topic_name='abcd')
    qst=topic.objects.order_by('topic_name')
    qst=topic.objects.order_by('-topic_name')
    qst=topic.objects.order_by(Length('topic_name'))
    qst=topic.objects.order_by(Length('topic_name').desc())
    qst=topic.objects.exclude(topic_name='class')
    d={'topics':qst}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    qsw=webpage.objects.all()
    qsw=webpage.objects.filter(name='abi')
    qsw=webpage.objects.order_by('name')
    qsw=webpage.objects.order_by('-name')
    qsw=webpage.objects.order_by(Length('name'))
    qsw=webpage.objects.order_by(Length('name').desc())
    qsw=webpage.objects.exclude(name='kupp')
    d={'webpage':qsw}
    return render(request,'display_webpage.html',d)

def records(request):
    qsa=accessrecords.objects.all()
    qsa=accessrecords.objects.filter(name='2')
    qsa=accessrecords.objects.order_by('date')
    qsa=accessrecords.objects.order_by('-date')
    qsa=accessrecords.objects.order_by(Length('name'))
    qsa=accessrecords.objects.order_by(Length('name').desc())
    qsa=accessrecords.objects.exclude(name='5')
    d={'arecords':qsa}
    return render(request,'records.html',d)