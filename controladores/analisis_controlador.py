from base_datos.conexion import obtener_conexion


def total_registros():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT COUNT(*) FROM registros
    """)

    total = cursor.fetchone()[0]

    conexion.close()

    print("\nTotal de registros:", total)


def top_departamentos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT TOP 10 departamento_hecho,
    SUM(total_procesos)
    FROM registros
    GROUP BY departamento_hecho
    ORDER BY SUM(total_procesos) DESC
    """)

    datos = cursor.fetchall()

    conexion.close()

    print("\nTOP 10 DEPARTAMENTOS")

    for fila in datos:
        print(fila[0], "-", fila[1])