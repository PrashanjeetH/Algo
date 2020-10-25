# Definition of forms for algo_bt
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import (
    EntryConditionModel,
    # EntryConditionLevel_1,
    # EntryConditionLevel_2,
    # EntryConditionField_3,
    # TrailConditionModel,
    # TrailConditionLevel_1,
    # RiskManagementModel,
)
from django import forms


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
                                   'placeholder': 'Password'
                               })
                               )


class EntryConditionForm(forms.ModelForm):
    class Meta:
        model = EntryConditionModel
        fields = ('field_1', 'field_2')
        labels = {
            'field_1': 'Choose',
            'field_2': 'Choose',
        }
        widgets = {
            'field_1': forms.RadioSelect(attrs={
                'class': 'entry-cond-form-1',
                'placeholder': 'Choose one',
            })
        }
