from django.urls import path
from . import views

app_name = 'messenger'

urlpatterns = [
    path(route='', view=views.sendMail, name='send_mail')   
]