def existe_tarj(numero):          # La tarjeta existe
    if numero != None:
        if len(str(numero)) == 9:
            return True

def verificada(mes, año):           # No está vencida
    fecha_hoy = [9, 2022]    # [mes, año de hoy]
    if año > fecha_hoy[1]:
        return True
      
    if año == fecha_hoy[1] and mes >= fecha_hoy[0]:
        return True
    
    
def tiene_saldo(balance, pago):
    if balance >= pago:
        return True

def pago_aceptado(numero, mes, año, balance, pago):
    if existe_tarj(numero) and verificada(mes, año) and tiene_saldo(balance, pago):
        return 'Pago aceptado'
    

numero = 123456789     # Número de tarjeta
mes = 8                # Mes de vencimiento
año = 2027             # Año de vencimiento]
balance = 1000         # Saldo de la tarjeta
fecha_hoy = [9, 2022]  # [mes, año de hoy]
pago = 700             # Pago a realizar


print(pago_aceptado(numero, mes, año, balance, pago))

