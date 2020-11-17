from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, Http404, FileResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import os


from algo.settings import BASE_DIR
from algobt.models import UserDataModel


def restricted_404_view(request):
    return Http404('SORRY! You Need To Login First. :)')


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



@login_required(redirect_field_name='login')
def conditionForm(request):
    if request.user.is_authenticated:
        if request.POST:
            if FormValidation(request):
                raw_data = {'username': request.user, 'data': request.POST.dict()}
                new_data = UserDataModel(**raw_data)
                new_data.save()
                return redirect('ShowRecords')

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
        # obj = your_model_name.objects.get(id=id)
        # filename = obj.model_attribute_name.path
        filename = os.path.join(BASE_DIR, "README.md")
        response = FileResponse(open(filename, 'rb'))
        # print(os.path.join(BASE_DIR, "README.md"))
        return response
        # return HttpResponse("<h1>" + str(record_id) + "</h1>")
    else:
        return Http404('NOT FOUND')


def FormValidation(raw_data):
    if raw_data.POST:
        print("Successfull!\n")
        # print(raw_data.user)
        # print(raw_data.user.username)
        # print(raw_data.user.first_name)
        # print(raw_data.user.last_name)
        # print(raw_data.user.email)
        # print(raw_data.content_params)
        # print(raw_data.path)
        dict_data = raw_data.POST.dict()
        # print(dict_data)
    return True



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
