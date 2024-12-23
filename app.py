import sqlite3

1
from colorama import init, Fore, Style, Back
from funciones_database import (
    crear_tabla_productos,
)
from funciones_menu import *

opcion = 0


def main():
    init()
    init(autoreset=True)
    while True:

        opcion = menu_mostrar_menu()
        print(Fore.RED + "usted seleccionola opcion:", opcion)

        if opcion == "1":
            menu_registrar_producto()
        elif opcion == "2":
            menu_mostrar_productos()

        elif opcion == "3":
            menu_actualizar_productos()
        elif opcion == "4":
            menu_eliminar_producto()
        elif opcion == "5":
            menu_reporte_bajo()
        elif opcion == "6":
            menu_buscar_id()
        elif opcion == "7":
            print("adios")
            break
        else:
            print("opcion no valida")


main()
