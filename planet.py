class planet:
	name = ''
	hasRing = False
	color = (255, 255, 255)
	
	x = 0
	y = 0
	radius = 200 
	speed = 2 
	angle = 0
	width = 10 
	def __init__(self, nameOfPlanet):
		self.hasRing = False
		self.name = nameOfPlanet
		self.width = 10
		self.color = (255, 255, 255) 

		
		self.x = 0
		self.y = 0
		self.radius = 200 
		self.speed = 2 
		self.angle = 0 

	def getColor(self):
		return self.color
	def setColor(self,inputColor):
		self.color = inputColor
		return True
	def setX(self,xIn):
		self.x = xIn
		return True
	def setY(self,yIn):
		self.y = yIn
		return True
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def setRadius(self,radIn):
		self.radius = radIn
		return True
	def getRadius(self):
		return self.radius
	def getNextAngle(self):
		self.angle = self.angle + self.speed
		if self.angle > 360:
			self.angle -= 360
		angleRad = self.angle * 0.0174532925
		return angleRad
	def setSpeed(self,sIn):
		self.speed = sIn
		return True
	def getSpeed(self):
		return self.speed
	def getAngle(self):
		return self.angle
	def setAngle(self,aIn):
		self.angle = aIn
		return True
	def getName(self):
		return self.name
	def setWidth(self, wIn):
		self.width = wIn
		return True
	def getWidth(self):
		return self.width
	def hasRings(self):
		return self.hasRing
	def toggleRings(self):
		self.hasRing = not self.hasRing
