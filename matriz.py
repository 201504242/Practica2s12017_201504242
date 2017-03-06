class NodoM:
	#constructor
	def _init_(self, valor):
		self.__anterior = None
		self.__siguiente = None
		self.__valor = valor

	def getSiguiente(self):
		return self.__siguiente

	def getAnterior(Self):
		return self.__anterior

	def setSiguiente(self, siguiente):
		self.__siguiente = siguiente

	def setAnterior(self, anterior):
		self.__anterior = anterior

	def getValor(self):
		return self.__valor

class ListaDoble:
	#constructor
	def _init_(self):
		self.__cabeza = None
		self.__length = 0

	def agregar(self, valor):
		if self.__cabeza == None:
			self.__cabeza = NodoM(valor)
		else:
			auxiliar = self.__cabeza
			self.__cabeza = NodoM(valor)
			self.__cabeza.setSiguiente(auxiliar)
			auxiliar.setAnterior(cabeza)
		self.__length = self.__length + 1

	def eliminar(self, valor):
		if self.__cabeza != None:
			auxiliar = self.__cabeza
			while(auxiliar.getValor() != valor):
				auxiliar = auxiliar.getSiguiente()
				if auxiliar == None:
					break
			if auxiliar != None:
				if auxiliar.getAnterior() != None:
					auxiliar.getAnterior().setSiguiente(auxiliar.getSiguiente())
				if auxiliar.getSiguiente() != None:
					auxiliar.getSiguiente().setAnterior(auxiliar.getAnterior())
				self.__length = self.__length - 1

	def getLength(self):
		return self.__length

class Nodo:
	def __init__(self,dato=None,sig=None):
		self.dato= dato
		self.sig = sig

	def getDato(self):
		return self.dato
	def getPos(self):
		return self.pos

class ListaSimple:
	def __init__(self):
		self.inicio = None
		self.fin = None
		self.tama=0
		self.pos=0

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

class NodoOrtogonal():
	#constructor
	def _init_(self):
		self.__up = None
		self.__down = None
		self.__left = None
		self.__right = None
		self.__fondo = ListaDoble()

	def add(self, valor):
		self.__fondo.agregar(valor)

	def delete(self, valor):
		self.__fondo.eliminar(valor)

	def getValues(self):
		return self.__fondo

	def getUp(self):
		return self.__up 

	def getDown(self):
		return self.__down

	def getLeft(self):
		return self.__left

	def getRigth(self):
		return self.__right

	def setUp(self, up):
		self.__up = up

	def setDown(self, down):
		self.__down = down

	def setLeft(self, left):
		self.__left = left

	def setRigth(self, right):
		self.__right = right

class Matriz():
	#constructor
	def _init_(self):
		self.raiz = NodoOrtogonal()	

class pruebaMatriz():
	def __init__(self):
		self.raiz = NodoOrtogonal()	
	#def insertar():

class Main:
	"""docstring for Main"""
	def __init__(self):
		return
iniciales = None
empresas = None
iniciales = ListaSimple()
empresas = ListaSimple()
while True:
	print("Menu 1)Agregar 3)salir")
	entrada = (raw_input("Seleccion"))
	if entrada == "1":
		c = (raw_input("Introduce correo:"))
		inicial = c[0]
		iniciales.insertar(Nodo(inicial))
		e = (raw_input("Introduce empresa :"))	
		empresas.insertar(Nodo(e))
	elif entrada == "3":
		iniciales.listar()
		empresas.listar()
		break	
	
