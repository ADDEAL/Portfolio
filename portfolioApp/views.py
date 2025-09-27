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
            # Create the email
            email = EmailMessage(
                subject=f"Contact from {form.cleaned_data['name']}",
                body=form.cleaned_data['message'],
                from_email=os.environ.get('EMAIL_HOST_USER'),  # always your verified email
                to=['adelekeadeal@gmail.com'],  # where you receive messages
                reply_to=[form.cleaned_data['email']]  # sender’s email
            )
            email.send(fail_silently=False)
            success = True
            form = ContactForm()
    return render(request, "contact.html", {"form": form, "success": success})
