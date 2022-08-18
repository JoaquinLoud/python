listauno=[]
terminar=True
while(terminar):
    nombre = input("Ingrese el Nombre = ")
    apellido = input("Ingrese el Apellido = ")
    edad = int(input("Ingrese la Edad = "))
    listauno.append([nombre, apellido, edad])
    t = input("Desea Continuar S/N =")
    if(t == "n"):
        terminar = False
print(listauno)
listados=([nombre,apellido,edad])
listados.reverse()
print(listados)