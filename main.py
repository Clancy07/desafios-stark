import os
from funciones import *
from data_stark import lista_personajes

heroes = duplicar_lista(lista_personajes)

heroes_normalizados = normalizar_diccionarios(heroes)

ejecutando = True

opciones_menu_principal = ['DESAFIO #00 ============================================================================================================',
                           '1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe.',
                           '2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo.',
                           '3. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO).',
                           '4. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO).',
                           '5. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO).',
                           '6. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO).',
                           '7. Calcular e informar cual es el superhéroe más y menos pesado.',
                           '========================================================================================================================',
                           '',
                           'DESAFIO #01 ============================================================================================================',
                           '10. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M.',
                           '11. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F.',
                           '12. Recorrer la lista y determinar cuál es el superhéroe más alto de género M.',
                           '13. Recorrer la lista y determinar cuál es el superhéroe más alto de género F.',
                           '14. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M.',
                           '15. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F.',
                           '16. Recorrer la lista y determinar la altura promedio de los superhéroes de género M.',
                           '17. Recorrer la lista y determinar la altura promedio de los superhéroes de género F.',
                           '18. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F).',
                           '19. Determinar cuántos superhéroes tienen cada tipo de color de ojos.',
                           '20. Determinar cuántos superhéroes tienen cada tipo de color de pelo.',
                           '21. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con "No Tiene").',
                           '22. Listar todos los superhéroes agrupados por color de ojos.',
                           '23. Listar todos los superhéroes agrupados por color de pelo.',
                           '24. Listar todos los superhéroes agrupados por tipo de inteligencia.',
                           '========================================================================================================================',
                           'X. SALIR',
                           '']

elecciones_validas_menu_principal = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                     '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', 'x']


while ejecutando:
    os.system('cls')

    opcion_elegida_menu_principal = crear_menu(opciones_menu_principal)
    while not verificar_opcion(opcion_elegida_menu_principal, elecciones_validas_menu_principal):
        print('\n',
              'Opcion invalida. Reingrese la opcion (1-26 o x para salir): \n')
        opcion_elegida_menu_principal = crear_menu(
            opciones_menu_principal)

    match(opcion_elegida_menu_principal):

        case '1':
            print()
            mostrar_valores_por_claves(heroes_normalizados, ['nombre'], 20)
            print()
            os.system('pause')

        case '2':
            print()
            mostrar_valores_por_claves(heroes_normalizados, [
                                       'nombre', 'altura'], 22)
            print()
            os.system('pause')

        case '3':
            print('Heroe mas alto')

            alturas = mapear_diccionarios(heroes_normalizados, ['altura'])
            heroes_mas_altos = []
            altura_maxima = alturas[0]["altura"]

            for altura in alturas:
                if altura["altura"] > altura_maxima:
                    altura_maxima = altura["altura"]

            for heroe in heroes_normalizados:
                if heroe["altura"] == altura_maxima:
                    heroes_mas_altos.append(heroe)

            mostrar_valores_por_claves(
                heroes_mas_altos, [heroes_mas_altos[0].keys()])

        case '4':
            pass

        case '5':
            pass

        case '6':
            pass

        case '7':
            pass

        case '8':
            pass

        case '9':
            pass

        case '10':
            pass

        case '11':
            pass

        case '12':
            pass

        case '13':
            pass

        case '14':
            pass

        case '15':
            pass

        case '16':
            pass

        case '17':
            pass

        case '18':
            pass

        case '19':
            pass

        case '20':
            pass

        case '21':
            pass

        case '22':
            pass

        case '23':
            pass

        case '24':
            pass

        case 'x':
            if input('¿CONFIRMAR SALIDA? (X):') == 'si':
                ejecutando = False
