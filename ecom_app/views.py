from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ecom_app.form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from datetime import time
# Create your views here.


def home(request):
    if request.method == "GET":
        content = {}
        return render(request, "home.html", context=content)


@login_required
def login_user(request):
    if request.method == "POST":
        print(request.POST)
        # username = request.POST.get("username")
        # password = request.POST.get("Password")
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("Password")
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, "loged in successfully...!")
                return redirect("/home")
        else:
            # messages.error(request,"invalid credential...!")
            # return redirect("login")
            return render(request, "home.html")

    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"login_form": form})


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out..!")
    return redirect("login_user")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                print("email send....!", message)
            except NameError:
                
                messages.error(request, "Something get wrong messages... ! ")
            return redirect("contact")

    form = ContactForm()
    return render(request, "contact.html", {'form': form})


class Student(models.model):
    name = models.charname(max_lenght = 500)



def register_func(request):
    if method.request == "POST":
        pass
    else :
        return HttpResponse(request, "not valid data...!")