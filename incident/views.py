from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from incident.models import Report
# Create your views here.


def home(request):
    return render(request, 'index.html')


# def login(request):
#     return render(request, 'authentication-login1.html')


def incident(request):
    if request.method =="POST":
        location =request.POST['location']
        description=request.POST['description']
        date =request.POST['date']
        time =request.POST['time']
        Incident_location =request.POST['Incident_location']
        Intial_Serverity =request.POST['Intial_Serverity']
        suspect_cause =request.POST['suspect_cause']
        immediaet_action =request.POST['immediaet_action']
        sub_incident_type =request.POST['sub_incident_type']

        Reports = Report (location=location ,description =description ,date=date,time=time , Incident_location=Incident_location ,
         Intial_Serverity=Intial_Serverity ,suspect_cause=suspect_cause,immediaet_action=immediaet_action,sub_incident_type=sub_incident_type, )
        Reports.save()

        messages.success(request,'Successfully !')


    return render(request, 'form-inputs.html')


def register(request):

    if request.method =="POST":
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        password =request.POST['password']
        password2 =request.POST['password2']
        email =request.POST['email']
        user = User.objects.create_user(username=username,password=password,email=email,first_name =first_name, last_name=last_name )
               
        user.save()
       
            
    else:
        return render(request,'authentication-register1.html')
    return HttpResponse('404 - Not Found')

def login(request):
    if request.method =="POST":
        username=request.POST['username']
        password =request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('/')
        else:
            messages.error(request,'incorrect username or password')
            return redirect('/login')
    else:
        return render(request,'authentication-login1.html')
def logout(request):
    logout(request)
    messages.success(request,'Successfully Logged Out')
