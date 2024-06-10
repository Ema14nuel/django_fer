from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path(
        'listar-todo-departamento', 
        views.DepartamentoListView.as_view(),
        name = 'departamento'
    ),
]