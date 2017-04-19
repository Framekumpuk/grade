from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Grade
import math
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
        credit = 1
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
    keep_grade = ['A','B+','B','C+','C','D+','D','F']
    grade_keep = [4,3.5,3,2.5,2,1.5,1,0]
    grade_alp = []
    cal_credit = []
    tmp = 0
    sum_credit = 0
    for i in range(0,len(subject_list)):
        grade_alp.append(str(subject_list[i].grade))
        cal_credit.append(float(subject_list[i].credit))
        sum_credit += float(subject_list[i].credit)
        for j in range(0,len(keep_grade)):
            if(str(subject_list[i].grade) == keep_grade[j]):
                tmp += (subject_list[i].credit*grade_keep[j])
                
    gpa = 0
    if sum_credit != 0:
        gpa = tmp/sum_credit
        result = math.floor(gpa * 100) / 100
        
    print(grade_alp)
    print(cal_credit)
    print(tmp)
    print(sum_credit)
    # Calculate balance of paylist.
    return render(request,"grade/show.html",{'subject_list':subject_list, 'result':result})
