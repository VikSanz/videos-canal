!pip install pulp

import pandas as np
from pulp import *
from pandas import DataFrame

### Creamos un Data frame con los datos y lo imprimimos
df = DataFrame({'Alimentos':['huevo','frijoles','tortilla','espinacas'],'Proteina':[25.4,4.1,5.7,2.5],'Calcio':[0,442,81,100],'Calorias':[141,71,218,23],'Costo':[6,4,1.5,1]})
df.head()

#### Creamos un problema LP con LpProblem, usamos LpMinimize pues queremos minimizar la función con los costos
problema = LpProblem("ProblemaDieta",LpMinimize)

### Creamos una lista con los alimentos
alimentos = list(df['Alimentos'])

### Creamos un diccionario con los costos
costos = dict(zip(alimentos,df['Costo']))

### Creamos un diccionario con las calorias
calorias = dict(zip(alimentos,df['Calorias']))

### Creamos un diccionario con los valores de calcio
calcio = dict(zip(alimentos,df['Calcio']))

### Creamos un diccionario con los valores de proteína
proteina = dict(zip(alimentos,df['Proteina']))

### Ponemos 0 ya que queremos valores >= 0 y 'Continuous' para regresernos valores reales o bien 'Integer' para valores enteros
alimentos_vars = LpVariable.dicts("Alimentos",alimentos,0,cat='Integer')

### Función objetivo
problema += lpSum([costos[i]*alimentos_vars[i] for i in alimentos]), "Costo total de la dieta"

### Establecemos las restricciones de Calorías
problema += lpSum([calorias[f] * alimentos_vars[f] for f in alimentos]) >= 2000.0, "MínimoCalorías"
problema += lpSum([calorias[f] * alimentos_vars[f] for f in alimentos]) <= 2200.0, "MáximoCalorías"

### Restricciones de proteínas
problema += lpSum([proteina[f] * alimentos_vars[f] for f in alimentos]) >= 158.4, "MínimoProteinas"
problema += lpSum([proteina[f] * alimentos_vars[f] for f in alimentos]) <= 258.4, "MáximoProteinas"

### Restricciones de Calcio
problema += lpSum([calcio[f] * alimentos_vars[f] for f in alimentos]) >= 1000.0, "MinimoCalcio"
problema += lpSum([calcio[f] * alimentos_vars[f] for f in alimentos]) <= 2500.0, "MaximoCalcio"

### Escribimos el problema en un archivo .lp
problema.writeLP("SimpleDietProblem.lp")

### PuLP resuelve el problema con las restricciones dadas y la función objetivo.
problema.solve()

### Veamos si existe una solución y si ésta es óptima
print("Status:", LpStatus[problema.status])

### Imprimimos la dieta
print("La dieta balanceada óptima(menor costo), donde cada unidad equivale a 100g, consiste de\n"+"-"*110)
for v in problema.variables():
    if v.varValue>0:
        print(v.name, "=", v.varValue)
        
### Imprimimos el costo
print("El costo diario de la dieta es: ${}".format(round(value(problema.objective),2)))
