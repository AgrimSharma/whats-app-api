from django.conf.urls import include, url
from .views import *
urlpatterns = [

    url(r'^whatsapp_api/', home, name="send"),
]
