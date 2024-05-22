import pygame
from settings import *
from support import *

class Player( pygame.sprite.Sprite ):
	def __init__( self, pos, group ):

		super().__init__(group)

		# Import player graphics
		self.import_assets()

		# Import attributes for player sprite image
		self.status = 'left_axe'
		self.frame_index = 0

		# General Setup of the Player space
		self.image = self.animations[ self.status ][ self.frame_index ]
		self.rect = self.image.get_rect( center = pos )

		# movement attributes
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2( self.rect.center )
		self.speed = 200

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[ pygame.K_UP ]:
			self.direction.y = -1
		elif keys[ pygame.K_DOWN ]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[ pygame.K_RIGHT ]:
			self.direction.x = 1
		elif keys[ pygame.K_LEFT ]:
			self.direction.x = -1
		else:
			self.direction.x = 0

	def import_assets( self ):
		self.animations = {'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
						   'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
						   'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
						   'right_water':[],'left_water':[],'up_water':[],'down_water':[]}

		for animation in self.animations.keys():
			full_path = '../graphics/character/' + animation
			self.animations[animation] = import_folder(full_path)

	def animate( self, dt ):
	
		# Speed of animation
		self.frame_index += 4 * dt

		if self.frame_index >= len( self.animations[ self.status ] ):
			self.frame_index = 0

			self.image = self.animations[ self.status ][ int( self.frame_index ) ]

	def input( self ):
		keys = pygame.key.get_pressed()

		if keys[ pygame.K_UP ]:
			self.direction.y = -1
			self.status = 'up'
		elif keys[ pygame.K_DOWN ]:
			self.direction.y = 1
			self.status = 'down'
		else:
			self.direction.y = 0

		if keys[ pygame.K_RIGHT ]:
			self.direction.x = 1
			self.status = 'right'

		elif keys[ pygame.K_LEFT ]:
			self.direction.x = -1
			self.status = 'left'
		else:
			self.direction.x = 0

	def get_status( self ):
		
		# idle
		if self.direction.magnitude() == 0:
			self.status = self.status.split( '_' )[ 0 ] + '_idle'

		# tool use

	def move (self, dt ):

		# normalizing a vector 
		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()

		# horizontal movement
		self.pos.x += self.direction.x * self.speed * dt
		self.rect.centerx = self.pos.x

		# vertical movement
		self.pos.y += self.direction.y * self.speed * dt
		self.rect.centery = self.pos.y

	def update( self, dt ):
		self.input()
		self.get_status()

		self.move(dt)
		self.animate( dt )
		self.input()
		self.move( dt )
