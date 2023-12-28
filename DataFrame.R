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

suma_df <- 0
suma_tb <- 0
for (i in 1: length(df$Precio)) {
  suma_df <- suma_df + df$Precio[i]
  suma_tb <- suma_tb + tb$Precio[i]
}
print(suma_df)
print(suma_tb)

