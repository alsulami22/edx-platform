from django.conf import settings
from django.conf.urls import url

from student_account import views

urlpatterns = [
    url(r'^finish_auth$', views.finish_auth, name='finish_auth'),
    url(r'^settings$', views.account_settings, name='account_settings'),
    url(r'^password$', views.password_change_request_handler, name='password_change_request'),
    url(r'^login$', views.login_and_registration_form,
        {'initial_mode': 'login'}, name='signin_user'),
    url(r'^register$', views.login_and_registration_form,
        {'initial_mode': 'register'}, name='register_user'),
]
