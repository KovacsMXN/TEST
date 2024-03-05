import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from datetime import date, datetime, timedelta, timezone
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db import transaction

#IMPORT DB MODELS
from .models import Scales, ScalesServiceProviders, ScalesBrands, ScalesStatus

#IMPORT FORMS 
from .forms import CreateScaleForm, CreateScaleBrands, CreateScaleStatus, CreateScaleServiceProviderForm

'''
"""""""""""""""""""""""""""""""""""""""""
""                                     ""
""  SECCION PARA LAS VISTAS DE SCALES  ""
""                                     ""
"""""""""""""""""""""""""""""""""""""""""
'''
#VIEW SCALE INDEX
@login_required
@permission_required("scales.view_scales", raise_exception=True)
def scales_index(request):
    return render(request, 'scales/index.html')

#VIEW SCALES JSON RESPONSE
@login_required
@permission_required("scales.view_scales", raise_exception=True)
def scales_index_json(request):
    query = list(Scales.objects.values("id","clave","brand__name","brand__color","service_provider__name","modelo","serial","nmax","clase","powersupply","imagen","status__name","status__color"))
    data = {'ladders':query}
    return JsonResponse(data)

#VIEW SCALE VIEW INDEX
@login_required
@permission_required("scales.view_scales", raise_exception=True)
def scales_view(request, id):
    query = get_object_or_404(Scales, id=id)
    status_color = query.status.color
    query2 = ScalesServiceProviders.objects.filter(scales=id)
    return render(request, 'scales/view.html',{'db_response':query,'status_color':status_color,'db_response2':query2})

#VIEW SCALE ADD INDEX
@login_required
@permission_required("scales.add_scales", raise_exception=True)
def scales_add(request):
    if request.method == 'POST':
        form = CreateScaleForm(request.POST, request.FILES)
        if form.is_valid():
            new_frk = form.save()
            return redirect('scales_view', id=new_frk.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CreateScaleForm()
    return render(request, 'scales/create.html', {'form': form})

#VIEW SCALE EDIT INDEX
@login_required
@permission_required("scales.change_scales", raise_exception=True)
def scales_edit(request, id):
    query = get_object_or_404(Scales, id=id)
    imagen_anterior = query.imagen  # Guarda la referencia a la imagen anterior

    if request.method == 'POST':
        form = CreateScaleForm(request.POST, request.FILES, instance=query)
        if form.is_valid():
            if 'imagen' in request.FILES:
                if imagen_anterior:
                    imagen_anterior_path = imagen_anterior.path
                    if os.path.exists(imagen_anterior_path):
                        os.remove(imagen_anterior_path)
            form.save()  # Guardar el formulario
            return redirect('scales_view', id=query.id)
    else:
        query = get_object_or_404(Scales, id=id)
        form = CreateScaleForm(instance=query)
    return render(request, 'scales/edit.html', {'form': form,'data':query})

#VIEW SCALE DELETE INDEX    
@login_required
@permission_required("scales.delete_scales", raise_exception=True)
@require_POST
def scales_delete(request, id):
    registro = get_object_or_404(Scales, id=id)
    ruta = registro.imagen.path
    if os.path.exists(ruta):
        os.remove(ruta)
    registro.delete()
    return redirect('scales_index_view')

'''
"""""""""""""""""""""""""""""""""""""""""
""                                     ""
""  SECCION PARA LAS VISTAS DE BRANDS  ""
""                                     ""
"""""""""""""""""""""""""""""""""""""""""
'''
#VIEW SCALE INDEX
@login_required
@permission_required("scales.view_scalesbrands", raise_exception=True)
def scale_brands(request):
    return render(request, 'scales/brands/index.html')

#VIEW SCALE INDEX
@login_required
@permission_required("scales.view_scalesbrands", raise_exception=True)
def scales_brands_json(request):
    query = list(ScalesBrands.objects.values(
        'id',
        'color',
        'name',
        'imagen'))
    data = {'brands':query}
    return JsonResponse(data)

#VIEW SCALE VIEW
@login_required
@permission_required("scales.view_scalesbrands", raise_exception=True)
def scales_brands_view(request, id):
    query = get_object_or_404(ScalesBrands, id=id)
    return render(request, 'scales/brands/view.html', {'data':query})

#VIEW SCALE INDEX
@login_required
@permission_required("scales.change_scalesbrands", raise_exception=True)
def scales_brands_edit(request,id):
    query_instance = get_object_or_404(ScalesBrands, id=id)
    imagen_anterior = query_instance.imagen
    if request.method == 'POST':
        form = CreateScaleBrands(request.POST, request.FILES, instance=query_instance)
        if form.is_valid():
            if 'imagen' in request.FILES:
                if imagen_anterior:
                    imagen_anterior_path = imagen_anterior.path
                    if os.path.exists(imagen_anterior_path):
                        os.remove(imagen_anterior_path)
            form.save()
            return redirect('scales_brands_view', id=query_instance.id)
    else:
        query = get_object_or_404(ScalesBrands, id=id)
        form = CreateScaleBrands(instance=query)
    return render(request, 'scales/brands/edit.html', {'form': form,'data':query})

#VIEW SCALE ADD
@login_required
@permission_required("scales.add_scalesbrands", raise_exception=True)
def scales_brands_add(request):
    if request.method == 'POST':
        form = CreateScaleBrands(request.POST, request.FILES)
        if form.is_valid():
            new_frk = form.save()
            return redirect('scales_brands_view', id=new_frk.id)
    else:
        form = CreateScaleBrands()
    return render(request, 'scales/brands/add.html', {'form': form})

#VIEW SCALE DELETE
@login_required
@permission_required("scales.delete_scalesbrands", raise_exception=True)
@require_POST
def scales_brands_delete(request, id):
    registro = get_object_or_404(ScalesBrands, id=id)
    ruta = registro.imagen.path
    if os.path.exists(ruta):
        os.remove(ruta)
    registro.delete()
    return redirect('scale_brands_view')

'''
"""""""""""""""""""""""""""""""""""""""""
""                                     ""
""  SECCION PARA LAS VISTAS DE STATUS  ""
""                                     ""
"""""""""""""""""""""""""""""""""""""""""
'''
#VIEW SCALE STATUS
@login_required
@permission_required("scales.view_scalesstatus", raise_exception=True)
def scales_status(request):
    if not ScalesStatus.objects.exists():
        with transaction.atomic():
            default_status = ScalesStatus.objects.create(name="Default Status (Rename)",color="#98eb34")
            default_status.save()
    query = ScalesStatus.objects.all()
    for status in query:
        statusconteo = Scales.objects.filter().count()
        status.count = Scales.objects.filter(status=status).count()
        status.objs = Scales.objects.filter(status=status)

    return render(request, 'scales/status/index.html', {'status_counts': query, 'conteo':statusconteo})

#VIEW SCALE STATUS VIEW
@login_required
@permission_required("scales.view_scalesstatus", raise_exception=True)
def scales_status_view(request, id):
    query = get_object_or_404(ScalesStatus, id=id)
    query_conteo = Scales.objects.filter(status_id=id)
    conteo = query_conteo.count()
    return render(request, 'scales/status/view.html', {'data':query, 'conteo':conteo, 'mas_data':query_conteo})

#VIEW SCALE STATUS EDIT
@login_required
@permission_required("scales.change_scalesstatus", raise_exception=True)
def scales_status_edit(request,id):
    query = get_object_or_404(ScalesStatus, id=id)
    if request.method == 'POST':
        new_frk = form = CreateScaleStatus(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('scales_status_view', id=query.id)
    else:
        query = get_object_or_404(ScalesStatus, id=id)
        form = CreateScaleStatus(instance=query)
    return render(request, 'scales/status/edit.html', {'form': form,'data':query})

#VIEW SCALE STATUS ADD
@login_required
@permission_required("scales.add_scalesstatus", raise_exception=True)
def scales_status_add(request):
    if request.method == 'POST':
        form = CreateScaleStatus(request.POST, request.FILES)
        if form.is_valid():
            new_frk = form.save()
            return redirect('scales_status_view', id=new_frk.id)
    else:
        form = CreateScaleStatus()
    return render(request, 'scales/status/add.html', {'form': form})

#VIEW SCALE STATUS DELETE
@login_required
@permission_required("scales.delete_scalesstatus", raise_exception=True)
@require_POST
def scales_status_delete(request, id):
    registro = get_object_or_404(ScalesStatus, id=id)
    registro.delete()
    return redirect('scales_status_index')

'''
"""""""""""""""""""""""""""""""""""""""""
""                                     ""
""  SECCION PARA LAS VISTAS DE SERVICE ""
""                                     ""
"""""""""""""""""""""""""""""""""""""""""
'''
#VIEW SCALE SERVICE PROVIDERS
@login_required
@permission_required("scales.view_scalesserviceproviders", raise_exception=True)
def scales_serviceprovider(request):
    query = ScalesServiceProviders.objects.all()
    return render(request, 'scales/service/index.html', {'data': query})

#VIEW SCALE STATUS VIEW
@login_required
@permission_required("scales.view_scalesserviceproviders", raise_exception=True)
def scales_serviceprovider_view(request, id):
    query = get_object_or_404(ScalesServiceProviders, id=id)
    return render(request, 'scales/service/view.html', {'data':query})

#VIEW SCALE STATUS EDIT
@login_required
@permission_required("scales.change_scalesserviceproviders", raise_exception=True)
def scales_serviceprovider_edit(request,id):
    query = get_object_or_404(ScalesServiceProviders, id=id)
    imagen_anterior = query.imagen
    form = CreateScaleServiceProviderForm(request.POST, request.FILES, instance=query)
    if form.is_valid():
        if 'imagen' in request.FILES:
            if imagen_anterior:
                imagen_anterior_path = imagen_anterior.path
                if os.path.exists(imagen_anterior_path):
                    os.remove(imagen_anterior_path)
                    form.save()  # Guardar el formulario
            return redirect('scales_serviceprovider_view', id=query.id)
    else:
        query = get_object_or_404(ScalesServiceProviders, id=id)
        form = CreateScaleServiceProviderForm(instance=query)
    return render(request, 'scales/service/edit.html', {'form': form,'data':query})

#VIEW SCALE STATUS ADD
@login_required
@permission_required("scales.add_scalesserviceproviders", raise_exception=True)
def scales_serviceprovider_add(request):
    if request.method == 'POST':
        form = CreateScaleServiceProviderForm(request.POST, request.FILES)
        if form.is_valid():
            new_frk = form.save()
            return redirect('scales_serviceprovider_view', id=new_frk.id)
    else:
        form = CreateScaleServiceProviderForm()
    return render(request, 'scales/service/add.html', {'form': form})

#VIEW SCALE STATUS DELETE
@login_required
@permission_required("scales.delete_scalesserviceproviders", raise_exception=True)
@require_POST
def scales_serviceprovider_delete(request, id):
    registro = get_object_or_404(ScalesServiceProviders, id=id)
    ruta = registro.imagen.path
    if os.path.exists(ruta):
        os.remove(ruta)
    registro.delete()
    return redirect('scales_serviceprovider_index')