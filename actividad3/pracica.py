# listas = [ "lunes" , "martes" , "miercoles", "jueves" , "viernes"]
# print(listas[-5])
def menu ():
    opción  =  int ( input ( "opciones del menu " ))
    diccionario  = {}

    for n in range ( 1 , n + 1 ):

        funcion  =  input ( "Nombre" )
        descFuncion  =  input ( "Descripción" )
        diccionario [ n ] = ( descFuncion , funcion )

    print ( " Bienvenido" )
    for  x  in  diccionario :
        print ( f" { x } . { diccionario [ x ][ 0 ] } " )
        opción  =  int ( input ( "Digite opción:" ))
    else( opción , diccionario ):

def  principal ():
 op  =  menu ()
    
    for clave in  [ 1 ]:
        if (  [ 0 ] == clave ):
            print ( "funcion llamada " )
            print (  [ 1 ][ clave ][ 1 ])
    
if __name__ ==  "__principal__" :
principal()