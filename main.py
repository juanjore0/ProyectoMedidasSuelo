import api.__init__ as api
import ui.__init__ as ui

def main():
    #"""Función principal que ejecuta el flujo del programa."""
    ruta_archivo = "C:/Users/risin/Downloads/Parcial_1/resultado_laboratorio_suelo.xlsx"  # Ruta del archivo de datos
    df = api.cargar_datos(ruta_archivo)
    
    departamento, municipio, cultivo, limite = ui.obtener_datos_usuario()
    
    df_resultado = api.consultar_datos(df, departamento, municipio, cultivo, limite)
    
    ui.mostrar_datos(df_resultado)

if __name__ == "__main__":
    main()