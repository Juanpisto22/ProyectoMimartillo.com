
from django.http.response import HttpResponse
from django.shortcuts import render, redirect 
from .models import*
from django.contrib import messages



# Create your views here.


def homeC(request):
    item_list = Item.objects.all()
    context = {
        'item_list' : item_list
    }
    return render (request,'homeC.html',context)

#añade y lista los items
def add_item(request):
    if request.method=="POST":
        NombreP = request.POST['NombreP']
        DescripcionP = request.POST['DescripcionP']
        item = Item(NombreP = NombreP,DescripcionP = DescripcionP)
        item.save()
        messages.info(request,"Producto Añadido Exitosamente")
    else:
        pass

    item_list = Item.objects.all()
    context = {
        'item_list' : item_list
    }


    return render(request,'homeC.html',context)

#Objeto que elimina el item
def delete_item(request,myid):
    item = Item.objects.get(id = myid)
    item.delete()
    messages.info(request,"El producto ha sido eliminado correctamente")
    return redirect(homeC)

#Objeto que edita un producto


def edit_item(request,myid):
    sel_item = Item.objects.get(id = myid)
    item_list = Item.objects.all()
    context = {
        'sel_item' : sel_item,
        'item_list' : item_list
    }
    return render(request,'homeC.html',context)


def update_item(request,myid):
    item = Item.objects.get(id = myid)
    item.NombreP = request.POST['NombreP']
    item.DescripcionP = request.POST['DescripcionP']
    item.save()
    messages.info(request, "El producto fue actualizado con exito")
    return redirect('homeC')
