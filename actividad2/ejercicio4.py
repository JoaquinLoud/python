NumRango = int(input("Ingrese el numero de Rango que desee Ver:"))
Fibonacci =[0,1]
for i in range(NumRango-2):
  Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])
print(Fibonacci)