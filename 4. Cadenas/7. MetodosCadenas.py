#Metodos de Cadena en python

#Creacion de cadenas 

Nombre = "jhon"
Apellido = "PEREZ"
Pais = "    Colombia   "
print(f"Cadena original {Nombre}")

#uso de upper, para convertir la cadena a mayusculas 
Mayuscula = Nombre.upper()
print(f"Cadena modificada usando upper {Mayuscula}")

#Uso de lower, para convertir la cadena a minusculas 
Minuscula = Apellido.lower()
print(f"Cadena modificada usando lower {Apellido}")    

#Uso de strip para eliminacion de espacios en blanco tanto al principio como al final de la cadena
Espacios = Pais.strip()
print(f"Cadena modificada usando strip {Espacios}")

#Uso de len para encontrar el tamaño de la cadena 
Tamaño = len(Nombre)
print(f"El tamaño de la cadena es : {Tamaño}")

#Bonus, Tambien podemos modificar las cadenas sin crear una nueva, simplemente modificando el valor en la impresion de esta 

print(f"Cadena modificada desde linea de impresion {Nombre.upper()} {Apellido.lower()} y soy de {Pais.strip()}")



