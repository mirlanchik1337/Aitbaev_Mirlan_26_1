
from django.shortcuts import HttpResponse , redirect
from datetime import datetime

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")

def now_date_view(request):
    if request.method == 'GET':
        now_date = datetime.now()
        return HttpResponse(f"{now_date}")

def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")



def google_view(request):
    if request.method == 'GET':
        return redirect('https://www.google.com/')
def youtube_view(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com/')

def instagram_view(request):
    if request.method == 'GET':
        return redirect('https://www.instagram.com')

def whatsapp_view(request):
    if request.method == 'GET':
        return redirect('https://www.whatsapp.com')

def telegram_view(request):
    if request.method == 'GET':
        return redirect('https://web.telegram.org')

