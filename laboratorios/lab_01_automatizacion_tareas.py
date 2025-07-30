"""
Laboratorio 1: Automatización de tareas de análisis

Objetivo: Automatizar la limpieza y análisis básico del dataset de producción.

Instrucciones:
1. Carga el archivo '../datos/datos_produccion_automatizada_grande.csv' en un DataFrame.
2. Elimina duplicados y valores nulos.
3. Calcula el total de producción y el promedio de presión.
4. Guarda el DataFrame limpio en '../datos/datos_produccion_automatizada_grande_limpio.csv'.
5. Imprime los resultados del análisis.
"""

# Tu código aquí 

import pandas as pd
import matplotlib.pyplot as plt

ubicacion = r'../datos/'
nombre = ubicacion+'datos_produccion_automatizada_grande.csv'
ubicacion_guardar = ubicacion+'datos_produccion_automatizada_grande_limpio.csv'
df = pd.read_csv(nombre, parse_dates=['fecha'])

df = df.drop_duplicates()
df = df.dropna()

df.to_csv(ubicacion+'datos_produccion_automatizada_grande_limpio.csv', index=False)
total_produccion = df['produccion_bpd'].sum()
promedio_presion = df['presion_psi'].mean()
print(f'Total produccion (bpd): {total_produccion}')
print(f'Promedio de presion (psi): {promedio_presion}')
print(df.describe())

df.groupby('fecha')['produccion_bpd'].sum().plot(kind='bar')
plt.title('Producción diaria')
plt.xlabel('Fecha')
plt.ylabel('Producción (bpd)')
plt.savefig(ubicacion+'produccion_diaria.png')
plt.close() 