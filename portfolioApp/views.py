from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.core.mail import EmailMessage
import os 

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    return render(request, "projects.html")

def contact(request):
    form = ContactForm()
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email = EmailMessage(
                subject=f"Contact from {form.cleaned_data['name']}",
                body=form.cleaned_data['message'],
                from_email=os.environ.get('DEFAULT_FROM_EMAIL'),  # your verified sender
                to=[os.environ.get('CONTACT_EMAIL')],  # receive messages here
                reply_to=[form.cleaned_data['email']]  # user who submitted
            )
            email.send(fail_silently=False)
            success = True
            form = ContactForm()
    return render(request, "contact.html", {"form": form, "success": success})