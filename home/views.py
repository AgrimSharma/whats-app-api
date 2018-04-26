from django.shortcuts import render, HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json

url = "http://139.59.46.61:8080/cakechat_api/v1/actions/get_response"


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
        url = "https://eu4.chat-api.com/instance1876/message?token=l25irc801wijrfq9"
        req = requests.post(url, data).json()
        return HttpResponse(json.dumps(req))


@csrf_exempt
def chat_bot(request):
    if request.method == 'GET':
        return render(request, 'chat_bot.html')
    elif request.method == "POST":
        context = request.POST.get('question')
        emoj = request.POST.get('emoction')
        data = dict(context=[context])
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url=url, data=json.dumps(data), headers=headers).json()
        if response['response']:
            response = response['response']
        else:
            response = "I'm unable to under stand you. Sorry for inconvenience."
        return HttpResponse(response)
