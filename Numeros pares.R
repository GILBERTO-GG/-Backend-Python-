
#Realizar un programa en R que sume todos los números pares entre 1 y 100

# Inicializar la variable de suma
suma <- 0

# Iterar desde 1 hasta 100
for (num in 1:100) {
  # Comprobar si el número es par
  if (num %% 2 == 0) {
    # Sumar el número a la suma total
    suma <- suma + num
  }
}

# Imprimir el resultado
print(paste("La suma de los números pares entre 1 y 100 es:", suma))






