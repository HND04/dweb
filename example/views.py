# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>it's me</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
   '''
    # views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
