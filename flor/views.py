from django.shortcuts import render, redirect, get_object_or_404
from .models import Flor
from .forms import FlorForm


def inicio(request):
    return render(request, 'inicio.html')

def lista_flor(request):
    flores = Flor.objects.all()
    return render(request, 'flor/lista.html', {'flores': flores})

def crear_flor(request):
    form = FlorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_flor')
    return render(request, 'flor/form.html', {'form': form})

def editar_flor(request, id):
    flor = get_object_or_404(Flor, id=id)
    form = FlorForm(request.POST or None, request.FILES or None, instance=flor)
    if form.is_valid():
        form.save()
        return redirect('lista_flor')
    return render(request, 'flor/form.html', {'form': form})

def eliminar_flor(request, id):
    flor = get_object_or_404(Flor, id=id)
    flor.delete()
    return redirect('lista_flor')