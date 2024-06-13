from django.shortcuts import render

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import  (
    ListView, 
    DetailView,
    CreateView,
    TemplateView
)

from .models import Departamento
# Create your views here.


class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'

