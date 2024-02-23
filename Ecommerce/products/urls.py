from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from products import views

urlpatterns = [

    path("admin/", admin.site.urls),
    path("about/", TemplateView.as_view(template_name="about.html")),
    path("team/", TemplateView.as_view(template_name="team.html")),
    
]