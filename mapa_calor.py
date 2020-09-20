### Estos son los comandos básicos que necesitas para graficar un mapa de calor con seaborn, puedes modificarlos de acuerdo al video:
### https://www.youtube.com/watch?v=ii1xcd3lZ_4&t=6s

### Instalamos Seaborn
pip install seaborn

###Importamos nuestras bibliotecas
import pandas as pd
import seaborns as sns
import matplotlib.pyplot as plt

from pylab import savefig

### Convertimos el archivo .csv en un Dataframe(guarda tu archivo en la misma carpeta para que funcione)
df = pd.read_csv('nombre de tu archivo',index_col=0)
df.head()
### Para quitar una columna usa la función df.drop

###Mapa de calor
plt.figure(figsize =(27,5))
mapa = sns.heatmap(df,cmap='BuPu') ### Cambia el color del cmap a tu gusto
figure = mapa.get_figure()
figure.savefig('nombre con el que quieres guardar tu archivo',dpi=400)

### Si tienes alguna duda esc´ribeme.(;
