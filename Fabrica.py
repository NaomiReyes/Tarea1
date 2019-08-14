#Clase que modela una fabrica de juguetes.

class Fabrica:
	def _init_(self, nom, pre_prod, ganan):
		self.nombre = nom
		self.costoPro = pre_prod
		self.ganancia = gana
		self.descuento = False
	def costo:
		if self.descuento:
			des = int(input("¿Cuanto es el descuento?"))
			costofin = (self.costoPro + self.ganancia) - des
			print costofin
		else:
			print self.costoPro + self.ganancia
	def nombreProducto:
		print self.nombre
		
			



