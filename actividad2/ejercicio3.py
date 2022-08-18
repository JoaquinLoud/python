# Ejercicio 3
# Crear una lista_uno y adicione elementos en ella hasta que el usuario elija terminar.
# Una vez terminada, crear una segunda lista_dos, en ella llene los valores de lista_uno de forma descentente.
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