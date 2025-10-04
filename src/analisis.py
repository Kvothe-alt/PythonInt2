import os
from preprocesamiento import cargar_datos, manejar_valores_nulos, estandarizar_texto, limpieza_especifica

# Construir rutas absolutas
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
usuarios = cargar_datos(os.path.join(base_dir, 'data', 'usuarios.csv'))
prestamos = cargar_datos(os.path.join(base_dir, 'data', 'prestamos.csv'))

# Limpiar datos
usuarios = manejar_valores_nulos(usuarios, 'rellenar', 'desconocido')
prestamos = manejar_valores_nulos(prestamos, 'eliminar')

usuarios = estandarizar_texto(usuarios, ['nombre', 'apellido'])
prestamos = limpieza_especifica(prestamos, ['monto'], '$')

# Merge de tablas
datos = usuarios.merge(prestamos, on='usuario_id')

# Pregunta 1: elemento con mayor cantidad de registros
print("Producto con más registros:")
print(datos['producto'].value_counts().idxmax())

# Pregunta 2: unidades totales por bodega
print("\nUnidades totales por bodega:")
print(datos.groupby('bodega')['unidades'].sum())

# Pregunta 3: envíos retrasados
print("\nEnvíos retrasados:")
print(len(datos[datos['estado'] == 'retrasado']))
