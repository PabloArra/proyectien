from django.shortcuts import render, redirect
from .models import Producto
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .form import *





def Public(request):
    news=Producto.objects.all()
    paginator = Paginator(news,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"core/about.html",{'news':page_obj})

def buscar(request, n):
    list=Producto.objects.get(pk=n)
    return render(request,"core/buscar.html",{'list':list})

def busqueda(request):
    if request.method == "POST":
        Buscado = request.POST['buscado']
        producto = Producto.objects.filter(Nombrez__contains=Buscado)
        return render(request, 'core/busqueda.html', {'buscado':Buscado, 'producto':producto})
    else:
        return render(request, 'core/busqueda.html', {})




def Inicio(request):
    return render(request,"core/home.html")




# def men(request):
#     news=Producto.objects.all()
#     paginator = Paginator(news,3)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request,"core/men.html",{'news':page_obj})



def catalogo(request):
    news=Producto.objects.all()
    paginator = Paginator(news,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"core/catalogo.html",{'news':page_obj})



@login_required
def publicar(request):
    return render(request,"core/about.html")



@login_required
def crear(request):
    submitted=False
    if request.method == 'POST':
            maq_form = admprodform(request.POST,request.FILES)
            if maq_form.is_valid():
                produc= maq_form.save(commit=False)
                produc.vende = request.user
                produc.save()
                return redirect('about.html')
    else:
        maq_form= admprodform()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,"fu/categoria.html",{'maq_form':maq_form})


@login_required
def editar(request,n):
    maqui= Producto.objects.get(pk = n)
    if request.method == 'GET':
        maq_form = articleform(instance= maqui)
    else:
        maq_form = articleform(request.POST, instance= maqui)
        if maq_form.is_valid():
            maq_form.save()
        redirect('about.html')
    return render(request,"fu/categoria.html",{'maq_form':maq_form,'maqui':maqui})


@login_required
def borr(request,n):
    bo= Producto.objects.get(pk = n)
    bo.delete()
    return redirect('/about.html')





