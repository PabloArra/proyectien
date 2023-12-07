from django.db import models
from django.contrib.auth.models import User



gen=[{"Masculino","Masculino."},
    {"Femenino","Femenino."},
    {"Otro","Otro."}]


    




class Categoria(models.Model):
    Nombrec=models.CharField(verbose_name="Nombre Categoria", max_length=30)
    crea=models.DateTimeField(auto_now_add=True)
    upda=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.Nombrec




class Producto(models.Model):
    Nombrez=models.CharField(verbose_name="Nombre", max_length=20)
    imgend=models.ImageField(upload_to="projects",verbose_name="imagen", null=True, blank=True)
    precioz=models.PositiveIntegerField(verbose_name="Precio del Producto")
    catego=models.ForeignKey(Categoria,blank=True,null=True,on_delete=models.SET_NULL)
    descrip=models.TextField(verbose_name="Descripcion del producto")
    vende=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.Nombrez
    



