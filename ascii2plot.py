import sys
import numpy as np
import matplotlib.pyplot as plt


filein = sys.argv[1]

data = np.loadtxt(filein)

plt.imshow(data, cmap='gray')
plt.show()

