from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from .models import Locations, Storage

from .forms import StorageForm, LocationForm

#STORAGE
@login_required
def storage_index(request):
	query = Storage.objects.all()
	return render(request, 'storage/index.html', {'data':query})

@login_required
def storage_view(request, id):
	query = get_object_or_404(Storage, id=id)
	return render(request, 'storage/view.html', {'data':query})

@login_required
def storage_add(request):
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            new = form.save()
            return redirect('storage_view', id=new.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = StorageForm()
    return render(request, 'storage/add.html', {'form': form})
@user_passes_test(lambda u: u.is_superuser)
def storage_edit(request, id):
    query = get_object_or_404(Storage, id=id)
    if request.method == 'POST':
        new_frk = form = StorageForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('storage_view', id=query.id)
    else:
        query = get_object_or_404(Storage, id=id)
        form = StorageForm(instance=query)
    return render(request, 'storage/edit.html', {'form': form,'data':query})
@user_passes_test(lambda u: u.is_superuser)
def storage_delete(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(Storage, id=id)
            registro.delete()
            return redirect('storage_index')
        except Storage.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

#LOCATIONS
@login_required
def locations_index(request):
    query = Locations.objects.all()
    return render(request, 'locations/index.html', {'data':query})

@login_required
def locations_view(request, id):
    query = get_object_or_404(Locations, id=id)
    return render(request, 'locations/view.html', {'data':query})

@login_required
def locations_add(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            new = form.save()
            return redirect('locations_view', id=new.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = LocationForm()
    return render(request, 'locations/add.html', {'form': form})
@user_passes_test(lambda u: u.is_superuser)
def locations_edit(request, id):
    query = get_object_or_404(Locations, id=id)
    if request.method == 'POST':
        new_frk = form = LocationForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('locations_view', id=query.id)
    else:
        query = get_object_or_404(Locations, id=id)
        form =LocationForm(instance=query)
    return render(request, 'locations/edit.html', {'form': form,'data':query})
@user_passes_test(lambda u: u.is_superuser)
def locations_delete(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(Locations, id=id)
            registro.delete()
            return redirect('locations_index')
        except Locations.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)