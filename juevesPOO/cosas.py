class Autor:

    def __init__(self,nombre,pseudo):
        self.__nombre = nombre
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self,pseudo):
        self.__pseudonimo = pseudo

    def __str__(self):
        return f"Mombre: {self.__nombre} pseudonimo: {self.__pseudonimo}"

    def escribir(self):
        print(f"{self.__pseudonimo} esta escribiendo su siguiente obra")




class Libro:
    def __init__(self,titulo,autor,anio,editorial):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__editorial = editorial

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self,titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self,autor):
        self.__autor = autor

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self,anio):
        self.__anio = anio

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def edad(self,editorial):
        self.__editorial = editorial

    def __str__(self):
        return f"""
            Titulo = {self.__titulo}
            Autor = {self.__autor}
            Año = {self.__anio}
            Editorial = {self.__editorial}"""

    @classmethod
    def libro_planeta(cls, titulo, autor, anio):
        return cls(titulo, autor, anio, "Palneta")

    def leer(self,minutos):
        print(f"leyendo por {minutos} minutos")

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

class Alumno(Persona):
    def __init__(self,nombre,edad,numero_cuenta,carrera,promedio):
        super().__init__(nombre,edad)
        self.__numero_cuenta = numero_cuenta
        self.__carrera = carrera
        self.__promedio = promedio
