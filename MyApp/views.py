from MyApp.models import Contact
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('textarea')
        date = datetime.today()

        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=date)
        contact.save() 
        messages.success(request, 'Details submitted successfully.')
    return render(request, 'contact-us.html')