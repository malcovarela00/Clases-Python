fecha_hoy = [9, 2022]    # [mes, año de hoy]
pago = 700               # Pago a realizar

class Tarjeta():
  numero = 123456789     # Número de tarjeta
  fecha = [8, 2027]      # [mes, año de vencimiento]
  balance = 1000         # Saldo de la tarjeta

def existe_tarj():          # La tarjeta existe
  if Tarjeta.numero != None and len(Tarjeta.numero) == 9:
    return True

def verificada():           # No está vencida
  if Tarjeta.fecha[1] > fecha_hoy[1]:
    return True
  
  if Tarjeta.fecha[1] == fecha_hoy[1] and Tarjeta.fecha[0] >= fecha_hoy[0]:
    return True

def tiene_saldo():
  if Tarjeta.balance >= pago:
    return

def pago_aceptado():
  if existe_tarj and verificada and tiene_saldo:
    return True
    
print(pago_aceptado)