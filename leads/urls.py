
from django.urls import path
from .views import lead_list, lead_dettail, lead_create 

app_name = "leads"

urlpatterns = [
    path('', lead_list),
    path('<int:pk>/', lead_dettail),
    path('create/', lead_create)

]