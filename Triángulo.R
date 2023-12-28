#Leer tres números de la consola, utilizando un programa en R, 
#y determinar si esos tres números podrían formar un triángulo:  
#a+b > c       a+c >b     b+c >a


# Leer los tres números desde la consola
a <- as.numeric(readline("Ingrese el primer número: "))
b <- as.numeric(readline("Ingrese el segundo número: "))
c <- as.numeric(readline("Ingrese el tercer número: "))

# Comprobar si los números pueden formar un triángulo
if ((a + b > c) && (a + c > b) && (b + c > a)) {
  print("Los números pueden formar un triángulo.")
} else {
  print("Los números no pueden formar un triángulo.")
}5