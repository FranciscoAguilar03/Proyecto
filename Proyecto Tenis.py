"""
El proyecto es un simulador de una tienda de tenis.
El programa realiza varias preguntas sobre las características
del tenis que desea para después mostrarle los modelos disponibles,
ofrecerle otros productos y preguntar por códigos de descuento.
El usuario puede comprar tantos tenis como el desee.
Finalmente muestra en total a pagar.
"""

"""
----Funciones---------------------------------------------------------------
"""
def caract(lista):
    """
    Función: Uso de variables, operadores, ciclos y cadenas
    Recibe: lista
    Uso: Imprime el texto inicial y después va añadiendo todos los datos a la
    cadena
    separados por un salto de línea
    Devuelve: texto
    """
    texto="Para su calzado, tenemos las siguientes carácterísticas:"
    i=0
    while i<len(lista):
        texto=texto+"\n"+lista[i]
        i=i+1
    return texto

def modelo(lista):
    """
    Función: Uso de variables, operadores, ciclos y cadenas
    Recibe: lista
    Uso: Imprime el texto inicial y después va añadiendo todos los datos a la
    cadena
    separados por un salto de línea
    Devuelve: texto
    """
    texto1="Elija su modelo favorito"
    i=0
    while i<len(lista):
        texto1=texto1+"\n"+lista[i]
        i=i+1
    return texto1
def costototal(costotenis, pares):
    """
    Función: Uso de operadores y variables
    Recibe: costotenis y pares
    Uso: Multiplica dos variables
    Devuelve: costotenis*pares
    """
    return costotenis*pares

def calculo (pagofinal, extra):
    pagofinal=pagofinal+extra
    return pagofinal
    """
    Función: Uso de variables y operadores
    Recibe: pagofinal y extra
    Uso: Suma dos variables
    Devuelve: pagofinal
    """
    
"""
----Listas------------------------------------------------------------------
"""
listatamaño=["High-top", "Low-top"]
listacolor=["Blanco", "Negro", "Gris"]

listamodelo1=["Nike Blazer", "Air Force One", "Adidas Forum"]
listamodelo2=["Vans sk8", "Jordan 1"]
listamodelo3=["Jordan 4", "Converse Chuck Taylor"]
listamodelo4=["Adidas Superstar", "Nike Huarache"]
listamodelo5=["Nike Air Max 1", "Vans old skul", "Nike 720"]
listamodelo6=["Asics Gel Kayano 5", "New Balance 992", "Adidas Ozweego"]


"""
----Inicio del código-------------------------------------------------------
"""
#Valores iniciales requeridos
costotenis=0
comprar="Sí"
pagofinal=0

print("Bienvenido a la tienda de tenis")

#Pregunta el nombre
print("Ingrese su nombre")
nombre=str(input())

#Inicia el ciclo para las características y las funciones con listas
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

#Calcula el costo actual 
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
    
"""
----Resultado final---------------------------------------------------------
"""

#Calcula el costo final a pagar
pagofinal=calculo(pagofinal,kit)
pagofinal=calculo(pagofinal,descuento)
print("Su pago final es de", pagofinal)
print("Gracias por su compra", nombre)
    




    






    
        
    
    
    