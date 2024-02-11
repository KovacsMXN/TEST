from django.shortcuts import render, redirect, get_object_or_404

import os
from decimal import Decimal, ROUND_DOWN
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from datetime import date, datetime, timedelta, timezone
import calendar

from django.http import JsonResponse, HttpResponse

from django.db.models import Count, Value, Q
from django.db.models.functions import Coalesce

from django.urls import reverse

from django.core.paginator import Paginator

#IMPORT FORMS
from .forms import ForkliftForm, CreateForkliftForm, CreateServiceProviderForm
from .forms import CreateForkliftOwnersForm
from .forms import CreateForkliftBrands
from .forms import CreateForkliftStatus
from .forms import CreateForkliftLOTO
from .forms import SearchForm
from .forms import WaterTrackForm

from .forms import EsInspectionForm, EnInspectionForm
from .forms import DisEsInspectionForm, DisEnInspectionForm
from .forms import ReleaseInspectionForm

from .models import Loto
from .models import Forklifts, ForkliftOwners, ForkliftStatus, ForkliftServiceProviders, ForkliftBrands, InitialLoto

from .models import WaterEntry
from staff.models import UsersExtension
from .models import ForkliftInspection
def is_valid_queryparam(param):
    return param != '' and param is not None

@staff_member_required
def forklift_index(request):
    return render(request, 'forklifts/index.html')
    
def generate_water_track():
    forklifts = Forklifts.objects.filter(powered='E')
    water_entries = WaterEntry.objects.values('forklift_id', 'fecha')

    # Convertir los resultados en un diccionario para un acceso más rápido
    water_entry_dict = {entry['forklift_id']: entry['fecha'].date() for entry in water_entries if entry['fecha']}

    lista = []
    todaysdate = date.today()
    for forklift in forklifts:
        fecha_registro = water_entry_dict.get(forklift.id)

        if fecha_registro:
            days_diff = (todaysdate - fecha_registro).days
            if days_diff == 0:
                color = "#3ad353"  # Azul para el mismo día
            elif days_diff == 1:
                color = "#26a641"  # Rojo para 1 día de diferencia
            elif days_diff == 2:
                color = "#016d31"  # Verde para 2 días de diferencia
            elif days_diff == 3:
                color = "#0d4429"  # Verde oscuro para 3 días de diferencia
            else:
                color = "#161b22"  # Gris para más de 3 días
        else:
            color = "#212529"  # Gris por defecto si no hay registro

        lista.append((forklift, fecha_registro, color))

    return lista

@staff_member_required
def water_track(request):
    lista = generate_water_track()
    return render(request, 'forklifts/watertrack/index.html',{'forklifts':lista})

@staff_member_required
def water_track_add(request, id):
    forklift = get_object_or_404(Forklifts, id=id)
    usuario = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = WaterTrackForm(request.POST, forklift=forklift, usuario=usuario)
        if form.is_valid():
            new_frk = form.save(commit=False)
            new_frk.usuario = request.user
            new_frk.save()
            return redirect('forklift_view', id=forklift.id)
    else:
        form = WaterTrackForm(forklift=forklift,usuario=usuario)
    
    return render(request, 'forklifts/watertrack/add.html', {'form': form, 'forklift': forklift})

def generate_dates(year, id):
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    todaysdate = date.today()
    delta = timedelta(days=1)
    delta1 = timedelta(days=2)
    delta2 = timedelta(days=3)
    delta3 = timedelta(days=4)
    all_dates = []
    forklift = get_object_or_404(Forklifts, id=id)
    water_entry_dates = set(WaterEntry.objects.filter(fecha__year=year).filter(forklift=forklift).values_list('fecha__date', flat=True))

    current_date = start_date
    while current_date <= end_date:
        if current_date == todaysdate:
            color = "#0366d6"
        elif current_date in water_entry_dates:
            color = "#3ad353"  
        elif (current_date - delta) in water_entry_dates:
            color = "#26a641"
        elif (current_date - delta1) in water_entry_dates:
            color = "#016d31"
        elif (current_date - delta2) in water_entry_dates:
            color = "#0d4429"
        elif (current_date - delta3) in water_entry_dates:
            color = "#082e1b"
        else:
            color = "#04120b"

        all_dates.append((current_date, color))
        current_date += delta

    return all_dates

@staff_member_required
def forklift_view(request, id):
    forklifts = get_object_or_404(Forklifts, id=id)
    #CONDICIONAL STATUS LOCKOUT/TAGOUT
    if forklifts.status.id == 3:
        lotoid = get_object_or_404(InitialLoto, forklift=forklifts)
        query2 = ForkliftServiceProviders.objects.filter(forklifts=id)
        status_color = forklifts.status.color if forklifts.status else None
        today = datetime.now()
        year = today.year
        all_dates = generate_dates(year, id)
        var = type(all_dates)
        batery_days_ago = (today - forklifts.last_batery).days
        batery_procentaje = Decimal(batery_days_ago / (forklifts.batery_target*365)) *100
        batery_procentaje = batery_procentaje.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
        return render(request, 'forklifts/view.html', {'db_response':forklifts, 'db_response2': query2, 'status_color':status_color,'lotoid':lotoid,'year':year,'dates':all_dates,'var':var,'days_ago':batery_days_ago})
    #CONDICIONAL STATUS SERVICE
    elif forklifts.status.id == 2:
        query2 = ForkliftServiceProviders.objects.filter(forklifts=id)
        status_color = forklifts.status.color if forklifts.status else None
        today = datetime.now()
        year = today.year
        all_dates = generate_dates(year, id)
        var = type(all_dates)
        batery_days_ago = (today - forklifts.last_batery).days
        batery_procentaje = Decimal(batery_days_ago / (forklifts.batery_target*365)) *100
        batery_procentaje = batery_procentaje.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
        return render(request, 'forklifts/view.html', {'db_response':forklifts, 'db_response2': query2, 'status_color':status_color,'year':year,'dates':all_dates,'var':var,'days_ago':batery_days_ago})
    #CONDICIONAL STATUS AVAILABLE
    elif forklifts.status.id == 1:
        query2 = ForkliftServiceProviders.objects.filter(forklifts=id)
        status_color = forklifts.status.color if forklifts.status else None
        today = datetime.now(timezone.utc)
        year = today.year
        all_dates = generate_dates(year, id)
        var = type(all_dates)
        batery_days_ago = (today - forklifts.last_batery).days
        batery_procentaje = Decimal(batery_days_ago / (forklifts.batery_target*365)) *100
        batery_procentaje = batery_procentaje.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
        return render(request, 'forklifts/view.html', {'db_response':forklifts, 'db_response2': query2, 'status_color':status_color,'year':year,'dates':all_dates,'var':var,'days_ago':batery_days_ago,'batery_procentaje':batery_procentaje})

def forklift_edit(request, id):
    forklift_instance = get_object_or_404(Forklifts, id=id)
    imagen_anterior = forklift_instance.imagen  # Guarda la referencia a la imagen anterior

    if request.method == 'POST':
        form = ForkliftForm(request.POST, request.FILES, instance=forklift_instance)
        if form.is_valid():
            if 'imagen' in request.FILES:
                if imagen_anterior:
                    imagen_anterior_path = imagen_anterior.path
                    if os.path.exists(imagen_anterior_path):
                        os.remove(imagen_anterior_path)
            form.save()  # Guardar el formulario
            return redirect('forklift_view', id=forklift_instance.id)
    else:
        query = get_object_or_404(Forklifts, id=id)
        form = ForkliftForm(instance=query)
    return render(request, 'forklifts/edit.html', {'form': form,'data':query})

@user_passes_test(lambda u: u.is_superuser)
def forklift_add(request):
    if request.method == 'POST':
        form = CreateForkliftForm(request.POST, request.FILES)
        if form.is_valid():
            new_frk = form.save()
            return redirect('forklift_view', id=new_frk.id)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CreateForkliftForm()
    return render(request, 'forklifts/create.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def api_del_forklifts(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(Forklifts, id=id)
            ruta = registro.imagen
            import os
            from django.conf import settings
            os.remove(os.path.join(settings.MEDIA_ROOT,str(ruta)))
            registro.delete()
            return redirect('forklift_index_view')
        except Forklifts.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)



#FORKLIFT HOLDERS
#HOLDERS
@staff_member_required
def forklift_holders(request):
    return render(request, 'forklifts/holders/index.html')

@staff_member_required
def forklift_holders_view(request, id):
    query = get_object_or_404(ForkliftOwners, id=id)
    return render(request, 'forklifts/holders/view.html',{'data':query})

@user_passes_test(lambda u: u.is_superuser)
def forklift_holders_edit(request, id):
    query_instance = get_object_or_404(ForkliftOwners, id=id)
    imagen_anterior = query_instance.imagen  # Guarda la referencia a la imagen anterior
    if request.method == 'POST':
        form = CreateForkliftOwnersForm(request.POST, request.FILES, instance=query_instance)
        if form.is_valid():
            if 'imagen' in request.FILES:
                if imagen_anterior:
                    imagen_anterior_path = imagen_anterior.path
                    if os.path.exists(imagen_anterior_path):
                        os.remove(imagen_anterior_path)
            form.save()  # Guardar el formulario
            return redirect('forklift_holders_view', id=query_instance.id)
    else:
        query = get_object_or_404(ForkliftOwners, id=id)
        form = CreateForkliftOwnersForm(instance=query_instance)
    return render(request, 'forklifts/holders/edit.html', {'form': form,'data':query_instance})

@user_passes_test(lambda u: u.is_superuser)
def forklift_holders_add(request):
    if request.method == 'POST':
        form = CreateForkliftOwnersForm(request.POST, request.FILES)
        if form.is_valid():
            new_frk = form.save()
            return redirect('forklift_holders_view', id=new_frk.id)
    else:
        form = CreateForkliftOwnersForm()
    return render(request, 'forklifts/holders/add.html', {'form': form})

#HOLDERS JSON
@user_passes_test(lambda u: u.is_superuser)
def api_del_forkliftowners(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(ForkliftOwners, id=id)
            ruta = registro.imagen
            import os
            from django.conf import settings
            os.remove(os.path.join(settings.MEDIA_ROOT,str(ruta)))
            registro.delete()
            return redirect('forklift_holders')
        except ForkliftOwners.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)



#SERVICE PROVIDERS    
@staff_member_required
def forklift_service_providers(request):
    return render(request, 'forklifts/service_providers/index.html')

@staff_member_required
def forklift_service_providers_view(request, id):
    query = get_object_or_404(ForkliftServiceProviders, id=id)
    return render(request, 'forklifts/service_providers/view.html', {'data':query})

@user_passes_test(lambda u: u.is_superuser)
def forklift_service_providers_add(request):
    if request.method == 'POST':
        form = CreateServiceProviderForm(request.POST, request.FILES)
        if form.is_valid():
            new_frk = form.save()
            return redirect('forklift_service_providers_view', id=new_frk.id)
    else:
        form = CreateServiceProviderForm()
    return render(request, 'forklifts/service_providers/add.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def forklift_service_providers_edit(request, id):
    query_instance = get_object_or_404(ForkliftServiceProviders, id=id)
    imagen_anterior = query_instance.imagen  # Guarda la referencia a la imagen anterior
    if request.method == 'POST':
        form = CreateForkliftOwnersForm(request.POST, request.FILES, instance=query_instance)
        if form.is_valid():
            if 'imagen' in request.FILES:
                if imagen_anterior:
                    imagen_anterior_path = imagen_anterior.path
                    if os.path.exists(imagen_anterior_path):
                        os.remove(imagen_anterior_path)
            form.save()  # Guardar el formulario
            return redirect('forklift_service_providers_view', id=query_instance.id)
    else:
        query = get_object_or_404(ForkliftServiceProviders, id=id)
        form = CreateServiceProviderForm(instance=query)
    return render(request, 'forklifts/service_providers/edit.html', {'form': form,'data':query})

@user_passes_test(lambda u: u.is_superuser)
def api_del_forklifts_service_provider(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(ForkliftServiceProviders, id=id)
            ruta = registro.imagen
            import os
            from django.conf import settings
            os.remove(os.path.join(settings.MEDIA_ROOT,str(ruta)))
            registro.delete()
            return redirect('forklift_brands')
        except ForkliftServiceProviders.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)



#BRANDS
@staff_member_required
def forklift_brands(request):
    return render(request, 'forklifts/brands/index.html')
@staff_member_required
def forklift_brands_view(request, id):
    query = get_object_or_404(ForkliftBrands, id=id)
    return render(request, 'forklifts/brands/view.html', {'data':query})
@user_passes_test(lambda u: u.is_superuser)
def forklift_brands_edit(request,id):
    query_instance = get_object_or_404(ForkliftBrands, id=id)
    imagen_anterior = query_instance.imagen  # Guarda la referencia a la imagen anterior
    if request.method == 'POST':
        form = CreateForkliftBrands(request.POST, request.FILES, instance=query_instance)
        if form.is_valid():
            if 'imagen' in request.FILES:
                if imagen_anterior:
                    imagen_anterior_path = imagen_anterior.path
                    if os.path.exists(imagen_anterior_path):
                        os.remove(imagen_anterior_path)
            form.save()  # Guardar el formulario
            return redirect('forklift_brands_view', id=query_instance.id)
    else:
        query = get_object_or_404(ForkliftBrands, id=id)
        form = CreateForkliftBrands(instance=query)
    return render(request, 'forklifts/brands/edit.html', {'form': form,'data':query})
@user_passes_test(lambda u: u.is_superuser)
def forklift_brands_add(request):
    if request.method == 'POST':
        form = CreateForkliftBrands(request.POST, request.FILES)
        if form.is_valid():
            new_frk = form.save()
            return redirect('forklift_brands_view', id=new_frk.id)
    else:
        form = CreateForkliftBrands()
    return render(request, 'forklifts/brands/add.html', {'form': form})
@user_passes_test(lambda u: u.is_superuser)
def api_del_forklifts_brands(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(ForkliftBrands, id=id)
            ruta = registro.imagen
            import os
            from django.conf import settings
            os.remove(os.path.join(settings.MEDIA_ROOT,str(ruta)))
            registro.delete()
            return redirect('forklift_brands')
        except ForkliftBrands.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

#STATUS
@staff_member_required
def forklift_status(request):
    forklift_statuses = ForkliftStatus.objects.all()
    for status in forklift_statuses:
        statusconteo = Forklifts.objects.filter().count()
        status.count = Forklifts.objects.filter(status=status).count()
        status.forklifts = Forklifts.objects.filter(status=status)
    return render(request, 'forklifts/status/index.html', {'status_counts': forklift_statuses, 'conteo':statusconteo})

@user_passes_test(lambda u: u.is_superuser)
def api_del_forklifts_status(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(ForkliftStatus, id=id)
            registro.delete()
            return redirect('forklift_status')
        except ForkliftStatus.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

@staff_member_required
def forklift_status_view(request, id):
    query = get_object_or_404(ForkliftStatus, id=id)
    query_conteo = Forklifts.objects.filter(status_id=id)
    conteo = query_conteo.count()
    return render(request, 'forklifts/status/view.html', {'data':query, 'conteo': conteo,'mas_data':query_conteo})

@user_passes_test(lambda u: u.is_superuser)
def forklift_status_edit(request,id):
    query = get_object_or_404(ForkliftStatus, id=id)
    if request.method == 'POST':
        new_frk = form = CreateForkliftStatus(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('forklift_status_view', id=query.id)
    else:
        query = get_object_or_404(ForkliftStatus, id=id)
        form = CreateForkliftStatus(instance=query)
    return render(request, 'forklifts/status/edit.html', {'form': form,'data':query})

@user_passes_test(lambda u: u.is_superuser)
def forklift_status_add(request):
    if request.method == 'POST':
        form = CreateForkliftStatus(request.POST)
        if form.is_valid():
            new_frk = form.save()
            return redirect('forklift_status_view', id=new_frk.id)
    else:
        form = CreateForkliftStatus()
    return render(request, 'forklifts/status/add.html', {'form': form})

@staff_member_required
def forklift_loto_log(request):
    qs = Loto.objects.all().order_by('-id')
    reason_contains_query = request.GET.get('title_contains')
    usuarioempezo = request.GET.get('title_or_author')
    usuariotermino = request.GET.get('title_or_author')
    title_or_author_query = request.GET.get('title_or_author')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    if request.method == 'POST':
        search = SearchForm(initial=request.POST)
        items = Loto.objects.all().order_by('-id')
        q = request.POST['q']
        q_clave = request.POST['q_clave']

        q_su = request.POST['formstartusuario']
        q_eu = request.POST['formendusuario']

        sdate_min = request.POST['sdate_min']
        sdate_max = request.POST['sdate_max']

        edate_min = request.POST['edate_min']
        edate_max = request.POST['edate_max']


        if is_valid_queryparam(q):
            qs = qs.filter(reason__icontains=q)
        elif is_valid_queryparam(q_clave):
            qs = qs.filter(forklift__clave__icontains=q_clave)
        if is_valid_queryparam(q) | is_valid_queryparam(q_clave):
            qs = qs.filter(Q(reason__icontains=q) & Q(forklift__clave__icontains=q_clave))

        if is_valid_queryparam(q_su):
            qs = qs.filter(startusuario=q_su)
        if is_valid_queryparam(q_eu):
            qs = qs.filter(endusuario=q_eu)

        if is_valid_queryparam(sdate_min):
            qs = qs.filter(start__gte=sdate_min)
        if is_valid_queryparam(sdate_max):
            qs = qs.filter(start__lt=sdate_max)


        if is_valid_queryparam(edate_min):
            qs = qs.filter(end__gte=edate_min)
        if is_valid_queryparam(edate_max):
            qs = qs.filter(end__lt=edate_max)

        paginator = Paginator(qs, 10)  # Show 10 items per page
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(request, 'forklifts/loto/log/index.html',{'page':page,'search':search})
    else:
        search = SearchForm()
        q = ""
        items = Loto.objects.all().order_by('-id')
        paginator = Paginator(items, 10)  # Show 10 items per page
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(request, 'forklifts/loto/log/index.html',{'page':page,'search':search})
@staff_member_required
def forklift_loto_log_view(request, id):
    query = get_object_or_404(Loto, id=id)
    query2  = get_object_or_404(Forklifts, id=query.forklift.id)
    status_color = query2.status.color if query2.status else None
    return render (request, 'forklifts/loto/log/view.html',{'query':query,'forklift':query2, 'status_color':status_color})

@staff_member_required
def forklift_loto_log_add(request, id):
    query = get_object_or_404(InitialLoto, id=id)
    user_creator = get_object_or_404(User, id=query.startusuario.id)
    exc = Loto(
            forklift = get_object_or_404(Forklifts, id=query.forklift.id),
            start = query.start,
            reason = query.reason,
            description = query.description,
            startusuario = user_creator,
            endusuario = get_object_or_404(User, username=request.user.username)
            )
    exc.save()
    if exc.id:
        query = get_object_or_404(InitialLoto, id=id)
        frk_query = get_object_or_404(Forklifts, id=query.forklift.id)
        frk_query.status = get_object_or_404(ForkliftStatus, id=1)
        frk_query.save()
        query.delete()
    return render(request, 'forklifts/loto/active/index.html')

@staff_member_required
def forklift_loto(request):
        typ = request.GET.get('typ')
        
        if typ == '2':
            items = InitialLoto.objects.all()
            paginator = Paginator(items, 10)  # Show 10 items per page
            page_number = request.GET.get('page')
            page = paginator.get_page(page_number)
            query= InitialLoto.objects.all().exclude(startusuario=request.user)
            return render(request, 'forklifts/loto/active/index.html',{'data':query})
        elif typ == '1':
            items = InitialLoto.objects.all()
            paginator = Paginator(items, 10)  # Show 10 items per page
            page_number = request.GET.get('page')
            page = paginator.get_page(page_number)
            query= InitialLoto.objects.all().filter(startusuario=request.user)
            return render(request, 'forklifts/loto/active/index.html',{'data':query})
        else:
            items = InitialLoto.objects.all()
            paginator = Paginator(items, 10)  # Show 10 items per page
            page_number = request.GET.get('page')
            page = paginator.get_page(page_number)
            query = InitialLoto.objects.all().order_by('-start')
            return render(request, 'forklifts/loto/active/index.html',{'data':query})

@staff_member_required
def forklift_loto_view(request,id):
    query = get_object_or_404(InitialLoto, id=id)
    query2  = get_object_or_404(Forklifts, id=query.forklift.id)
    status_color = query2.status.color if query2.status else None
    return render (request, 'forklifts/loto/active/view.html',{'query':query,'forklift':query2, 'status_color':status_color})

@staff_member_required
def forklift_loto_add(request, id):
    if request.method == 'POST':
        form = CreateForkliftLOTO(request.POST)
        if form.is_valid():
            modelo = get_object_or_404(Forklifts, id=id)
            new_post = form.save(commit=False)
            new_post.forklift = modelo
            new_post.startusuario = request.user
            new_post.save()
            query = get_object_or_404(Forklifts, id=new_post.forklift.id)
            sta = ForkliftStatus.objects.get(id=3)

            if new_post:
                query.status = sta
                query.save()
            return redirect('forklift_loto')
    else:
        form = CreateForkliftLOTO()
    return render (request, 'forklifts/loto/add.html',{'form':form})

@staff_member_required
def forklift_loto_delete(request, id):
    if request.method == 'POST':
        try:
            registro = get_object_or_404(InitialLoto, id=id)
            if registro.delete():
                fork = get_object_or_404(Forklifts, id=registro.forklift.id)
                obj = get_object_or_404(ForkliftStatus, id=1)
                fork.status = obj
                fork.save()
            return redirect('forklift_loto')
        except InitialLoto.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

@staff_member_required
def api_pull_forklifts(request):
    query = list(Forklifts.objects.values(
        'id',
        'clave',
        'modelo',
        'serial',
        'brand__name',
        'brand__color',
        'owner__name',
        'status__name',
        'status__color'))
    data = {'forklifts':query}
    return JsonResponse(data)

@staff_member_required
def api_pull_holders(request):
    owners = ForkliftOwners.objects.annotate(
        num_forklifts=Count('forklifts'),
    )
    owners_data = []
    for owner in owners:
        # Use Coalesce to handle cases where the count is None (0 for unlinked statuses)
        statuses = ForkliftStatus.objects.filter(forklifts__owner=owner).values('name').annotate(num_statuses=Coalesce(Count('id'), Value(0)))

        # Obtaining all ForkliftStatus that aren't linked to the owner
        unlinked_statuses = ForkliftStatus.objects.exclude(forklifts__owner=owner).values('name').annotate(num_statuses=Coalesce(Count('id'), Value(0)))

        all_statuses = list(statuses)# + list(unlinked_statuses)

        owner_data = {
            'imagen': str(owner.imagen),
            'id': owner.id,
            'name': owner.name,
            'num_forklifts': owner.num_forklifts,
            'statuses': all_statuses
        }
        owners_data.append(owner_data)
    response_data = {'owners': owners_data}
    return JsonResponse(response_data)

@staff_member_required
def api_pull_serviceproviders(request):
    providers = ForkliftServiceProviders.objects.all()

    data = [{"imagen": str(provider.imagen), "id": provider.id, "name": provider.name} for provider in providers]

    # Wrapping the data in a named variable
    response = {
        "providers_data": data
    }
    return JsonResponse(response, safe=False)

@staff_member_required
def api_pull_brands(request):
    brands = ForkliftBrands.objects.all()

    data = [{"imagen": str(brand.imagen), "color": brand.color, "id": brand.id, "name": brand.name} for brand in brands]
    response = {
        "brands_data": data
    }
    return JsonResponse(response, safe=False)

@staff_member_required
def api_pull_status(request, id):
    statuses = ForkliftStatus.objects.annotate(
    forklift_count=Count('forklifts__id', filter=Q(forklifts__owner_id=id))
    )
    status_counts = {(status.name, status.color): status.forklift_count for status in statuses}
    return render(request, 'forklifts/misc/status_holders.html', {'status_counts': status_counts})


@staff_member_required
def inspection(request):
    query = ForkliftInspection.objects.all().filter(valid=0)
    return render(request, 'forklifts/inspection/index.html',{'query':query})

@staff_member_required
def inspection_log(request):
    qs = ForkliftInspection.objects.all().order_by('-id')
    reason_contains_query = request.GET.get('title_contains')
    usuarioempezo = request.GET.get('title_or_author')
    usuariotermino = request.GET.get('title_or_author')
    title_or_author_query = request.GET.get('title_or_author')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    if request.method == 'POST':
        search = SearchForm(initial=request.POST)
        items = Loto.objects.all().order_by('-id')
        q_clave = request.POST['q_clave']
        q_su = request.POST['formstartusuario']

        sdate_min = request.POST['sdate_min']
        sdate_max = request.POST['sdate_max']

        if is_valid_queryparam(q_clave):
            qs = qs.filter(forklift__clave__icontains=q_clave)

        if is_valid_queryparam(q_su):
            qs = qs.filter(usuario=q_su)

        if is_valid_queryparam(sdate_min):
            qs = qs.filter(fecha__gte=sdate_min)
        if is_valid_queryparam(sdate_max):
            qs = qs.filter(fecha__lt=sdate_max)

        paginator = Paginator(qs, 10)  # Show 10 items per page
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(request, 'forklifts/inspection/log.html',{'page':page,'search':search})
    else:
        search = SearchForm()
        items = ForkliftInspection.objects.all().order_by('-id')
        paginator = Paginator(items, 10)  # Show 10 items per page
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(request, 'forklifts/inspection/log.html',{'page':page,'search':search})

@staff_member_required
def inspection_view(request, id):
    i = get_object_or_404(ForkliftInspection, id=id)
    form = DisEnInspectionForm(instance=i)
    return render(request, 'forklifts/inspection/view.html',{'form':form,'i':i})

@staff_member_required
def inspection_release(request, id):
   # Obtiene la instancia de ForkliftInspection
    inspection = get_object_or_404(ForkliftInspection, id=id)
    
    if request.method == 'POST':
        form = ReleaseInspectionForm(request.POST)
        if form.is_valid():
            # Cambia el valor de valid a 1 (True)
            inspection.valid = True
            
            # Guarda los cambios en la base de datos
            inspection.save()
            
            # Redirige a la vista de detalles o a donde desees
            return redirect('inspection')  # Ajusta la redirección según tu configuración
    else:
        form = ReleaseInspectionForm()
    
    return render(request, 'forklifts/inspection/release.html', {'form': form,'inspection':inspection})
@login_required
def inspection_sheet_language(request):
    usuario = get_object_or_404(User, id=request.user.id)
    query = get_object_or_404(UsersExtension, user=usuario)
    if query.language == "ES":
        return redirect('inspection_sheet_form_es')
    elif query.language == "EN":
        return redirect('inspection_sheet_form_en')
    else:
        return render(request, 'forklifts/sheet/index.html')

@login_required
def inspection_sheet_form_es(request):
    usuario = get_object_or_404(User, id=request.user.id)
    query = get_object_or_404(UsersExtension, user=usuario)

    if request.method == 'POST':
        form = EsInspectionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario = usuario
                
            if all(getattr(instance, f'check{i}') == False for i in range(1, 12)):
                instance.valid = 1
            else:
                instance.valid = 0
            instance.save()
            return redirect('ins_logout_view')  # Redirecciona a una nueva URL
        else:
            messages.error(request, 'Hubo errores en el formulario. Por favor, corrígelos.')

    else:
        form = EsInspectionForm()

    return render(request, 'forklifts/sheet/sheet_es.html', {
        'usuario': usuario,
        'query': query,
        'form': form
    })
@login_required
def inspection_sheet_form_en(request):
    usuario = get_object_or_404(User, id=request.user.id)
    query = get_object_or_404(UsersExtension, user=usuario)

    if request.method == 'POST':
        form = EnInspectionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario = usuario
                
            if all(getattr(instance, f'check{i}') == False for i in range(1, 12)):
                instance.valid = 1
            else:
                instance.valid = 0
            instance.save()
            return redirect('ins_logout_view')  # Redirecciona a una nueva URL
        else:
            messages.error(request, 'Hubo errores en el formulario. Por favor, corrígelos.')

    else:
        form = EnInspectionForm()

    return render(request, 'forklifts/sheet/sheet_en.html', {
        'usuario': usuario,
        'query': query,
        'form': form
    })