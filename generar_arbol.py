from anytree import Node, PreOrderIter, RenderTree
from anytree.exporter import UniqueDotExporter
from anytree.util import rightsibling
import numpy as np
import pygraphviz as pvg
import random
import os, hashlib
from tkinter import *
from tkinter import messagebox
import cv2
# import pygame

def uniqueID():
	return hashlib.md5(os.urandom(32)).hexdigest()[:5]

def indiceAleatorio(limite):
	return random.randint(0,limite-1)

def construirTablero(cantidadFilas, obstaculos_):
	tablero = []
	cantidadFilas = cantidadFilas
	obstaculos_ = obstaculos_

	tablero = []
	contador = 0
	for i in range(0, cantidadFilas):
		row = []
		for j in range(contador+1, (contador + cantidadFilas)+1):
			row.append(j)
			contador = j
		tablero.append(row)

	for i in range(obstaculos_):
		x = indiceAleatorio(len(tablero))
		y = indiceAleatorio(len(tablero[0]))
		tablero[x][y] = -1  # Obstaculo

	xInicio = indiceAleatorio(len(tablero))
	yInicio = indiceAleatorio(len(tablero[0]))

	xSalida = indiceAleatorio(len(tablero))
	ySalida = indiceAleatorio(len(tablero[0]))
	tablero[xInicio][yInicio] = 0
	# Fijar la casilla final
	tablero[xSalida][ySalida] = -100

	return tablero, xInicio, yInicio

def mostrarTablero(tablero):
	print("\n")
	for row in tablero:
		print(row)
	print("\n")

def arriba(tablero, x, y):
	# Ir hacia arriba
	try:
		if tablero[x-1][y] != -1 and x > 0:
			return tablero[x-1][y]
	except IndexError:
		pass
	return None

def derecha(tablero, x, y):
	# Ir hacia la derecha
	try:
		if tablero[x][y+1] != -1:
			return tablero[x][y+1]
	except IndexError:
		pass
	return None

def abajo(tablero, x, y):
	# Ir hacia abajo
	try:
		if tablero[x+1][y] != -1:
			return tablero[x+1][y]
	except IndexError:
		pass
	return None

def izquierda(tablero, x, y):
	# Ir hacia la izquierda
	try:
		if tablero[x][y-1] != -1 and y > 0:
			return tablero[x][y-1]
	except IndexError:
		pass
	return None

def showRecorridos(nodoPadre):
	preorder = PreOrderIter(nodoPadre)
	camino = ""
	for node in preorder:
		if node.name == -100:
			camino += f"{node.name}"
			break
		camino += f"{node.name} > "
	print(camino)
	return camino
	

def getCoords(tablero, valorBuscado):
	tmp = np.array(tablero)
	return np.where(tmp==valorBuscado, )

def existeEnLaPila(pila, valor):
	result = False
	for v in pila:
		if v == valor:
			result = True
	return result

def doAlgorithm(size, obstaculos):	
	tablero, xInicio, yInicio = construirTablero(size, obstaculos)
	expansionMaxima = ((len(tablero) * len(tablero)) - obstaculos) * 2

	print(f'Numero de estados => {expansionMaxima}')
	if tablero[xInicio][yInicio] != 0:
		messagebox.showerror(message="Por azares del destino, el tablero no cuenta con una casilla de salida, que mala suerte...", title="Upss")
		raise Exception("Por azares del destino, el tablero no cuenta con una casilla de salida, que mala suerte...")

	nodoRaiz = Node(tablero[xInicio][yInicio], id=uniqueID())
	nodoCursor = None

	nodosVisitados = []

	mostrarTablero(tablero)

	valorArriba = arriba(tablero, xInicio, yInicio)
	if(valorArriba != None):
		uid = uniqueID()
		nodoCursor = Node(valorArriba, parent=nodoRaiz, id=uid)
	
	valorDerecha = derecha(tablero, xInicio, yInicio)
	if(valorDerecha != None):
		uid = uniqueID()
		nodoCursor = Node(valorDerecha, parent=nodoRaiz, id=uid)
	
	valorAbajo = abajo(tablero, xInicio, yInicio)
	if(valorAbajo != None):
		uid = uniqueID()
		nodoCursor = Node(valorAbajo, parent=nodoRaiz, id=uid)
	
	valorIzquierda = izquierda(tablero, xInicio, yInicio)
	if(valorIzquierda != None):
		uid = uniqueID()
		nodoCursor = Node(valorIzquierda, parent=nodoRaiz, id=uid)

	nodosVisitados.append(nodoRaiz.name)
	nodoHijoEvaluando = nodoRaiz.children[0]
	while nodoHijoEvaluando != None:
		yaPasePorAqui = existeEnLaPila(nodosVisitados, nodoHijoEvaluando.name)
		if yaPasePorAqui == False:
			nodosVisitados.append(nodoHijoEvaluando.name)
			if nodoHijoEvaluando.name == -100: # Solucion
				break
			coordenadasHijoEvaluando = getCoords(tablero, nodoHijoEvaluando.name)
			_x = int(coordenadasHijoEvaluando[0])
			_y = int(coordenadasHijoEvaluando[1])
			valorArriba = arriba(tablero, _x, _y)
			if(valorArriba != None):
				uid = uniqueID()
				hijo = Node(valorArriba, parent=nodoHijoEvaluando, id=uid)
			
			valorDerecha = derecha(tablero, _x, _y)
			if(valorDerecha != None):
				uid = uniqueID()
				hijo = Node(valorDerecha, parent=nodoHijoEvaluando, id=uid)
			
			valorAbajo = abajo(tablero, _x, _y)
			if(valorAbajo != None):
				uid = uniqueID()
				hijo = Node(valorAbajo, parent=nodoHijoEvaluando, id=uid)
			
			valorIzquierda = izquierda(tablero, _x, _y)
			if(valorIzquierda != None):
				uid = uniqueID()
				hijo = Node(valorIzquierda, parent=nodoHijoEvaluando, id=uid)
			nodoHijoEvaluando = nodoHijoEvaluando.children[0]
		else:
			try:
				nodoHijoEvaluando = rightsibling(nodoHijoEvaluando)
			except Exception:
				nodoHijoEvaluando = rightsibling(nodoHijoEvaluando.parent)
	return nodoRaiz

def evaluarEntradas(size, obstaculos, txtSize, txtObst):
	txtSize.config(state=DISABLED)
	txtObst.config(state=DISABLED)

	nodoRaiz = None
	while(True):
		nodoRaiz = doAlgorithm(size, obstaculos)
		# if(showRecorridos(nodoRaiz).find("-100") == -1):
		# 	break
		if(showRecorridos(nodoRaiz).find("-100") > 0):
			break
	
	UniqueDotExporter(nodoRaiz).to_picture("arbol_unique.png")
	showRecorridos(nodoRaiz)
	# showRecorridos(nodoRaiz, tablero)
	imagenResultante = cv2.imread("arbol_unique.png", cv2.IMREAD_GRAYSCALE)
	cv2.imshow('Arbol resultante', imagenResultante)
	cv2.waitKey()
	cv2.destroyAllWindows()

	txtSize.config(state=NORMAL)
	txtObst.config(state=NORMAL)
	messagebox.showinfo(message="Algoritmo terminado", title="Información")


if __name__ == "__main__":
	window = Tk()
	window.title("DSI - DFS Obstaculos")
	window.geometry('350x200')	
	# Etiqueta de Tamaño de cuadricula
	lblCuadSize = Label(window, text="Ingresa el tamaño de la cuadrícula: ", font=("Arial Bold", 15))
	lblCuadSize.grid(column=0, row=0)
	txtCuadSize = Entry(window, width=10)
	txtCuadSize.grid(column=1, row=0)
	txtCuadSize.config(state=NORMAL)

	lblObstAmmount = Label(window, text="Número de obstáculos: ", font=("Arial Bold", 15))
	lblObstAmmount.grid(column=0, row=1)
	txtObstAmmount = Entry(window, width=10)
	txtObstAmmount.grid(column=1, row=1)
	txtObstAmmount.config(state=NORMAL)
	

	# btnStart = Button(window, text="Let's go!", fg="black", command=lambda: evaluarEntradas(int(txtCuadSize.get()), int(txtObstAmmount.get()), txtCuadSize, txtObstAmmount))
	btnStart = Button(window, text="Let's go!", fg="black", command=lambda: evaluarEntradas(3, 1, txtCuadSize, txtObstAmmount))
	btnStart.grid(column=0, row=2)
	window.mainloop()
