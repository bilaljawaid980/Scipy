import scipy as sp
from scipy import integrate
v=lambda x:x**3
v2=integrate.quad(v,0,6)
print(v2)
