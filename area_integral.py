
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from time import perf_counter, sleep

def cube(x):
 return x**3
 
def cube_integral(x):
 return float((x**4))/4

def chart_area(a,b):
 start = perf_counter()
 print(cube_integral(b))
 v = cube_integral(b) - cube_integral(a)
 end = perf_counter()
 
 total_time = end - start
 print(total_time*1000)
 return float(v)
 
a, b = 0, 8  # integral limits
x = np.linspace(-10, 10)
y = cube(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
#ax.set_ylim(bottom=0)

# Make the shaded region
ix = np.linspace(a, b, 10)
iy = cube(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

ax.text(0.5 * (a + b), 30, f"Área do gráfico {chart_area(a,b)}",
        horizontalalignment='center', fontsize=20)
        
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.set_xticks([a, b])
ax.set_xticklabels(['$a$', '$b$'])

plt.show()
