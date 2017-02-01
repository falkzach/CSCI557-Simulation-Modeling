# Plot the full time series:
# don't forget to use title, xlable,ylabel,xlim,and grid
# all can be imported from pylab

import matplotlib.pyplot as plt
import numpy

def running_average(x, r):
    out = []
    total = 0
    range = numpy.arange(-1 * r, r, 1)
    for idx, val in x:
        value = 1 / (2 * r) * numpty.sum(range * val + idx)




# force plot to appear in browser window
filename = './week2/sunspots.txt'
data = numpy.loadtxt(filename)

# it will be convenient to assign the columns of the data files to
# named variables for future use...

x = data[0:1000,0]
y = data[0:1000,1]

yk = [i for i in x ]

plt.plot(x, y, 'k')
plt.show()

