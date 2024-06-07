import os
from funciones import *
from data_stark import lista_personajes

heroes = duplicar_lista(lista_personajes)

heroes_normalizados = normalizar_diccionarios(heroes)

ejecutando = True

flag_3 = False
flag_4 = False

flag_10 = False
flag_11 = False
flag_12 = False
flag_13 = False

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
                           '8. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M.',
                           '9. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F.',
                           '10. Recorrer la lista y determinar cuál es el superhéroe más alto de género M.',
                           '11. Recorrer la lista y determinar cuál es el superhéroe más alto de género F.',
                           '12. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M.',
                           '13. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F.',
                           '14. Recorrer la lista y determinar la altura promedio de los superhéroes de género M.',
                           '15. Recorrer la lista y determinar la altura promedio de los superhéroes de género F.',
                           '16. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems 10 al 13).',
                           '17. Determinar cuántos superhéroes tienen cada tipo de color de ojos.',
                           '18. Determinar cuántos superhéroes tienen cada tipo de color de pelo.',
                           '19. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con "No Tiene").',
                           '20. Listar todos los superhéroes agrupados por color de ojos.',
                           '21. Listar todos los superhéroes agrupados por color de pelo.',
                           '22. Listar todos los superhéroes agrupados por tipo de inteligencia.',
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
            flag_3 = True

            print('Heroes mas altos')

            alturas = mapear_diccionarios(heroes_normalizados, ['altura'])
            heroes_mas_altos = []
            altura_maxima = alturas[0]["altura"]

            for altura in alturas:
                if altura["altura"] > altura_maxima:
                    altura_maxima = altura["altura"]

            for heroe in heroes_normalizados:
                if heroe["altura"] == altura_maxima:
                    heroes_mas_altos.append(heroe)

            for heroe in heroes_mas_altos:
                print(f'Nombre: {heroe["nombre"]}. Altura: {heroe["altura"]}')

            os.system('pause')

        case '4':
            flag_4 = True
            print('Heroes mas bajos')

            alturas = mapear_diccionarios(heroes_normalizados, ['altura'])
            heroes_mas_bajos = []
            altura_minima = alturas[0]["altura"]

            for altura in alturas:
                if altura["altura"] < altura_minima:
                    altura_minima = altura["altura"]

            for heroe in heroes_normalizados:
                if heroe["altura"] == altura_minima:
                    heroes_mas_bajos.append(heroe)

            for heroe in heroes_mas_bajos:
                print(f'Nombre: {heroe["nombre"]}. Altura: {heroe["altura"]}')

            os.system('pause')

        case '5':
            promedio_alturas = calcular_promedio_en_clave_diccionarios(
                heroes_normalizados, 'altura')

            print(
                f'\nEl promedio de alturas de los superheroes es de: {promedio_alturas:.2f}\n')
            os.system('pause')

        case '6':
            if flag_3 and flag_4:
                for heroe in heroes_mas_altos:
                    print(
                        f'Nombre: {heroe["nombre"]}. Altura: {heroe["altura"]}')

                for heroe in heroes_mas_bajos:
                    print(
                        f'Nombre: {heroe["nombre"]}. Altura: {heroe["altura"]}')

                os.system('pause')
            else:
                print(
                    'Debe calcular primero las alturas maximas y minimas de los heroes (puntos 3 y 4)')
                os.system('pause')

        case '7':
            heroe_mas_pesado = calcular_maximo_en_clave_diccionarios(
                heroes_normalizados, 'peso')
            heroe_menos_pesado = calcular_minimo_en_clave_diccionarios(
                heroes_normalizados, 'peso')

            heroes_mas_pesados = filtrar_lista_diccionarios(
                heroes_normalizados, 'peso', heroe_mas_pesado)
            heroes_menos_pesados = filtrar_lista_diccionarios(
                heroes_normalizados, 'peso', heroe_menos_pesado)

            print('\nHEROE MAS PESADO')
            mostrar_valores_por_claves(
                heroes_mas_pesados, ['nombre', 'identidad', 'empresa', 'altura', 'peso', 'genero', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia'], 20)
            print('\n\n')
            print('HEROE MENOS PESADO')
            mostrar_valores_por_claves(
                heroes_menos_pesados, ['nombre', 'identidad', 'empresa', 'altura', 'peso', 'genero', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia'], 20)

            os.system('pause')

        case '8':
            heoroes_genero_m = filtrar_lista_diccionarios(
                heroes_normalizados, 'genero', 'M')

            mostrar_valores_por_claves(heoroes_genero_m, ['nombre'], 20)

            os.system('pause')

        case '9':
            heoroes_genero_f = filtrar_lista_diccionarios(
                heroes_normalizados, 'genero', 'F')

            mostrar_valores_por_claves(heoroes_genero_f, ['nombre'], 20)

            os.system('pause')

        case '10':
            flag_10 = True
            heoroes_genero_m = filtrar_lista_diccionarios(
                heroes_normalizados, 'genero', 'M')

            altura_maxima_m = calcular_maximo_en_clave_diccionarios(
                heoroes_genero_m, 'altura')

            heroes_genero_m_mas_altos = filtrar_lista_diccionarios(
                heoroes_genero_m, 'altura', altura_maxima_m)

            print('\nHEROE MAS ALTO')
            mostrar_valores_por_claves(heroes_genero_m_mas_altos, [
                                       'nombre', 'identidad', 'empresa', 'altura', 'peso', 'genero', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia'], 20)

            os.system('pause')

        case '11':
            flag_11 = True
            heoroes_genero_f = filtrar_lista_diccionarios(
                heroes_normalizados, 'genero', 'F')

            altura_maxima_f = calcular_maximo_en_clave_diccionarios(
                heoroes_genero_f, 'altura')

            heroes_genero_f_mas_altos = filtrar_lista_diccionarios(
                heoroes_genero_f, 'altura', altura_maxima_f)

            print('\nHEROINA MAS ALTA')
            mostrar_valores_por_claves(heroes_genero_f_mas_altos, [
                                       'nombre', 'identidad', 'empresa', 'altura', 'peso', 'genero', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia'], 23)

            os.system('pause')

        case '12':
            flag_12 = True
            heoroes_genero_m = filtrar_lista_diccionarios(
                heroes_normalizados, 'genero', 'M')

            altura_minima_m = calcular_minimo_en_clave_diccionarios(
                heoroes_genero_m, 'altura')

            heroes_genero_m_mas_bajos = filtrar_lista_diccionarios(
                heoroes_genero_m, 'altura', altura_minima_m)

            print('\nHEROE MAS BAJO')
            mostrar_valores_por_claves(heroes_genero_m_mas_bajos, [
                                       'nombre', 'identidad', 'empresa', 'altura', 'peso', 'genero', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia'], 20)

            os.system('pause')

        case '13':
            flag_13 = True
            heoroes_genero_f = filtrar_lista_diccionarios(
                heroes_normalizados, 'genero', 'F')

            altura_minima_f = calcular_minimo_en_clave_diccionarios(
                heoroes_genero_f, 'altura')

            heroes_genero_f_mas_bajos = filtrar_lista_diccionarios(
                heoroes_genero_f, 'altura', altura_minima_f)

            print('\nHEROINA MAS BAJA')
            mostrar_valores_por_claves(heroes_genero_f_mas_bajos, [
                                       'nombre', 'identidad', 'empresa', 'altura', 'peso', 'genero', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia'], 20)

            os.system('pause')

        case '14':
            heoroes_genero_m = filtrar_lista_diccionarios(
                heroes_normalizados, 'genero', 'M')

            altura_promedio_m = calcular_promedio_en_clave_diccionarios(
                heoroes_genero_m, 'altura')

            print(
                f'\nEl promedio de alturas de los superheroes de genero masculino es de: {altura_promedio_m:.2f}\n')
            os.system('pause')

        case '15':
            heoroes_genero_f = filtrar_lista_diccionarios(
                heroes_normalizados, 'genero', 'F')

            altura_promedio_f = calcular_promedio_en_clave_diccionarios(
                heoroes_genero_f, 'altura')

            print(
                f'\nEl promedio de alturas de los superheroes de genero femenino es de: {altura_promedio_f:.2f}\n')
            os.system('pause')

        case '16':
            if flag_10 and flag_11 and flag_12 and flag_13:
                print('\nHeroe mas alto')
                mostrar_valores_por_claves(heroes_genero_m_mas_altos, [
                    'nombre', 'altura'], 15)
                print('\n------------------------------\n')

                print('Heroina mas alta')
                mostrar_valores_por_claves(heroes_genero_f_mas_altos, [
                    'nombre', 'altura'], 15)
                print('\n------------------------------\n')

                print('Heroe mas bajo')
                mostrar_valores_por_claves(heroes_genero_m_mas_bajos, [
                    'nombre', 'altura'], 15)
                print('\n------------------------------\n')

                print('Heroina mas bajo')
                mostrar_valores_por_claves(heroes_genero_f_mas_bajos, [
                    'nombre', 'altura'], 15)
                print('\n------------------------------\n')

                os.system('pause')

            else:
                print(
                    'Debe calcular primero las alturas maximas y minimas de los heroes (puntos 10 al 13)')
                os.system('pause')

        case '17':
            determinar_colores_de_ojo(heroes_normalizados)

            os.system('pause')

        case '18':
            determinar_colores_de_pelo(heroes_normalizados)

            os.system('pause')

        case '19':
            determinar_tipos_de_inteligencia(heroes_normalizados)

            os.system('pause')

        case '20':
            heroes_por_color_de_ojos = duplicar_lista(heroes_normalizados)

            ordenar_diccionarios(
                lambda heroe1, heroe2: heroe1["color_ojos"] < heroe2["color_ojos"], heroes_por_color_de_ojos)

            mostrar_valores_por_claves(heroes_por_color_de_ojos, [
                'nombre', 'identidad', 'empresa', 'altura', 'peso', 'genero', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia'], 30)

            os.system('pause')

        case '21':
            heroes_por_color_de_pelo = duplicar_lista(heroes_normalizados)

            ordenar_diccionarios(
                lambda heroe1, heroe2: heroe1["color_pelo"] < heroe2["color_pelo"], heroes_por_color_de_pelo)

            mostrar_valores_por_claves(heroes_por_color_de_pelo, [
                'nombre', 'identidad', 'empresa', 'altura', 'peso', 'genero', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia'], 30)

            os.system('pause')

        case '22':
            heroes_por_tipo_de_inteligencia = duplicar_lista(
                heroes_normalizados)

            ordenar_diccionarios(
                lambda heroe1, heroe2: heroe1["inteligencia"] < heroe2["inteligencia"], heroes_por_tipo_de_inteligencia)

            mostrar_valores_por_claves(heroes_por_tipo_de_inteligencia, [
                'nombre', 'identidad', 'empresa', 'altura', 'peso', 'genero', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia'], 30)

            os.system('pause')

        case 'x':
            if input('¿CONFIRMAR SALIDA? (X):') == 'si':
                ejecutando = False
