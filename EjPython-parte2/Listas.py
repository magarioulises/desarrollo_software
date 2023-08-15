"""Generar una lista con 10 valores enteros aleatorios entre 1 y 20
 (se puede usar randint() del módulo random). Luego:

Muestre la lista
El usuario ingresa debe ingresar un valor. El programa debe informar cuántos valores de la lista 
son mayores a dicho valor, para eso debe utilizar una función. La función debe recibir 
como argumentos la lista y un entero, y debe retornar la cantidad de valores de la lista 
mayores a dicho entero.
Crear una función que calcule el promedio de la lista y utilizarla.
Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne."""


import random

lista = [random.randint(1, 20) for _ in range(10)]

print("Lista de enteros aleatorios:", lista)

def cantidadMayor(listaEntero, numero):
    cantidad = 0
    for valor in listaEntero:
        if valor > numero:
            cantidad += 1
    return cantidad 


def calcular_promedio(listaEntero):
    return sum(listaEntero) / len(listaEntero)

def encontrar_extremos(listaEntero):
    maximo = max(listaEntero)
    minimo = min(listaEntero)
    return maximo, minimo

valor=int(input("Ingrese un valor: "))

cant=cantidadMayor(lista, valor)
print(f"La cantidad de numeros mayores a {valor} es de {cant}")

promedio = calcular_promedio(lista)
print("Promedio de la lista:", promedio)

maximo, minimo = encontrar_extremos(lista)
print("Valor más grande:", maximo)
print("Valor más pequeño:", minimo)
