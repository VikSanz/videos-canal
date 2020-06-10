#### Series de Tiempo simples con Matplotlib y Pandas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#### Leer archivo CSV y convertilo en un Dataframa
df = pd.read_csv('datos_covid2019.csv',index_col=None)
### Imprime el dataframe
df.head()


### Gráfica 1
fig, ax = plt.subplots()
plt.figure(figsize=(10,6))

row = df.drop('nombre',axis=1).iloc[32]
row.plot(lw=2, colormap='jet', marker='.', markersize=10,title='Contagios Confirmados COVID al día 6 de Junio',ax=ax)

### Gráfica 2
fig, ax = plt.subplots()
plt.figure(figsize=(10,6))

row = df.drop('nombre',axis=1).iloc[30]['01-05-2020':'31-05-2020']
row.plot(lw=2, colormap='jet', marker='.', markersize=10, 
         title='Contagios Confirmados Marzo 2020 en CDMX',ax=ax)
row = df.drop('nombre',axis=1).iloc[3]['01-05-2020':'31-05-2020']
row.plot(lw=2, colormap='prism', marker='.', markersize=10, 
         title='Contagios Confirmados Marzo 2020',ax=ax)
row = df.drop('nombre',axis=1).iloc[22]['01-05-2020':'31-05-2020']
row.plot(lw=2, colormap='cool', marker='.', markersize=10, 
         title='Contagios Confirmados Mayo 2020',ax=ax)
ax.legend(["YUCATAN","CAMPECHE","QUINTANA ROO"]);

### Gráfica 3
fig, ax = plt.subplots()

row = df.drop('nombre',axis=1).iloc[30]['01-05-2020':'31-05-2020']
row.plot(lw=2, colormap='jet', marker='.', markersize=10, 
         title='Contagios Confirmados Marzo 2020 en CDMX',ax=ax)
row = df.drop('nombre',axis=1).iloc[3]['01-05-2020':'31-05-2020']
row.plot(lw=2, colormap='prism', marker='.', markersize=10, 
         title='Contagios Confirmados Marzo 2020',ax=ax)
row = df.drop('nombre',axis=1).iloc[22]['01-05-2020':'31-05-2020']
row.plot(lw=2, colormap='cool', marker='.', markersize=10, 
         title='Contagios Confirmados Mayo 2020',ax=ax)
row = df.drop('nombre',axis=1).iloc[6]['01-05-2020':'31-05-2020']
row.plot(lw=2, colormap='hot', marker='.', markersize=10, 
         title='Contagios Confirmados Mayo 2020',ax=ax)
plt.figure(figsize=(10,6))
ax.legend(["YUCATAN","CAMPECHE","QUINTANA ROO","CDMX"]);
plt.savefig("Ejemplo.jpg", bbox_inches='tight')

#### Contagios de Mayo
row = df.drop('nombre',axis=1).iloc[30]['01-05-2020':'31-05-2020']
contagios_yucatan=row.sum()
row = df.drop('nombre',axis=1).iloc[3]['01-05-2020':'31-05-2020']
contagios_campeche=row.sum()
row = df.drop('nombre',axis=1).iloc[22]['01-05-2020':'31-05-2020']
contagios_quintanaroo =row.sum()

#### Contagios de Abril
row = df.drop('nombre',axis=1).iloc[30]['01-04-2020':'30-04-2020']
contagios_yucatan1=row.sum()
row = df.drop('nombre',axis=1).iloc[3]['01-04-2020':'30-04-2020']
contagios_campeche1=row.sum()
row = df.drop('nombre',axis=1).iloc[22]['01-04-2020':'30-04-2020']
contagios_quintanaroo1=row.sum()

#### Contagios de Marzo
row = df.drop('nombre',axis=1).iloc[30]['01-03-2020':'31-03-2020']
contagios_yucatan2=row.sum()
row = df.drop('nombre',axis=1).iloc[3]['01-03-2020':'31-03-2020']
contagios_campeche2=row.sum()
row = df.drop('nombre',axis=1).iloc[22]['01-03-2020':'31-03-2020']
contagios_quintanaroo2=row.sum()

### Gráfica 4
total_mayo = [contagios_yucatan,contagios_campeche,contagios_quintanaroo]
total_abril = [contagios_yucatan1,contagios_campeche1,contagios_quintanaroo1]
total_marzo = [contagios_yucatan2,contagios_campeche2,contagios_quintanaroo2]
N=3
ind = np.arange(N) # the x locations for the groups
width = 0.35
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(ind, total_marzo, width, color='r')
ax.bar(ind, total_abril, width,bottom=total_marzo, color='b')
ax.bar(ind, total_mayo, width,bottom=total_abril, color='g')
ax.set_ylabel('Contagios')
plt.xticks(np.arange(3), ('Yucatan', 'Campeche', 'Quintana Roo'))
ax.legend(labels=['Marzo', 'Abril','Mayo'])
plt.title('')
plt.show()

###Contagios el 6 de Junio
row1 = df.drop('nombre',axis=1).iloc[6]
contagios_cdmx=row1.sum()
row = df.drop('nombre',axis=1).iloc[20]
contagios_puebla=row.sum()
row = df.drop('nombre',axis=1).iloc[14]
contagios_edomex=row.sum()
row = df.drop('nombre',axis=1).iloc[32]
contagios_nacional=row.sum()- row1.sum()

###Últimas gráficas
total=[contagios_cdmx,contagios_puebla,contagios_puebla]
labels=['CDMX','Puebla','EdoMex']
colors = ['gold', 'yellowgreen', 'lightcoral']
plt.pie(total, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Contagios confirmados de COVID al 6 de Junio 2020")
plt.axis('equal')
plt.show()

total=[contagios_cdmx,contagios_nacional]
labels=['CDMX','Nacional']
colors = ['gold', 'yellowgreen']
plt.pie(total, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Contagios confirmados de COVID al 6 de Junio 2020")
plt.axis('equal')
plt.show()
