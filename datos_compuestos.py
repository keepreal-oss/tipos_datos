#Listas
#Son conjuntos de datos ordenados y mutables
#pueden almacenar distintos tipos de datos

print("Tipos de datos LISTA")
lista= ["Aquiles Baeza", True, 45]
print(lista) 
print(type(lista))
print(lista[0])

lista[1]= False
print(lista)

# Diccionarios
# Son conjuntos de pares de datos ordenados y mutables
# se puede acceder a cada elemento de la lista por su indice o su nombre

print("Tipos de datos DICCIONARIO")
diccionario= { 
  'nombre': 'Alan Brito Delgado',
 'estudiante': False ,
   'edad': 21
}

print(diccionario)
print(diccionario['edad'])

diccionario['edad']= 22
print(diccionario['edad'])

# Conjuntos
# Son conjuntos de pares de datos desordenados e inmutable
# podemos agregar nuevos elementos

print("Tipos de datos CONJUNTO")
conjunto = {2,'Marco Henriquez',True} 
print(conjunto)
print(type(conjunto))

conjunto.add('Jaime Rios')
print(conjunto)
conjunto.pop()
print(conjunto)

# Tuplas
print("Tipos de datos TUPLA")
tupla= ('Armando Casas', False,45)
print(tupla)
print(type(tupla))

# Los cambios en tuplas
#  tupla[0]='Jose Feliciano'
#  print(tupla)