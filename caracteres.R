#Realizar un programa en R que solicite caracteres alfabeticos al usuario 
#(e inmediatamente los imprima) hasta que se introduzca un cero



# Solicitar caracteres alfabéticos al usuario
caracter <- readline("Ingrese un carácter alfabético (o '0' para terminar): ")

# Iterar hasta que se introduzca un cero
while (caracter != "0") {
  # Imprimir el carácter ingresado
  print(paste("Carácter ingresado:", caracter))
  
  # Solicitar el siguiente carácter alfabético al usuario
  caracter <- readline("Ingrese un carácter alfabético (o '0' para terminar): ")
}

# Imprimir mensaje de finalización
print("Programa finalizado.")