alfa_g= int(input ("ingrese los grados del primer angulo:"))
alfa_n= int(input ("ingrese los minutos del primer angulo:"))
alfa_s= int(input ("ingrese los segundos del primer angulo:"))

beta_g= int(input ("ingrese los grados del segundo angulo:"))
beta_n= int(input ("ingrese los minutos del segundo angulo:"))
beta_s= int(input ("ingrese los segundos del segundoo angulo:"))

suma_g = alfa_g + beta_g
suma_n=  alfa_n + beta_n
suma_s=  alfa_s + beta_s

if suma_s >= 60:
  suma_s = suma_s -60
  suma_n = suma_n + 1
if suma_n >= 60:
  suma_n = suma_n -60
  suma_g = suma_g + 1

print("la suma es", suma_g, "grados", suma_n, "minutos", suma_s, "segundos")

import math as mat

numero_pi= mat.pi
180= numero_pi
360= 2* numero_pi

print(135*(numero_pi / 180))

import math as mat

numero_pi= mat.pi

print(35*(numero_pi) / 180))

import math as mat

numero_pi= mat.pi

print(185*((2*numero_pi) / 185))

import math as mat

numero_pi= mat.pi
## numero_pi= 180
## 2 * numero_pi=360


print(((numero_pi*3)/4)* (360/(2*numero_pi)))

import math as mat


print((numero_pi/6)* (180/(numero_pi)))

import math as mat


print(((2*numero_pi/7)* (360/(2*numero_pi)))