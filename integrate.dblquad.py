import scipy as sp
from scipy import integrate
v=lambda x , y:x*y**4
v2=integrate.dblquad(v,0,6,lambda x:0 , lambda y: 1)
print(v2)
