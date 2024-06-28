class Boligrafo:
    def __init__ (self, grosor_punta, color):
        self.__grosor = grosor_punta
        self.__color = color
        self.__capacidad_maxima = 100
        self.__cantidad_tinta = 80

    @property
    def grosor_punta(self):
        return self.__grosor
    @property
    def color(self):
        return self.__color
    @property
    def capacidad_maxima(self):
        return self.__capacidad_maxima
    @property
    def cantidad_tinta(self):
        return self.__cantidad_tinta
    
    def descripcion(self):
        return "{0}, {1}, {2}, {3}".format(self.__grosor, self.__color, self.__capacidad_maxima, self.cantidad_tinta)
    
    def escribir(self, texto):
        if self.__cantidad_tinta >= len(texto):
            self.__cantidad_tinta -= len(texto)
            mensaje = texto
        else:
            mensaje ="No alcanza la tinta"

        return mensaje
    
    def recargar (self, cantidad):
        auxiliar = cantidad + self.__cantidad_tinta
        if auxiliar > self.__capacidad_maxima:
            self.__cantidad_tinta = 100
            auxiliar -= 100
            sobrante = auxiliar
            mensaje = f"Lapicera recargada. Sobra {sobrante} cantidad de tinta"
        else:
            self.__cantidad_tinta = auxiliar
            mensaje = f"Lapicera recargada {self.__cantidad_tinta}"

        return mensaje



boligrafo_azul = Boligrafo("Grueso", "Azul")
print(boligrafo_azul.descripcion())


print(boligrafo_azul.escribir("hola"), boligrafo_azul.cantidad_tinta)
print(boligrafo_azul.escribir("hola"), boligrafo_azul.cantidad_tinta)
print(boligrafo_azul.escribir("hola"), boligrafo_azul.cantidad_tinta)
print(boligrafo_azul.escribir("hola"), boligrafo_azul.cantidad_tinta)

print(boligrafo_azul.recargar(20))
print(boligrafo_azul.recargar(20))
print(boligrafo_azul.recargar(30))
    

        
