#Hecho por Emiliano Villanueva Barrera
from matplotlib.pylab import *
from math import *
from numpy import *

a=(2143)
b=(1726)
c=(3494)
d=a+b+c

a1=str(a)
b1=str(b)
c1=str(c)
d1=str(d)

Estados = ['COAHUILA ', 'YUCATAN ', 'SINALOA ','T.MUERTES ']

deads = [a,b,c,d]

pos = arange(len(Estados))

figure(figsize=(80, 40),facecolor=('yellow'))

subplot(132)
bar(Estados, deads)
colores=('orange','green','blue','black')
bar(pos, deads, color=colores)
grid()
title('Muertes COVID con barras')
xlabel('Estados',)
ylabel('Muertes')

subplot(132,)
scatter(Estados, deads)
scatter(pos, deads, color='brown')
plot(Estados, deads)
plot(pos, deads, color='yellow')
grid()
title('Muertes COVID con barras, lineas y puntos')
xlabel('Estados')
ylabel('Muertes')

show()
#Hecho por Emiliano Villanueva Barrera