import json

''' OPERADORES TERNARIOS
ES UN IF RESUMIDO,
x = 43
result = "Es la respuesta" if x == 42 else "anduviste cerca" 
    VERDADERO                 CONDICION        FALSO

    
    FUNCIONES LAMBDA
ES UNA FUNCION DE UNA SOLA LINEA
'''

def suma (a, b):
    return a + b

#print(suma(5,2))

#sumar = lambda a, b: a + b

#print(sumar)

''' ARCHIVOS
Archivos de texto
TXT     HTML
Archivos binarios
JPG     GIF     PDF     MP4

r               abre archivo texto para lectura
rb              abre un archivo binario para lectura
r+              abre un archivo de texto para escritura/lectura
w               abre un archivo de texto para escritura (SI EXISTE, LO SOBREESCRIBE)
wb              abre archivo para escritura binario (SI EXISTE, SE SOBREESCRIBE)
w+              abre un archivo para escritura/lectura (SI EXISTE, LO SOBREESCRIBE)
a               abre un archivo y anexa informacion (lo concatena)

("modo", ruta y archivo)
archivo = open(nombre_archivo, "modo")

.tell()         indica en qué byte está situado el puntero
.mode           devuelve el modo con el que se interactua
.name           devuelve el nombre del archivo
.read           lee el archivo
.readlines      lee linea por linea (se separan por el ENTER)
open()          abre archivo
.close()        cierra el archivo
.write()        escribe en el archivo
.writelines()   escribe lineas en el archivo
.seek()         permite modificar la posicion del puntero
with / as       abre el archivo y luego python se encarga de cerrarlo

CSV es un tipo de archivo que está delimitado. Funciona como un tipo de tabla
JSON es un formato para intercambio de datos, es de lectura para humano y maquina. Es muy utilizado.
'''

archivo = open("texto.txt", "r") #el archivo es un tipo FILE
#uso los datos para lo que necesite y luego se cierra.

'''print(archivo.mode)  #modo en que se está interactuando
print(archivo.name) #nombre del archivo

texto = archivo.read(10) #lee el archivo
print(texto)

lineas_texto = archivo.readlines()
for linea in lineas_texto:
    print(linea)'''

'''archivo.close()

with open('data.json') as file:
    data = json.load(file)
    print(data['clientes'])
    print(data['clientes'][1])
    print(data['clientes'][1]['edad'])

'''