from django.urls import path
from sisolo.views import landing_page, login_user, register, registerAddition, editProfile, logout_user, all_user_data_json, login_user_mobile, register_mobile, logout_mobile, edit_user_mobile

app_name = 'sisolo'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    path('registerAddition/', registerAddition, name='registerAddition'),
    path('update/', editProfile, name='update'),
    path('json/', all_user_data_json, name='show_user_json'),
    path('login_mobile/', login_user_mobile, name='login_user_mobile'),
    path('register_mobile/', register_mobile, name='register_mobile'),
    path('logout_mobile/', logout_mobile, name='logout_mobile'),
    path('edit_user_mobile/', edit_user_mobile, name='edit_user_mobile'),
]