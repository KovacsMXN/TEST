from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse, HttpResponse
from django.urls import reverse

from .models import Equipment_brands
from .forms import EquipmentBrandsForm

#### EQUIPMENT ####
@user_passes_test(lambda u: u.is_superuser)
def equipment_index(request):
	return render(request, 'equipment/index.html')

@user_passes_test(lambda u: u.is_superuser)
def equipment_add(request):
	return render(request, 'equipment/index.html')

@user_passes_test(lambda u: u.is_superuser)
def equipment_view(request):
	return render(request, 'equipment/index.html')

@user_passes_test(lambda u: u.is_superuser)
def equipment_edit(request):
	return render(request, 'equipment/index.html')

@user_passes_test(lambda u: u.is_superuser)
def equipment_delete(request):
	return render(request, 'equipment/index.html')

#### MANUFACTURERS ####
@user_passes_test(lambda u: u.is_superuser)
def equipment_manufacturers(request):
	return render(request, 'equipment/manufacturers/index.html')

@user_passes_test(lambda u: u.is_superuser)
def equipment_manufacturers_add(request):
    if request.method == 'POST':
        form = EquipmentBrandsForm(request.POST)
        if form.is_valid():
            new = form.save()
            return redirect('equipment_manufacturers_view', id=new.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = EquipmentBrandsForm()
        return render(request, 'equipment/manufacturers/add.html',{'form':form})

@user_passes_test(lambda u: u.is_superuser)
def equipment_manufacturers_view(request, id):
	query = get_object_or_404(Equipment_brands, id=id)
	return render(request, 'equipment/manufacturers/view.html',{'data':query})

@user_passes_test(lambda u: u.is_superuser)
def equipment_manufacturers_edit(request, id):
    query = get_object_or_404(Equipment_brands, id=id)
    if request.method == 'POST':
        new_frk = form = EquipmentBrandsForm(request.POST, request.FILES, instance=query)
        if form.is_valid():
            form.save()
            return redirect('equipment_manufacturers_view', id=query.id)
    else:
        query = get_object_or_404(Equipment_brands, id=id)
        form = EquipmentBrandsForm(instance=query)
        return render(request, 'equipment/manufacturers/edit.html',{'data':query,'form':form})

@user_passes_test(lambda u: u.is_superuser)
def equipment_manufacturers_delete(request,id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(Equipment_brands, id=id)
            registro.delete()
            response_data = {
            'success': True,
            'redirect_url': reverse('equipment_manufacturers')
    }
        except Equipment_brands.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

#### PULL JSON ####
@staff_member_required
def equipment_manufacturers_json(request):
    query = list(Equipment_brands.objects.values(
        'id',
        'name',))
    data = {'data':query}
    return JsonResponse(data)

    return JsonResponse(response, safe=False)