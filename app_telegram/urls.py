from django.urls import path
from .views import thanks, UserList

urlpatterns = [
    path('', thanks, name='parser'),
    path('users/', UserList.as_view(), name='user_list'),
]
