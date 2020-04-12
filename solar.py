import pygame
import math
import Color
from planet import planet
pygame.init()
screenWidth = 1377
screenHeight = 720
screenWidthHalf = screenWidth // 2
screenHeightHalf = screenHeight // 2

size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)

 
pygame.display.set_caption("Solar System")
logo = pygame.image.load("Star-Galaxy-300x300.jpg")
pygame.display.set_icon(logo) 
done = False
clock = pygame.time.Clock()
#Planets

#mercury
mercury = planet('Mercury')
mercury.setColor(Color.mercury)
mercury.setWidth(10)
mercury.setRadius(50)
mercury.setSpeed(3)
mercury.setX(50)
mercury.setY(250)
#venus
venus = planet('Venus')
venus.setColor(Color.venus)
venus.setWidth(13)
venus.setRadius(100)
venus.setSpeed(2.1946939628159598913724670983915)
venus.setX(100)
venus.setY(250)
#earth
earth = planet('Earth')
earth.setColor(Color.earth)
earth.setWidth(14)
earth.setRadius(150)
earth.setSpeed(1.8663045748903279715897221641948)
earth.setX(150)
earth.setY(250)
#mars
mars = planet('Mars')
mars.setColor(Color.mars)
mars.setWidth(11)
mars.setRadius(180)
mars.setSpeed(1.5088991017338625443910591184459)
mars.setX(180)
mars.setY(250)


#jupiter
jupiter = planet(Color.jupiter)
jupiter.setWidth(22)
jupiter.setRadius(250)
jupiter.setSpeed(0.81909337789847503655734280342598)
jupiter.setX(250)
jupiter.setY(250)
#saturn
saturn = planet('Saturn')
saturn.setColor(Color.saturn)
saturn.setWidth(20)
saturn.setRadius(280)
saturn.setSpeed(0.60726968874033841654480885732194)
saturn.setX(280)
saturn.setY(250)
saturn.toggleRings()
#uranus
uranus = planet('Uranus')
uranus.setColor(Color.uranus)
uranus.setWidth(18)
uranus.setRadius(320)
uranus.setSpeed(0.42678086484228117819093377898477)
uranus.setX(320)
uranus.setY(250)
#neptune
neptune = planet('Neptune')
neptune.setColor(Color.neptune)
neptune.setWidth(17)
neptune.setRadius(350)
neptune.setSpeed(0.34029663672446208481303530394821)
neptune.setX(350)
neptune.setY(250)

def drawPlanets(planetIn):
	pygame.draw.circle(screen, Color.white, [screenWidthHalf,screenHeightHalf], planetIn.getRadius(), 1)
	pygame.draw.circle(screen, planetIn.getColor(), [planetIn.getX(), planetIn.getY()], planetIn.getWidth(), planetIn.getWidth())
	if planetIn.hasRings() == True:
		pygame.draw.circle(screen, Color.white, [planetIn.getX(), planetIn.getY()], planetIn.getWidth()+5, 1)

def movePlanets(planetIn):
	angl = planetIn.getNextAngle()
	planetIn.setX(int(screenWidthHalf + math.sin(angl) * planetIn.getRadius()))
	planetIn.setY(int(screenHeightHalf + math.cos(angl) * planetIn.getRadius()))
def movePlanetsS(planetIn):
	angl = planetIn.getNextAngle()
	planetIn.setX(int(screenWidthHalf + math.cos(angl) * planetIn.getRadius()))
	planetIn.setY(int(screenHeightHalf + math.sin(angl) * planetIn.getRadius()))



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(Color.black)

    pygame.draw.circle(screen, Color.orange, [screenWidthHalf, screenHeightHalf], 40, 40)
#planets
    drawPlanets(mercury)
    drawPlanets(venus)
    drawPlanets(earth)
    drawPlanets(mars)
    drawPlanets(jupiter)
    drawPlanets(saturn)
    drawPlanets(uranus)
    drawPlanets(neptune)
#Movements
    movePlanets(mercury)
    movePlanetsS(venus)
    movePlanets(earth)
    movePlanets(mars)
    movePlanets(jupiter)
    movePlanets(saturn)
    movePlanets(uranus)
    movePlanetsS(neptune)
    
    pygame.display.flip()
    clock.tick(120)
 
pygame.quit()
