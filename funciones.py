"""
Los scripts de python se ejecutan linea a linea
Las funciones son formas de separar la lógica en piezas sin tener que ejecutarlas linea a linea,
 y ademas permitir reutilizar partes del código que se repiten
"""

"""
Las funciones se definen de la forma:
    
def nombre_de_la_funcion(argumento1, argumento2,...):
    logica_de_la_funcion
"""
#%%
def saludar():
    print("Hola Mundo!")
 
# Al crear la funcion saludar, no tenemos que escribir el print cada vez    
print(type(saludar))
saludar()

#%%

# La principal ventaja de las funciones es que nos permiten usar argumentos y 
# flexibilizar la lógica de nuestro código

def saludar(nombre):
    print(f"Hola {nombre}, ¿como estás?")
    
saludar("Manuel")
saludar("Antonio")

#%%
# Como esta función necesita un argumento, si la llamamos sin ningún argumento
# nos dará un error
saludar()
#%%
# Las funciones también pueden tener valores por defecto en los argumentos,
def saludar_despistado(nombre="amigo"):
    saludar(nombre)

saludar_despistado("Manuel")
saludar_despistado()

#%%
# Las funciones pueden devolver un valor. 

def suma(a, b):
    return a + b
    print("esto no se va a imprimir, porque la función acaba con el return")

resultado_suma1 = suma(2.5, 5)
print(resultado_suma1)
#%%
# ahora podemos usar el resultado de la función como input
resultado_suma2 = suma(resultado_suma1, 50)
print(resultado_suma2)
#%%
#Una funcion que no tiene un return devuelve None
def suma_erronea(a, b):
    resultado = a + b
    
resultado_suma1 = suma_erronea(2.5, 5)
print(resultado_suma1)


#%% Las funciones pueden tener un solo return, pero se pueden devolver multiples cosas!

def suma_y_resta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado = suma_y_resta(10, 5)
print(resultado)
print(type(resultado))

#%%
# podemos desempaquetar el resultado directamente
resultado_suma, resultado_resta = suma_y_resta(10, 5)
print(resultado_suma)
print(resultado_resta)


#%%
"""
Existe otra forma de crear funciones, las llamadas lambda o funciones anónimas
Se definen de la forma:
func_lambda = lambda input: output
Las funciones lambda se suelen utilizar cuando queremos aplicar lógica sencilla 
para la cual definir una función "oficial" no es necesario
"""

suma_lambda = lambda a, b: a + b
resultado_suma1 = suma_lambda(2.5, 5)
print(resultado_suma1)
#%%
# ahora podemos usar el resultado de la función como input
resultado_suma2 = suma_lambda(resultado_suma1, 50)
print(resultado_suma2)

def cuenta_regr(n):
	while n > 0:
		print(n)
		n -=1

cuenta_regr(-1)

def cuenta_regr(n):
	while n > 0 and n < 100:
		print(n)
		n +=1


def count_v2(dna, base):
    i = 0 # counter
    for c in dna:
        if c == base:
            i += 1
    return i

dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v2(dna, base)

# printf-style formatting
print '%s appears %d times in %s' % (base, n, dna)

# or (new) format string syntax
print '{base} appears {n} times in {dna}'.format(
    base=base, n=n, dna=dna)


def count_v1(dna, base):
    dna = list(dna)  # convert string to list of letters
    i = 0            # counter
    for c in dna:
        if c == base:
            i += 1
    return i

def count_v2_demo(dna, base):
    print ('dna:', dna)
    print ('base:', base)
    i = 0 # counter
    for c in dna:
        print ('c:', c)
        if c == base:
            print ('True if test')
            i += 1
    return i

n = count_v2_demo('ATGCGGACCTAT', 'C')



def count_v4(dna, base):
    i = 0 # counter
    j = 0 # string index
    while j < len(dna):
        if dna[j] == base:
            i += 1
        j += 1
    return i

