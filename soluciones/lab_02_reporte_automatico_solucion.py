import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos limpios
df = pd.read_csv('../datos/datos_produccion_automatizada_limpio.csv', parse_dates=['fecha'])

# Resumen estadístico
describe = df.describe()

df.groupby('fecha')['produccion_bpd'].sum().plot(kind='bar')

# Gráfico de producción
plt.figure(figsize=(8,4))
plt.plot(df['fecha'], df['produccion_bpd'], marker='o')
plt.title('Producción diaria')
plt.xlabel('Fecha')
plt.ylabel('BPD')
plt.tight_layout()
grafico_path = '../datos/grafico_produccion_lab.png'
plt.savefig(grafico_path)
plt.close()

# Exportar a HTML
html = f"""
<html>
<head><title>Reporte de Producción</title></head>
<body>
<h1>Reporte de Producción</h1>
<h2>Resumen estadístico</h2>
{describe.to_html()}
<h2>Gráfico de producción</h2>
<img src='{grafico_path}' width='600'>
</body>
</html>
"""
with open('../datos/reporte_produccion_lab.html', 'w') as f:
    f.write(html)
print('Reporte HTML generado.') 