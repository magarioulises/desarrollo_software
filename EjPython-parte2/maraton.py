import random

def generar_lista_de_atletas():
	"""
	Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
	Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
		- nombre: el nombre del atleta
		- numero: el número con el que participó en la maratón
		- tiempo_llegada: la cantidad de segundos que tardó en llegar
	"""
	lista_atletas = []
	nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
	apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')	
	for i in range(1, 21):
		atleta = {
			"nombre": random.choice(nombres)+" "+random.choice(apellidos),
			"numero": i,
			"tiempo_llegada": random.random()*120
		}
		lista_atletas.append(atleta)
	return lista_atletas

def imprimirAtletas(lista_atletas):
    for atleta in lista_atletas:
        print(f"{atleta['numero']} - {atleta['nombre']}: ({atleta['tiempo_llegada']} segundos)")

def encontrarGanador(lista_atletas):
    ganador = lista_atletas[0]  # Inicializo con el primer atleta como ganador
    for atleta in lista_atletas:
        if atleta['tiempo_llegada'] < ganador['tiempo_llegada']:
            ganador = atleta
    return ganador['numero']

def datosAtletaNumero(lista_atletas, numAtleta):
     for atleta in lista_atletas:
          if atleta['numero'] == numAtleta:
               return atleta


          
#1-Utilizar la función anterior para generar y almacenar una lista de atletas
lista_atletas=generar_lista_de_atletas()
#2-Escribir una función que reciba la lista de atletas e imprima una línea por 
#cada atleta respetando el siguiente formato: "<num_atleta> - : (<tiempo_llegada> segundos)", 
# donde <num_atleta> es el número del atleta, su nombre y <tiempo_llegadad> su tiempo de llegada.
imprimirAtletas(lista_atletas)
#3-Escribir una función que devuelva el número del atleta que resultó ganador.
ganadorNum = encontrarGanador(lista_atletas)
print(f"El ganador es el atleta número {ganadorNum}")
#4-Escribir una función que, recibiendo el número de atleta de un competidor, 
# devuelva todos sus datos (nombre, número y tiempo de llegadad).
numAtleta=7
datosAtleta=datosAtletaNumero(lista_atletas,numAtleta)
if datosAtleta:
    print(f"Datos del atleta número {numAtleta}:")
    print(f"Nombre: {datosAtleta['nombre']}")
    print(f"Número: {datosAtleta['numero']}")
    print(f"Tiempo de llegada: {datosAtleta['tiempo_llegada']} segundos")
#5-OPCIONAL: Escribir una función que devuelva una tupla con los números de los 3 
# atletas que entraron al podio de ganadores en orden de llegada.