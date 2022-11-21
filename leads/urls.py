
from django.urls import path
from .views import lead_list, lead_dettail 

app_name = "leads"

urlpatterns = [
    path('', lead_list),
    path('<pk>', lead_dettail)
]