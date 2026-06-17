import requests

from base_datos.conexion import obtener_conexion
from modelos.registro_modelo import insertar_registro


def cargar_datos_api():

    # LIMPIAR TABLA ANTES DE CARGAR NUEVOS DATOS
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM registros")

    conexion.commit()
    conexion.close()
    
    # CONSUMO LA API
    url = "https://www.datos.gov.co/resource/wxd8-ucns.json?$limit=4000"

    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        print("Error al consumir API")
        return

    registros = respuesta.json()

    contador = 0

    for fila in registros[:4000]:

        contador += 1
        print("Insertando registro:", contador)

        criminalidad = str(fila["criminalidad"])
        es_archivo = str(fila["es_archivo"])
        es_preclusion = str(fila["es_preclusion"])
        estado = str(fila["estado"])
        etapa_caso = str(fila["etapa_caso"])
        ley = str(fila["ley"])
        pais_hecho = str(fila["pais_hecho"])

        departamento_hecho = str(fila["departamento_hecho"])
        municipio_hecho = str(fila["municipio_hecho"])

        seccional = str(fila["seccional"])

        anio_hechos = str(fila["a_o_hechos"])

        delito = str(fila["delito"])
        grupo_delito = str(fila["grupo_delito"])

        consumado = str(fila["consumado"])

        try:
            total_procesos = int(fila["total_procesos"])
        except:
            total_procesos = 0

        insertar_registro(
            criminalidad,
            es_archivo,
            es_preclusion,
            estado,
            etapa_caso,
            ley,
            pais_hecho,
            departamento_hecho,
            municipio_hecho,
            seccional,
            anio_hechos,
            delito,
            grupo_delito,
            consumado,
            total_procesos
        )

    print("Datos cargados correctamente")