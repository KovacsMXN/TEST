from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib.auth.decorators import user_passes_test


#CREATE VIEW FOR MAIN INDEX DOMAIN
@login_required
def index(request):
    return render(request, 'index.html')

#VIEW FOR INDEX EQUIPMENT
@login_required
def equipment_index(request):
    return render(request, 'equipment/index.html')
@user_passes_test(lambda u: u.is_superuser)
def equipment_delete(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(Equipment, id=id)
            registro.delete()
            response_data = {'mensaje': 'Registro eliminado exitosamente.'}
        except User.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
#VIEW FOR VIEW EQUIPMENT
@login_required
def equipment_view(request, id):
    db_request = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        form = EditEquipment(request.POST, instance=db_request)
        if form.is_valid():
            if user_passes_test(lambda u: u.is_superuser):
                form.save()
                return render(request, 'equipment/view.html', {'data_db': db_request, 'form': form})
            else:
                return render(request, 'equipment/view.html', {'data_db': db_request, 'form': form})
        else:
            return render(request, 'equipment/view.html', {'data_db': db_request, 'form': form})
    else:
        db_request = get_object_or_404(Equipment, id=id)
        form = EditEquipment(instance=db_request)
        return render(request, 'equipment/view.html', {'data_db': db_request, 'form': form})

@user_passes_test(lambda u: u.is_superuser)
def equipment_imagen_upload_view(request, id):
    if request.method == "POST":
        modelo = Equipment.objects.get(id=id)
        ruta = modelo.imagen
        form = UploadImgForm(request.POST, request.FILES, instance=modelo)
        if form.is_valid():
            import os
            from django.conf import settings
            os.remove(os.path.join(settings.MEDIA_ROOT,str(ruta)))
            form.save()
            return redirect('equipment_view', id=id)
    else:
        modelo = Equipment.objects.get(id=id)
        form = UploadImgForm(request.POST, instance=modelo)

    return render(request, 'equipment/imagen.html', {'form': form, 'modelo': modelo})

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
        'location__name',  # Accedemos al nombre de la ubicación a través de la relación ForeignKey
        'location__color',
    )
    return JsonResponse({'equipment': list(db_request1)}, safe=False)
