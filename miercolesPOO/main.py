from Cosas import Alumno, Perro
def main():
   al1 = Alumno("jose", 19, "ICO")
   print(vars(al1))
   al1.__nombre = "Diego"
   print(vars(al1))
   al1.set_nombre("Maria")
   print(vars(al1))
   print("-----To string----")
   print(al1)
   al1.set_edad(999)
   print(al1)
   al1.estudiar(4)

   print("===================perro===================")
   perro1 = Perro("Schauzer",2.5,.30)
   print(vars(perro1))
   perro1.raza = "Chihuahueño" #set pyhotonic
   print(vars(perro1))
   perro1.__raza = "otra"
   print(vars(perro1))


   print("================ TO STRING =================")
   print(perro1)
   perro1.raza= "salchicha"
   perro1.tamaño = ".2"
   print(perro1)
   cachorro = Perro.es_cachorro(perro1.edad)
   print(cachorro)
   Perro.dormir()

   danes = Perro.perro_grande(0.8)
   print(danes)



main()