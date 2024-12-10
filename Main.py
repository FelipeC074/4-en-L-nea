import pygame
import Funciones_Clases as FC
import sys

#Paso 1: dibujar correctamente las fichas, que se muevan cn las flechas y bajen cuando se cliquee ||||LISTO||||

#Paso 2: Hacer que las fichas bajen hasta encontrarse con otra ficha debajo 

#Paso 3: Calcular quien gana y quien pierde según las posiciones de las fichas
pygame.init()  #
Running = True
Ancho, Alto = 700,700
Pantalla = pygame.display.set_mode((Ancho,Alto))
pygame.display.set_caption("4 En Raya")

ListaFichs = []
PrimFich = FC.Ficha(True)
ListaFichs.append(PrimFich)
ListSeps = []

for i in range(7):
   separ = FC.Separador_H(i * 100, 7 - i)
   ListSeps.append(separ)


def DibujarFichas():
    for obj in ListaFichs:
      if obj.Color:
        pygame.draw.circle(Pantalla, "red",(obj.posx, obj.posy), obj.Tam)
      else:
        pygame.draw.circle(Pantalla, "yellow",(obj.posx, obj.posy), obj.Tam)


def DibujarSeparadoresH():
   for sep in ListSeps:
      pygame.draw.rect(Pantalla, sep.color,(sep.posx, sep.posy, sep.width, sep.alto))


def Clic_Hecho():
   #Caiga la ficha
   ListaFichsPosXY = []
   for fich in ListaFichs:
      if fich.tirda == False:
        fichCaer = fich
        ListaFichs.remove(fich)
      else:
           ListaFichsPosXY.append(fich.posy)
   while True:   #whosvnio
      fichCaer.Caer()#gjvsivsjpv
      break   #vtkmvvspj
    
   fichCaer.tirda = True
   ListaFichs.append(fichCaer)
   #Se genere otra ficha
   if FC.Turno:
      FC.Turno = False
      Newfich = FC.Ficha(FC.Turno)
   else:
      FC.Turno = True
      Newfich = FC.Ficha(FC.Turno)
   ListaFichs.append(Newfich)

while Running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONUP:
            Clic_Hecho()
        if evento.type == pygame.KEYDOWN:  
          if evento.key == pygame.K_LEFT:
           for fich in ListaFichs:
              if fich.tirda == False:
                 fich.posx -= 100
          if evento.key == pygame.K_RIGHT:
           for fich in ListaFichs:
              if fich.tirda == False:
                 fich.posx += 100
                 ListaFichs.remove(fich)
                 ListaFichs.append(fich)
    Pantalla.fill((0, 0, 0))
    DibujarFichas()
    DibujarSeparadoresH()
    pygame.display.flip()
