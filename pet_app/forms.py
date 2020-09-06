from .models import Pet
from django import forms


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "age", "price", "image"]
