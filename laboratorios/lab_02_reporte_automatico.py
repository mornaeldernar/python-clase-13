"""
Laboratorio 2: Generación de reportes automáticos

Objetivo: Crear un reporte automático con análisis y visualizaciones.

Instrucciones:
1. Usa el archivo del ejercicio anterior.
2. Genera un resumen estadístico y al menos un gráfico de producción.
3. Exporta el reporte en dos de los siguientes formatos: Excel, PDF o HTML.
4. El reporte debe incluir el resumen y el gráfico.
"""

# Tu código aquí 

import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

ubicacion = r'../datos/datos_produccion_automatizada_grande_limpio.csv'
df = pd.read_csv(ubicacion, parse_dates=['fecha'])

describe = df.describe()

# serie temporal
df.set_index('fecha', inplace=True)
#produccion por dia en una ventana de un año 
df['produccion_bpd'].resample('D').sum().plot(figsize=(12, 6))
#mostrar solo el año 2025
plt.xlim(pd.Timestamp('2025-01-01'), pd.Timestamp('2025-12-31'))
plt.title('Producción diaria')
plt.xlabel('Fecha')
plt.ylabel('Producción')
plt.grid()
plt.savefig('../datos/produccion_diaria.png')
plt.close()


# Crear PDF e insertar gráfico
pdf_path = '../datos/reporte_produccion_lab_02.pdf'
c = canvas.Canvas(pdf_path, pagesize=letter)
c.drawString(100, 750, 'Reporte de Producción')
c.drawImage('../datos/produccion_diaria.png', 100, 500, width=400, height=200)
#nueva pagina
c.showPage()
c.setPageSize(landscape(letter))
# Agregar resumen estadístico
c.setFont("Helvetica-Bold", 18)
c.drawString(100, 550, 'Resumen Estadístico')
c.setFont("Helvetica", 12)

# Rotar el describe para que las variables sean filas
describe_t = describe.T

# Convertir el DataFrame a lista de listas (para Table)
tabla_data = [ [ "Variable" ] + list(describe_t.columns) ]  # Encabezado
for idx, row in describe_t.iterrows():
    fila = [idx] + [f"{row[col]:.2f}" for col in describe_t.columns]
    tabla_data.append(fila)

# Crear la tabla
tabla = Table(tabla_data, colWidths=70)
tabla.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 8),
]))
c.drawString(100, 750, 'Resumen Estadístico:')

# Dibujar la tabla en el PDF
tabla.wrapOn(c, 50, 600)
tabla.drawOn(c, 50, 200)  # Ajusta la posición vertical según el tamaño de la tabla

# Guardar el PDF
c.save()
print('Reporte PDF generado.') 


# Exportar a HTML
html = f"""
<html>
<head>
<meta charset="utf-8">
<title>Reporte de Producci&oacute;n</title>
</head>
<body>
<h1>Reporte de Producci&oacute;n</h1>
<h2>Resumen estad&iacute;stico</h2>
{describe.to_html()}
<h2>Gráfico de producci&oacute;n</h2>
<img src='produccion_diaria.png' width='600'>
</body>
</html>
"""
with open('../datos/reporte_produccion_lab.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Reporte HTML generado.') 