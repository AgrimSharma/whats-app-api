from django.conf.urls import include, url
from .views import home, chat_bot

urlpatterns = [

    url(r'^whatsapp_api/', home, name="send"),
    url(r'^chat/', chat_bot, name="chat_bot"),
]
