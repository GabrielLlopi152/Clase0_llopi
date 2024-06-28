'''diccionario_personaje = {
    'nombre': 'Ricky',
    'apellido': 'bartocenllo',
    'edad': '23',
    'genero': 'M'
}

print(diccionario_personaje)
'''

#CLASES (CLASS)
#se definen con la primer letra en mayuscula

class Personaje:                                     #ESTO ES UNA CLASE
    tipo = "Personaje"                                     
    def __init__(self, id, nombre, apellido, edad) -> None:
        self.id = id
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self.lista = [id, nombre, apellido, edad]

    def __getitem__(self, index):
        return self.lista[index]
    def __contains__(self, item):
        return item in self.lista
    
    def descripcion(self):
        return "{0}, {1}".format(self._nombre, self._apellido)
    def get_nombre(self):
        return self._nombre
    def get_apellido(self):
        return self._apellido
    def get_edad(self):
        return self._edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
personaje_1 = Personaje(0, 'Gabriel', 'Llopi', 19)   #ESTO ES UN OBJETO
personaje_2 = Personaje(1, 'Leonel', 'Messi', 37)

print(Personaje.tipo)
print(personaje_1.get_apellido(), personaje_1.get_nombre())

personaje_1.nombre = "Jerry"
print(personaje_1.descripcion())
print(personaje_2.lista)

print(personaje_2.nombre)

'''
"_"             el guion aclara que es un elemento protegido, usado para seguridad
"__"            el doble guion vuelve privado el elemento
"self"          significa propio. se usa para interactuar con los datos de una clase
__str__         devuelve un mensaje determinado al llamar al objeto
__len__         devuelve numeros
__getitem__     guarda la informacion en una lista y la muestra al llamar el metodo
__setitem__     permite modificar datos de la lista interna del objeto}
__delitem__     elimina de la lista el index que se ingresa
__contains__    verifica si un elemento está contenido en la lista
'''




