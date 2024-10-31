#Inmutabilidad de cadenas 

Cadena1 = "Hola mundo"          #Creacion de una cadena 
print ("Esta es la cadena original : ",  Cadena1)
#Cadena1[0] = "q"            #Modificacion ILEGAL de una cadena, no se puede, ya que son inmutables 

Cadena1 = "Adios"           #Creacion de una nueva cadena que permite ocupar el espacio en memoria de la cadena anterior
print ("Esta es la cadena despues de ser asignada con otro valor : ", Cadena1)
