import pandas as pd

df = pd.read_csv('../datos/datos_produccion_automatizada_grande.csv', parse_dates=['fecha'])
df = df.drop_duplicates()
df = df.dropna()
total_produccion = df['produccion_bpd'].sum()
promedio_presion = df['presion_psi'].mean()
df.to_csv('../datos/datos_produccion_automatizada_limpio.csv', index=False)
print(f'Total producción (bpd): {total_produccion}')
print(f'Presión promedio (psi): {promedio_presion:.2f}') 