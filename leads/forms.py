from django import forms
from django.contrib.auth import get_user_model
from .models import Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'firstName',
            'lastName',
            'age',
            'agent',
        )

class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)

#here we have taken the original class and custumized it with our needs
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username' : UsernameField}
