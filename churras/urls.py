#from django.urls import path
#from .views import *

#urlpatterns = [
#    path('', index, name='index'),
#    path('buscar/', buscar, name='buscar'),
#   path('<int:id>', churrasco, name='churrasco'),
#]

from django.urls import path
from churras.views import index, buscar, churrasco

app_name = 'churras' 

urlpatterns = [
    path('', index, name='index'),
    path('buscar/', buscar, name='buscar'),
    path('prato/<int:id>/', churrasco, name='churrasco'),
]