from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm

def index(request):
    context = {
        'form': PhotoForm(),
    }
    return render(request, 'videos/index.html', context)

def predict(request):
    form = PhotoForm(request.POST, request.FILES)
    
    form.is_valid()  # 無効の場合

    photo = Photo(image=form.cleaned_data['image'])
    
    context = {
        'photo_name': photo.image.name,
        'photo_data': photo.image_src(),
    }
    
    return render(request, 'videos/result.html', context)