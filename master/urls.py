from django.urls import path
from . import views

urlpatterns = [
    path('districts', views.district_list_view.as_view(), name='district_list'),
    path('blood_groups', views.blood_group_list_view.as_view(), name='blood_group_list'),
]
