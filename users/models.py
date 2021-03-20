from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class EmployeeManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            password=password,
            username=username,
            email=self.normalize_email(email),
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True, null=False)
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    address = models.CharField(max_length=64, null=True)
    email = models.EmailField(verbose_name="email", max_length=60, null=True)
    date_joined = models.DateTimeField(verbose_name='Data dolaczenia', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Ostatnie logowanie', auto_now=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = EmployeeManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
