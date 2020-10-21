from django.shortcuts import render

# Create your views here.

# Definition of views.

from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person, City, Country


class PersonListView(ListView):
    model = Person
    template_name = 'app/person_list.html'
    context_object_name = 'people'


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'app/city_lists.html', {'cities': cities})


class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')


class PersonUpdateView(UpdateView):
    model = Person
    fields = ('id','name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')


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
