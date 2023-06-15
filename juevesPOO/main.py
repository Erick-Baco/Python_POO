from cosas import Libro,Autor,Alumno

def main():
    l1 = Libro.libro_planeta("El perfume",Autor("Patrick","PS"),1980)
    print(l1)

    #codigo para cambiar pseudonimo
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)

    print("========= HERENCIA ===========")
    al2 = Alumno("Erick",18,123456789,"ICO",9)
    al2.nombre = "Pablo"
    print(vars(al2))

main()