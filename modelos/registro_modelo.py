from base_datos.conexion import obtener_conexion

def insertar_registro(
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
):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO registros
    (
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
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
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

    conexion.commit()
    conexion.close()


def consultar_registros():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT TOP 20 * FROM registros")

    datos = cursor.fetchall()

    conexion.close()

    return datos


def actualizar_registro(id_registro, nuevo_municipio):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    UPDATE registros
    SET municipio_hecho = ?
    WHERE id = ?
    """,
    nuevo_municipio,
    id_registro
    )

    conexion.commit()
    conexion.close()


def eliminar_registro(id_registro):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    DELETE FROM registros
    WHERE id = ?
    """,
    id_registro
    )

    conexion.commit()
    conexion.close()





def buscar_por_departamento(departamento):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT *
    FROM registros
    WHERE departamento_hecho = ?
    """, departamento)

    datos = cursor.fetchall()

    conexion.close()

    return datos


def buscar_por_municipio(municipio):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT *
    FROM registros
    WHERE municipio_hecho = ?
    """, municipio)

    datos = cursor.fetchall()

    conexion.close()

    return datos


def buscar_por_anio(anio):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT *
    FROM registros
    WHERE anio_hechos = ?
    """, anio)

    datos = cursor.fetchall()

    conexion.close()

    return datos

