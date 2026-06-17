import matplotlib.pyplot as plt

from base_datos.conexion import obtener_conexion


def grafica_departamentos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT TOP 10
    departamento_hecho,
    SUM(total_procesos)
    FROM registros
    GROUP BY departamento_hecho
    ORDER BY SUM(total_procesos) DESC
    """)

    datos = cursor.fetchall()

    conexion.close()

    departamentos = []
    procesos = []

    for fila in datos:
        departamentos.append(fila[0])
        procesos.append(fila[1])

    plt.figure(figsize=(10,6))

    plt.bar(departamentos, procesos)

    plt.title("Top 10 departamentos por procesos")

    plt.xlabel("Departamento")

    plt.ylabel("Procesos")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()