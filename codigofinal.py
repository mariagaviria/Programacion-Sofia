import pygame
import time
import random

pygame.init()

Surface_ancho =750
Surface_alto =1000

gameSurfaces = pygame.display.set_mode((Surface_ancho,Surface_alto))
pygame.display.set_caption('Poison Course')

Img = pygame.image.load('ballena.png')
fondo= pygame.image.load("fondo-arenoso.jpeg")
fondo = pygame.transform.scale(fondo,(1000,1000))

imgcom=pygame.image.load('comienzodel.jpeg')
imgcom= pygame.transform.scale(imgcom,(1000,1000))

ballenita_ancho = 128
ballenita_alto=206

verde=(103, 234, 26)
colordescore=(255,254,0)
morado= (126,39,207)
moradoclaro=(132,2,254)
gris=(154,152,155)

clock = pygame.time.Clock()


def obstaculoesquivado(contador):
    font=pygame.font.SysFont('freesansbold',35)
    Textodescore= font.render("SCORE: "+str(contador), True, colordescore)
    gameSurfaces.blit(Textodescore, (0,950))

def creaciondelobstaculo(ladox, ladoy, objetoancho, objetoalto, color):
    pygame.draw.rect(gameSurfaces, color, [ladox, ladoy, objetoancho, objetoalto])

def ballenam(x,y):
    gameSurfaces.blit(Img,(x,y))

def texto_objetos(texto, font):
    textsurface=font.render(texto,True,verde)
    return textsurface, textsurface.get_rect()

def mensaje(texto):
    caracteristicas= pygame.font.Font('freesansbold.ttf',125)
    TextSurf, TextRect= texto_objetos(texto, caracteristicas)
    TextRect.center= ((Surface_ancho/2),(Surface_alto/2))
    gameSurfaces.blit(TextSurf, TextRect)

    pygame.display.flip()

    time.sleep(2)

    main()
   
def estrellarse():
    mensaje('Has fallado!')
   
def interacciondelboton(contienemensaje,estaenx,estaeny,ancho,alto,colbotconmouseencima,colbotsinmouseencima,acccomenjuego= None):
    mouse= pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
   
    if estaenx+ancho> mouse[0]>estaenx and estaeny+alto> mouse[1]> estaeny:
        pygame.draw.rect(gameSurfaces,colbotconmouseencima,(estaenx,estaeny,ancho,alto))
        if click[0]==1 and acccomenjuego!=None:
            acccomenjuego()
           
    else:
        pygame.draw.rect(gameSurfaces,colbotsinmouseencima,(estaenx,estaeny,ancho,alto))
       
    textodelstart=pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect= texto_objetos(contienemensaje, textodelstart)
    TextRect.center=((estaenx+(ancho/2)), (estaeny+(alto/2)))
    gameSurfaces.blit(TextSurf,TextRect)
   
def intro_game():

    comienzo= True
   
    while comienzo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameSurfaces.blit(imgcom,(0,0)) 
       
        caracteristicas= pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect= texto_objetos("Dodging Whale", caracteristicas)
        TextRect.center= ((Surface_ancho/2),(Surface_alto/2))
        gameSurfaces.blit(TextSurf, TextRect)
       
        interacciondelboton("Start",300,610,150,100,moradoclaro,morado,main)
       
        pygame.display.flip()
        clock.tick(15)
   
def main():
    x = (Surface_ancho * 0.45)
    y = (Surface_alto * 0.8)

    lavariaciondex = 0

    objetoysupuntodepartidax = random.randrange(0, Surface_ancho)
    objetoysupuntodepartiday = -600
    velocidaddelobstaculoinicial = 3
    anchodelobjeto = 118
    altodelobjeto = 100


    Score = 0

    Fin= False

    while not Fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lavariaciondex = -5
                if event.key == pygame.K_RIGHT:
                    lavariaciondex = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lavariaciondex = 0

        x += lavariaciondex
        gameSurfaces.blit(fondo,(0,0))

        creaciondelobstaculo(objetoysupuntodepartidax, objetoysupuntodepartiday, anchodelobjeto, altodelobjeto, gris)     
        objetoysupuntodepartiday += velocidaddelobstaculoinicial
       
        ballenam(x,y)
        obstaculoesquivado(Score)

        if x > Surface_ancho - ballenita_ancho or x < 0:
            estrellarse()

        if objetoysupuntodepartiday > Surface_alto:
            objetoysupuntodepartiday = 0 - altodelobjeto
            objetoysupuntodepartidax = random.randrange(0,Surface_ancho)
            Score += 1
            velocidaddelobstaculoinicial += 0.8

        if y < objetoysupuntodepartiday + altodelobjeto:
            print('')
                     
            if x > objetoysupuntodepartidax and x < objetoysupuntodepartidax + anchodelobjeto or x+ballenita_ancho > objetoysupuntodepartidax and x + ballenita_ancho < objetoysupuntodepartidax + anchodelobjeto:
                print('')
                estrellarse()
       
        pygame.display.flip()
       clock.tick(60)
intro_game()
main()
pygame.quit()
quit()
