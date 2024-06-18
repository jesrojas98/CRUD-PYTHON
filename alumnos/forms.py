from django import forms
from .models import Alumno

from django.forms import ModelForm

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = "__all__"