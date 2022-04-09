class Personaje:

    #CONSTRUCTOR
    def __init__(self):
        #ATRIBUTOS
        # _ se utiliza para protejer un atributo asi= self._nombre
        # __ se utiliza para hacer un atributo privado asi= self.__nombre
        self.__nombre=None
        self.__edad=None

    #METODOS GET (LEER/OBTENER VALOR DE UN ATRIBUTO)
    # @property anotacion
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    #METODOS SET (ESCRIBIR/INGRESAR/LLEVAR UN VALOR A UN ATRIBUTO)

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    
    @edad.setter
    def edad(self,edad):
        if(edad < 0):
            print("Digite edad valida no permito numeros negativos")
        else:
            self.__edad=edad