import os
from funciones import *
from data_stark import lista_personajes

heroes = duplicar_lista(lista_personajes)
heroes_normalizados = normalizar_diccionarios(heroes)
# == == == == == == == == == == == == == == == == == == == == == == == ==

alturas = mapear_diccionarios(heroes_normalizados, ['altura'])

heroes_mas_altos = []

altura_maxima = alturas[0]["altura"]

for altura in alturas:
    if altura["altura"] > altura_maxima:
        altura_maxima = altura["altura"]

for heroe in heroes_normalizados:
    if heroe["altura"] == altura_maxima:
        heroes_mas_altos.append(heroe)

print(heroes_mas_altos)
