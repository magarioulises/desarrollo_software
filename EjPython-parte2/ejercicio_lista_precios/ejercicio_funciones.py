# -*- coding: utf-8 -*-
# TODO #1a: importar  el modulo db_productos
from db_productos import cargar_productos

productos = []
# TODO #1b: cargar la lista de productos con la función
#          cargar_productos() del módulo db_productos.
productos = cargar_productos()
# TODO #2: definir una función mostrar_productos()
#          que reciba la lista de productos, no retorne nada,
#          y muestre la lista utilizando el siguiente formato para cada producto:
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# ...
def mostrar_productos(prod):
    for producto in prod:
        print(f"Producto {producto['id']}")
        print(f"Nombre {producto['nombre']}")
        print(f"Precio {producto['precio']}")



# TODO #3: definir una función calcular_precio_actualizado()
#          que reciba: el precio anterior y porcentaje de aumento
#          y retorne: el precio con el aumento.

def calcular_precio_actualizado(precioAnterior, porcentajAum):
    aumento = (precioAnterior*porcentajAum)/100
    precioActual = precioAnterior + aumento
    return precioActual

#precio=int(input("Ingrese el precio anterior: "))
#aument=int(input("Ingrese el aumento: "))
#precioTotal = calcular_precio_actualizado(precio,aument)
#print(f"El precio total con el aumento es de {precioTotal}")

# TODO #4: Crear una función actualizar_precios() que reciba la lista de productos y 
#          el porcentaje de aumento. La función debe recorrer cada producto de la
#          lista e invocar calcular_precio_actualizado() (a la cual tendrá que pasarle
#          el precio del producto y el porcentaje de aumento) para obtener el precio
#          actualizado y modifique la lista "in-place" actualizando el precio de cada
#          producto. La función no debe retornar nada sino dejar modificada la lista
#          pasada por el usuario.
def actualizar_precios(prod, porcentajAum):
       for producto in prod:
        precioAnterior = producto['precio']
        precio_nuevo = calcular_precio_actualizado(precioAnterior, porcentajAum)
        producto['precio'] = precio_nuevo

#actualizar_precios(productos, aument)
#mostrar_productos(productos)


#  """if __name__ == '__main__':"""
    # TODO #5a: mostrar la lista cargada
    # TODO #5b: el usuario debe ingresar el porcentaje de aumento
    # TODO #5c: usar la función actualizar_precios() para actualizar los precios de la lista
    # TODO #5d: mostrar la lista con los precios actualizados
print("LISTA CARGADA\n")
mostrar_productos(productos)
print("\nAUMENTO!!")
aument=int(input("Ingrese el aumento: "))
actualizar_precios(productos, aument)
print("\nPRECIOS ACTUALIZADOS:\n")
mostrar_productos(productos)
