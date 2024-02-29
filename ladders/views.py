from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Ladders
from django.http import JsonResponse, HttpResponse
from . models import LattersStatus, LattersMaterials, LattersBrands, LadderInspectionEntry
from datetime import date, datetime, timedelta, timezone
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
import os

from forklift.views import generate_water_track
from .forms import CreateLadderStatus, CreateLadderMaterials, CreateLadderBrands, CreateLadderForm, LadderInspectionForm

@staff_member_required
def ladders_index(request):
    return render(request, 'ladders/index.html')
@staff_member_required
def ladders_index_json(request):
    query = list(Ladders.objects.values(
        'id',
        'imagen',
        'clave',
        'brand',
        'brand__color',
        'brand__name',
        'modelo',
        'agregado',
        'material',
        'material__color',
        'material__name',
        'pasos',
        'status',
        'status__color',
        'status__name'))
    data = {'ladders':query}
    return JsonResponse(data)

@staff_member_required
def ladders_edit(request, id):
    query = get_object_or_404(Ladders, id=id)
    imagen_anterior = query.imagen  # Guarda la referencia a la imagen anterior

    if request.method == 'POST':
        form = CreateLadderForm(request.POST, request.FILES, instance=query)
        if form.is_valid():
            if 'imagen' in request.FILES:
                if imagen_anterior:
                    imagen_anterior_path = imagen_anterior.path
                    if os.path.exists(imagen_anterior_path):
                        os.remove(imagen_anterior_path)
            form.save()  # Guardar el formulario
            return redirect('ladders_view', id=query.id)
    else:
        query = get_object_or_404(Ladders, id=id)
        form = CreateLadderForm(instance=query)
    return render(request, 'ladders/edit.html', {'form': form,'data':query})

@staff_member_required
def ladders_view(request, id):
    query = get_object_or_404(Ladders, id=id)
    status_color = query.status.color
    return render(request, 'ladders/view.html',{'db_response':query,'status_color':status_color})



@user_passes_test(lambda u: u.is_superuser)
def ladders_add(request):
    if request.method == 'POST':
        form = CreateLadderForm(request.POST, request.FILES)
        if form.is_valid():
            new_frk = form.save()
            return redirect('ladders_view', id=new_frk.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CreateLadderForm()
    return render(request, 'ladders/create.html', {'form': form})




@user_passes_test(lambda u: u.is_superuser)
def ladders_delete(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(Ladders, id=id)
            ruta = registro.imagen
            import os
            from django.conf import settings
            os.remove(os.path.join(settings.MEDIA_ROOT,str(ruta)))
            registro.delete()
            return redirect('ladders_index_view')
        except Ladders.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)




@staff_member_required
def ladders_brands(request):
    return render(request, 'ladders/brands/index.html')
@staff_member_required
def ladders_brands_json(request):
    query = list(LattersBrands.objects.values(
        'id',
        'color',
        'name',
        'imagen'))
    data = {'brands':query}
    return JsonResponse(data)

#LADDER MATERIALS
@login_required
def ladders_materials(request):
    return render(request, 'ladders/materials/index.html')
@staff_member_required
def ladders_materials_json(request):
    query = list(LattersMaterials.objects.values(
        'id',
        'color',
        'name'))
    data = {'materiales':query}
    return JsonResponse(data)
@user_passes_test(lambda u: u.is_superuser)
def ladders_materials_add(request):
    if request.method == 'POST':
        form = CreateLadderMaterials(request.POST)
        if form.is_valid():
            new_frk = form.save()
            return redirect('ladders_materials_view', id=new_frk.id)
    else:
        form = CreateLadderMaterials()
    return render(request, 'ladders/status/add.html', {'form': form})
@staff_member_required
def ladders_materials_view(request, id):
    query = get_object_or_404(LattersMaterials, id=id)
    query_conteo = Ladders.objects.filter(status_id=id)
    conteo = query_conteo.count()
    return render(request, 'ladders/materials/view.html', {'data':query, 'conteo': conteo,'mas_data':query_conteo})
@user_passes_test(lambda u: u.is_superuser)
def ladders_materials_delete(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(LattersMaterials, id=id)
            registro.delete()
            return redirect('ladders_materials')
        except ForkliftStatus.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
@user_passes_test(lambda u: u.is_superuser)
def ladders_materials_edit(request,id):
    query = get_object_or_404(LattersMaterials, id=id)
    if request.method == 'POST':
        new_frk = form = CreateLadderMaterials(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('ladders_materials_view', id=query.id)
    else:
        query = get_object_or_404(LattersMaterials, id=id)
        form = CreateLadderMaterials(instance=query)
    return render(request, 'ladders/materials/edit.html', {'form': form,'data':query})



#BRANDS
@staff_member_required
def ladders_brands(request):
    return render(request, 'ladders/brands/index.html')
@staff_member_required
def ladders_brands_view(request, id):
    query = get_object_or_404(LattersBrands, id=id)
    return render(request, 'ladders/brands/view.html', {'data':query})
@user_passes_test(lambda u: u.is_superuser)
def ladders_brands_edit(request,id):
    query_instance = get_object_or_404(LattersBrands, id=id)
    imagen_anterior = query_instance.imagen  # Guarda la referencia a la imagen anterior
    if request.method == 'POST':
        form = CreateLadderBrands(request.POST, request.FILES, instance=query_instance)
        if form.is_valid():
            if 'imagen' in request.FILES:
                if imagen_anterior:
                    imagen_anterior_path = imagen_anterior.path
                    if os.path.exists(imagen_anterior_path):
                        os.remove(imagen_anterior_path)
            form.save()  # Guardar el formulario
            return redirect('ladders_brands_view', id=query_instance.id)
    else:
        query = get_object_or_404(LattersBrands, id=id)
        form = CreateLadderBrands(instance=query)
    return render(request, 'ladders/brands/edit.html', {'form': form,'data':query})
@user_passes_test(lambda u: u.is_superuser)
def ladders_brands_add(request):
    if request.method == 'POST':
        form = CreateLadderBrands(request.POST, request.FILES)
        if form.is_valid():
            new_frk = form.save()
            return redirect('ladders_brands_view', id=new_frk.id)
    else:
        form = CreateLadderBrands()
    return render(request, 'ladders/brands/add.html', {'form': form})
@user_passes_test(lambda u: u.is_superuser)
def ladders_brands_delete(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(LattersBrands, id=id)
            ruta = registro.imagen
            import os
            from django.conf import settings
            os.remove(os.path.join(settings.MEDIA_ROOT,str(ruta)))
            registro.delete()
            return redirect('ladders_brands')
        except LattersBrands.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)




#LADDER STATUS
@staff_member_required
def ladders_status(request):
    query = LattersStatus.objects.all()
    for status in query:
        statusconteo = Ladders.objects.filter().count()
        status.count = Ladders.objects.filter(status=status).count()
        status.objs = Ladders.objects.filter(status=status)
    return render(request, 'ladders/status/index.html', {'status_counts': query, 'conteo':statusconteo})
@user_passes_test(lambda u: u.is_superuser)
def ladders_status_add(request):
    if request.method == 'POST':
        form = CreateLadderStatus(request.POST)
        if form.is_valid():
            new_frk = form.save()
            return redirect('ladders_status_view', id=new_frk.id)
    else:
        form = CreateLadderStatus()
    return render(request, 'ladders/status/add.html', {'form': form})
@staff_member_required
def ladders_status_view(request, id):
    query = get_object_or_404(LattersStatus, id=id)
    query_conteo = Ladders.objects.filter(status_id=id)
    conteo = query_conteo.count()
    return render(request, 'ladders/status/view.html', {'data':query, 'conteo': conteo,'mas_data':query_conteo})
@user_passes_test(lambda u: u.is_superuser)
def ladders_status_delete(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(LattersStatus, id=id)
            registro.delete()
            return redirect('ladders_status')
        except ForkliftStatus.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
@user_passes_test(lambda u: u.is_superuser)
def ladders_status_edit(request,id):
    query = get_object_or_404(LattersStatus, id=id)
    if request.method == 'POST':
        new_frk = form = CreateLadderStatus(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('ladders_status_view', id=query.id)
    else:
        query = get_object_or_404(LattersStatus, id=id)
        form = CreateLadderStatus(instance=query)
    return render(request, 'ladders/status/edit.html', {'form': form,'data':query})



#LADDER INSPECTION    
@staff_member_required
def ladders_inspection(request):
    lista = generate_ladder_records()
    return render(request, 'ladders/inspection/index.html',{'ladders':lista})

@staff_member_required
def ladders_inspection_add(request, id):
    ladder = get_object_or_404(Ladders, id=id)
    usuario = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = LadderInspectionForm(request.POST, ladder=ladder, usuario=usuario)
        if form.is_valid():
            new_frk = form.save(commit=False)
            new_frk.usuario = request.user
            new_frk.save()
            return redirect('ladders_view', id=ladder.id)
    else:
        form = LadderInspectionForm(ladder=ladder,usuario=usuario)
    
    return render(request, 'ladders/inspection/add.html', {'form': form, 'ladder': ladder})

def generate_ladder_records():
    forklifts = Ladders.objects.all()
    water_entries = LadderInspectionEntry.objects.values('ladder_id', 'fecha')
    # Convertir los resultados en un diccionario para un acceso más rápido
    water_entry_dict = {entry['ladder_id']: entry['fecha'].date() for entry in water_entries if entry['fecha']}

    lista = []
    todaysdate = date.today()
    for forklift in forklifts:
        fecha_registro = water_entry_dict.get(forklift.id)
        monthinspection = LadderInspectionEntry.ha_sido_inspeccionado_este_mes(forklift.id)
        lastmonthinspection = LadderInspectionEntry.ha_sido_inspeccionado_el_mes_anterior(forklift.id)
        lastlastmonthinspection = LadderInspectionEntry.ha_sido_inspeccionado_dos_meses_atras(forklift.id)
        lista.append((forklift, fecha_registro, monthinspection, lastmonthinspection, lastlastmonthinspection))

    return lista