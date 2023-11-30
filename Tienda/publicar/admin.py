from django.contrib import admin

from .models import *


admin.site.register(Categoria)
    

@admin.register(Producto)
class ProductoAdm(admin.ModelAdmin):
    list_display = ('id', 'Nombrez','vende')

