import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


plt.plot([1,2,3,4])
plt.ylabel('jakieś liczby')
plt.show()


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
plt.axis((0, 6, 0, 20))
plt.show()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
plt.xlim(0, 6)
plt.ylim(0, 20)
plt.show()
