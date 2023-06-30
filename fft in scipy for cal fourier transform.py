import scipy as sp
import numpy as np
from scipy import fft
v=np.array([[1,2,3,4,5],[6,7,8,9,10]])
trans=sp.fft(v)
print(trans)
