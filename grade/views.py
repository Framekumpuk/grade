from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Grade
import math
import csv

def login(request):
    return render(request,"grade/login.html")

def signup(request):
    return render(request,"grade/signup.html")

def keepUser(request):
    name = request.POST['name']
    password = request.POST['password']    

    if name == '' or len(password) == 0:
        return render(request, 'grade/error_register.html')

    user = User.objects.create_user(username=name, password=password)
    user.save()
    return render(request, 'grade/success.html', {'name':name})

def index(request):
    user = User.objects.all()
    name = request.POST['name']
    password = request.POST['password']
    user = authenticate(username=name, password=password)
    if user is not None:
        # A backend authenticated the credentials
        login(request)
        return render(request,"grade/index.html")
    else:
        # No backend authenticated the credentials
        return render(request, 'grade/error_login.html')  

def about(request):
    return render(request,"grade/about.html")

def operand(request):
    error_message = 0
    subject = ""
    score = 0
    full = 1
    credit = 1
    mean = 0
    sd = 0
    final_score = 0
    final_full = 1
    try:
        subject = request.POST['subject']
        score = float(request.POST['score'])
        full = float(request.POST['full'])
        credit = float(request.POST['credit'])
        mean = float(request.POST['mean'])
        sd = float(request.POST['sd'])
        final_score = float(request.POST['final_score'])
        final_full = float(request.POST['final_full'])
    except:
        error_message = 1
        
    if(subject != ""):
        equation = (float(score)+float(final_score))*100/(float(full)+float(final_full))  # make score to 100 percent
        net = ("%.2f" % round(equation,2))  # make decimal two position
        if float(net) < 0.0:
            grade = 'Null'
        elif float(net) < float(mean)-(1.5*float(sd)):
            grade = 'F'
        elif float(net) < float(mean)-float(sd):
            grade = 'D'
        elif float(net) < float(mean)-(0.5*float(sd)):
            grade = 'D+'
        elif float(net) < float(mean):
            grade = 'C'
        elif float(net) < float(mean)+(0.5*float(sd)):
            grade = 'C+'
        elif float(net) < float(mean)+(1*float(sd)):
            grade = 'B'
        elif float(net) < float(mean)+(1.5*float(sd)):
            grade = 'B+'
        elif float(net) >= float(mean)+(1.5*float(sd)):
            grade = 'A'
        elif float(net) > 100.0:
            grade = 'Null'
                
        information = Grade(subject=subject, score=score, full=full, total=net, grade=grade, credit=credit, mean=mean, sd=sd, final_score=final_score, final_full=final_full)
        information.save()
    # user hits the Back button.
    return render(request,"grade/detail.html")

def show(request):
    subject_list = Grade.objects.all()
    keep_grade = ['A','B+','B','C+','C','D+','D','F']
    grade_keep = [4,3.5,3,2.5,2,1.5,1,0]
    grade_alp = []
    cal_credit = []
    tmp = 0
    sum_credit = 0
    # this loop will pull data from database that calculate grade of that semeter
    for i in range(len(subject_list)):
        grade_alp.append(str(subject_list[i].grade))
        cal_credit.append(float(subject_list[i].credit))
        sum_credit += float(subject_list[i].credit)
        for j in range(0,len(keep_grade)):
            if(str(subject_list[i].grade) == keep_grade[j]):
                tmp += (subject_list[i].credit*grade_keep[j])
                
    gpa = 0
    # calculate GPA
    if sum_credit != 0:
        gpa = tmp/sum_credit
        result = math.floor(gpa * 100) / 100
        
    print(grade_alp)
    print(cal_credit)
    print(tmp)
    print(sum_credit)
    # Calculate balance of paylist.
    return render(request,"grade/show.html",{'subject_list':subject_list, 'result':result})
