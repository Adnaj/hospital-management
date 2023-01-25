from django.shortcuts import render
from django.http import HttpResponse
from .models import*
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'conformation.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html',dict_form)

def doctors(request):
    dict_doc={
        'doc':Doctor.objects.all()
    }
    return render(request, 'doctors.html',dict_doc)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request, 'department.html',dict_dept)
