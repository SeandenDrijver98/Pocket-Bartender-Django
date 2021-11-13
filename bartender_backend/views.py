from django.shortcuts import render
from .forms import ContactForm


def index(request):
    contact_form = ContactForm()
    return render(request, "index.html", {"form": contact_form})
