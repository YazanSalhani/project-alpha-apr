from django.urls import path
from accounts.views import accounts_login, accounts_logout

urlpatterns = [
    path('login/', accounts_login, name='login'),
    path('logout/', accounts_logout, name='logout'),
]
