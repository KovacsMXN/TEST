from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def equipment_index(request):
    return render(request, 'forklifts/index.html')