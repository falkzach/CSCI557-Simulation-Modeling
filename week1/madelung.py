from __future__ import division, print_function # Get in the habit of writing this
# Madelung constant approximation
import math # You'll need this

total = 0.0
L = 20
a = 1
for i in range(-L, L):
    for j in range(-L, L):
        for k in range(-L, L):
            if (i == 0 and j== 0 and k == 0): continue
            if (i + j + k)%2 == 0:
                epsilon = 1
            else:
                epsilon = -1
            total += 1/(4 * math.pi * epsilon * a * math.sqrt(i**2 + j**2 + k**2))
print(total * (4.0 * math.pi * a), " is our approximation of M")
