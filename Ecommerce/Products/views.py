from django.shortcuts import render
from django.views.generic import View, ListView
from django.decorators.http import require_http_methods
from .models import Product, Post

def product_list_view(request):
    if request.method == "POST":
        print(request.POST)
        return render(request, "template", {})
    
#--------------------------------------------------------------------------------------------------------------------------------    

class ProductHomeView(View):
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