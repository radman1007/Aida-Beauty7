from django.shortcuts import render, redirect
from .forms import LoginForm
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _
import random
import ghasedakpack
from config.radman import *
from cart.models import Order, OrderItem

sms = ghasedakpack.Ghasedak(GHASEDAK_API_KEY)


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
                messages.success(request, "با موفقیت وارد شدید.")
                return redirect('index')
            else:
                form.add_error("phone", "شماره و رمز عبور را چک کنید")
        else:
            form.add_error("phone", "لطفا مقادیر را به درستی تکمیل کنید")
        return render(request, 'account/login.html', {'form' : form})


class UserRegisterView(View):        
    def post(self, request):
        if len(request.POST["password"]) >= 8:
            if len(get_user_model().objects.filter(phone=request.POST["phone"])) == 0:        
                user = get_user_model().objects.create_user(request.POST["phone"], request.POST["password"])
                user.save()
                user = authenticate(username=request.POST['phone'], password=request.POST['password'])
                if user is not None:
                    login(request, user)
                    messages.success(request, "با موفقیت وارد شدید.")
                    return redirect('profile')
        return render(request, 'account/login.html')

@login_required()
def profile(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items')
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
    context = {
        'orders' : orders,
    }
    return render(request, 'my-account.html', context)


def forgot_password(request):
    return render(request, 'account/forgot-password.html')

class ForgotPassword(generic.TemplateView):
    otps = dict()

    def get(self, request, *args, **kwargs):
        phone_number = request.GET.get('phone')
        if phone_number==None:
            return redirect('forgot_password')
        if phone_number.isalpha() or len(phone_number)!=11:
            return redirect('forgot_password')
        otp = str(random.randint(100000, 999999))
        username = get_user_model().objects.filter(phone=phone_number).first()
        if username == None:
            return redirect('forgot_password')
        ForgotPassword.otps[phone_number]={
            'otp': otp,
            'username': username,
        }
        context = {
            'username': username,
            'phone_number': phone_number,
        }
        try:
            answer = sms.verification({'receptor': phone_number, 'linenumber': '30005088','type': '1', 'template': 'AidaBeauty7', 'param1': otp})
            if answer:
                return render(request, 'account/login_with_phone_number.html', context)
            return redirect('forgot_password')
        except:
            return redirect('forgot_password')

    def post(self, request, *args, **kwargs):
        phone_number = request.POST.get('phone')
        sent_otp = request.POST.get('otp')
        otps = ForgotPassword.otps
        current_user = otps.get(phone_number)
        if current_user == None:
            return redirect('forgot_password')
        correct_otp = current_user.get('otp')
        username = current_user.get('username')
        try:
            del ForgotPassword.otps[phone_number]
        except:
            pass
        if correct_otp==sent_otp:
            try:
                if username==None:
                    return redirect('forgot_password')
                else:
                    user = get_user_model().objects.get(phone=username)
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('index')
            except:
                return redirect('forgot_password')
        else:
            return redirect('forgot_password')
