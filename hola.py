print ("hola mundo - hello world") #Primera linea de comando en python

x= 4 * 3    #para comprobar como hacer calculos aritmeticos
print (x)

# vamos a importar el modulo math para ver como funciona
import math
print (math.pi * 4)    #no olvidarse de poner el print() y salvar antes de ejecutar

print (math.pi ** 2)

print (math.sqrt(4)) #raiz cuadrada de 4 y de 12

print (math.sqrt(12))

#vamos a importar el modulo random
import random
print (random.random ())
lista = [1, 2, 3, 4]
print (random.choice(lista))
random.shuffle(lista)
print (lista)