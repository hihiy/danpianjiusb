import math
h=30.0
l=50.0
w=25.0
sigma=0.0
n=1
u=1.0

for i in range(n,100000,2):
    sigma+=(1/(i**5)*(192/math.pi**5)*h/w*math.tanh(i*math.pi*w)/2/h)

result = 12*u*l/(h**3)/w/(1-sigma)

print(result)