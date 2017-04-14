from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Grade
import csv


def index(request):
    return render(request,"grade/index.html",'')

def operand(request):
    error_message = 0 
    try:
        subject = request.POST['subject']
        score = request.POST['score']
        full = request.POST['full']
    except:
        error_message = 1
        subject = ""
        score = 0
        full = 1
    else:        
            a = float(score)*100/float(full)
            information = Grade(subject=subject, score=score, full=full, total=a)
            information.save()
    # user hits the Back button.
    return render(request,"grade/detail.html",'')

def show(request):
    subject_list = Grade.objects.all()
    # Calculate balance of paylist.
    return render(request,"grade/show.html",{'subject_list':subject_list})
