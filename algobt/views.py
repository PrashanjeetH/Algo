from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponse, Http404
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


@login_required(redirect_field_name='login')
def conditionForm(request):
    if request.user.is_authenticated:
        if request.POST:
            raw_data = {'username': request.user, 'data': request.POST.dict()}
            new_data = UserDataModel(**raw_data)
            new_data.save()
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


@login_required(redirect_field_name='login')
def ShowDataRecords(request):
    # Double Check on user authentication
    if request.user.is_authenticated:
        # collect all the data from DB belonging to the user
        allRecords = UserDataModel.objects.filter(username=request.user)
        context = {
            'records': allRecords,
            'year': datetime.now().year,
        }
        return render(request, 'app/showrecords.html', context)


@login_required(redirect_field_name='login')
def DownloadDataRecords(request, record_id):
    # Double check on user autentication
    if request.user.is_authenticated:
        return HttpResponse("<h1>" + str(record_id) + "</h1>")
    else:
        return Http404('NOT FOUND')
