import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos limpios
df = pd.read_csv('../datos/datos_produccion_automatizada_limpio.csv', parse_dates=['fecha'])

# Crear gráfico
plt.figure(figsize=(8,4))
plt.plot(df['fecha'], df['produccion_bpd'], marker='o')
plt.title('Producción diaria')
plt.xlabel('Fecha')
plt.ylabel('BPD')
plt.tight_layout()
grafico_path = '../datos/grafico_produccion_html.png'
plt.savefig(grafico_path)
plt.close()

# Exportar resumen y gráfico a HTML
resumen = df.describe().to_html()
html = f"""
<html>
<head><title>Reporte de Producción</title></head>
<body>
<h1>Reporte de Producción</h1>
<h2>Resumen estadístico</h2>
{resumen}
<h2>Gráfico de producción</h2>
<img src='{grafico_path}' width='600'>
</body>
</html>
"""
with open('../datos/reporte_produccion.html', 'w') as f:
    f.write(html)
print('Reporte HTML generado.') 