import numpy as np
import matplotlib.pyplot as pp

def sech(x):
    return (1/np.cosh(x))

def function(x):
    return (2 + (0.75 * np.tanh(2*x)))

def derivative(x):
    return (1.5*(sech(x)**2))

def central_differencing(x,h):
    return ((function(x+h))-(function(x-h))/(2*h))

figure = pp.figure(figsize=(7,5),layout='constrained')
spec = figure.add_gridspec(ncols=2, nrows=2)

x1 = []
x2 = []
x3 = []
x4 = []

y1 = []
y2 = []
y3 = []
y4 = []

s1 = 1
s2 = 0.5
s3 = 0.1
s4 = 0.1

l1 = 5
l2 = 9
l3 = 41
l4 = 41

for i in range (l1):
    x1.append(-2+(s1*i))
    y1.append(central_differencing(x1[i],s1))

for i in range (l2):
    x2.append(-2+(s2*i))
    y2.append(central_differencing(x2[i],s2))

for i in range (l3):
    x3.append(-2+(s3*i))
    y3.append(central_differencing(x3[i],s3))

for i in range (l4):
    x4.append(-2+(s4*i))
    y4.append(derivative(x4[i]))

plot1 = figure.add_subplot(spec[0,0])
plot1.plot(x1,y1)

plot2 = figure.add_subplot(spec[0,1])
plot2.plot(x2,y2)

plot3 = figure.add_subplot(spec[1,0])
plot3.plot(x3,y3)

plot4 = figure.add_subplot(spec[1,1])
plot4.plot(x4,y4)

pp.show()

