from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

#VISTA PARA LOG-IN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('floatingInput')
        password = request.POST.get('floatingPassword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../')
        else:
            return render(request, 'autentificacion/sign-in.html', {'error': 'Invalid login credentials'})
    return render(request, 'autentificacion/sign-in.html')

#VISTA PARA LOG-OUT
def logout_view(request):
    logout(request)
    return render(request, 'autentificacion/logout.html')