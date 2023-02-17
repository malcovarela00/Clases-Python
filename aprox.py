import matplotlib.pyplot as plt

terminos = float(input('Ingrese cantidad de terminos a sumar: '))

n = 0
suma = 0

x = []
y = []

while n < terminos:
    serie = 1/(2**n)
    suma = serie + suma
    x.append(n)
    y.append(suma)
    n += 1

print('La suma de la serie es: ', suma)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafico')
plt.show()
    