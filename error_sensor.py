https://replit.com/join/xxmcqbxkqd-sol-veronicaver

"""
Desarrolla un programa que calcule el porcentaje de error de un sensor de temperatura
LM35 en un laboratorio. El programa debe detectar y almacenar las lecturas incorrectas,
mostrando al final el porcentaje de veces que el sensor dio valores fuera del rango esperado
(entre 10 y 40 grados Celsius).
"""

lect_temp = int(input("Cuántas lecturas de temperatura tienes?   "))
c = 0 
temp = 0
sens_err = 0
while c < lect_temp:
  c += 1
  temp = float(input("Inserta la temperatura:  "))
  if temp >= 10 and temp <= 40:
    pass
  else:
    sens_err += 1

print(f"El número de lecturas incorrectas fue:  {sens_err}")
porcentaje_equivocado = sens_err*100/lect_temp
print(f"El procentaje de lecturas incorrectas es:   {porcentaje_equivocado}")
