from django.shortcuts import render

def profile(request):
    return render(request, 'my-account.html')