from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def stock_index(request):
    return render(request, 'inventory/index.html')

@login_required
def stock_motors_index(request):
    return render(request, 'inventory/motors/index.html')

@login_required
def stock_motorsbrands_index(request):
    return render(request, 'inventory/motors/index.html')