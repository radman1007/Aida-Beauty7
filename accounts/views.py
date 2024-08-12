from django.shortcuts import render, redirect
from .forms import LoginForm
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model


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


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/login.html', {'form' : form})

@login_required()
def profile(request):
    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        phone=request.POST.get('phone')
        sent_password=request.POST.get('password')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        prev_password = request.user.password
        user = get_user_model().objects.filter(phone=phone).first()
        if user:
            if user!=request.user:
                return redirect('login')
            else:
                if check_password(sent_password,prev_password):
                    if  password1 == password2:
                        if len(password1) >= 8 and len(fullname) >= 1:
                            user.fullname=fullname
                            user.set_password(password1)
                            user.save()
                        if len(password1) >= 8:
                            user.set_password(password1)
                            user.save()
                        if len(fullname) >= 1:
                            user.fullname=fullname
                            user.save()
                            
    return render(request, 'my-account.html')
