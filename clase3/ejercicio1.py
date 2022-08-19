# # Tuplas
# # calcular dia año y hora en formato 
# """dia=int(input("Dijite el dia"))
# año=int(input("Dijite el dia"))
# hora=int(input("Dijite la hora"))
# fecha=(dia,año,hora)
# for x in fecha:
#     print(x)
# print(f"dia:{fecha[0]}mes:{fecha[1]}anyo:{fecha[2]}")"""
# # Diccionario
# # dictConElementos={

   
# # }
# # n=input("Ingrese el nombre :")
# # c=input("Ingrese el cargo :")
# # s=int(input("Ingrese el salario :"))
# # dictConElementos['nombre'] = n
# # dictConElementos['cargo'] = c
# # dictConElementos['salario'] = s

# # for (clave, valor)in dictConElementos.items():
# #     print (clave, valor)


# # print(dictConElementos)
# # dictConElementos.clear() #borra los elementos del diccionario
# # dictConElementos2 = dictConElementos.copy()
# # dictConElementos2 ['salario'] =200000
# # for(clave,valor)in dictConElementos2.items():
# #     print(f"{clave}:{valor}")
# # if(dictConElementos==dictConElementos2):
# #     print("True")
# # else:       
# # #     print("else")     
# # Lista=[]
# # dictConElementos={
# # } 
# # if(dictConElementos.get('salario')>1000000):
# #     print("Debe pagar seg social")
# # else:print("No Debe pagar seg social")


# from calendar import c

# listaemp=[]
# dictConElementos={}

# continuar=True
# while (continuar):
#     n=input("Ingrese el nombre :")
#     c=input("Ingrese el cargo :")
#     s=int(input("Ingrese el salario :"))
#     dictConElementos['nombre']=n
#     dictConElementos['cargo']=c
#     dictConElementos['salario']=s
#     cont=input("desea continuars/n")
#     listaemp.append(dictConElementos)
#     if(cont =='n'):
#         continuar=False
#     print(listaemp)

# dictConElementos={
#     'nombre':'joaquin',
#     'cargo':'Docente',
#     'salario':200000,}
# dictConElementos.pop('cargo')
# print(dictConElementos.values())

# """Ejercicio en clase
# utilizar una tupla donde tengo todas las opciones de in menu 
# 1 opcion 1 crear lista
# 2 opcion2  crear tupla
# 3 opcion3 crear diccionario
# y luego pintar el menu
#  """

# Diccioneario=[]

# continuar=True
# while (continuar):
#     opcion=input("Porfavor Ingrese una opcion: ")
#     o1=input(" Opcion 1: ")
#     o2=input(" Opcion 2: ")
#     o3=input(" Opcion 3: ")
#     tupla=(o1,o2,o3)
#     Diccioneario['Crear lista']=o1
#     Diccioneario['Crear tupla']=o2
#     Diccioneario['Crear diccionario']=o3
#     tupla=(o1,o2,o3)
#     for x in tupla:
#       print(x)
      
#     cont=input("desea continuars/n")
#     if(cont =='n'):
#         continuar=False


# def calcularArea():
#     base=int(input("Ingese la base"))
#     altura=int(input("Ingese la altura"))
#     area=base*altura/2
#     print(f"El area del triangula de base{base}yaltura{altura}es:{area}")

# def inicio():
#     calcularArea()

# if __name__ == "__main__":
#     inicio()
def calcularArea(b,a):
    alt=b*a/2
    return(alt)

base=int(input("Ingese la base>"))
altura=int(input("Ingese la altura>"))
def inicio():
    area=calcularArea(base,altura)
    print(f"El area del triangula de base(base)yaltura{altura}es:{area}")

if __name__ == "__main__":
    inicio()

    