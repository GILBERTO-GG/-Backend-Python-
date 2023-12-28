library(tidyverse)
rm(list=ls())
cat("\014")

tb <- tibble(Autor = c("Baldor, Aurelio", "Baldor, Aurelio", "Baldor, Aurelio"), 
             Titulo = c("Aritmética", "Álgebra", "Geometría y Trigonometría"), 
             Editorial = c("Patria", "Patria", "Patria"), 
             Edicion = c(4, 4, 4), Fecha = c(2019, 2019, 2019), 
             ISBN13 = c(9786075502076, 9786075502090, 9786075502069),
             Precio = c(410, 410, 410))

df <- data.frame(Autor = c("Baldor, Aurelio", "Baldor, Aurelio", "Baldor, Aurelio"), 
                 Titulo = c("Aritmética", "Álgebra", "Geometría y Trigonometría"), 
                 Editorial = c("Patria", "Patria", "Patria"), 
                 Edicion = c(4, 4, 4), Fecha = c(2019, 2019, 2019), 
                 ISBN13 = c(9786075502076, 9786075502090, 9786075502069),
                 Precio = c(410, 410, 410))

print(class(tb))
print(class(df))

# Funciones de conversión
df2tb <- as_tibble(df)
tb2df <- as.data.frame(tb)
print(class(df2tb))
print(class(tb2df))

# Impresión de tibble vs data frame
print(tb)
print(df)

# Subconjuntos de tibble vs data frame
print(class(tb[1,1]))
print(class(df[1,1]))

# Referencia a variables dentro de la misma estructura (tibble vs. data frame)
tb <- tibble(Autor = c("Baldor, Aurelio", "Baldor, Aurelio", "Baldor, Aurelio"), 
             Titulo = c("Aritmética", "Álgebra", "Geometría y Trigonometría"), 
             Editorial = c("Patria", "Patria", "Patria"), 
             Edicion = c(4, 4, 4), Fecha = c(2019, 2019, 2019), 
             ISBN13 = c(9786075502076, 9786075502090, 9786075502069),
             Precio = c(410, 410, 410), Adquisicion = Fecha)

df <- data.frame(Autor = c("Baldor, Aurelio", "Baldor, Aurelio", "Baldor, Aurelio"), 
                 Titulo = c("Aritmética", "Álgebra", "Geometría y Trigonometría"), 
                 Editorial = c("Patria", "Patria", "Patria"), 
                 Edicion = c(4, 4, 4), Fecha = c(2019, 2019, 2019), 
                 ISBN13 = c(9786075502076, 9786075502090, 9786075502069),
                 Precio = c(410, 410, 410), Adquisicion = Fecha)




