import pandas as pd

def cargar_datos(ruta_archivo):
    #Carga el archivo Excel y devuelve un DataFrame.
    xls = pd.ExcelFile(ruta_archivo)
    df = pd.read_excel(xls, sheet_name="resultado_laboratorio_suelo")
    return df


def consultar_datos(df, departamento, municipio, cultivo, limite):
    """Filtra los datos según los parámetros ingresados y calcula la mediana de las variables edáficas."""
    df_filtrado = df[
        (df['Departamento'].str.upper() == departamento.upper()) &
        (df['Municipio'].str.upper() == municipio.upper()) &
        (df['Cultivo'].str.upper() == cultivo.upper())
    ]

    # Seleccionar columnas de interés
    columnas_interes = [
        'Departamento', 'Municipio', 'Cultivo', 'Topografia',
        'pH agua:suelo 2,5:1,0', 'Fósforo (P) Bray II mg/kg', 'Potasio (K) intercambiable cmol(+)/kg'
    ]
    
    # Asegurar que las columnas existen en el DataFrame
    df_filtrado = df_filtrado[columnas_interes]

    # Convertir las columnas numéricas a tipo float, ignorando errores
    columnas_numericas = ['pH agua:suelo 2,5:1,0', 'Fósforo (P) Bray II mg/kg', 'Potasio (K) intercambiable cmol(+)/kg']
    for col in columnas_numericas:
        df_filtrado[col] = pd.to_numeric(df_filtrado[col], errors='coerce')  # Convierte valores no numéricos en NaN

    # Calcular mediana, ignorando NaN
    medianas = df_filtrado[columnas_numericas].median()

    # Agregar medianas al DataFrame
    df_medianas = pd.DataFrame({
        'Departamento': ['Mediana'],
        'Municipio': ['-'],
        'Cultivo': ['-'],
        'Topografia': ['-'],
        'pH agua:suelo 2,5:1,0': [medianas['pH agua:suelo 2,5:1,0']],
        'Fósforo (P) Bray II mg/kg': [medianas['Fósforo (P) Bray II mg/kg']],
        'Potasio (K) intercambiable cmol(+)/kg': [medianas['Potasio (K) intercambiable cmol(+)/kg']]
    })

    df_final = pd.concat([df_filtrado.head(limite), df_medianas], ignore_index=True)
    return df_final
