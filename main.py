#from graphviz import Graphviz
from graphviz import Digraph
class Nodo:
	def __init__(self,dato=None,sig=None):
		self.dato= dato
		self.sig = sig

	def getDato(self):
		return self.dato

class nodoCola:
	def __init__(self,dato=None,primero=None,sig=None):
		self.dato= dato
		self.primero = primero
		self.sig = sig
	def getDato(self):
		return self.dato

class nodoPila:
	def __init__(self):
		self.dato=None
		self.atras = None	

	def getDato(self):
		return self.dato

		
class Cola:
	def __init__(self):
		self.tama=0
		self.primero=None

	def getTama(self):
		return self.tama

	def insertar(self,NodoCol):	
		self.tama = self.tama + 1	
		if self.primero == None:
			self.primero = NodoCol		
			print self.primero.getDato()
		else:
			actual = self.primero
			while actual.sig != None:				
				actual= actual.sig
			actual.sig = NodoCol
			print actual.sig.getDato()

	def listar(self):
		aux = self.primero
		while aux != None:
			print(aux.getDato())
			aux = aux.sig

	def eliminar(self):
		aux = self.primero
		self.primero = self.primero.sig
		self.tama = self.tama - 1
		return aux.getDato()
		
	def pintar(self,col):
		g1 = Digraph(format='svg')
		aux = self.primero
		while aux!=None:
			primero =aux.getDato()
			g1.node(primero)
			aux = aux.sig
			if aux !=None :
				g1.edge(aux.getDato(),primero)
		print(g1.source)
		
class pila:
	def __init__(self):
		self.tope= nodoPila()
		self.tama = 0

	def getTama(self):
		return self.tama
	
	def push(self,nodoInsertar):
		self.tama= self.tama + 1
		if self.tope == None:
			self.tope= nodoInsertar
		else:
			nodoInsertar.atras = self.tope
			self.tope = nodoInsertar
		
		
	def pop(self):
		self.tama = self.tama -1
		aux = self.tope
		if aux == None:
			print "pila vacia"
		else:
			print self.tope.getDato()	
			self.tope=aux.atras			

			if aux.atras == None:
				self.tope = nodoPila()

			
	def consultar(self):
		aux = self.tope
		if aux.getDato() == None:
			print "lista vacia"
		else:
			while aux != None:
				print aux.getDato()
				aux = aux.atras

	def graficar(self,pila):
		g3 = Digraph(format='svg')
		aux = self.tope
		if aux.getDato() == None:
			print "lista vacia"
		else:
			while aux != None:
				if aux.getDato() != None:
					primero = aux.getDato()
					g3.node(primero)					
					
					print aux.atras.getDato()	
					
					if aux.atras.getDato() != None:
						g3.edge(aux.atras.getDato(),primero)								
					aux = aux.atras
				else:
					break
		print(g3.source)
							
class ListaSimple:
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.tama=0

	def listar(self):
		aux = self.inicio
		while aux != None:
			print(aux.getDato())
			aux = aux.sig

	def getTama(self):
		return self.tama

	def insertar(self,nodoNuevo):		
		if self.inicio == None :
			self.inicio=nodoNuevo

		if self.fin != None:
			self.fin.sig = nodoNuevo

		self.fin = nodoNuevo
		self.tama = self.tama + 1

	def buscar(self,palabra):
		aux = self.inicio		
		contador=0
		while True:
			if aux !=None:
				if aux.getDato() is palabra:
					print "Encontrado en: " + str(contador)
					break
				else:
					contador =contador +1
					aux=aux.sig
					
			else:
				print("No se encontro")
				break

	def eliminar(self,index):
		aux = self.inicio
		contador = 0
		anterior = None
		while True:			
			if contador == index:
				if anterior != None:
					anterior.sig = aux.sig	
				else:
					self.inicio = aux.sig	
				break
			else:
				anterior= aux
				aux= aux.sig				
				contador = contador+1

	def dibujarLs(self,lista):
		g2 = Digraph(format='svg')
		aux = self.inicio
		while aux != None:			
			primero = aux.getDato()
			g2.node(primero)
			aux = aux.sig
			if aux !=None :
				g2.edge(primero,aux.getDato())
		print(g2.source)

class main:
	def __init__(self):
		return
while True:
	print("--MENU--")
	print("1Llista Simple")
	print("2 cola")
	print("3 pila")	
	print("4 Salir")
	sele = (raw_input("Seleccion"))
	if sele=="1":
		while true:
			print("--MENU--")
			print("1 Agregar")
			print("2 Borrar")
			print("3 Buscar")
			print("4 Graficar")
			ope = (raw_input("Operacion"))
				if ope == "1":
				elif ope == "2":
				elif ope == "3":
				elif ope == "3":
	elif sele == "2":
	elif sele == "3":
	elif sele == "4":
		break
#-------------------LISTA SIMPLE--------------------------------
ver = ListaSimple()
nod1 = Nodo("15")
nod2 = Nodo("7")
nod3 = Nodo("98")
nod4 = Nodo("1")
ver.insertar(nod1)
ver.insertar(nod2)
ver.insertar(nod3)
print "Tamano Lista: " + str(ver.getTama())
ver.dibujarLs(ver)
#print("ELIMINAR")
#ver.eliminar(0)
#print("lISTA NUEVA")
#ver.listar()

#-------------------COLA----------------------------
cola = Cola()
cola.insertar(nodoCola("1"))
cola.insertar(nodoCola("2"))
cola.insertar(nodoCola("3"))
cola.insertar(nodoCola("4"))
print "Eliminado: "+ str(cola.eliminar())
#cola.listar()
cola.pintar(cola)
#----------------------PILA--------------------

pila = pila()
nodo1 = nodoPila()
nodo1.dato = "5"
nodo2 = nodoPila()
nodo2.dato = "10"
nodo3 = nodoPila()
nodo3.dato = "15"

pila.push(nodo1)
pila.push(nodo2)
pila.push(nodo3)
#pila.pop()
#print "NUEVA"
#pila.consultar()
pila.graficar(pila)