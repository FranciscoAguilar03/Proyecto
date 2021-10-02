#Funciones
def caract(lista):
    print("Para su calzado, tenemos las siguientes carácterísticas:")
    i=0
    while i<len(lista):
        print(lista[i])
        i=i+1
    i=0
def modelo(lista):
    print("Eliga su modelo favorito")
    i=0
    while i<len(lista):
        print(lista[i])
        i=i+1
    i=0
def costototal(costotenis, pares):
    return costotenis*pares
def pagoparcial(pago, descuento):
    return pago*(1-(descuento/100))

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
    pago=costototal(costotenis, pares)
    print("¿Tiene algún código de descuento?")
    codigo=str(input())
    if codigo=="Sí":
        print("¿De cuanto es su porcentaje de descuento?")
        descuento=int(input())
    else:
        descuento=0

    print("El costo es de", pagoparcial(pago, descuento), "por el par")
    pagofinal=pagofinal+pagoparcial(pago, descuento)
    print("¿Desea seguir comprando?")
    comprar=str(input())

#Resultado final
print("Su pago final es de", pagofinal)
print("Gracias por su compra", nombre)
    




    






    
        
    
    
    