from django.shortcuts import render
from django.views.generic import View, ListView
from django.views.decorators.http import require_http_methods
from .models import Product, Post
from django.contrib.auth.models import User


def product_list_view(request):
    if request.method == "POST":
        print(request.POST)
    print(request.method == "POST")    
    return render(request, "template", {})
    
#--------------------------------------------------------------------------------------------------------------------------------    

class ProductHomeView(View):     #------>hereda de view  (View)
    def get(self, *args, **kwargs):
        return render(request, "template", {})
    
    def post(self, *args, **kwargs):
        print(request.POST)
        return render(request, "template", {})
    

#--------------------------------------------------------------------------------------------------------------------------------    

class ProductListView(ListView):              #<------está heredando de ListView
    queryset =  Product.objects.all() 

product_list_view = ProductListView.as_view 

#--------------------------------------------------------------------------------------------------------------------------------

class BlogPostListView(ListView):
    queryset = Post.objects.all()

#--------------------------------------------------------------------------------------------------------------------------------    

class UsersPostListView(ListView):
    queryset = User.objects.all()

#----------------------------------------------------------------------------------------------------------------

'''def about_us_view(request):
    return render(request,"about.html", {})
                  
                  
class AboutUsView(View):
    def get(self, request):
        return render(request, "about.html", {})


class AboutUsView(TemplateView):
    template_name = "about.html"   '''                 