# Proyecto DatosColombia - Delitos Informaticos

## Sistema de Análisis y Gestión de Datos Abiertos de Colombia

### Integrantes

* Jesus Garcia Mendoza
* Keyla Navarro Polo
* Alis Saavedra
* Sebastian Gonzalez

---

## Descripción

Este proyecto consiste en el desarrollo de una aplicación en Python que consume información desde una API pública de Datos Abiertos de Colombia llamada Delitos Informaticos V1, almacena los registros en una base de datos SQL Server y permite realizar operaciones CRUD mediante una interfaz de línea de comandos (CLI).

La aplicación fue desarrollada siguiendo el patrón de arquitectura MVC (Modelo - Vista - Controlador), garantizando una correcta separación de responsabilidades y una mejor organización del código.

---

## Objetivos

* Consumir datos desde una API pública.
* Almacenar la información en una base de datos relacional.
* Implementar operaciones CRUD.
* Aplicar el patrón MVC.
* Realizar análisis de datos.
* Generar visualizaciones gráficas.
* Documentar el proyecto para facilitar su uso y mantenimiento.

------------------------------------------------------------------------------

## Tecnologías Utilizadas

* Python 3.14.5
* Visual Studio Code 
* SQL Server Management Studio 22 
* pyodbc
* requests
* matplotlib
* Patrón MVC
* Git y GitHub

-------------------------------------------------------------------------------

## API Utilizada

Datos Abiertos de Colombia: Delitos informaticos V1

https://www.datos.gov.co/resource/wxd8-ucns.json?$limit=4000

---------------------------------------------------------------------------------

## Patrón MVC Implementado

### Modelo

Contiene las operaciones relacionadas con la base de datos:

* Insertar registros
* Consultar registros
* Actualizar registros
* Eliminar registros
* Búsquedas avanzadas

### Vista

Presenta el menú interactivo al usuario y muestra la información en pantalla.

### Controlador

Gestiona la lógica de negocio y la comunicación entre la vista y el modelo.

-----------------------------------------------------------------------------------

## Funcionalidades

### Cargar datos desde API

Permite obtener los datos desde la API pública e insertarlos en SQL Server.

### Consultar registros

Muestra los registros almacenados en la base de datos.

### Actualizar registros

Permite modificar información existente.

### Eliminar registros

Permite borrar registros de la base de datos.

### Búsqueda avanzada

Permite realizar búsquedas por:

* Departamento
* Municipio
* Año

### Estadísticas

Muestra:

* Total de registros almacenados.
* Top departamentos con mayor cantidad de registros.

### Visualización de datos

Genera gráficas utilizando la librería Matplotlib.

------------------------------------------------------------------------------------

# Instalación y ejecución

## Requisitos previos

Antes de ejecutar el proyecto es necesario tener instalado:

* Python 3.13 o superior.
* SQL Server.
* SQL Server Management Studio (SSMS).
* Git.

## Paso 1. Clonar el repositorio

Abrir una terminal (CMD o PowerShell) y ejecutar:

```bash
git clone https://github.com/Solutech01/DelitosInformaticos.git
```

Esto descargará una copia del proyecto en el equipo local.

## Paso 2. Ingresar a la carpeta del proyecto

Ubicarse dentro de la carpeta descargada:

```bash
cd DatosColombia
```

## Paso 3. Instalar las dependencias

Una vez que el repositorio haya sido clonado y el usuario se encuentre dentro de la carpeta del proyecto, debe abrir una terminal (CMD, PowerShell o la terminal de VS Code) y verificar que la ruta actual corresponda a la carpeta `DatosColombia`.

Por ejemplo:

```text
C:\Users\Usuario\Documents\DatosColombia>
```

Si aún no se encuentra dentro de la carpeta del proyecto, debe ingresar con el siguiente comando:

```bash
cd DatosColombia
```

Luego, ejecutar el siguiente comando para instalar todas las librerías necesarias definidas en el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Durante la instalación se descargarán e instalaran automáticamente las dependencias requeridas por el proyecto. Es importante esperar hasta que el proceso finalice correctamente y verificar que no se presenten mensajes de error en la terminal.

Una vez completada la instalación, el proyecto estará listo para ejecutarse.

## Paso 4. Crear la base de datos

1. Abrir SQL Server Management Studio (SSMS).
2. Conectarse al servidor SQL Server.
3. Crear una nueva base de datos llamada:

```sql
DatosColombia
```

4. Ejecutar los scripts SQL incluidos en la carpeta del proyecto para crear las tablas necesarias.

## Paso 5. Configurar la conexión a la base de datos

Abrir el archivo donde se encuentra la cadena de conexión y verificar:

* Nombre del servidor.
* Nombre de la base de datos.
* Usuario y contraseña (si aplica).

Ejemplo:

```python
server = "NOMBRE_SERVIDOR"
database = "DatosColombia"
```

## Paso 6. Ejecutar el proyecto

Desde la terminal ejecutar:

```bash
python main.py
```

## Paso 7. Utilizar el sistema

Al iniciar la aplicación aparecerá el menú principal.

Las opciones permiten:

* Consultar datos abiertos de Colombia mediante la API.
* Registrar información en la base de datos.
* Buscar registros almacenados.
* Actualizar registros existentes.
* Eliminar registros.
* Generar estadísticas.
* Visualizar gráficas.

Para utilizar cada función, ingresar el número de la opción correspondiente y seguir las instrucciones mostradas en pantalla.


----------------------------------------------------------------------------------------
## ¿Cómo utilizar el sistema?

1. Ejecutar el archivo principal del proyecto mediante el comando:

   python main.py

2. Al iniciar la aplicación se mostrará el menú principal con las diferentes opciones disponibles.

3. Seleccionar la opción deseada ingresando el número correspondiente.

4. Dependiendo de la opción elegida, el sistema permitirá:

   * Consultar datos abiertos de Colombia mediante la API.
   * Registrar información en la base de datos SQL Server.
   * Buscar registros almacenados.
   * Actualizar información existente.
   * Eliminar registros.
   * Generar estadísticas.
   * Visualizar gráficas de los datos obtenidos.

5. Seguir las instrucciones que aparecen en pantalla para ingresar los datos solicitados.

6. Utilizar la opción de salida para finalizar la ejecución del programa.
-------------------------------------------------------------------------------------

## Evidencias



![Menu Inicial](Evidencias/menu_inicial.png)

### Carga de Datos desde la API

![Carga de Datos](Evidencias/Carga_de_datos_desde_la_API.png)

### Consulta de Registros

![Consulta de Registros](Evidencias/Consulta_de_registros.png)

### Actualizacion de Registro

![Actualización de Registro](Evidencias/Actualizacion_de_registro.png)

### Eliminacion de Registro

![Eliminacion de Registro](Evidencias/Eliminar_registro.png)

### Búsqueda Avanzada

![Busqueda Avanzada](Evidencias/Busqueda_avanzada.png)

### Top Departamentos y Gráfica Generada

![Top y Gráfica](Evidencias/Top_y_grafica_generadas.png)

-------------------------------------------------------------------------------------------

## Resultados Obtenidos

La aplicación permitio consumir datos abiertos de Colombia desde la base de datos llamada Delitos Informaticos y almacenarlos en SQL Server, realizar operaciones CRUD, generar estadísticas y visualizar información mediante gráficos, cumpliendo con los requisitos planteados para el proyecto integrador.

----------------------------------------------------------------------------------------------

## Conclusiones

* Aplicamos correctamente el patrón MVC, logrando una adecuada organización y separación de las responsabilidades dentro del proyecto.

* Integramos exitosamente una API pública de Datos Abiertos de Colombia con una base de datos SQL Server para almacenar y gestionar la información obtenida.

* Implementamos las operaciones CRUD (Crear, Consultar, Actualizar y Eliminar), permitiendo administrar los registros de manera eficiente.

* Desarrollamos funcionalidades de análisis y búsqueda avanzada que facilitan la consulta de información según diferentes criterios.

* Generamos visualizaciones gráficas que nos permitieron interpretar y presentar los datos de forma más clara y comprensible.

* Fortalecimos nuestros conocimientos en consumo de APIs, manejo de bases de datos, programación en Python, arquitectura MVC y uso de herramientas de control de versiones como Git y GitHub.

* Cumplimos satisfactoriamente con los objetivos planteados para el proyecto, obteniendo una aplicación funcional, organizada y escalable.


------------------------------------------------------------------------------------------------

## Versión

v1.0 - Entrega Final
