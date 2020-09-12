# Regresión Lineal: Mínimos Cuadrados
In [1]:

import numpy as np
from numpy.linalg import inv 
%matplotlib inline
import matplotlib.pyplot as plt
In [2]:

### El arreglo guarda los días, como buenos computólogos empezamos a contar desde el día cero.
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
### El arreglo subs el número de suscriptores correspondientes al día x
subs=[432,439,442,444,446,447,449,451,453,458,463,466,468,470,472,477,479,491,516,516,521,524,526,533,541,548,555,560,563,564]
In [3]:

### Graficamos
plt.scatter(x, subs); plt.xlabel('días'); plt.ylabel('Cantidad de suscriptores');

In [4]:

### Creamos el modelo
X = np.array([np.ones(len(x)), x]).T
a = inv(X.T @ X) @ X.T @ subs    ### Fórmula para minimizar los cuadrados
In [5]:

### Hacemos la "predicción"
x_predict = np.linspace(0, 29, num=100)
subs_predict = a[0] + a[1] * x_predict ### Recta 
In [6]:

a[1]
Out[6]:
4.838709677419358
In [7]:

### Graficamos
plt.scatter(x, subs)
plt.xlabel('x'); plt.ylabel('Suscriptores'); plt.plot(x_predict, subs_predict, 'c');

In [8]:

### Fórmula de la recta, donde a_1 es la pendiente, 
### basta variar el valor de x para conocer el número de suscriptores al día x
y = a[1]*(59)+a[0]
​
​
### Cortamos el float
y1 = f"{y:.1f}"
​
###Imprimimos
print('En un mes tendré:'+ str(y1) + 'suscriptores.')
En un mes tendré:705.8suscriptores.
In [11]:

### Fórmula de la recta, donde a_1 es la pendiente, 
### basta variar el valor de x para conocer el número de suscriptores al día x
y = a[1]*(365)+a[0]
​
​
### Cortamos el float
y2 = f"{y:.1f}"
​
###Imprimimos
print('En tres meses tendré:'+ str(y2) + 'suscriptores.')
En tres meses tendré:2186.4suscriptores.
