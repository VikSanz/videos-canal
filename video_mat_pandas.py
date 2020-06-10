import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('datos_covid2019.csv',index_col=None)
df.head()

fig, ax = plt.subplots()
plt.figure(figsize=(10,6))

row = df.drop('nombre',axis=1).iloc[22]
row.plot(lw=2, colormap='jet', marker='.', markersize=10,title='Contagios Confirmados COVID al día 6 de Junio',ax=ax)
row = df.drop('nombre',axis=1).iloc[20]
row.plot(lw=2, colormap='cool', marker='.', markersize=10,title='Contagios Confirmados COVID al día 6 de Junio',ax=ax)
