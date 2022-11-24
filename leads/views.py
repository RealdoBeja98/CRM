from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

# Create your views here.

def lead_list(request):
    #return HttpResponse("Hello world")
    leads = Lead.objects.all()
    context = {
        "leads" : leads
    }
    return render(request, "lead_list.html", context) 

def lead_dettail(request, pk): #pk is primary key
    lead = Lead.objects.get(id = pk)
    context = {
        "lead" : lead
    }
    return render(request, "lead_dettail.html", context )

def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("/leads/")
    context = {
        "form" : form
    }
    return render(request, "lead_create.html", context)

def lead_update(request, pk):
    lead = Lead.objects.get(id = pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect ("/leads/")
    context = {
        "form" : form,
        "lead" : lead
    }
    return render(request, "lead_update.html", context)

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
# def lead_create(request):
#     form = LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 firstName = first_name,
#                 lastName = last_name,
#                 age = age,
#                 agent = agent
#             )
#             print("Lead created")
#             return redirect ("/leads/")
#     context = {
#         "form" : form
#     }
#     return render(request, "lead_create.html", context)