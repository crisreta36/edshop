
from django.urls import path
from . import views

app_name='web' #esto es para los enlaces que estoy creando

urlpatterns = [
    path('', views.index,name='index'),#ruta principal y name para el alias del url
    path('productosPorCategoria/<int:categoria_id>',views.productosPorCategoria,name='productosPorCategoria'),
    path('productosPorNombre',views.productosPorNombre,name='productosPorNombre'),
    path('producto/<int:producto_id>',views.productoDetalle,name='producto')
]
