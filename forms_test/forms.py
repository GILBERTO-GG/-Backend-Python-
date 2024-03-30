from django import forms
from .models import Product
from django.contrib.auth.models import User
'''
YEARS = [x for x in range(1900, 2030)]

MY_CHOICES = [
      ("db_value1", "Opción 1"),
      ("o2", "Opción 2"),
      ("o3", "Opción 3")

]



class ProductModelForm(forms.ModelForm):
    labels = {
        "title":"Mi etiqueta para el título",
        "slug":"Mi etiqueta para el slug",
        "price":"Mi etiqueta para el precio",
    }

    class Meta:
        model =Product
        fields = [
            "title",
            "slug",
            "price"
        ]
        exclude = []

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if len(title) <= 10:
            raise forms.ValidationError("El título debe tener más de 10 caracteres")
        return title    

    
    def clean_slug(self, *args, **kwargs):
        slug = self.cleaned_data.get("slug")
        if len(slug) <= 10:
            raise forms.ValidationError("El slug debe tener más de 10 caracteres")
        if "misupermarca" not in slug:
             raise forms.ValidationError("El slug debe incluir misupermarca")
        #if " " in slug: 
         #   raise forms.ValidationError("El slug no puede contener espacios, te recomendamos sustituirlos por guiones")
        
        return slug  


class TestForm(forms.Form):
    fecha = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    un_texto = forms.CharField(label="Ingresa un texto: ", widget=forms.Textarea(attrs={"rows":4, "cols":10}))
    booleano = forms.BooleanField()
    entero = forms.IntegerField(initial=80)
    correo = forms.EmailField()
    opciones = forms.CharField(label="Selecciona una opción", widget=forms.Select(choices=MY_CHOICES))
    opciones_radio = forms.CharField(label="Selecciona una opción", widget=forms.RadioSelect(choices=MY_CHOICES))
    opciones_checkbox = forms.CharField(label="Selecciona una opción", widget=forms.CheckboxSelectMultiple(choices=MY_CHOICES))


    def clean_entero(self, *args, **kwargs):
        entero = self.cleaned_data.get("entero")
        if entero > 100:
            raise forms.ValidationError("El número debe ser menor o igual que 100")
        return entero
    
    def clean_un_texto(self, *args, **kwargs):
        un_texto = self.cleaned_data.get("un_texto")
        if len(un_texto) < 10:
            raise forms.ValidationError("El texto debe contener mas de 10 caracteres")
        return un_texto'''


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']