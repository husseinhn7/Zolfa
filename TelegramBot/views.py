from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .d2 import  send
from telegram._bot import Bot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import telebot
from Zolfa.settings import TELEGRAM_BOT_TOKEN
# Create your views here.






# bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# @csrf_exempt
# def telegram_webhook(request):
#     if request.method == 'POST':
#         update = telebot.types.Update.de_json(request.body.decode('utf-8'))
#         bot.process_new_updates([update])
#         return HttpResponse('')
#     else:
#         return HttpResponse('Hello, world!')


# bot.set_webhook(url='http://192.168.1.8:8000/bot/telegram-webhook/')















class View(APIView):
    def post(self ,request):
        data = request.data
        
        a = data["link"]
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        bot.send_message(chat_id = 1494250709  ,  text=a )
        send(a)
        print(a)
        return Response({'msg' : f"link was send successfully  {a}"})
    
    
v = View.as_view()
    
    
    
class Demo(APIView):
    def post(self ,request , format=None):
        update = telebot.types.Update.de_json(request.data)
        pass
    
