from django.shortcuts import render,redirect
#from django.forms import modelformset_factory
#from .forms import TestForm, ProductModelForm, RegistroForm
from .models import Product
#from .forms import ProductModelForm
from .forms import UserRegistrationForm



'''def home(request):
    initial_data = {
        "un_texto":"Texto inicial",
        "booleano":True, 
        #"entero":100,
        "correo":"test@test.com"
    }
    form = TestForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "forms.html", {"form":form})


def home(request):
    TestFormSet = formset_factory(TestForm, extra=3)
    formset = TestFormSet(request.POST or None)
    if formset.is_valid():
        for form in formset:
            print(form.data)
    context = {
        "formset":formset
    }
    
    # form = ProductModelForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    # initial_data = {
    #     "un_texto":"Texto inicial",
    #     "booleano": True,
    #     #"entero":100,
    #     #"correo":"test@test.com"
    # }
    # form = TestForm(request.POST or None, initial=initial_data)
    # if form.is_valid():
    #     print(form.cleaned_data)
    return render(request, "formset_view.html", context)



def home(request):
    ProductModelFormSet = modelformset_factory(Product, form=ProductModelForm)
    formset = ProductModelFormSet(request.POST or None, queryset= Product.objects.all())
    
    print("formset.data")
    print(formset.data)

    print("formset.errors")
    print(formset.errors)

    if formset.is_valid():
        print("ModelFormset es valido")
        formsave.save()

    # for form in formset:
    #      print(form.data)
    context = {
        "formset":formset
    }    

    # form = ProductModelForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    # initial_data = {
    #     "un_texto":"Texto inicial",
    #     "booleano": True,
    #     #"entero":100,
    #     #"correo":"test@test.com"
    # }
    # form = TestForm(request.POST or None, initial=initial_data)
    # if form.is_valid():
    #     print(form.cleaned_data)
    return render(request, "formset_view.html", context)'''

# 




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')  # redirigir a una página de registro exitoso
    else:
        form = UserRegistrationForm()
    return render(request, 'registro.html', {'form': form})



def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')  



