from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from configuracion.models import Equipment_Locations, Equipment

@login_required
def index(request):
    return render(request, 'index.html')

def equipment_index(request):
    db_request1 = Equipment_Locations.objects.all()
    db_request2 = Equipment.objects.all()
    return render(request, 'equipment/index.html', {'db_request1': db_request1,'db_request2':db_request2})

def equipment_request_json(request):
    db_request1 = list(Equipment.objects.values())
    data = {'equipment':db_request1}
    return JsonResponse(data)
