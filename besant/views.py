from django.shortcuts import render
from besant.models import Students

def Home(request):
      return render(request,"home.html")

def Register(request):
      if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            abc = Students(Name=name,Email=email,Phone=phone)
            abc.save()
      return render(request,"register.html")