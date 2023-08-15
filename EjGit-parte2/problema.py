"""
Problema
Escriba un algoritmo que permita al usuario ingresar 2 valores numéricos 
y seguidamente muestre un menú como el siguiente:

1. Ingresar valor 1
2. Ingresar valor 2
3. Mostrar suma
4. Mostrar resta
5. Mostrar multiplicación
6. Mostrar división
7. Salir

Elija una opción:
El programa debe continuar pidiendo al usuario que seleccione una opción hasta que se ingrese 7 (Salir).
Si se selecciona alguna de las opciones: 3, 4, 5 o 6 sin antes haber pasado por las opciones 1 y 2
(ingresar valores) se debe mostrar un mensaje de error.
"""

def menu():
    print ("""\n1. Ingresar valor 1
2. Ingresar valor 2
3. Mostrar suma
4. Mostrar resta
5. Mostrar multiplicación
6. Mostrar división
7. Salir
           """)
    opcion=int(input("Elija una opción: "))
    while (opcion > 7 or opcion == 0):
        print("Opcion INCORRECTA")
        opcion=int(input("Elija una opción: "))

    return(opcion)
    
def ingresar_valor():
    num = int(input("Ingrese un valor: "))
    return(num)

def suma(valor1, valor2):
    rtdo = valor1 + valor2
    return(rtdo)

def resta(valor1, valor2):
    rtdo = valor1 - valor2
    return(rtdo)

def multiplicacion(valor1, valor2):
    rtdo = valor1 * valor2
    return(rtdo)

def division(valor1, valor2):
    rtdo = valor1 / valor2
    return(rtdo)

"EJERCICIO"
num1=-1
num2=-1
opc = menu()
while (opc != 7):
    if opc == 1:
        num1 = ingresar_valor()
    if opc == 2:
        num2 = ingresar_valor()
    if opc > 2:
        if num1 == -1 or num2 == -1:
            print("\nERROR\n")
            break
        elif opc == 3: 
            resultado = suma(num1, num2)
            print(f"\nEl resultado de la suma es: {resultado}")
        elif opc == 4:
            resultado = resta(num1, num2)
            print(f"\nEl resultado de la resta es: {resultado}")
        elif opc == 5:
            resultado = multiplicacion(num1, num2)
            print(f"\nEl resultado de la multiplicación es: {resultado}")
        elif opc == 6:
            resultado = division(num1, num2)
            print(f"\nEl resultado de la división es de: {resultado}")
    opc = menu()