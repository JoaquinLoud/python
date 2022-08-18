#Ejericico 2
#Leer una cadena y devolver cada palabra de la cadena y el nuemero de veces que se repite
cadena = "Desarrollo de Software: Desarrollo \n"
print(cadena)

print(f"-{cadena[0:10]}- las veces que se repite esta palabra son:  {cadena.count('Desarrollo')}\n")
print(f"-{cadena[11:13]}- las veces que se repite esta palabra son:  {cadena.count('de')}\n")
print(f"-{cadena[14:22]}- las veces que se repite esta palabra son: {cadena.count('Software')}\n")
