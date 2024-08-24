from django.urls import path
from . import views

urlpatterns = [
    path('new-donor', views.new_donor.as_view(), name='new_donor'),
    # path('blood_groups', views.blood_group_list_view.as_view(), name='blood_group_list'),
]
