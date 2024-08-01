from django.shortcuts import render, redirect
from .forms import LoginForm
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login


class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form' : form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error("phone", "شماره و رمز عبور را چک کنید")
        else:
            form.add_error("phone", "لطفا مقادیر را به درستی تکمیل کنید")
        return render(request, 'account/login.html', {'form' : form})


def profile(request):
    return render(request, 'my-account.html')
