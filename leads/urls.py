
from django.urls import path
from .views import lead_list, lead_dettail, lead_create, lead_update, lead_delete

app_name = "leads"

urlpatterns = [
    path('', lead_list),
    path('<int:pk>/', lead_dettail),
    path('create/', lead_create),
    path('<int:pk>/update/', lead_update),
    path('<int:pk>/delete/', lead_delete),

]