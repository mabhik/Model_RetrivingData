from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topic(request):
    qst=topic.objects.all()
    qst=topic.objects.filter(topic_name='abcd')
    qst=topic.objects.order_by('topic_name')
    qst=topic.objects.order_by('-topic_name')
    qst=topic.objects.order_by(Length('topic_name'))
    qst=topic.objects.order_by(Length('topic_name').desc())
    qst=topic.objects.exclude(topic_name='class')
    qst=topic.objects.filter(topic_name__startswith='c')
    qst=topic.objects.filter(topic_name__endswith='t')
    qst=topic.objects.filter(topic_name__contains='a')
    qst=topic.objects.filter(topic_name='class').delete()
    qst=topic.objects.all()
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
    qsw=webpage.objects.filter(name__startswith='a')
    qsw=webpage.objects.filter(name__endswith='a')
    qsw=webpage.objects.filter(name__in=['abhi','kupp','katt','madhu'])
    qsw=webpage.objects.all()
    qsw=webpage.objects.filter(Q(topic_name='cricket')|Q(name='abcd'))
    qsw=webpage.objects.filter(Q(topic_name='cricket')&Q(name='abcd'))
    qsw=webpage.objects.filter(topic_name='cricket').update(name='anjiu')
    qsw=webpage.objects.filter(name='kupp').update(topic_name='volleyball')
    qsw=webpage.objects.all()
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
    qsa=accessrecords.objects.filter(date__month='8')
    qsa=accessrecords.objects.filter(date__year='2022')
    qsa=accessrecords.objects.filter(date__year__gte='2022')
    d={'arecords':qsa}
    return render(request,'records.html',d)