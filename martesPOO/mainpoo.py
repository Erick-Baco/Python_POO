from cosas import Alumno

def main():

    """al1 = Alumno()
    print(al1)

    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("=========")

    Alumno.facultad = "TEC"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print("vistazo a los objetos")
    print(vars(al1))
    print(vars(al2))

    print("modificar atributos publicos (no encapsulamiento)")
    al1.edad=999
    print(vars(al1))"""

    al1 = Alumno("Diego",19,"ICO")
    al2 = Alumno("Erick",18,"IEE")
    print(vars(al1))
    al1.__edad = 333
    print(al1.__edad)
    print(vars(al1))


main()
