from django.urls import path
from . import views

urlpatterns = [
    path('new-donor', views.new_donor.as_view(), name='new_donor'),
    path('donor-list', views.donor_list_view.as_view(), name='donor-list'),
]
