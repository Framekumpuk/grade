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
        credit = request.POST['credit']
    except:
        error_message = 1
        subject = ""
        score = 0
        full = 1
        credit = 0
    else:        
            equation = float(score)*100/float(full)
            net = ("%.2f" % round(equation,2))
            if float(net) < 0.0:
                grade = 'Null'
            elif float(net) < 50.0:
                grade = 'F'
            elif float(net) < 55.0:
                grade = 'D'
            elif float(net) < 60.0:
                grade = 'D+'
            elif float(net) < 65.0:
                grade = 'C'
            elif float(net) < 70.0:
                grade = 'C+'
            elif float(net) < 75.0:
                grade = 'B'
            elif float(net) < 80.0:
                grade = 'B+'
            elif float(net) >= 80.0:
                grade = 'A'
            elif float(net) > 100.0:
                grade = 'Null'
            information = Grade(subject=subject, score=score, full=full, total=net, grade=grade, credit=credit)
            information.save()
    # user hits the Back button.
    return render(request,"grade/detail.html",'')

def show(request):
    subject_list = Grade.objects.all()
    # Calculate balance of paylist.
    return render(request,"grade/show.html",{'subject_list':subject_list})
