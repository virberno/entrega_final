import sqlite3
from funciones_database import *
from funciones_validacion import *
from colorama import init, Fore, Style, Back

init()
init(autoreset=True)


def menu_registrar_producto():
    print(
        Back.CYAN + Fore.YELLOW + Style.BRIGHT + "Ingrese los datos de los productos: "
    )
    nombre = validaciion_get_nombre()
    descripcion = validacion_get_descripcion()
    categoria = validacion_get_categoria()
    cantidad = validacion_get_cantidad()
    precio = validacion_get_precio()

    print("Producto ingresado")

    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }
    print(producto)
    db_insertar_productos(producto)

    print(Back.CYAN + Fore.YELLOW + Style.BRIGHT + "registro insertado correctamente")


def menu_mostrar_productos():
    lista_productos = db_mostrar_productos()

    if not lista_productos:
        print(FORE.RED + "no hay productos que mostrar")
    else:
        for producto in lista_productos:
            print(
                producto[0],
                producto[1],
                producto[2],
                producto[3],
                producto[4],
                producto[5],
            )


def menu_buscar_id():
    id = int(
        input(
            Back.CYAN
            + Fore.YELLOW
            + Style.BRIGHT
            + "ingrese el id del producto que quiere buscar"
        )
    )
    producto = db_get_productos_by_id(id)
    if not producto:
        print("ningun producto encontrado")
    else:
        print(producto)


def menu_actualizar_productos():
    id = int(
        input(Back.CYAN + Fore.YELLOW + Style.BRIGHT + "ingrese el id del producto")
    )
    producto = db_get_productos_by_id(id)
    if producto:
        print(producto)
        nueva_cantidad = int(input("ingrese actualizacion"))
        db_actualizar_producto(id, nueva_cantidad)

    else:
        print(Fore.GREEN + "no existe el id")


def menu_eliminar_producto():
    id = int(
        input(Back.CYAN + Fore.YELLOW + Style.BRIGHT + "ingrese el id del producto")
    )
    producto = db_get_productos_by_id(id)
    if producto:
        print(producto)
        db_eliminar_producto(id)
        print(Fore.LIGHTRED_EX + "producto eliminado")
    else:
        print("no existe el producto")


def menu_reporte_bajo():
    minimo_stock = int(
        input(Back.CYAN + Fore.YELLOW + Style.BRIGHT + "ingrese el minimo stock")
    )
    lista_productos = db_get_productos_by_condicion(minimo_stock)
    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print(
            Fore.LIGHTYELLOW_EX
            + "no hay productos con sstock menor a "
            + str(minimo_stock)
        )


def menu_mostrar_menu():

    print("1-Agregar producto")
    print("2-Mostrar Stock")
    print("3-Actualizar cantidad de producto")
    print("4-Eliminar producto")
    print("5-Reporte de bajo stock")
    print("6-Salir")

    opcion = input(Fore.GREEN+"Ingrese una opcion")
    return opcion
