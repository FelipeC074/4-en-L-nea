Turno = True

class Ficha:
    def __init__(self, Color):
     self.Color = Color
     self.Tam = 40
     self.posx = 350
     self.posy = 50
     self.tirda = False
    def Caer(self):
       self.posy += 5
class Separador_H:
   def __init__(self, posy, nivel):
      self.posx = 0
      self.posy = posy
      self.color = "blue"
      self.width = 700
      self.alto = 10
      self.nivel = nivel