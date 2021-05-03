from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent to Jignesh')
        
    
    return render(request, 'index.html')

    # return HttpResponse("This Is Home Page")