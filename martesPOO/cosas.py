class Alumno:
    #Atributo de clase, es igual para todos los objetos
    facultad = "FES Aragón"

    #self es al1, se refiere al mismo objeto
    # self es equivalente a this de java

    def __init__(self,nom,ed,car):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = car