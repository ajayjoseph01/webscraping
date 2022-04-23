from django.shortcuts import render

# Create your views here.
def Register(request):
    return render(request,'user_registration.html')

def Login(request):
    return render(request,'user_login.html') 

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')
    
