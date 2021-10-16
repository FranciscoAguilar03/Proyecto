#Funciones
def caract(lista):
    texto="Para su calzado, tenemos las siguientes carácterísticas:"
    i=0
    while i<len(lista):
        texto=texto+"\n"+lista[i]
        i=i+1
    return texto

def modelo(lista):
    texto1="Elija su modelo favorito"
    i=0
    while i<len(lista):
        texto1=texto1+"\n"+lista[i]
        i=i+1
    return texto1
def costototal(costotenis, pares):
    return costotenis*pares

def calculo (pagofinal, a):
    pagofinal=pagofinal+a
    return pagofinal

#Arreglos    
listatamaño=["High-top", "Low-top"]
listacolor=["Blanco", "Negro", "Gris"]

listamodelo1=["Nike Blazer", "Air Force One", "Adidas Forum"]
listamodelo2=["Vans sk8", "Jordan 1"]
listamodelo3=["Jordan 4", "Converse Chuck Taylor"]
listamodelo4=["Adidas Superstar", "Nike Huarache"]
listamodelo5=["Nike Air Max 1", "Vans old skul", "Nike 720"]
listamodelo6=["Asics Gel Kayano 5", "New Balance 992", "Adidas Ozweego"]


#Inicio del código
print("Bienvenido a la tienda de tenis")
print("Ingrese su nombre")
nombre=str(input())
costotenis=0
comprar="Sí"
pagofinal=0
while comprar=="Sí":
    print(caract(listatamaño))
    altura=str(input())
    print(caract(listacolor))
    color=str(input())
    if altura=="High-top" and color=="Blanco":
        print(modelo(listamodelo1))
        costotenis=2500
    elif altura=="High-top" and color=="Negro":
        print(modelo(listamodelo2))
        costotenis=2250
    elif altura=="High-top" and color=="Gris":
        print(modelo(listamodelo3))
        costotenis=2750
    elif altura=="Low-top" and color=="Blanco":
        print(modelo(listamodelo4))
        costotenis=1750
    elif altura=="Low-top" and color=="Negro":
        print(modelo(listamodelo5))
        costotenis=1500
    elif altura=="Low-top" and color=="Gris":
        print(modelo(listamodelo6))
        costotenis=1250
    else:
        print("Una disculpa, no tenemos ese par en existencia")
    tenis=str(input())

    
    print("¿Cuantos pares quieres?")
    pares=int(input())


        

    pagofinal=calculo(pagofinal, costototal(costotenis, pares))
    print("El costo es de", pagofinal, "por el par")
    print("¿Desea seguir comprando?")
    comprar=str(input())
    
print("¿Desea añadir a su carrito un kit de limpieza con un costo de $200")
kit=str(input())
if kit=="Sí":
    kit=200
else:
    kit=0
print("¿Tiene algún código de descuento? Ingreselo")
codigo=str(input())
if codigo=="descuento500":
    descuento=-500
else:
    descuento=0
    
#Resultado final
pagofinal=calculo(pagofinal,kit)
pagofinal=calculo(pagofinal,descuento)
print("Su pago final es de", pagofinal)
print("Gracias por su compra", nombre)




    






    
        
    
    
    
