
# Defini
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from django import forms
from .models import Person, City


class BootstrapAuthenticationForm(AuthenticationForm):

# Authentication form which uses boostrap CSS.

    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                                       'class': 'form-control',
                                                       'placeholder': 'User name'}
                                                      )
                               )
    password = forms.CharField(label=_('Password'),
                               widget=forms.PasswordInput({
                                                           'class': 'form-control',
                                                           'placeholder':'Password'
                                                           })
                               )


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'birthdate', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
