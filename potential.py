import numpy as np
import matplotlib.pyplot as pp

class field_vector:
    def __init__(self,x,y,xcomp,ycomp):
        self.x = x
        self.y = y
        self.xc = xcomp
        self.yc = ycomp

def potential_calculation(x,y):
    k = 9000000000
    
    r1 = np.sqrt(((x+0.05)**2)+((y)**2))
    r2 = np.sqrt(((x-0.05)**2)+((y)**2))
    
    return (((k*1)/r1)+((k*-1)/r2))

def field_x(x,y):
    k = 9000000000

    return (((k*(x+0.5))/((((x+0.5)**2)+(y**2))**1.5)))-(((k*(x-0.5))/((((x-0.5)**2)+(y**2))**1.5)))

def field_y(x,y):
    k = 9000000000

    return (((k*y))/((((x+0.5)**2)+(y**2))**1.5))-(((k*y)/((((x-0.5)**2)+(y**2))**1.5)))


x = np.linspace(-2,2,5)
y = np.linspace(-2,2,5)


potentials = np.zeros((len(y),len(x)))

fields = np.zeros((len(y),len(x),2))

for i in range(len(x)):
    for j in range(len(y)):
            potentials[j,i] = potential_calculation(x[i],y[j])
            fields[j,i,0] = field_x(x[i],y[j])
            fields[j,i,1] = field_y(x[i],y[i])

figure = pp.figure(figsize=(9,7),layout='constrained')
spec = figure.add_gridspec(ncols=2, nrows=2)

potential_graph = figure.add_subplot(spec[0,0])
potential_graph = pp.contour(x,y,potentials)
pp.clabel(potential_graph,fontsize = 3)

fields_graph = figure.add_subplot(spec[0,1])
fields_graph = pp.quiver([x,y],fields[:,:,0],fields[:,:,1])
pp.quiverkey(fields_graph,5,5,1)

'''
This should function. For some reason, pp.quiver is interpreting [x,y] as 2 lists, but not using them to form an array.
It is just using the 2 lists as raw values, generating only 10 possible locations instead of 25. I have no clue how
to fix this
'''

pp.show()