from django.shortcuts import render, redirect
from .forms import LoginForm
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _
import random, string
import ghasedakpack
from config.radman import *
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


def forgot_password(request):
    return render(request, 'account/forgot-password.html')

class ForgotPassword(generic.TemplateView):
    otps = dict()

    def get(self, request, args, *kwargs):
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
            answer = True
            if answer:
                messages.success(request, _("A verification code sent to %s. Please enter the recieved code to continue." %phone_number))
                return render(request, 'login_with_phone_number.html', context)
            messages.error(request, _("A problem occured in sending message. Please try again in a few minutes."))
            return redirect('account_login')
        # except ConnectTimeout as error:
            messages.error(request, _("A problem occured in sms message server. Please try again in a few minutes."))
            messages.error(request, error)
            return redirect('account_login')
        # except SSLError as error:
            messages.error(request, _("A problem occured which is related to SSL. Please check your VPN status or proxy settings!"))
            messages.error(request, error)
            return redirect('account_login')
        except ConnectionError as error:
            messages.error(request, _("A connection error occured. Please check your Internet!"))
            messages.error(request, error)
            return redirect('change_otp_number')

    def post(self, request, args, *kwargs):
        phone_number = request.POST.get('phone_number')
        sent_otp = request.POST.get('otp')
        otps = ForgotPassword.otps
        current_user = otps.get(phone_number) # اگه طرف شماره رو انگولک نکرده باشه از تو اچ تی ام ال
        if current_user == None: # یعنی یا منقضی شده و یا طرف دستکاری کرده فرم رو با اچ تی ام ال
            messages.error(request, _("OTP has been expired!"))
            return redirect('account_login')
        correct_otp = current_user.get('otp')
        username = current_user.get('username')
        try:
            del ForgotPassword.otps[phone_number]
        except: # ممکنه اکسپایر شده باشه یا نباشه تو دیکشنری یا به هر دلیلی. به هر حال میگم ارور نده. سعی کن پاکش کنی. شد شد نشد نشد ولش کن😁
            pass
        if correct_otp==sent_otp:
            try:
                if username==None: # پس دفعه اول هست و میخواد اکانت بسازه
                    random_username = phone_number 
                    not_ok = get_user_model().objects.filter(username=random_username).first()
                    while not_ok:
                        random_username = phone_number+str(''.join(random.choices(string.ascii_letters+string.digits,k=random.randint(8, 10))))
                        not_ok = get_user_model().objects.filter(username=random_username).first()
                    new_user = get_user_model().objects.create(username=random_username, phone_number=phone_number)
                    PhoneNumber.objects.create(user=new_user, phone_number=phone_number)
                    login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
                else: # قبلا حداقل یه بار وارد شده. پس اکانت داره
                    user = get_user_model().objects.get(username=username)
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    temp = PhoneNumber.objects.get(phone_number=phone_number)
                    if temp.verified:
                        messages.success(request, _("Welcome %s" %username))
                        return redirect('homepage')
                context = {'phone_number': phone_number}
                messages.success(request, _("Successfull Login."))
                return render(request, 'register_with_phone_number.html', context)
            except:
                pass
        else:
            messages.error(request, _("Sorry. OTP is invalid!"))
            return redirect('')
