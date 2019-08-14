class Pelotas(Fabrica):

	def _init_(self, pre_prod, ganan, tamano, color):
		Fabrica._init_(self, "Pelota", pre_prod, ganan)
		self.tam = tamano
		self.col = color
	def pelota (self):
		print "Tu pelota es " + self.tamano + "de color " + self.color
 






