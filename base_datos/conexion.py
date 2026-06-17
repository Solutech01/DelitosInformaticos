import pyodbc

def obtener_conexion():
    conexion = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost\\SQLEXPRESS;'
        'DATABASE=DatosColombia;'
        'Trusted_Connection=yes;'
    )

    return conexion