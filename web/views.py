from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def index(request):
    return render(request, 'index.html', {})

def contact(request):


    if request.method == "POST":
        name= request.POST['name']
        email= request.POST['email']
        sub= request.POST['subject']
        message= request.POST['message']
        recipient_list = ['chatouirabie@gmail.com']

        send_mail(sub, message,email,recipient_list,fail_silently=False )
        return render(request, 'contact.html', {'name':name})
    else :
        return render(request, 'contact.html', {})