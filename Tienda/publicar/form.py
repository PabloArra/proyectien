from django import forms
from .models import Producto

class articleform(forms.ModelForm):
    class Meta:
        model = Producto
        fields= ['Nombrez','imgend','precioz','catego']
        labels= {
            'Nombrez': 'Nombre',
            'imgend': 'Img',
            'precioz': 'Precio',
            'catego': 'Categoria',
            'descrip': 'Descipcion'
        }
        widgets = {
            'Id': forms.NumberInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el ID',
                    'id':'Id'
                }
            ),
            'Nombrez': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre',
                    'id':'Nombrez'
                }
            ),

            'precioz': forms.NumberInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el Precio',
                    'id':'precioz'
                }
            ),

        }
class admprodform(forms.ModelForm):
    class Meta:
        model = Producto
        fields= ['Nombrez','imgend','precioz','catego']
        labels= {
            'Nombrez': 'Nombre',
            'imgend': 'Img',
            'precioz': 'Precio',
            'catego': 'Categoria',
            'descrip': 'Descipcion',
        }
        widgets = {
            'Id': forms.NumberInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el ID',
                    'id':'Id'
                }
            ),
            'Nombrez': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre',
                    'id':'Nombrez'
                }
            ),

            'precioz': forms.NumberInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el Precio',
                    'id':'precioz'
                }
            ),

        }