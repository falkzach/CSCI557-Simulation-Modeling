# Lookup the followin functions in the matplotlib documentation
# and use them here;
# plot,xlabel,ylabel,title, legend
# all of these can be imported from pylab
#
# also learn to use numpy's mean function for Ex,Ey, etc.
#
# finally, learn to print latex strings in matplotlib by
# adding an 'r' to the begining of the string and escaping
# with the $ characters, eg xlabel(r"$\nu")

import numpy as np
import matplotlib.pyplot as plt

inFile = open('millikan.txt', 'rb', 0)
xs = []
ys = []

for line in inFile:
    tokens = line.decode().rstrip().split(' ')
    xs.append(float(tokens[0]))
    ys.append(float(tokens[1]))

inFile.close()  # a good idea to do!
xs = np.array(xs)
ys = np.array(ys)

ex = np.mean(xs)
ey = np.mean(ys)
exx = np.mean(xs * xs)
exy = np.mean(xs * ys)

m = (exy - ex * ey) / (exx - ex**2)
c = (exx * ey - ex * exy) / (exx - ex**2)

bf = [m * i + c for i in xs]

plt.plot(xs, ys, 'ko', label = 'Data Points')
plt.plot(xs, bf, 'r', label = 'Best Fit')
plt.title('Millikans Data')
plt.xlabel(r'$\nu$ (Hertz)')
plt.ylabel('V (volts)')
plt.legend()
plt.show()

e = 1.602e-19
phi = c * -1
plancks = (e * (ey + phi)) / ex
# h = e (V + O) / v

google_plancks = 6.62607004e-34
print('Planck\'s constant is about: {0}'.format(plancks))
print('Modern Value is {0}'.format(google_plancks))
