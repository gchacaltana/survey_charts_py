"""
app.py
"""
import pandas as pd
import matplotlib.pyplot as plt
from utils import map_response, show_label
from settings import (COLOR_YES, COLOR_NO)

# Cargar el archivo CSV
file: str = 'data.csv'

# Creamos dataframe (DF)
df = pd.read_csv(file)

# Aplicamos la función para revisar y convertir cada respuesta del DF
for col in df.columns:
    df[col] = df[col].apply(map_response)

for col in df.columns:
    # Contar las respuestas "si" y "no"
    yes_count = df[col].value_counts().get('si', 0)
    no_count = df[col].value_counts().get('no', 0)

    # Datos para el gráfico
    labels = ['Si', 'No']
    sizes = [yes_count, no_count]
    colors = [COLOR_YES, COLOR_NO]

    # Crear y mostrar gráfico
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors,
            autopct=lambda pct: show_label(pct, sizes), startangle=90)
    plt.axis('equal')
    plt.title(f"{col}", fontsize=14, pad=20, loc='center', wrap=True)
    plt.show()
