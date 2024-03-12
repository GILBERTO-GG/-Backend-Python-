from typing import Any
from django.forms import BaseModelForm
from django.shortcuts import render, get_object_or_404
#from django.views.generic import View, ListView
#from django.views.generic import View, TemplateView, RedirectView
#from django.decorators.http import require_http_methods
from .models import Product, DigitalProduct
#from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView
from .mixins import TemplateTitleMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductModelForm


'''def product_list_view(request):
    if request.method == "POST":
        print(request.POST)
    print(request.method == "POST")    
    return render(request, "template", {})
    
#--------------------------------------------------------------------------------------------------------------------    

class ProductHomeView(View):     #------>hereda de view  (View)
    def get(self, request,*args, **kwargs):
        return render(request, "template", {})
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        return render(request, "template", {})
    

#------------------------------------------------------------------------------------------------------------------------    

class ProductListView(ListView):              #<------está heredando de ListView
    queryset =  Product.objects.all() 

product_list_view = ProductListView.as_view()    


#-----------------------------------------------------------------------------------------------------------------------

class BlogPostListView(ListView):
    queryset = Post.objects.all()

#-----------------------------------------------------------------------------------------------------------------------    

class UsersPostListView(ListView):
    queryset = User.objects.all()

#-------------------------------------------------------------------------------------------------------

def about_us_view(request):
    return render(request,"about.html", {})
                  
                  
class AboutUsView(View):
    def get(self, request):
        return render(request, "about.html", {})'''


#class AboutUsRedirectView(RedirectView):
 #   url = "/about/"      


#def about_us_redirect_view(request):
 #   return HttpResponseRedirect("/products/about/")


class ProtectedProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductModelForm
    template_name = "forms.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
   

class ProductIDRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        pk = url_params.get("pk")
        obj = get_object_or_404(Product, pk=pk)
        slug = obj.slug
        return f"/products/products/{slug}"
    
class ProductRedirectView(RedirectView):
    def get_redirect_url(self, *args,  **kwargs):
        url_params = self.kwargs
        slug = url_params.get("slug")
        return f"/products/products/{slug}"


class DigitalProductListView(TemplateTitleMixin, ListView):
    model = DigitalProduct 
    template_name = "products/product_list.html"
    title = "Productos Digitales"
    
   
class ProductListView(TemplateTitleMixin, ListView):
    # app_label = "Products"
    # model = Product
    # view_name = List
    # template_name = <app_name>/<model>_<view_name>.html
    # template_name = products/product_list.html
    model = Product 
    title = "Productos Físicos"
    

class ProductDetailView(DetailView):
    model = Product    


class ProtectedProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProtectedProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProductModelForm
    template_name = "products/product_detail.html"
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def get_success_url(self):
        return self.object.get_edit_url()
    
    
class ProtectedProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "forms-delete.html"
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def get_success_url(self):
        return "/products/products"   
    

class ProtectedListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'
        

    def get_queryset(self):
        
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)    