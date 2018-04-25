from django.shortcuts import render, HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def home(request):
    if request.method == 'GET':
        return render(request, "home.html", {"title": "WhatsApp API"})
    else:
        phone = request.POST.get('phone')
        text = request.POST.get('message')
        data = {
            "phone": "{}".format(phone),
            "body": "{}".format(text)
        }
        url = "https://eu4.chat-api.com/instance1918/message?token=aq9cfvr84pgviw1r"
        req = requests.post(url, data).json()
        return HttpResponse(json.dumps(req))

