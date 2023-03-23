from django.shortcuts import render
from django.contrib.auth import login
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from sci_home_2023.forms import CustomUserCreationForm
from django.http import HttpResponseRedirect
from .forms import DocumentForm, ContactForm
from .models import Document

from django.core.mail import send_mail
from django.template.loader import render_to_string

def index(request):
    return render(request, 'sci_home_2023/pages/index.html')

def kmpage(request):
    return render(request, 'sci_home_2023/pages/km_page.html')
    
def beingspage(request):
    return render(request, 'sci_home_2023/pages/beings_page.html')

def medicalpage(request):
    return render(request, 'sci_home_2023/pages/medical_page.html')

def geneticspage(request):
    return render(request, 'sci_home_2023/pages/genetics_page.html')

def contentpage(request):
    return render(request, 'sci_home_2023/pages/content_page.html')

def company(request):
    return render(request, 'sci_home_2023/pages/company.html')

def converse(request):
    return render(request, 'sci_home_2023/pages/converse.html')

def aboutus(request):
    return render(request, 'sci_home_2023/pages/about_us.html')

def foundations(request):
    return render(request, 'sci_home_2023/pages/foundations.html')

def careers(request):
    return render(request, 'sci_home_2023/pages/careers.html')

def complete(request):
    return render(request, 'sci_home_2023/pages/complete.html')

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))

def careersform(request):
	if request.method == "POST":
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect("complete")
	form = DocumentForm()
	file = Document.objects.all()
	return render(request, 'sci_home_2023/pages/careers_form.html', context={'form':form, 'file':file})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            
            send_mail(
                'Subject here',
                'Here is the message.',
                'jamal@science-counter.com',
                ['jamal@science-counter.com', 'leyla@science-counter.com'],
                fail_silently=False,
            )
            
        return redirect("complete")

    form = ContactForm()
    return render(request, 'sci_home_2023/pages/contact.html', {'form': form})