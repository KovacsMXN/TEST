from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserChangeForm, SetPasswordForm
from django.urls import reverse

from .models import UsersExtension

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .forms import CustomUsersExtension

####GENERIC VIEWS FOR STAFF####
#VIEW FOR STAFF INDEX
@user_passes_test(lambda u: u.is_superuser)
def staff_index(request):
	return render(request, 'staff/index.html')

#VIEW FOR VIEW STAFF
@user_passes_test(lambda u: u.is_superuser)
def staff_view(request, id):
    query = get_object_or_404(User, id=id)
    extension_values = {
    'numeroempleado': '9999',  
    'language': 'ES',           
    }
    user_extension, created = UsersExtension.objects.get_or_create(user=query, defaults=extension_values)
    return render(request, 'staff/view.html', {'data': query, 'user_extension': user_extension})


#VIEW FOR STAFF EDIT
@user_passes_test(lambda u: u.is_superuser)
def staff_add(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form.fields['password1'].widget.attrs['class'] = 'form-control'
        form.fields['password2'].widget.attrs['class'] = 'form-control'
        if form.is_valid():
            user = form.save()
            return redirect('staff_view', id=user.id)
    else:
        form = CustomUserCreationForm()
        form.fields['password1'].widget.attrs['class'] = 'form-control'
        form.fields['password2'].widget.attrs['class'] = 'form-control'

    return render(request, 'staff/create.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def staff_edit(request, id):
    user = get_object_or_404(User, id=id)
    users_extension_instance, created = UsersExtension.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        user_extension_form = CustomUsersExtension(request.POST, instance=users_extension_instance)

        if form.is_valid() and user_extension_form.is_valid():
            user = form.save()
            user_extension = user_extension_form.save()
            return redirect('staff_view', id=user.id)
    else:
        form = CustomUserChangeForm(instance=user)
        user_extension_form = CustomUsersExtension(instance=users_extension_instance)

    return render(request, 'staff/edit.html', {'form': form, 'data': user, 'user_extension_form': user_extension_form})


#VIEW FOR STAFF PASSWORD EDIT
@user_passes_test(lambda u: u.is_superuser)
def staff_password_edit(request, id):
	if request.method == 'POST':
		registro = get_object_or_404(User, id=id)
		form = SetPasswordForm(registro, request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('staff_view', id=user.id)
		else:
			messages.error(request, 'Please correct the error below.')
			return redirect('staff_index')
	else:
		query = get_object_or_404(User, id=id)
		form = SetPasswordForm(request.user)
		form.fields['new_password1'].widget.attrs['class'] = 'form-control'
		form.fields['new_password2'].widget.attrs['class'] = 'form-control'
		return render(request, 'staff/updatepassword.html', {'form': form, 'data':query})

####JSON VIEWS FOR STAFF####
#PULL USERS
@user_passes_test(lambda u: u.is_superuser)
def staff_json_response(request):
    db_request1 = list(User.objects.values('id','first_name', 'last_name', 'username', 'is_active', 'is_staff', 'is_superuser'))
    data = {'usuarios':db_request1}
    return JsonResponse(data)

#DELETE USER
@user_passes_test(lambda u: u.is_superuser)
def staff_json_delete(request, id):
    if request.method == 'POST':
        try:
        	registro = get_object_or_404(User, id=id)
        	registro.delete()
        	return redirect('staff_index')
        except User.DoesNotExist:
            response_data = {'mensaje': 'El registro no existe.'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)