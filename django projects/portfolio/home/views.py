from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse('this is my homepage of portfolio')
    context = {'name':'harry','course':'django'}
    return render(request,'home.html')

def about(request):
    #return HttpResponse('this is my about of portfolio')
    return render(request,'about.html')

def project(request):
    #return HttpResponse('this is my project of portfolio')
    return render(request,'project.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("The data is written successfully")

    #return HttpResponse('this is my contact of portfolio') 
    return render(request,'contact.html')