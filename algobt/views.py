from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


from algobt.models import *


def home(request):
    # Renders the home page.

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def contact(request):
    # Renders the contact page.

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def about(request):
    # Renders the about page.

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


# @login_required(redirect_field_name='login')
def conditionForm(request):
    if request.POST:
        print(request.POST)
        print(request.POST.dict())
        return redirect('home')
    else:
        return render(
            request,
            'app/conditionform.html',
            {
                'title': 'Condition Form',
                'message': 'Your application Condition Form page.',
                'year': datetime.now().year,
            }
        )