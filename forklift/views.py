from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .models import Forklifts, ForkliftOwners, ForkliftStatus, ForkliftServiceProviders, ForkliftBrands
from django.db.models import Count, Value, Q
from django.db.models.functions import Coalesce
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from .forms import ForkliftForm, UploadImgForm, CreateForkliftForm

from .forms import CreateForkliftOwnersForm
@login_required
def forklift_index(request):
    return render(request, 'forklifts/index.html')

@login_required
def forklift_view(request, id):
    query = get_object_or_404(Forklifts, id=id)
    if request.method == 'POST':
        form = ForkliftForm(request.POST, instance=query)
        if form.is_valid():
            if user_passes_test(lambda u: u.is_superuser):
                frk = form.save()
                return redirect('forklift_view', id=frk.id)
            else:
                return render(request, 'forklifts/view.html.html', {'data_db': db_request, 'form': form})
        else:
                form = ForkliftForm()
                for field, errors in form.errors.items():
                        for error in errors:
                            messages.error(request, f"{field}: {error}")
        return render(request, 'forklifts/view.html.html', {'form': form, 'db_response':query})
    else:
        query = get_object_or_404(Forklifts, id=id)
        form = ForkliftForm(instance=query)
        return render(request, 'forklifts/view.html', {'form': form, 'db_response':query})
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
def forklift_imagen_upload(request, id):
    if request.method == "POST":
        modelo = Forklifts.objects.get(id=id)
        ruta = modelo.imagen
        form = UploadImgForm(request.POST, request.FILES, instance=modelo)
        if form.is_valid():
            import os
            from django.conf import settings
            os.remove(os.path.join(settings.MEDIA_ROOT,str(ruta)))
            form.save()
            return redirect('forklift_view', id=id)
    else:
        modelo = Forklifts.objects.get(id=id)
        form = UploadImgForm(request.POST, instance=modelo)
    return render(request, 'forklifts/imagen.html', {'form': form, 'modelo': modelo})
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
            response_data = {'mensaje': 'Registro eliminado exitosamente.'}
        except User.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)



#FORKLIFT HOLDERS
#FORLKIFT HOLDERS INDEX
@staff_member_required
def forklift_holders(request):
    return render(request, 'forklifts/holders/index.html')
#FORKLIFT HOLDERS VIEW
@staff_member_required
def forklift_holders_view(request, id):
    query = get_object_or_404(ForkliftOwners, id=id)
    return render(request, 'forklifts/holders/view.html',{'data':query})
#FORKLIFT HOLDERS EDIT
@user_passes_test(lambda u: u.is_superuser)
def forklift_holders_edit(request, id):
    query = get_object_or_404(ForkliftOwners, id=id)
    if request.method == 'POST':
        new_frk = form = CreateForkliftOwnersForm(request.POST, request.FILES, instance=query)
        if form.is_valid():
            form.save()
            return redirect('forklift_holders_view', id=query.id)
    else:
        query = get_object_or_404(ForkliftOwners, id=id)
        form = CreateForkliftOwnersForm(instance=query)
    return render(request, 'forklifts/holders/edit.html', {'form': form,'data':query})
#FORKLIFT HOLDERS ADD
@user_passes_test(lambda u: u.is_superuser)
def forklift_holders_add(request):
    if request.method == 'POST':
        form = CreateForkliftOwnersForm(request.POST, request.FILES)
        if form.is_valid():
            new_frk = form.save()
            return redirect('forklift_holders_view', id=new_frk.id)
    else:
        form = CreateForkliftOwnersForm()
    return render(request, 'forklifts/holders/edit.html', {'form': form})
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
            response_data = {'mensaje': 'Registro eliminado exitosamente.'}
        except User.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)



#FO    
@login_required
def forklift_service_providers(request):
    return render(request, 'forklifts/service_providers/index.html')
@login_required
def forklift_brands(request):
    return render(request, 'forklifts/brands/index.html')

@login_required
def forklift_status(request):
    forklift_statuses = ForkliftStatus.objects.all()
    for status in forklift_statuses:
        statusconteo = Forklifts.objects.filter().count()
        status.count = Forklifts.objects.filter(status=status).count()
        status.forklifts = Forklifts.objects.filter(status=status)

    return render(request, 'forklifts/status/index.html', {'status_counts': forklift_statuses, 'conteo':statusconteo})
@login_required
def inspection_sheet_language(request):
    return render(request, 'forklifts/sheet/index.html')

@login_required
def inspection_sheet_form_es(request):
    return render(request, 'forklifts/sheet/sheet_es.html')

@login_required
def inspection_sheet_form_en(request):
    return render(request, 'forklifts/sheet/sheet_en.html')
@login_required
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

@login_required
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

@login_required
def api_pull_serviceproviders(request):
    providers = ForkliftServiceProviders.objects.all()

    data = [{"imagen": str(provider.imagen), "id": provider.id, "name": provider.name} for provider in providers]

    # Wrapping the data in a named variable
    response = {
        "providers_data": data
    }

    return JsonResponse(response, safe=False)

@login_required
def api_pull_brands(request):
    brands = ForkliftBrands.objects.all()

    data = [{"imagen": str(brand.imagen), "color": brand.color, "id": brand.id, "name": brand.name} for brand in brands]
    response = {
        "brands_data": data
    }

    return JsonResponse(response, safe=False)

def api_pull_experimental(request, id):
    statuses = ForkliftStatus.objects.annotate(
    forklift_count=Count('forklifts__id', filter=Q(forklifts__owner_id=id))
    )

    # Crear un diccionario para almacenar los resultados
    status_counts = {(status.name, status.color): status.forklift_count for status in statuses}

    # Renderizar la plantilla con el diccionario 'status_counts'
    return render(request, 'forklifts/misc/status_holders.html', {'status_counts': status_counts})
