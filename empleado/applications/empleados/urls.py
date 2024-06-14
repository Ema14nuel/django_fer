from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(),
        name = 'inicio'
    ),
    path(
        'listar-todo-empleados/', 
        views.ListaAllEmpleados.as_view(),
        name = 'empleados_all'
    ),
    path(
        'listar-by-area/<shortname>/', 
        views.ListByAreaEmpleado.as_view(),
        name='empleados_area'),
    path(
        'lista-empleados-admin/', 
        views.ListaEmpleadosAdmin.as_view(),
        name='empleados_detail'),
    path('buscar-empleado/', views.ListEmpleadosByWork.as_view()),
    path('lista-habilidaes-empleado/', views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>', 
        views.EmpleadoDetailView.as_view(),
        name = 'empleados_detalle'
    ),
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
]