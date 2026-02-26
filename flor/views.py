from django.shortcuts import render

def inicio(request):
    return render(request, 'flor/inicio.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Flor
from .forms import FlorForm

def lista_flores(request):
    flores = Flor.objects.all()
    return render(request, 'flor/lista.html', {'flores': flores})

def crear_flor(request):
    if request.method == 'POST':
        form = FlorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_flores')
    else:
        form = FlorForm()
    return render(request, 'flor/form.html', {'form': form})

def eliminar_flor(request, id):
    flor = get_object_or_404(Flor, id=id)
    flor.delete()
    return redirect('lista_flores')