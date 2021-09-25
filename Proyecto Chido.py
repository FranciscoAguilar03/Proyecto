#Funciones 

def costototal(costotenis, pares):
    return costotenis*pares
def pagoparcial(pago, descuento):
    return pago*(1-(descuento/100))

#Inicio del código
print("Bienvenido a la tienda de tenis")
print("Ingrese su nombre")
nombre=str(input())
costotenis=0
comprar="sí"
pagofinal=0
while comprar=="sí":
    print("Qué altura quiere para su calzado: high-top o low-top")
    altura=str(input())

    if altura=="high-top":
        print("Qué color buscaba su calzado, tenemos blanco, negro y verde")
        color=str(input())
        if color=="blanco":
            print("Tenemos: Nike blazer, Jordan 1 y Adidas Forum")
            modelo=str(input())
            costotenis=costotenis+2500
        elif color=="negro":
            print("Tenemos: Vans SK8 y Nike air force 1 high")
            modelo=str(input())
            costotenis=costotenis+2000
        elif color=="verde":
            print("Tenemos:Converse Chuck Taylor y Jordan 5")
            modelo=str(input())
            costotenis=costotenis+2300
        print("¿Cuantos pares quieres?")
        pares=int(input())
    elif altura=="low-top":
        print("Qué color buscaba su calzado, tenemos gris, beige y azul")
        color=str(input())
        if color=="gris":
            print("Tenemos: New balance 552, Adidas ozweego y Adidas superstar")
            modelo=str(input())
            costotenis=costotenis+1800
        elif color=="beige":
            print("Tenemos: Jordan 4, Adidas continental y Asics gel-kayano")
            modelo=str(input())
            costotenis=costotenis+1600
        elif color=="azul":
            print("Tenemos:Converse all star, Adidas ultraboost y Nike cortez")
            modelo=str(input())
            costotenis=costotenis+1900
        print("¿Cuantos pares quieres?")
        pares=int(input())
    pago=costototal(costotenis, pares)
    print("¿Tiene algún código de descuento?")
    codigo=str(input())
    if codigo=="sí":
        print("¿De cuanto es su porcentaje de descuento?")
        descuento=int(input())
    else:
        descuento=0

    print("¿Desea seguir comprando?")
    comprar=str(input())
    print("El costo es de", pagoparcial(pago, descuento))
    pagofinal=pagofinal+pagoparcial(pago, descuento)
#Resultado final

print("Su pago final es de", pagofinal)
print("Gracias por su compra", nombre)
    




    






    
        
    
    
    