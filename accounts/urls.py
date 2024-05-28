from django.urls import path
from accounts.views import accounts_login

urlpatterns = [
    path('login/', accounts_login, name='login'),
]
