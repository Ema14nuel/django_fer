from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import  ListView

from .models import Empleado
# Create your views here.

class ListaAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 5
    ordering = 'first_name'
    model = Empleado

class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    
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