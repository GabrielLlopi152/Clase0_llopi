#CADENA DE CARACTERES

'''
\ (contrabarra), secuencia de escape para usar comillas dentro de una cadena de caracteres, o usar comandos
\n              separa en lineas el texto (como el "enter")
\t              tabula el texto, separandolo un espacio
%               permite añadir un numero al texto, (se debe aclarar al final que variable es)
%d              decimal
%f              float
%s              str
in/not in       busca la cadena de caracteres en otra cadena, y devuelve True o False
.algo()         es un metodo
[1:10]          rango que recorre
[1:]            recorre hasta el final
[1:5:2]         el tercer Num indica el salto que da entre los caracteres
[1::2]          hasta el final y cada 2 caracteres
del             elimina una cadena de caracteres/variable
'''

Taberna = 'Moe\'s'
saludo = 'hola\nchau'
mensaje = """
hola papus
adios papus"""

numero = 3
resultado = "El numero es: %d" %numero

print(Taberna * 3) #Se puede multiplicar cadenas
print(saludo)
print(mensaje)
print(resultado)
print("cielo" in "rascacielos") # busca la cadena de caracteres
