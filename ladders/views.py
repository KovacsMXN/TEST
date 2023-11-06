from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def ladders_index(request):
    return render(request, 'ladders/index.html')