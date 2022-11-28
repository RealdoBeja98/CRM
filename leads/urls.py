
from django.urls import path
from .views import (lead_list, lead_dettail, lead_create, lead_update, lead_delete,
    LeadListView, LeadDettailView, LeadCreateView, LeadUpdateView, LeadDeleteView
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDettailView.as_view(), name='lead-dettail'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),

]