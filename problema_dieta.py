!pip install pulp

import pandas as np
from pulp import *
from pandas import DataFrame

### Creamos un Data frame con los datos y lo imprimimos
df = DataFrame({'Alimentos':['huevo','frijoles','tortilla','espinacas'],'Proteina':[25.4,4.1,5.7,2.5],'Calcio':[0,442,81,100],'Calorias':[141,71,218,23],'Costo':[6,4,1.5,1]})
df.head()
