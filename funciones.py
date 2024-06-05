import os


def crear_menu(opciones):
    """
    Crea un menu de opciones con las opciones recibidas y devuelve la opcion elegida por el usuario.

    Args:
        opciones (list): Son las opciones del menu

    Returns:
        char: Es la opcion elegida por el usuario
    """
    for opcion in opciones:
        print(f'{opcion}')

    return input('ingrese una opcion: ')


def verificar_opcion(opcion: str, opciones_validas: list) -> True | False:
    """Recibe por parametros una opcion solicitada y una lista con opcione validas y comprueba que la opcion solicitada este dentro de las validas.

    Args:
        opcion (str): Opcion solicitada.
        opciones_validas (list): Lista de opciones validas

    Returns:
        True | False: Si la opcion solicitada es valida: True | Si la opcion solicitada es invalida: False.
    """
    return opcion in opciones_validas


def mapear_diccionarios(diccionarios: list, claves: list) -> list:
    diccionarios_mapeados = []
    diccionario_mapeado = {}
    for diccionario in diccionarios:
        for clave in claves:
            diccionario_mapeado = {clave: diccionario[clave]}
            diccionarios_mapeados.append(diccionario_mapeado)

    return diccionarios_mapeados


def duplicar_lista(lista_original: list) -> list:
    lista_duplicada = []
    for elemento in lista_original:
        lista_duplicada.append(elemento)

    return lista_duplicada


def normalizar_diccionarios(diccionarios):
    diccionarios_normalizados = []

    for diccionario in diccionarios:
        diccionario_normalizado = {}

        for clave in diccionario.keys():

            try:
                diccionario_normalizado[clave] = float(diccionario[clave])

            except:
                diccionario_normalizado[clave] = diccionario[clave]

        diccionarios_normalizados.append(diccionario_normalizado)

    return diccionarios_normalizados


def mostrar_valores_por_claves(diccionarios, claves, espaciado: int = 12):
    encabezados = []
    for clave in claves:
        encabezados.append(clave)

    for encabezado in encabezados:
        print(f'{encabezado.capitalize():^{espaciado}}', end='')

    print()
    print('=' * (len(encabezados) * espaciado))

    for diccionario in diccionarios:
        for clave in claves:
            print(f'{diccionario[clave]:^{espaciado}}', end='')

        print()
