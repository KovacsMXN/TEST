from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from configuracion.models import Equipment_Locations, Equipment
from django.core import serializers

from .forms import EditEquipment, ImagenForm

#CREATE VIEW FOR MAIN INDEX DOMAIN
@login_required
def index(request):
    return render(request, 'index.html')

#VIEW FOR INDEX EQUIPMENT
@login_required
def equipment_index(request):
    return render(request, 'equipment/index.html')

#VIEW FOR VIEW EQUIPMENT
@login_required
def equipment_view(request, id):
    db_request = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        form = EditEquipment(request.POST, instance=db_request)
        if form.is_valid():
            form.save()
            return render(request, 'equipment/view.html', {'data_db': db_request, 'form': form})
        else:
            return render(request, 'equipment/view.html', {'data_db': db_request, 'form': form})
    else:
        db_request = get_object_or_404(Equipment, id=id)
        form = EditEquipment(instance=db_request)
        return render(request, 'equipment/view.html', {'data_db': db_request, 'form': form})

#VIEW FOR VIEW EQUIPMENT
@login_required
def equipment_imagen_view(request, id):
    db_request = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        form = EditEquipment(request.POST, instance=registro)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'equipment/imagen.html', {'data_db': db_request, 'form': form})
        return redirect('../../')
    else:
        form = get_object_or_404(Equipment, id=id)
        form = EditEquipment(request.POST, instance=registro)
        return render(request, 'configuracion/settings/equipment_locations_edit.html',{'form': form, 'registro':registro})

#VIEW TO DELETE MAIN IMAGE
@login_required
def equipment_imagen_delete_view(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(Equipment, id=id)
            registro.imagen = "equipment/main/default.png"
            registro.save()
            response_data = {'mensaje': 'Registro eliminado exitosamente.'}
        except Equipment.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

def equipment_imagen_upload_view(request, id):
    db_request = get_object_or_404(Equipment, id=id)
    return render(request, 'equipment/imagen.html', {'data_db': db_request})

#VIEW JSON RESPONSE EQUIPMENT DB
@login_required
def equipment_request_json(request):
    db_request1 = Equipment.objects.values(
        'id',
        'fa_number',
        'name',
        'brand__name',  # Accedemos al nombre de la marca a través de la relación ForeignKey
        'model',
        'serial',
        'location__name'  # Accedemos al nombre de la ubicación a través de la relación ForeignKey
    )
    return JsonResponse({'equipment': list(db_request1)}, safe=False)
