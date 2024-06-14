from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import  (
    ListView, 
    DetailView,
    CreateView,
    TemplateView
)

from .models import Empleado
# Create your views here.


class InicioView(TemplateView):
    template_name = "inicio.html"




class ListaAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 3
    ordering = 'id'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'id'
    context_object_name = 'empleados'
    model = Empleado


class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        # se recibe variable de la url
        area = self.kwargs['shortname'] 
        lista = Empleado.objects.filter(
            departamento__short_name = area
        )
        return lista

class ListEmpleadosByWork(ListView):
    """ Lista a través de empleados """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('******************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        print('lista resultado: ', lista)
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"


class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    fields = ('__all__')
    success_url = '.'
