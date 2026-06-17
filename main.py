from vistas.menu import mostrar_menu

from controladores.registro_controlador import cargar_datos_api

from modelos.registro_modelo import (
    consultar_registros,
    actualizar_registro,
    eliminar_registro,
    buscar_por_departamento,
    buscar_por_municipio,
    buscar_por_anio,
    
)

from controladores.analisis_controlador import (
    total_registros,
    top_departamentos
)

from graficas.graficas import grafica_departamentos


while True:

    opcion = mostrar_menu()

    if opcion == "1":

        cargar_datos_api()

    elif opcion == "2":

        datos = consultar_registros()

        for fila in datos:
            print(fila)

    elif opcion == "3":

        id_registro = int(input("ID a actualizar: "))
        nuevo_municipio = input("Nuevo municipio: ")

        actualizar_registro(
            id_registro,
            nuevo_municipio
        )

        print("Registro actualizado")

    elif opcion == "4":

        id_registro = int(input("ID a eliminar: "))

        eliminar_registro(id_registro)

        print("Registro eliminado")

    elif opcion == "5":

        total_registros()

    elif opcion == "6":

        top_departamentos()

    elif opcion == "7":

        grafica_departamentos()

    elif opcion == "8":

        print("\n===== BUSQUEDA AVANZADA =====")
        print("1. Departamento")
        print("2. Municipio")
        print("3. Año")

        filtro = input("Seleccione filtro: ")

        if filtro == "1":

            departamento = input(
            "Ingrese departamento: "
            )

            resultados = buscar_por_departamento(
            departamento
            )

        elif filtro == "2":

            municipio = input(
            "Ingrese municipio: "
        )

            resultados = buscar_por_municipio(
            municipio
        )

        elif filtro == "3":

            anio = input(
            "Ingrese año: "
        )

            resultados = buscar_por_anio(
            anio
        )

        else:

            resultados = []

        print("\nRESULTADOS")

        for fila in resultados:
            print(fila)

    elif opcion == "9":

        print("Programa finalizado")
        break

    else:

        print("Opción invalida")