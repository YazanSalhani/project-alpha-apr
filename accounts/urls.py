from django.urls import path
from accounts.views import accounts_login, accounts_logout, accounts_signup

urlpatterns = [
    path('login/', accounts_login, name='login'),
    path('logout/', accounts_logout, name='logout'),
    path('signup/', accounts_signup, name='signup'),
]
