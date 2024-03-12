from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ProductModel
from .forms import ProductModelForm
from django.contrib.auth.decorators import login_required      #-----> proteger nuestras vistas.
from django.contrib import messages

from django.db.models import Q

# Create your views here.

"""def home(request):
    return HttpResponse("<h1>Hola Mundo</h1>")"""

#--------------------------------------------------------------------------------------------------------------------------------

"""def home(request):
    html = ""
    <!DOCTYPE html>
    <html>
        <head>
            <style>
              h1 {color: blue}
              h2 {color: yellow}
              h3 {color: green}
              h4 {color: red}
            </style>
        </head>
        
        <body>
           <h1>Hola Mundo</h1>
           <h2>Hola Mundo</h2>
           <h3>Hola Mundo</h3>
           <h4>Hola Mundo</h4>
        </body>
    </html>
    
    
    return HttpResponse(html)"""

#------------------------------------------------------------------------------------------------------------------------------

"""def home(request):
    response = HttpResponse()
    response.write("<p>Texto de prueba para ecommerce</p>")
    response.write("<p>Texto de prueba para ecommerce</p>")
    response.write("<p>Texto de prueba para ecommerce</p>")
    return response"""


#--------------------------------------------------------------------------------------------------------------------------------


"""def home(request):
    response = HttpResponse()
    response.content = "Algún contenido de prueba"
    response.write("<p>Texto de prueba para ecommerce</p>")
    return response"""

#--------------------------------------------------------------------------------------------------------------------------------

"""def home(request):
    response = HttpResponse()
    response.content = "Algún contenido de prueba"
    response.write("<p>Página no encontrada</p>")
    response.status_code = 404
    return response """

#--------------------------------------------------------------------------------------------------------------------------------


"""def redirect_to_test(request):
    return HttpResponseRedirect("/MyEcommerceApp")"""

#--------------------------------------------------------------------------------------------------------------------------------

#@login_required(login_url="/admin/login/")      #---------------------> proteger nuestras vistas (decorador).

def product_model_list_view(request):
    #print(request.user)
    query = request.GET.get("q", None)
    queryset = ProductModel.objects.all()
    if query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(price__icontains=query) | 
            Q(description__icontains=query) |  
            Q(seller__icontains=query) |  
            Q(color__icontains=query) |  
            Q(product_dimensions__icontains=query)  
        )
    #print(queryset)
    template = "ecommerce/list-view.html"
    context = {
        "products": queryset,
        "description": query if query else "",  # Verifica si query es None antes de acceder al método get
        "seller": query if query else "",  
        "color": query if query else "",  
        "product_dimensions": query if query else "" 
    }

    if request.user.is_authenticated:
        template= "ecommerce/list-view.html"
    else:
        template= "ecommerce/list-view-public.html" 

    return render(request, template, context)


#--------------------------------------------------------------------------------------------------------------------------

@login_required(login_url="/admin/login/")      

def login_required_view(request):
    print(request.user)
    queryset = ProductModel.objects.all()
    print(queryset)
    template = "ecommerce/list-view.html"
    context = {
        "products" : queryset       
    }

    if request.user.is_authenticated:
        template= "ecommerce/list-view.html"
    else:
        template= "ecommerce/list-view-public.html" 

    return render(request, template, context)

#---------------------------------------------------------------------------------------------------------------------------------

def product_model_detail_view(request, product_id):
    instance = get_object_or_404(ProductModel, id=product_id)
    context = {
        "product" : instance,  
        "description": instance.description,  
        "seller": instance.seller,  
        "color": instance.color,  
        "product_dimensions": instance.product_dimensions   
    }
    template= "ecommerce/detail-view.html" 
    return render(request, template, context)


#---------------------------------------------------------------------------------------------------------------------------------
def product_model_create_view(request):
      form = ProductModelForm(request.POST or None)
      if form.is_valid():
          instance = form.save(commit=False)
          instance.save()
          messages.success(request, "Producto creado con éxito")
          return HttpResponseRedirect("/MyEcommerceApp/{product_id}".format(product_id=instance.id))
      context = {
          "form":form
      }
      
      template = "ecommerce/create-view.html"
      return render(request, template, context)
#---------------------------------------------------------------------------------------------------------------------------------


def product_model_update_view(request, product_id=None):
      instance = get_object_or_404(ProductModel, id=product_id)
      form = ProductModelForm(request.POST or None, instance=instance)
      if form.is_valid():
          instance = form.save(commit=False)
          instance.save()
          messages.success(request, "Producto actualizado con éxito")
          return HttpResponseRedirect("/MyEcommerceApp/{product_id}".format(product_id=instance.id))
      context = {
          "form":form
      }
      
      template = "ecommerce/update-view.html"
      return render(request, template, context)

#---------------------------------------------------------------------------------------------------------------------------------

def product_model_delete_view(request, product_id):
    instance = get_object_or_404(ProductModel, id=product_id)
    if request.method == "POST":
        instance.delete()
        HttpResponseRedirect("/MyEcommerceApp/")
        messages.success(request, "Producto eliminado")
        return HttpResponseRedirect("/MyEcommerceApp/")
    context = {
        "product" : instance,
        "description": instance.description,  
        "seller": instance.seller,  
        "color": instance.color,  
        "product_dimensions": instance.product_dimensions     
    }
    template= "ecommerce/delete-view.html" 
    return render(request, template, context)


#---------------------------------------------------------------------------------------------------------------------------------