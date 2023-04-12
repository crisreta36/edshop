from django.shortcuts import render,get_object_or_404

from .models import Categoria,Producto  # se importa los modelos

# Create your views here.
"""vistas para el catalogo de productos"""

def index(request): #creamos una lista de productos
    listaProductos=Producto.objects.all()#vamos a retornar todos los productos
    #print(listaProductos)
    listaCategorias=Categoria.objects.all()
    context=   {
         'productos':listaProductos,
         'categorias':listaCategorias
    }                                      #creamos un context para crear un diccionario se crea pra enviar todas las variablesque viajen al template
    return render(request,'index.html',context) #le pasamos el context que tiene el diccionario

#Creamos una vista

def productosPorCategoria(request,categoria_id):#recibe un id de categoria
    """Vista para filtrar productos por categorias"""
    objCategoria = Categoria.objects.get(pk=categoria_id)#aqui hacemos select * from categoria where ud categoria es igual a al parametro que estoy investiegando o busvando
    #objCategoria es un objeto de la clase categoria
    listaProductos = objCategoria.producto_set.all()# esto trae un listado de todos los productos que pertenecen a esa categoria

    listaCategorias = Categoria.objects.all()

    context={
        'categorias':listaCategorias,
        'productos':listaProductos
    }

    return render(request,'index.html',context)

def productosPorNombre(request): #filtrado de busqueda de productos por un nombre esto va a ser enviado ddesde un formulario capturamos lo enviado por un post no por get
    nombre = request.POST['nombre']     #captura la informacion que a sido envida por un metodo post en este caso por un formulario

    listaProductos=Producto.objects.filter(nombre__contains=nombre)#para poder filtrar por un nombre me tre todos los productos que contegan dentro de nombre el valor que voy a enviar por el formulario
    listaCategorias=Categoria.objects.all()

    context={
        'categorias':listaCategorias,
        'productos':listaProductos
    }

    return render(request,'index.html',context)# que hacemos es capturar el nombre por el metodo post lo almaceno en la variable nombre luego hago una lista de productos que es igual a producto.object.filter

def productoDetalle(request,producto_id):
    """vista para el detalle de del producto"""

    #objProducto = Producto.objects.get(pk=producto_id)
    objProducto = get_object_or_404(Producto,pk=producto_id)
    context={
        'producto':objProducto
    }
    return render(request,'producto.html',context)
