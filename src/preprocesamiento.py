import pandas as pd

def cargar_datos(ruta):
    """Carga un archivo CSV y lo retorna como DataFrame."""
    return pd.read_csv(ruta)

def manejar_valores_nulos(df, metodo='rellenar', valor=None):
    """Maneja valores nulos en el DataFrame."""
    if metodo == 'rellenar':
        return df.fillna(valor)
    elif metodo == 'eliminar':
        return df.dropna()
    else:
        return df

def estandarizar_texto(df, columnas):
    """Convierte a minúsculas y quita espacios extra en las columnas indicadas."""
    for col in columnas:
        df[col] = df[col].astype(str).str.lower().str.strip()
    return df

def limpieza_especifica(df, columnas, simbolo):
    """Elimina un símbolo específico (ej: moneda) en las columnas indicadas."""
    for col in columnas:
        df[col] = df[col].astype(str).str.replace(simbolo, '', regex=False)
    return df
