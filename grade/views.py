from django.http import HttpResponse


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
        score = ""
        full = ""
    else:
            information = Grade(subject=subject, score=score, full=full)
            information.save()
    # user hits the Back button.
    total = (score*100)/full
    # Calculate balance of paylist.
    return render(request,"grade/detail.html",{'payment_list':payment_list, 'total':total})
