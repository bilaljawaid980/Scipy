import scipy as sp
import numpy as np
from scipy import linalg
v=np.array([[1,2],[7,8]])
n=np.array([[9,2],[7,5]])

w=linalg.eig(n)
print(w)
