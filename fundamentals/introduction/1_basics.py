print('hola mundo con python')      #impresión}

#Variables
x=2                                 # esta es una variable de tipo entero conb valor 2
y=3                                 # variable entera de valor 3
z=x+y                               # variable son valor asignado de la suma de x+y (5)
print(z)                            # impresion del valor de z

#¿Qué podemos almacenar en variables python?
a1=10              #números enteros
a2=15.3            #números decimales (reales). Es tipo de dato flotante
a3="Este es un texto con comillas simples" #texto
a4='Texto, pero con comillas simples' #texto
a5= True            #valor booleano, cuidar la semantica ya que iniciar con mayúscula
a6=3.3+5.1j         # números complejos, parte real e imaginaria usando la letra j

#Tipos de datos compuestos: tuplas, listas, rangos y diccionarios

#Listas
lista1=[1,2,3]              #lista1 es un elemento de tipo lista, tiene 3 elementos contenidos
lista2=[1,9.5,'texto']      #lista2 es una lista con varios tipos de datos en la misma

#Cómo puedo acceder a los elementos de listas?
# Para acceder a los elementos de listas debo utilizar un índice. Tener en cuenta que el primer elemento
# de una lista, es elemento 0.

print(lista1[0])            #imprime el valor del primer elemento de lista 1, en este caso es 1

#imprimir mensaje con valores de variables
print('El valor de z es', z, 'mientras que el segundo elemento de lista2 es', lista2[1])

#Modificar elementos de una lista
lista2[0]='NuevoValor'

print(lista2)