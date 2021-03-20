from django.urls import path

from users.views import users_list, add_user, edit_user, delete_user

urlpatterns = [
    path('', users_list, name='users_list'),
    path('add/', add_user, name='add_user'),
    path('edit/<int:user_id>', edit_user, name='edit_user'),
    path('delete/<int:user_id>', delete_user, name='delete_user')
]
