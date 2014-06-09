#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# programa bajo la licencia GPL v3 #
print ('''Bienvenido a este pro-mediador de calificaciones 
de cobaed por favor ingresa tus datos
''')
# variables a utilizar
m = str(input('Nombre de materia: '))
c = float(input('¿que calificación deseas?: '))
s = int(input('¿cuantos parciales has terminado?: '))
error = 'lo sentimos no puedes sacar esa calificación :/'
#Funciones, 1 para comprobar promedio y otro el resultado	
def final():
	if prom_par <= 2:
		resultado()
	else :
		print(error)
def resultado():
	print('Tu necesitas en',m,' mínimo : ',prom,' en cada parcial y ',prom_par,'en el semestral')
#comprovación de calificaciones aceptables
if c <= 10:
	if s == 0:
		prom = float(c * 0.8)
		prom_par = c - prom
		final()
	elif s == 1:
		p1 = float(input('por favor escribe la calificación del parcial 1: '))
		prom1 = ((c * 4)-p1) / 3
		prom = prom1 * 0.8 
		prom_par = c - prom
		final()
	elif s == 2:
		p1 = float(input('por favor escribe la calificación del parcial 1: '))
		p2 = float(input('por favor escribe la calificación del parcial 2: '))
		pf = (p1 + p2)
		prom1 = ((c * 4)-pf) / 2
		prom = prom1 * 0.8 
		prom_par = c - prom
		final()
	elif s == 3:
		p1 = float(input('por favor escribe la calificación del parcial 1: '))
		p2 = float(input('por favor escribe la calificación del parcial 2: '))
		p3 = float(input('por favor escribe la calificación del parcial 3: '))
		pf = p1 + p2 + p3
		prom1 = ((c * 4)-pf)
		prom = prom1 * 0.8 
		prom_par = c - prom
		final()
	elif s == 4:
		p1 = float(input('por favor escribe la calificación del parcial 1: '))
		p2 = float(input('por favor escribe la calificación del parcial 2: '))
		p3 = float(input('por favor escribe la calificación del parcial 3: '))
		p4 = float(input('por favor escribe la calificación del parcial 4: '))
		pf = (p1 + p2 + p3 +p4) / 4
		prom1 = c - pf
		prom = prom1 * 0.8 
		prom_par = c - prom
		final()
	else :
		print('Lo sentimos no tenemos registrados tantos parciales.')
else :
	print(error)
