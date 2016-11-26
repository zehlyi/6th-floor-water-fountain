import numpy as np
import matplotlib.pyplot as plt
import datetime
from scipy.optimize import curve_fit

def fit_func_lin(x, a, b):
    return a*x + b

fp = open("water_count.txt", 'r')

x = []
y = []
A = 0
B = 0

for line in fp:
    x.append(int(line.strip().split()[0]))
    y.append(int(line.strip().split()[1]))

    if len(x) > 15:
        xarr = np.array(x[14:])
        yarr = np.array(y[14:])
        A,B = curve_fit(fit_func_lin, xarr, yarr)[0]
        print datetime.datetime.fromtimestamp((100000-B)/A)
    
x_plot = []
y_plot = []
    
for xp in x:
    x_plot.append(xp)
    y_plot.append(fit_func_lin(xp, A, B))

plt.scatter(x, y)
plt.plot(x_plot, y_plot, color="red")
plt.title("Prediction for 100,000: " + str(datetime.datetime.fromtimestamp((100000-B)/A)))
plt.show()
plt.ylim(0, 20000)
fuzz = 1000000
plt.xlim(x[0]-fuzz, x[-1]+fuzz)
plt.savefig('~/public/html/water_graph.png')
