import random

class Character():

	def __init__(self, x: int, y: int):
		self.x = x	# +HP  -AG
		self.y = y	# +DMG -ED3
		self.HP = (5+x)*10
		self.ED = 5-y
		self.inventory = []
		self.weapon :Item = None
		self.helmet :Item = None
		self.armor  :Item = None
		self.boots  :Item = None
		self.moveSet = []
		baseAttack = Attack()
		baseAttack.name = 'baseAttack'
		self.moveSet.append(baseAttack)

	def getBaseHP(self):
		return (5+self.x)*10

	def getARM(self):
		ARM = 0
		if self.weapon is not None:
			ARM += self.weapon.ARM
		if self.helmet is not None:
			ARM += self.helmet.ARM
		if self.armor is not None:
			ARM += self.armor.ARM
		if self.boots is not None:
			ARM += self.boots.ARM
		for item in self.inventory:
			if item.charges is None:
				ARM += item.ARM
		return ARM

	def getDMG(self):
		DMG = 5+self.y
		if self.weapon is not None:
			DMG += self.weapon.DMG
		if self.helmet is not None:
			DMG += self.helmet.DMG
		if self.armor is not None:
			DMG += self.armor.DMG
		if self.boots is not None:
			DMG += self.boots.DMG
		for item in self.inventory:
			if item.charges is None:
				DMG += item.DMG
		return DMG

	def getAG(self):
		AG = 5-self.x
		if self.weapon is not None:
			AG += self.weapon.AG
		if self.helmet is not None:
			AG += self.helmet.AG
		if self.armor is not None:
			AG += self.armor.AG
		if self.boots is not None:
			AG += self.boots.AG
		for item in self.inventory:
			if item.charges is None:
				AG += item.AG
		return AG

	def getED(self):
		ED = 5-self.y
		if self.weapon is not None:
			ED += self.weapon.ED
		if self.helmet is not None:
			ED += self.helmet.ED
		if self.armor is not None:
			ED += self.armor.ED
		if self.boots is not None:
			ED += self.boots.ED
		for item in self.inventory:
			if item.charges is None:
				ED += item.ED
		return ED


class Move():

	def __init__(self, charges :int=None, HPA: int=0, HPAScale: float=1.0, ARMA :int=0, ARMAScale :float=1.0, DMGA :int=0, DMGAScale :float=1.0, AGA :int=0, AGAScale :float=1.0, EDA :int=0, EDAScale :float=1.0, HPB: int=0, HPBScale :float=1.0, ARMB :int=0, ARMBScale :float=1.0, DMGB :int=0, DMGBScale :float=1.0, AGB :int=0, AGBScale :float=1.0, EDB :int=0, EDBScale :float=1.0):
		self.HPA  = HPA
		self.HPAScale  = HPAScale		
		self.ARMA = ARMA
		self.ARMAScale = ARMAScale
		self.DMGA = DMGA
		self.DMGAScale = DMGAScale
		self.AGA  = AGA
		self.AGAScale  = AGAScale
		self.EDA  = EDA
		self.EDAScale  = EDAScale
		self.HPB  = HPB
		self.HPBScale  = HPBScale
		self.ARMB = ARMB
		self.ARMBScale = ARMBScale
		self.DMGB = DMGB
		self.DMGBScale = DMGBScale
		self.AGB  = AGB
		self.AGBScale  = AGBScale
		self.EDB  = EDB
		self.EDBScale  = EDBScale
		self.charges = charges

	def justDoIt(self, a :Character, b :Character):
		pass


class Attack(Move):

	def justDoIt(self, a :Character, b :Character):
		if random.randrange(0,a.getAG()*self.AGAScale+self.AGA,1) > random.randrange(0,b.getAG()*self.AGBScale+self.AGB,1):
			print('attack hit')
			DMG = a.getDMG()*self.DMGAScale+self.DMGA - b.getARM()*self.ARMBScale+self.ARMB
			if DMG > 0:
				print('armor break')
				DMG = random.randrange(1, int(DMG),1)
				print(str(DMG) + ' DMG')
				b.HP -= DMG
				if b.HP <= 0:
					b.HP = 0
					print('target killed')
		else:
			print('attack miss')


class Item():

	def __init__(self, ARM :int, DMG :int, AG :int, ED :int, charges :int):
		self.ARM = ARM #armor
		self.DMG = DMG #damage
		self.AG  = AG  #agility
		self.ED  = ED  #endurance
		self.charges = charges


class Interaction():

	def __init__(self, a :Character, b :Character):
		self.a = a
		self.b = b


class Fight(Interaction):

	def __init__(self, a :Character, b :Character):
		super(Fight, self).__init__(a, b)
		self.current :Character = a
		self.target  :Character = b

	def nextRound(self, move :int):
		self.current.moveSet[move].justDoIt(self.current, self.target)
		if self.current is self.a:
			self.current = self.b
			self.target  = self.a
		else:
			self.current = self.a
			self.target  = self.b

class RPG():

	def getAssasin():
		x = Character(-4, 4)
		x.name = "Assasin"
		return x

	def getFechter():
		x = Character(-4, -4)
		x.name = "Fechter"
		return x

	def getKaempfer():
		x = Character(4, -4)
		x.name = "Kaempfer"
		return x

	def getFetteSau():
		x = Character(4, 4)
		x.name = "Fette Sau"
		return x
