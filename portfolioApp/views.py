from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.conf import settings

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
                from_email=settings.DEFAULT_FROM_EMAIL,     # Gmail account you’re sending with
                to=[settings.CONTACT_EMAIL],                # inbox where you want to receive
                reply_to=[form.cleaned_data['email']]       # user’s email (so you can reply)
            )
            email.send(fail_silently=False)
            success = True
            form = ContactForm()
    return render(request, "contact.html", {"form": form, "success": success})