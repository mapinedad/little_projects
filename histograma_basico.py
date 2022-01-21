"""Práctica de histograma usando sólo sentencias puras de Python.
	Sin librerías de visualización gráfica.
"""
from collections import Counter

edades = [12, 15, 20, 18, 12, 19, 19, 20, 13, 16, 17, 13, 12, 18, 20, 19, 20, 13, 12, 13, 17, 15, 16, 13, 14, 13, 17, 19]
intervalos = [(10, 13), (13, 16), (16, 19), (19, 22)]
mapa_edades = dict(zip(intervalos, [0]*len(intervalos)))
#print(mapa_edades)

for edad in edades:
	for intervalo in mapa_edades:
		if intervalo[0] <= edad < intervalo[1]:
			mapa_edades[intervalo] += 1
			break
			
for valor in sorted(mapa_edades):
	print(f'{valor}: {"-" * mapa_edades[valor]}')