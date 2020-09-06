from django.shortcuts import render, redirect
from .models import Pet


# from .forms import CarForm

# Create your views here.
def pet_list(request):
    pets = Pet.objects.all()
    context = {
        "pets": pets,
    }
    return render(request, 'list.html', context)


def pet_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    context = {
        "pet": pet,
    }
    return render(request, 'detail.html', context)
