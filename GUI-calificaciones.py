#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# programa bajo la licencia GPL v3 #
from tkinter import *
ventana = Tk()
ventana.geometry('385x330+100+100')
ventana.title('calificaciones')

#creacion de plantillas de texto/Label
lbltexto = Label(ventana,text="Bienvenido a este programa para promediar de calificaciones\n de cobaed por favor ingresa tus datos").place(x=10,y=10)
lbltuto = Label(ventana,text="Escribe la calificación que desees y tus calificaciones\n en caso de aun no tenerlas dejarlas en cero o poner cero").place(x=10,y=50)
cal = Label(ventana,text="¿que calificasión deseas?").place(x=10,y=100)
lpar1 = Label(ventana,text="parctial 1").place(x=10,y=120)
lpar2 = Label(ventana,text="parctial 2").place(x=10,y=140)
lpar3 = Label(ventana,text="parctial 3").place(x=10,y=160)
lpar4 = Label(ventana,text="parctial 4").place(x=10,y=180)
lsem = Label(ventana,text="semestral").place(x=10,y=210)

#Crecion y acomodo de los spinbox/caja_de_números
cal = Spinbox(ventana,from_=0, to=10,)
cal.pack()
cal.place(x=170,y=100)
par1 = Spinbox(ventana,from_=0, to=10,)
par1.pack()
par1.place(x=80,y=120)
par2 = Spinbox(ventana,from_=0, to=10)
par2.pack()
par2.place(x=80,y=140,)
par3 = Spinbox(ventana,from_=0, to=10)
par3.pack()
par3.place(x=80,y=160)
par4 = Spinbox(ventana,from_=0, to=10)
par4.pack()
par4.place(x=80,y=180)
sem  = Spinbox(ventana,from_=0, to=2)
sem.pack()
sem.place(x=80,y=210)

#Funciones
#Una función para realizar las operaciones de cada parcial
def parcial0():
	
	c = float(cal.get())
	p1 = float(par1.get())
	p2 = float(par2.get())
	p3 = float(par3.get())
	p4 = float(par4.get())
	s = float(sem.get())
	m = (c * 0.8)
	ms = c - m
	def resultado():#si lo defino fuera no funciona :/
		if ms <= 2 and c <= 10:	
			par1.insert(0,m)
			par2.insert(0,m)
			par3.insert(0,m)
			par4.insert(0,m)
			sem.insert(0,ms)
		else:
			error = Label(ventana,text="lo sentimos no puedes sacar esa calificación :/").place(x=10,y=250)
	resultado()
def parcial1():
	c = float(cal.get())
	p1 = float(par1.get())
	p2 = float(par2.get())
	p3 = float(par3.get())
	p4 = float(par4.get())
	s = float(sem.get())
	prom1 = ((c * 4)-p1) / 3
	m = prom1 * 0.8 
	ms = c - m
	def resultado():#si lo defino fuera no funciona :/
		if ms <= 2 and c <= 10:	
			par2.insert(0,m)
			par3.insert(0,m)
			par4.insert(0,m)
			sem.insert(0,ms)
		else:
			error = Label(ventana,text="lo sentimos no puedes sacar esa calificación :/").place(x=10,y=250)
	resultado()
def parcial2():
	c = float(cal.get())
	p1 = float(par1.get())
	p2 = float(par2.get())
	p3 = float(par3.get())
	p4 = float(par4.get())
	s = float(sem.get())
	pf = (p1 + p2)
	prom1 = ((c * 4)-pf) / 2
	m = prom1 * 0.8 
	ms = c - m
	def resultado():#si lo defino fuera no funciona :/
		if ms <= 2 and c <= 10:	
			par3.insert(0,m)
			par4.insert(0,m)
			sem.insert(0,ms)
		else:
			error = Label(ventana,text="lo sentimos no puedes sacar esa calificación :/").place(x=10,y=250)
	resultado()
def parcial3():
	c = float(cal.get())
	p1 = float(par1.get())
	p2 = float(par2.get())
	p3 = float(par3.get())
	p4 = float(par4.get())
	s = float(sem.get())
	pf = p1 + p2 + p3
	prom1 = ((c * 4)-pf)
	m = prom1 * 0.8 
	ms = c - m
	def resultado():#si lo defino fuera no funciona :/
		if ms <= 2 and c <= 10:	
			par4.insert(0,m)
			sem.insert(0,ms)
		else:
			error = Label(ventana,text="lo sentimos no puedes sacar esa calificación :/").place(x=10,y=250)
	resultado()
def parcial4():
	c = float(cal.get())
	p1 = float(par1.get())
	p2 = float(par2.get())
	p3 = float(par3.get())
	p4 = float(par4.get())
	s = float(sem.get())
	pf = (p1 + p2 + p3 +p4) / 4
	prom1 = c - pf
	m = prom1 * 0.8 
	ms = c - m
	def resultado():#si lo defino fuera no funciona :/
		if ms <= 2 and c <= 10:	
			sem.insert(0,ms)
		else:
			error = Label(ventana,text="lo sentimos no puedes sacar esa calificación :/").place(x=10,y=250)
	resultado()
#Ejecuta y verifica los datos
def ejecutar():
	c = float(cal.get()) #Al no convertirlo da problemas
	p1 = float(par1.get())# por defecto es str
	p2 = float(par2.get())
	p3 = float(par3.get())
	p4 = float(par4.get())
	s = float(sem.get())
	if p1 != 0 and p2 != 0 and p3 !=0 and p4 != 0:
		parcial4()
	elif p1 != 0 and p2 != 0 and p3 !=0 and p4 == 0:
		parcial3()
	elif p1 != 0 and p2 != 0 and p3 ==0 and p4 == 0:
		parcial2()
	elif p1 != 0 and p2 == 0 and p3 ==0 and p4 == 0:
		parcial1()
	elif p1 == 0 and p2 == 0 and p3 ==0 and p4 == 0:
		parcial0()
	
	else:
		t = error = Label(ventana,text="lo sentimos no puedes sacar o tener esa calificación :/").place(x=10,y=250)
	
	
#Botones de ejecucion de programa uno para pruebas
boton1 = Button(ventana, text='ejecutar', command=ejecutar).place(x=150,y=290)

ventana.mainloop()
