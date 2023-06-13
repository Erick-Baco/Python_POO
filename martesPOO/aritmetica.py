
def suma(a,b):
    if a != None and b != None:
        c = a + b
    else:
        print("Envía ambos valores")
        c=0
    return c

#valores por defecto
def resta(a=0,b=1):
    return  a-b