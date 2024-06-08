from prog_funcional.funciones_prog import *
from tp_stark.data_stark import lista_personajes
altura_a_float(lista_personajes)
peso_a_float(lista_personajes)


#A
heroes_masculinos = mapear_lista(lambda nombres_pj : nombres_pj["nombre"] ,filtra_lista(lambda pj_masculinos : pj_masculinos["genero"] == "M", lista_personajes))

print(heroes_masculinos)

# masculinos = filtra_lista(lambda generos: generos["genero"] == "M", lista_personajes)
# lista_heroes_masculino = mapear_lista(lambda nombre: nombre["nombre"], masculinos)
# print(lista_heroes_masculino)

#B
heroes_femeninos = mapear_lista(lambda nombres_pj : nombres_pj["nombre"] ,filtra_lista(lambda pj_femenino : pj_femenino["genero"] == "F", lista_personajes))

print(heroes_femeninos)

#C
heroes_masculinos = filtra_lista(lambda pj_masculino : pj_masculino["genero"] == "M", lista_personajes)

alturas_masculinas = mapear_lista(lambda altura : (altura["altura"]),heroes_masculinos)

heroe_masculino_mas_alto = reduce(lambda heroe_masc_mas_alto, heroe_nuevo_masc_mas_alto : heroe_masc_mas_alto if (heroe_masc_mas_alto["altura"]) > (heroe_nuevo_masc_mas_alto["altura"]) else heroe_nuevo_masc_mas_alto, heroes_masculinos)

print(f"el heroe masculino mas alto mide {heroe_masculino_mas_alto["altura"]}")

#D
heroes_femeninos = filtra_lista(lambda pj_femenino : pj_femenino["genero"] == "F", lista_personajes)

alturas_femeninas = mapear_lista(lambda altura : (altura["altura"]),heroes_femeninos)

heroes_femenino_mas_alto = reduce(lambda heroe_fem_mas_alto, heroe_nuevo_fem_mas_alto : heroe_fem_mas_alto if (heroe_fem_mas_alto["altura"]) > (heroe_nuevo_fem_mas_alto["altura"]) else heroe_nuevo_fem_mas_alto, heroes_femeninos)

print(f"el heroe femenino mas alto mide {heroes_femenino_mas_alto["altura"]}")

#E
heroes_masculinos = filtra_lista(lambda pj_masculino : pj_masculino["genero"] == "M", lista_personajes)

alturas_masculinas = mapear_lista(lambda altura : (altura["altura"]),heroes_masculinos)

heroe_masculino_mas_bajo = reduce(lambda heroe_masc_mas_bajo, heroe_nuevo_masc_mas_bajo : heroe_masc_mas_bajo if (heroe_masc_mas_bajo["altura"]) < (heroe_nuevo_masc_mas_bajo["altura"]) else heroe_nuevo_masc_mas_bajo, heroes_masculinos)

print(f"el heroe masculino mas bajo mide {heroe_masculino_mas_bajo["altura"]}")

#F
heroes_femeninos = filtra_lista(lambda pj_femenino : pj_femenino["genero"] == "F", lista_personajes)

alturas_femeninas = mapear_lista(lambda altura : (altura["altura"]),heroes_femeninos)

heroes_femenino_mas_bajo = reduce(lambda heroe_fem_mas_bajo, heroe_nuevo_fem_mas_bajo : heroe_fem_mas_bajo if (heroe_fem_mas_bajo["altura"]) < (heroe_nuevo_fem_mas_bajo["altura"]) else heroe_nuevo_fem_mas_bajo, heroes_femeninos)

print(f"el heroe femenino mas bajo mide {heroes_femenino_mas_bajo["altura"]}")

#G
heroes_masculinos = filtra_lista(lambda pj_masculino : pj_masculino["genero"] == "M", lista_personajes)
alturas_masculinas = mapear_lista(lambda altura : (altura["altura"]) ,heroes_masculinos)
promedio_altura_masc = calcular_promedio(alturas_masculinas)
print(f"El promedio de las alturas de los masculinos es: {promedio_altura_masc}")

#H
heroes_femeninos = filtra_lista(lambda pj_femenino : pj_femenino["genero"] == "F", lista_personajes)
alturas_femeninas = mapear_lista(lambda altura : (altura["altura"]) ,heroes_femeninos)
promedio_altura_fem = calcular_promedio(alturas_femeninas)
print(f"El promedio de las alturas de los femeninos es: {promedio_altura_fem}")







