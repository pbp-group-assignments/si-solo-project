from django.urls import path
from sisolo.views import landing_page, login_user, register, registerAddition, logout_user

app_name = 'sisolo'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    path('registerAddition/', registerAddition, name='registerAddition'),
]