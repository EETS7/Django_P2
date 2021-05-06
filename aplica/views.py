from django.shortcuts import render
from django.http import HttpResponse
from aplica.models import uno

def juegosss(request):
    return render(request,"juego.html")
def boletos(request):
    return render(request,"boletoventa.html")
def boletoscondicional(request):
    cc1=int(request.GET["c1"])
    cc2=int(request.GET["c2"])
    cc3=int(request.GET["c3"])
    bb1=int(request.GET["b1"])
    bb2=int(request.GET["b2"])
    bb3=int(request.GET["b3"])
    pp1=int(request.GET["p1"])
    pp2=int(request.GET["p2"])
    pp3=int(request.GET["p3"])
    tipo=int(request.GET["tipoclase"])
    suma=cc1+cc2+cc3+bb1+bb2+bb3+pp1+pp2+pp3
    comida=(cc1*50)+(cc2*40)+(cc3*25)
    bebida=(bb1*35)+(bb2*25)+(bb3*10)
    pelicula=(pp1*70)+(pp2*55)+(pp3*25)
    subtotal=(cc1*50)+(cc2*40)+(cc3*25)+(bb1*35)+(bb2*25)+(bb3*10)+(pp1*70)+(pp2*55)+(pp3*25)
    if (tipo == 1):
        tip="Primera Clase"
    elif (tipo == 2):
        tip="Segunda Clase"
    elif (tipo == 3):
        tip="Tercera Clase"
    else:
        tip="No se selecciono"
    if ((cc1!=0)and(bb1!=0)and(pp1!=0)and(tipo=="1")):
        descuento=subtotal*0.05
        total=subtotal-descuento
    elif (suma > 9):
        descuento=subtotal*0.1
        total=subtotal-descuento
    elif (suma < 10):
        descuento=0
        total = subtotal
    else: 
        descuento=0
        total=0

    return render(request,"factura.html",{"tipovuelo":tip,"subtotal1":subtotal,"descuento1":descuento,"total1":total,"comida1":comida,"bebida1":bebida,"pelicula1":pelicula})

def juegocondicional(request):
    numuno=request.GET["primero"]
    name1=request.GET["nombre"]
    return render(request,"resultado.html",{"numuno1":numuno,"name11":name1})
def oportunidadsegunda(request):
    numdos=request.GET["segundo"]
    #name2=request.GET["nombre"]
    return render(request,"resultadot.html",{"numdos1":numdos})
def oportunidadtercera(request):
    numtres=request.GET["tercero"]
    #name3=request.GET["nombre"]
    return render(request,"resultadoc.html",{"numtres1":numtres})
def oportunidadcuarta(request):
    numcuatro=request.GET["cuarta"]
    #name4=request.GET["nombre"]
    return render(request,"resultadof.html",{"numcuatro1":numcuatro})
# Create your views here.
