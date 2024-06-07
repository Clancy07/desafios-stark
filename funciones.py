import os


def crear_menu(opciones: list) -> str:
    """
    Crea un menu de opciones con las opciones recibidas y devuelve la opcion elegida por el usuario.

    Args:
        opciones (list): Son las opciones del menu

    Returns:
        str: Es la opcion elegida por el usuario
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
    """Mapea una lista de diccionarios acorde a las claves recibidas

    Args:
        diccionarios (list): Lista de diccionarios a mapear
        claves (list): Lista de las claves segun las cuales se mapearan los diccionarios

    Returns:
        list: Diccionarios mapeados acorde a las claves recividas
    """
    diccionarios_mapeados = []
    diccionario_mapeado = {}
    for diccionario in diccionarios:
        for clave in claves:
            diccionario_mapeado = {clave: diccionario[clave]}
            diccionarios_mapeados.append(diccionario_mapeado)

    return diccionarios_mapeados


def duplicar_lista(lista_original: list) -> list:
    """Recive una lista y crea una copia

    Args:
        lista_original (list): Lista a duplicar

    Returns:
        list: Copia de la lista original
    """
    lista_duplicada = []
    for elemento in lista_original:
        lista_duplicada.append(elemento)

    return lista_duplicada


def normalizar_diccionarios(diccionarios: list) -> list:
    """Normaliza los valores de una lista de diccionarios, intentando convertir los valores a números flotantes cuando sea posible.

    Args:
        diccionarios (list): lista de diccionarios cuyos valores se intentaran convertir a numeros flotantes

    Returns:
        list: diccionarios con los valores convertidos a flotantes en los casos en los que haya sido posible
    """
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


def mostrar_valores_por_claves(diccionarios: list, claves: list, espaciado: int = 12) -> None:
    """Muestra en formato de tabla los valores asociados a un conjunto de claves recividas para una lista de diccionarios.

    Args:
        diccionarios (list): Lista de diccionarios que contienen los datos a mostrar.
        claves (list): Lista de claves cuyos valores asociados en los diccionarios se mostraran
        espaciado (int, optional): Cantidad de esapacios que se utilizarán para formatear las columnas de la tabla. Defaults to 12.
    """
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


def calcular_maximo_en_clave_diccionarios(diccionarios: list, clave: str) -> int:
    """Calcula el maximo valor entre los valores asociados a una clave dentro de una lista de diccionarios.

    Args:
        diccionarios (list): Lista de diccionarios donde se buscara el maximo valor.
        clave (str): Clave en la que se buscará el maximo valor los diccionarios.

    Returns:
        int: El maximo valor encontrado entre los valores asociados a la clave recivida.
    """
    maximo = diccionarios[0][clave]

    for diccionario in diccionarios:
        if diccionario[clave] > maximo:
            maximo = diccionario[clave]

    return maximo


def calcular_minimo_en_clave_diccionarios(diccionarios: list, clave: str) -> int:
    """Calcula el minimo valor entre los valores asociados a una clave dentro de una lista de diccionarios.

    Args:
        diccionarios (list): Lista de diccionarios donde se buscara el minimo valor.
        clave (str): Clave en la que se buscará el minimo valor los diccionarios.

    Returns:
        int: El minimo valor encontrado entre los valores asociados a la clave recivida.
    """
    minimo = diccionarios[0][clave]

    for diccionario in diccionarios:
        if diccionario[clave] < minimo:
            minimo = diccionario[clave]

    return minimo


def calcular_promedio_en_clave_diccionarios(diccionarios: list, clave: str) -> float:
    """Calcula el promedio de los valores asociados a una clave recivida dentro de una lista de diccionarios.

    Args:
        diccionarios (list): Lista de diccionarios donde se buscaran los valores para calcular el promedio.
        clave (str): Clave entre cuyos valores asociadosen se buscaran los valores para calcular el promedio en cada diccionario.

    Returns:
        float: El promedio de los valores calculado entre los valores asociados a la clave recivida de los diccionarios.
    """
    cantidad_diccionarios = len(diccionarios)
    acumulador = 0
    for diccionario in diccionarios:
        acumulador += diccionario[clave]

    promedio = acumulador / cantidad_diccionarios
    return promedio


def filtrar_lista_diccionarios(lista: list, clave: str, valor_buscado: any) -> list:
    """Recorre una lista de diccionarios buscando coincidencias con el valor recivido en una clave especifica

    Args:
        lista (list): lista de diccionarios en la que se buscara el valor recivido
        clave (str): Clave entre cuyos valores asociados se buscara el valor recivido
        valor_buscado (any): Valor que se buscara en la lista de diccionarios

    Returns:
        list: Lista filtrada que solo contiene los diccionarios que contienen coincidencias con el valor buscado
    """
    lista_filtrada = []
    for elemento in lista:
        if elemento[clave] == valor_buscado:
            lista_filtrada.append(elemento)

    return lista_filtrada


def determinar_colores_de_ojo(heroes_normalizados: list) -> None:
    """Ordena la lista de heroes por color de ojos y los muestra

    Args:
        heroes_normalizados (list): Lista de heroes que se ordenara y mostrara segun el color de ojos
    """

    contador_colores_de_ojo = {}
    contador_colores_de_ojo["Yellow"] = 0
    contador_colores_de_ojo["Silver"] = 0
    contador_colores_de_ojo["Brown"] = 0
    contador_colores_de_ojo["Yellow (without irises)"] = 0
    contador_colores_de_ojo["Blue"] = 0
    contador_colores_de_ojo["Green"] = 0
    contador_colores_de_ojo["Red"] = 0
    contador_colores_de_ojo["Hazel"] = 0

    for heroe in heroes_normalizados:
        match(heroe["color_ojos"]):

            case 'Yellow':
                contador_colores_de_ojo["Yellow"] += 1

            case 'Silver':
                contador_colores_de_ojo["Silver"] += 1

            case 'Brown':
                contador_colores_de_ojo["Brown"] += 1

            case 'Yellow (without irises)':
                contador_colores_de_ojo["Yellow (without irises)"] += 1

            case 'Blue':
                contador_colores_de_ojo["Blue"] += 1

            case 'Green':
                contador_colores_de_ojo["Green"] += 1

            case 'Red':
                contador_colores_de_ojo["Red"] += 1

            case 'Hazel':
                contador_colores_de_ojo["Hazel"] += 1

    for clave, valor in contador_colores_de_ojo.items():
        print(f'{clave}: {valor}')


def determinar_colores_de_pelo(heroes_normalizados):
    """Ordena la lista de heroes por color de pelo y los muestra

    Args:
        heroes_normalizados (list): Lista de heroes que se ordenara y mostrara segun el color de pelo
    """

    contador_colores_de_pelo = {}
    contador_colores_de_pelo["Black"] = 0
    contador_colores_de_pelo["Auburn"] = 0
    contador_colores_de_pelo["Brown"] = 0
    contador_colores_de_pelo["White"] = 0
    contador_colores_de_pelo["Green"] = 0
    contador_colores_de_pelo["Brown / White"] = 0
    contador_colores_de_pelo["Red / Orange"] = 0
    contador_colores_de_pelo["Yellow"] = 0
    contador_colores_de_pelo["No Hair"] = 0
    contador_colores_de_pelo["Red"] = 0
    contador_colores_de_pelo["Blond"] = 0

    for heroe in heroes_normalizados:
        match(heroe["color_pelo"]):

            case 'Black':
                contador_colores_de_pelo["Black"] += 1

            case 'Auburn':
                contador_colores_de_pelo["Auburn"] += 1

            case 'Brown':
                contador_colores_de_pelo["Brown"] += 1

            case 'White':
                contador_colores_de_pelo["White"] += 1

            case 'Green':
                contador_colores_de_pelo["Green"] += 1

            case 'Brown / White':
                contador_colores_de_pelo["Brown / White"] += 1

            case 'Red / Orange':
                contador_colores_de_pelo["Red / Orange"] += 1

            case 'Yellow':
                contador_colores_de_pelo["Yellow"] += 1

            case 'No Hair':
                contador_colores_de_pelo["No Hair"] += 1

            case 'Red':
                contador_colores_de_pelo["Red"] += 1

            case 'Blond':
                contador_colores_de_pelo["Blond"] += 1

    for clave, valor in contador_colores_de_pelo.items():
        print(f'{clave}: {valor}')


def determinar_tipos_de_inteligencia(heroes_normalizados):
    """Ordena la lista de heroes por tipo de inteligencia y los muestra

    Args:
        heroes_normalizados (list): Lista de heroes que se ordenara y mostrara segun el tipo de inteligencia
    """
    tipos_de_inteligencia = []

    for heroe in heroes_normalizados:
        tipos_de_inteligencia.append(heroe["inteligencia"])

    tipos_de_inteligencia = list(set(tipos_de_inteligencia))

    contador_colores_de_pelo = {}
    contador_colores_de_pelo["No tiene"] = 0
    contador_colores_de_pelo["average"] = 0
    contador_colores_de_pelo["good"] = 0
    contador_colores_de_pelo["high"] = 0

    for heroe in heroes_normalizados:
        match(heroe["inteligencia"]):

            case '':
                contador_colores_de_pelo["No tiene"] += 1

            case 'average':
                contador_colores_de_pelo["average"] += 1

            case 'good':
                contador_colores_de_pelo["good"] += 1

            case 'high':
                contador_colores_de_pelo["high"] += 1

    for clave, valor in contador_colores_de_pelo.items():
        print(f'{clave}: {valor}')


def ordenar_diccionarios(criterio, diccionarios: list) -> None:
    """Ordena una lista de diccionarios segun el criterio recivido

    Args:
        criterio (_type_): Criterio segun el cual se ordenara la lista
        diccionarios (list): Lista de diccionarios a ordenar
    """
    tam = len(diccionarios)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if criterio(diccionarios[i], diccionarios[j]):
                swap_lista(diccionarios, i, j)


def swap_lista(lista: list, i: int, j: int) -> None:
    """Swapea dos elementos de la lista recivida

    Args:
        lista (list): Lista cuyos elementos se swapearan
        i (int): indice del primer elemento del swap
        j (int): Indice del segundo elemento del swap
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
