from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import Employee


class EmployeeCreate(UserCreationForm):
    class Meta:
        model = Employee
        exclude = ('password',)


class EmployeeChange(UserChangeForm):
    class Meta:
        model = Employee
        exclude = ('username',)
