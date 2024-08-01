from django.urls import path
from .views import profile, UserLoginView

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('login/', UserLoginView.as_view(), name="login"),
]
