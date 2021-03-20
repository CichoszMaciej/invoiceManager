from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from users.forms import EmployeeCreate, EmployeeChange
from users.models import Employee


@login_required()
def users_list(request):
    users = Employee.objects.all()
    info = ''
    if 'info' in request.GET:
        info = request.GET['info']
    context = {
        'users': users,
        'length': len(users),
        'info': info
    }

    return render(request, 'users/list_users.html', context)


@login_required()
def add_user(request):
    if request.method == 'POST':
        form = EmployeeCreate(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect(reverse(users_list) + '?info=success')
        else:
            return render(request, 'users/new_user.html', {'form': form})

    else:
        context = {
            'form': EmployeeCreate()
        }

        return render(request, 'users/new_user.html', context)


@login_required()
def edit_user(request, user_id):
    user = get_object_or_404(Employee, pk=user_id)
    if request.method == 'POST':
        form = EmployeeChange(request.POST, instance=user)
        if form.is_valid():
            u = form.save(commit=False)
            u.save()
            return HttpResponseRedirect(reverse(users_list) + '?info=success-edit')
        else:
            return render(request, 'users/edit_user.html', {'form': form, 'username': user.username})

    else:
        return render(request, 'users/edit_user.html',
                      {'form': EmployeeChange(instance=user), 'username': user.username})


@login_required()
def delete_user(request, user_id):
    user = Employee.objects.get(pk=user_id)
    if 'd' in request.GET and request.GET['d'] == 'yes':
        user.delete()
        return HttpResponseRedirect(reverse(users_list) + '?info=delete')
    else:
        return render(request, 'users/delete_user.html', {'user': user})
