from cosas import *

def main():
    persona1 = Persona("Juan",19)
    print(persona1)
    print(Persona.descripcion)

    print("====== HERENCIA ALUMNO =============")
    alumno1 = Alumno ("JUAN",19,"123456789","ICO")
    print(alumno1)
    print(Alumno.descripcion)

    alumno2 = Alumno.constructor_defecto()
    print(alumno2)

    alumno2.nombre = "Pedro"
    print(alumno2)

    alumno2.dormir()

    print("============ HERENCIA PROFESOR ===========")
    profe1 = Profesor("Jesus",46,878787,"Ingenieria de Software")
    print(profe1)
    profe1.dormir()

    print("========== HERENCIA AYUDANTE PROFE ============")
    ayudante = AyudanteProfesor("Adrian",20,123321123,"ICO",123321,"Ingeniería de software",4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Hola"
    print(ayudante)
    ayudante.dar_clase("POO")

main()