from django.urls import path
from .views import profile, UserLoginView, ForgotPassword, forgot_password, UserRegisterView

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('signup/', UserRegisterView.as_view(), name="signup"),
    path('forgot-password/', forgot_password, name="forgot_password"),
    path('otp/', ForgotPassword.as_view(), name="otp"),
]
