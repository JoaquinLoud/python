# # # # Tuplas
# # # # calcular dia año y hora en formato 
# # # """dia=int(input("Dijite el dia"))
# # # año=int(input("Dijite el dia"))
# # # hora=int(input("Dijite la hora"))
# # # fecha=(dia,año,hora)
# # # for x in fecha:
# # #     print(x)
# # # print(f"dia:{fecha[0]}mes:{fecha[1]}anyo:{fecha[2]}")"""
# # # # Diccionario
# # # # dictConElementos={

   
# # # # }
# # # # n=input("Ingrese el nombre :")
# # # # c=input("Ingrese el cargo :")
# # # # s=int(input("Ingrese el salario :"))
# # # # dictConElementos['nombre'] = n
# # # # dictConElementos['cargo'] = c
# # # # dictConElementos['salario'] = s

# # # # for (clave, valor)in dictConElementos.items():
# # # #     print (clave, valor)


# # # # print(dictConElementos)
# # # # dictConElementos.clear() #borra los elementos del diccionario
# # # # dictConElementos2 = dictConElementos.copy()
# # # # dictConElementos2 ['salario'] =200000
# # # # for(clave,valor)in dictConElementos2.items():
# # # #     print(f"{clave}:{valor}")
# # # # if(dictConElementos==dictConElementos2):
# # # #     print("True")
# # # # else:       
# # # # #     print("else")     
# # # # Lista=[]
# # # # dictConElementos={
# # # # } 
# # # # if(dictConElementos.get('salario')>1000000):
# # # #     print("Debe pagar seg social")
# # # # else:print("No Debe pagar seg social")


# # # from calendar import c

# # # listaemp=[]
# # # dictConElementos={}

# # # continuar=True
# # # while (continuar):
# # #     n=input("Ingrese el nombre :")
# # #     c=input("Ingrese el cargo :")
# # #     s=int(input("Ingrese el salario :"))
# # #     dictConElementos['nombre']=n
# # #     dictConElementos['cargo']=c
# # #     dictConElementos['salario']=s
# # #     cont=input("desea continuars/n")
# # #     listaemp.append(dictConElementos)
# # #     if(cont =='n'):
# # #         continuar=False
# # #     print(listaemp)

# # # dictConElementos={
# # #     'nombre':'joaquin',
# # #     'cargo':'Docente',
# # #     'salario':200000,}
# # # dictConElementos.pop('cargo')
# # # print(dictConElementos.values())

# # # """Ejercicio en clase
# # # utilizar una tupla donde tengo todas las opciones de in menu 
# # # 1 opcion 1 crear lista
# # # 2 opcion2  crear tupla
# # # 3 opcion3 crear diccionario
# # # y luego pintar el menu
# # #  """

# # Diccionario=[]
# # def inicio():
    
# #  while continuar=True:
# # opcion=input("Porfavor Ingrese una opcion: ")
# # print(" 1-sumar /n 2-Restar /n 4-Multiplicar")

# # if opcion==1:
# #      print("la suma de los valores es ")
# # def suma ():



# #     # tupla=(o1,o2,o3)
# #     # Diccionario['Crear lista']=o1
# #     # Diccionario['Crear tupla']=o2
# #     # Diccionario['Crear diccionario']=o3
# #     # tupla=(o1,o2,o3)
# #     # for x in tupla:
# #     #   print(x)
      
# #     cont=input("desea continuars/n")
# #     if(cont =='n'):
# #         continuar=False
# # if __name__ == "__main__":
# #     inicio()


# # # def calcularArea():
# # #     base=int(input("Ingese la base"))
# # #     altura=int(input("Ingese la altura"))
# # #     area=base*altura/2
# # #     print(f"El area del triangula de base{base}yaltura{altura}es:{area}")

# # # def inicio():
# # #     calcularArea()

# # # if __name__ == "__main__":
# # #     inicio()
# # # def calcularArea(b,a):
# # #     alt=b*a/2
# # #     return(alt)

# # # base=int(input("Ingese la base>"))
# # # altura=int(input("Ingese la altura>"))
# # # def inicio():
# # #     area=calcularArea(base,altura)
# # #     print(f"El area del triangula de base(base)yaltura{altura}es:{area}")

# # # if __name__ == "__main__":
# # #     inicio()


# from multiplicacion import multiplicacion
# from resta import resta
# from suma import suma

# listaEmp = []
# dicEmp = {}
# continuar = True
# while(continuar):
#     print("Ingrese una opcion en el menu")
#     print("1-Suma\n2-Resta\n3-Multiplicacion") 
#     opcion =input("Porfavor dijite una opcion =>")
#     if(opcion=="1"):
#      print("Usted dijito la opcion numero 1  a continuacion dijite los valores que quiere sumar ")
#      sumar=suma()
#      dicEmp = {'la suma es ': suma}
#     if(opcion=="2"):
#         print("Usted dijito la opcion numero 2  a continuacion dijite los valores que quiere restar ")
#         restar=resta()
#     if(opcion=="3"):
#         print("Usted dijito la opcion numero 3  a continuacion dijite los valores que quiere restar ")
#         multiplicar=multiplicacion()
# # s = int(input("Usted dijito la opcion numero 1  a continuacion dijite los valores que quiere multiplicar "))
# # dicEmp = {'la suma es ': suma, 'la resta es ': resta, 'la resta es': multiplicacion}
# # listaEmp.append(dicEmp)
#     cont = input("desea continuar s/n: ")
#     if (cont == 'n'):
#         continuar = False
#     for lista in listaEmp:
#         print(lista)
