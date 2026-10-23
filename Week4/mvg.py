import numpy as np
import matplotlib.pyplot as plt

mean = [0,10]

cov = [[10,0.8],
       [0.8,1]]

samples = np.random.multivariate_normal(mean,cov,500)

plt.scatter(samples[:,0], samples[:,1])
plt.axis('equal')
plt.show()