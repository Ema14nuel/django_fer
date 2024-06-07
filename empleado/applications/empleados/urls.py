from django.urls import path
from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListaAllEmpleados.as_view()),
    path('listar-by-area/<shortname>/', views.ListByAreaEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByWork.as_view()),
    path('lista-habilidaes-empleado/', views.ListHabilidadesEmpleado.as_view()),
]