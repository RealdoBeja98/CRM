from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

class LandingPageView(TemplateView):
    template_name = "landings.html"

# Create your views here.

def landing_page(request):
    return render(request, "landings.html" ) 

class LeadListView(ListView):
    template_name = "lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

def lead_list(request):
    #return HttpResponse("Hello world")
    leads = Lead.objects.all()
    context = {
        "leads" : leads
    }
    return render(request, "lead_list.html", context) 

class LeadDettailView(DetailView):
    template_name = "lead_dettail.html"
    queryset = Lead.objects.all()
    

def lead_dettail(request, pk): #pk is primary key
    lead = Lead.objects.get(id = pk)
    context = {
        "lead" : lead
    }
    return render(request, "lead_dettail.html", context )

class LeadCreateView(CreateView):
    template_name = "lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

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

class LeadUpdateView(UpdateView):
    template_name = "lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

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

class LeadDeleteView(DeleteView):
    template_name = "lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
    