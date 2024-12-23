from colorama import init, Fore, Style, Back

init()
init(autoreset=True)


def validaciion_get_nombre():
    while True:
        nombre = input("ingrese el nombre: ").strip()
        if not nombre:
            print("no se admite dato nulo.ingrese le nombre: ")
        else:
            return nombre


def validacion_get_descripcion():
    while True:
        descripcion = input("ingrese la descripcion del producto: ").strip()
        return descripcion


def validacion_get_categoria():
    while True:
        categoria = input("ingrese la categoria del producto: ").strip()
        if not categoria:
            print("ingrese la categoria")
        else:
            return categoria


def validacion_get_cantidad():
    while True:
        try:
            cantidad = int(input("ingrese la cantidad del producto: "))
            if not cantidad:
                print("no se admite dato nulo.Ingrese la cantidad: ")
            else:
                return cantidad

        except ValueError:
            print("Tipo de dato no valido. Ingrese la cantidad: ")


def validacion_get_precio():
    while True:
        try:
            precio = float(input("ingrese el precio del producto: "))
            if not precio:
                print("no se admite dato nulo.Ingrese el precio: ")
            else:
                return precio

        except ValueError:
            print("Tipo de dato no valido. Ingrese el precio: ")
