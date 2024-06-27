from django.shortcuts import render
    
def login_register(request):
    return render(request, "login-register.html")
