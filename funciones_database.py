import sqlite3


def crear_tabla_productos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXIST Productos(
                   nombre TEXT NOT NULL,
                    descripcion TEXT,
                   categoria TEXT NOT NULL,
                   cantidad INTEGER NOT NULL,
                   precio REAL NOT NULL,
                   id INTEGER PRIMARY KEY AUTOINCREMENT
                   )"""
    )

    conexion.commit()
    conexion.close()


def db_insertar_productos(producto):
    try:

        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre,descripcion,categoria,cantidad,precio)VALUES (?,?,?,?,?)",
            (
                producto["nombre"],
                producto["descripcion"],
                producto["categoria"],
                producto["cantidad"],
                producto["precio"],
            ),
        )

        conexion.commit()
        state = True
    except Exception as error:
        print(f"error:{error}")
        conexion.close()
        state: False
    finally:
        conexion.close()
        return state


def db_mostrar_productos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    lista_productos = cursor.fetchall()
    cursor.close()
    return lista_productos


def db_get_productos_by_id(id):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE id = ? "
    datos = (id,)
    cursor.execute(query, datos)
    lista_producto = cursor.fetchone()
    conexion.close()
    return lista_producto


def db_actualizar_producto(id, nueva_cantidad):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = "UPDATE productos SET cantidad = ? WHERE id = ? "
    datos = (nueva_cantidad, id)
    cursor.execute(query, datos)
    conexion.commit()
    conexion.close()


def db_eliminar_producto(id):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = "DELETE FROM productos  WHERE id = ? "
    datos = (id,)
    cursor.execute(query, datos)
    conexion.commit()
    conexion.close()


def db_get_productos_by_condicion(minimo_stock):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE cantidad < ? "
    datos = (minimo_stock,)
    cursor.execute(query, datos)
    lista_productos = cursor.fetchall()
    conexion.close()
    return lista_productos
