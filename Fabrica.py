#Clase que modela una fabrica de juguetes.

class Fabrica:
	def _init_(self, nom, pre_prod, ganan):
		self.nombre = nom
		self.costoPro = pre_prod
		self.ganancia = gana
		self.descuento = False
<<<<<<< HEAD
	def costo:
=======
<<<<<<< HEAD
	def costo:
=======
	def costo(self):
>>>>>>> branch-1
>>>>>>> staging
		if self.descuento:
			des = int(input("¿Cuanto es el descuento?"))
			costofin = (self.costoPro + self.ganancia) - des
			print costofin
		else:
			print self.costoPro + self.ganancia
<<<<<<< HEAD
	def nombreProducto:
=======
<<<<<<< HEAD
	def nombreProducto:
=======
	def nombreProducto(self):
>>>>>>> branch-1
>>>>>>> staging
		print self.nombre
		
			



