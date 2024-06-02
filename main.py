import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


plt.plot([1,2,3,4])
plt.ylabel('jakieś liczby')
plt.show()


# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# plt.axis((0, 6, 0, 20))
# plt.show()
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
# plt.xlim(0, 6)
# plt.ylim(0, 20)
# plt.show()

x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linowa')
plt.plot(x, x**2, label="kwadratowa")
plt.plot(x, x**3, label="sześcienna")
plt.xlabel('etykieta x')
plt.ylabel('etykieta y')
plt.title("Prosty wykres")
plt.legend()
plt.savefig('wykres matplot.png')
plt.show()
im1 = Image.open('wykres matplot.png')
im1 = im1.convert('RGB')
im1.save('nowy.jpg')

x = np.arange(0, 10.1, 0.1)
s = np.sin(x)
plt.plot(x, s, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x)')
plt.legend()
plt.show()
