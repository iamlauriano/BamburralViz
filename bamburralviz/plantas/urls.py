from django.urls import path
from .views import *

urlpatterns = [
        path('consulta/', consulta, name='rota do nossa app'),
        ]
