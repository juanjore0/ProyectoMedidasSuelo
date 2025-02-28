def mostrar_datos(df):
    # Muestra los datos en forma de tabla con numeración.
    df.index += 1
    print(df.to_string(index=True))

def obtener_datos_usuario():
    #Solicita al usuario los parámetros de búsqueda.
    departamento = input("Ingrese el nombre del Departamento: ").strip()
    municipio = input("Ingrese el nombre del Municipio: ").strip()
    cultivo = input("Ingrese el tipo de Cultivo: ").strip()
    limite = int(input("Ingrese el número de registros a consultar: "))
    return departamento, municipio, cultivo, limite