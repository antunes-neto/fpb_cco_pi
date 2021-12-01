from django.shortcuts import render, redirect
from django.http import JsonResponse
from PIL import Image
from .models import Photo
from .forms import PhotoForm


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')

    else:
        form = PhotoForm()
    context = {'form': form, 'photos': photos}
    return render(request, 'main.html', context)
