#IMPORT DJANGO FUNCTIONS
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.decorators import user_passes_test

from django.utils import timezone



#MAIN INDEX VIEW
@user_passes_test(lambda u: u.is_superuser)
def index(request):
	db_request_sl = Storage_Locations.objects.all()
	db_request_el = Equipment_Locations.objects.all()
	db_request_eb = Equipment_brands.objects.all()
	db_request_b = Equipment.objects.all()
	return render(request, 'configuracion/settings/index.html', {'db_r1':db_request_sl, 'db_r2':db_request_el,'db_r3':db_request_eb,'db_r4':db_request_b})



#PLATFORM SETTINGS VIEWS

#MAIN STORAGE LOCATIONS VIEWS
@user_passes_test(lambda u: u.is_superuser)
def configuracion_storage_index(request):
	return render(request, 'configuracion/settings/settings_storage_locations.html')
#ADD STORAGE LOCATIONS VIEWS
@user_passes_test(lambda u: u.is_superuser)
def configuracion_storage_add(request):
	if request.method == 'POST':
		form = CreateNewStorageLocation(request.POST)
		if form.is_valid():
				form.save()
				return redirect('configuracion_storage_index')
		else:
				form = CreateNewStorageLocation()
				for field, errors in form.errors.items():
						for error in errors:
							messages.error(request, f"{field}: {error}")
				usuarios = User.objects.all()
		return render(request, 'configuracion/settings/storage_location_add.html', {'usuarios': usuarios, 'form': form})
	else:
		form = CreateNewStorageLocation(request.POST)
		return render(request, 'configuracion/settings/storage_location_add.html', {'form': form})
#EDIT STORAGE LOCATIONS VIEWS
@user_passes_test(lambda u: u.is_superuser)
def configuracion_storage_edit(request, id):
	registro = get_object_or_404(Storage_Locations, id=id)
	if request.method == 'POST':
		form = CreateNewStorageLocation(request.POST, instance=registro)
		if form.is_valid():
			form.save()
		else:
			return render(request, 'configuracion/settings/storage_edit.html',{'form': form, 'registro':registro})
		return redirect('../../')
	else:
		registro = get_object_or_404(Storage_Locations, id=id)
		form = CreateNewStorageLocation(instance=registro)
		return render(request, 'configuracion/settings/storage_edit.html',{'form': form, 'registro':registro})
#STORAGE LOCATIONS JSON RESPONSE
@user_passes_test(lambda u: u.is_superuser)
def configuracion_storage_json_response(request):
    db_request1 = list(Storage_Locations.objects.values())
    data = {'storage_location':db_request1}
    return JsonResponse(data)
@user_passes_test(lambda u: u.is_superuser)
#STORAGE LOCATION JSON DELETE    
def configuracion_storage_json_delete(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(Storage_Locations, id=id)
            registro.delete()
            response_data = {'mensaje': 'Registro eliminado exitosamente.'}
        except User.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)


#MAIN STORAGE LOCATIONS VIEWS
@user_passes_test(lambda u: u.is_superuser)
def equipment_locations_index(request):
	instance = Equipment_Locations.objects.all()
	return render(request, 'configuracion/settings/equipment_locations.html', {'context': instance})
#DELETE STORAGE LOCATIONS VIEWS
@user_passes_test(lambda u: u.is_superuser)
def equipment_locations_delete(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(Equipment_Locations, id=id)
            registro.delete()
            response_data = {'mensaje': 'Registro eliminado exitosamente.'}
        except User.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
#EDIT EQUIPMENT LOCATIONS VIEWS
@user_passes_test(lambda u: u.is_superuser)
def configuracion_locations_edit(request, id):
	registro = get_object_or_404(Equipment_Locations, id=id)
	if request.method == 'POST':
		form = CreateNewEquipmentLocation(request.POST, instance=registro)
		if form.is_valid():
			form.save()
		else:
			return render(request, 'configuracion/settings/equipment_locations_edit.html',{'form': form, 'registro':registro})
		return redirect('../../')
	else:
		registro = get_object_or_404(Equipment_Locations, id=id)
		form = CreateNewEquipmentLocation(instance=registro)
		return render(request, 'configuracion/settings/equipment_locations_edit.html',{'form': form, 'registro':registro})
#ADD EQUIPMENT LOCATIONS VIEWS
@user_passes_test(lambda u: u.is_superuser)
def configuracion_locations_add(request):
	if request.method == 'POST':
		form = CreateNewEquipmentLocation(request.POST)
		if form.is_valid():
				form.save()
				return redirect('equipment_locations_index')
		else:
				form = CreateNewEquipmentLocation()
				for field, errors in form.errors.items():
						for error in errors:
							messages.error(request, f"{field}: {error}")
				usuarios = User.objects.all()
		return render(request, 'configuracion/settings/equipment_location_add.html', {'usuarios': usuarios, 'form': form})
	else:
		form = CreateNewEquipmentLocation(request.POST)
		return render(request, 'configuracion/settings/equipment_location_add.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def equipment_locations_json_response(request):
    locations = Equipment_Locations.objects.all()
    locations_data = []
    for location in locations:
    	equipment_count = location.equipment_set.count()
    	location_info = {
            'id': location.id,
            'name': location.name,
            'color': location.color,
            'equipment_count': equipment_count,
        }
    	locations_data.append(location_info)
    	data = {'data_raw': locations_data}    
    return JsonResponse(data)

@user_passes_test(lambda u: u.is_superuser)
def equipment_brands(request):
	if request.method == 'POST':
		form = CreateNewEquipmentBrands(request.POST)
		if form.is_valid():
				user = form.save()
				return redirect('equipment_brands')
		else:
				form = CreateNewEquipmentBrands()
				for field, errors in form.errors.items():
						for error in errors:
							messages.error(request, f"{field}: {error}")
				usuarios = Equipment_brands.objects.all()
		return render(request, 'configuracion/settings/equipment_brands.html', {'usuarios': usuarios, 'form': form})
	else:
		form = CreateNewEquipmentBrands(request.POST)
		form.fields['name'].widget.attrs['class'] = 'form-control'
		return render(request, 'configuracion/settings/equipment_brands.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def equipment_brands_json_response(request):
    db_request1 = list(Equipment_brands.objects.values())
    data = {'brands':db_request1}
    return JsonResponse(data)

@user_passes_test(lambda u: u.is_superuser)
def equipment_brands_edit(request, id):
	registro = get_object_or_404(Equipment_brands, id=id)
	if request.method == 'POST':
		form = CreateNewEquipmentBrands(request.POST, instance=registro)
		if form.is_valid():
			form.save()
		else:
			return render(request, 'configuracion/settings/brands_edit.html',{'form': form, 'registro':registro})
		return redirect('../../')

	else:
		registro = get_object_or_404(Equipment_brands, id=id)
		form = CreateNewEquipmentBrands(instance=registro)
		return render(request, 'configuracion/settings/brands_edit.html',{'form': form, 'registro':registro})

@user_passes_test(lambda u: u.is_superuser)
def equipment_brands_delete(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(Equipment_brands, id=id)
            registro.delete()
            response_data = {'mensaje': 'Registro eliminado exitosamente.'}
        except User.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)