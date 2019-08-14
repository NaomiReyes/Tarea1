#Clase que modela muñecas.

class Muneca:

	def _init_(self, pre_prod, ganan, tipo, acsesorio):
		Fabrica._init_(self, "Muneca", pre_prod*tipo, ganan)
		self.tipo = tipo
		self.acsesorio = acsesorio
	def cambiaTipo (self, tipo2):
		self.tipo = tipo2
