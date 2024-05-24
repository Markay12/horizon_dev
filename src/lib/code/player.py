import pygame
from settings import *
from support import *
from timer import Timer

## Class for the Player Sprite Image and Animations
class Player( pygame.sprite.Sprite ):

	## Init method
	## Parameters: self, pos, group
	def __init__( self, pos, group ):

		super().__init__( group )

		# Import player graphics
		self.import_assets()

		# Import attributes for player sprite image
		self.status = 'down_idle'
		self.frame_index = 0

		# General Setup of the Player space
		self.image = self.animations[ self.status ][ self.frame_index ]
		self.rect = self.image.get_rect( center = pos )
		self.z = LAYERS[ 'main' ]

		# movement attributes
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2( self.rect.center )
		self.speed = 200

		# Timers
		self.timers = {
			'use tool': Timer( 350, self.use_tool ),
			'switch tool': Timer( 200 ),
			'use seed': Timer( 350, self.use_seed ),
			'switch seed': Timer( 200 )
		}

		# Tools
		self.tools = [ 'hoe', 'axe', 'water' ]
		self.tool_index = 0
		self.selected_tool = self.tools[ self.tool_index ]

		# Seeds
		self.seeds = [ 'corn', 'tomato' ]
		self.seed_index = 0
		self.selected_seed = self.seeds[ self.seed_index ]

	# Use the selected tool, use cases include the water bucket, axe, etc...
	def use_tool( self ):
		pass

	def use_seed( self ):
		pass

	def input( self ):
		keys = pygame.key.get_pressed()

		# If we are not actively using some tool
		if not self.timers[ 'tool use' ].active:

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

			# Using a tool
			if keys[ pygame.K_SPACE ]:
				self.timers[ 'tool use' ].activate()
				self.direction = pygame.math.Vector2()
				self.frame_index = 0

	def import_assets( self ):

		# Different player animations as they move and perform actions dictionary
		self.animations = { 'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
						   'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
						   'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
						   'right_water':[],'left_water':[],'up_water':[],'down_water':[] }

		# Which graphics to pull when the player is moving in different directions
		for animation in self.animations.keys():
			full_path = '../graphics/character/' + animation
			self.animations[ animation ] = import_folder( full_path )

	def animate( self, dt ):
	
		# Speed of animation
		self.frame_index += 4 * dt

		if self.frame_index >= len( self.animations[ self.status ] ):
			self.frame_index = 0

			self.image = self.animations[ self.status ][ int( self.frame_index ) ]

	def input( self ):
		keys = pygame.key.get_pressed()

		if not self.timers[ 'use tool' ].active:

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

			# Tool Use
			if keys[ pygame.K_SPACE ]:
				self.timers[ 'use tool' ].activate()
				self.direction = pygame.math.Vector2()
				self.frame_index = 0

			# Change the Tool
			if keys[ pygame.K_q ] and not self.timers[ 'switch tool' ].active:
				self.timers[ 'switch tool' ].activate()
				self.tool_index += 1

				# Protection at the end of the tools 
				self.tool_index = self.tool_index if self.tool_index < len( self.tools ) else 0
				self.selected_tool = self.tools[ self.tool_index ]

			# Use the Seeds
			if keys[ pygame.K_LCTRL ]:
				self.timers[ 'use seed' ].activate()
				self.direction = pygame.math.Vector2()
				self.frame_index = 0

			# Change the seed
			if keys[ pygame.K_e ] and not self.timers[ 'switch seed' ].active:
				self.timers[ 'switch seed' ].activate()
				self.seed_index += 1

				# protection at the end of the list of seeds
				self.seed_index = self.seed_index if self.seed_index < len( self.seeds ) else 0
				self.selected_seed = self.seeds[ self.seed_index ]


	def get_status( self ):
		
		# idle
		if self.direction.magnitude() == 0:
			self.status = self.status.split( '_' )[ 0 ] + '_idle'

		# tool use
		if self.timers[ 'use tool' ].active:
			self.status = self.status.split('_')[0] + '_' + self.selected_tool

	def update_timers( self ):
		for timer in self.timers.values():
			timer.update()

	def move ( self, dt ):

		# Vector Normalization
		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()

		# Moving on the X-Axis
		self.pos.x += self.direction.x * self.speed * dt
		self.rect.centerx = self.pos.x

		# Moving on the Y-Axis
		self.pos.y += self.direction.y * self.speed * dt
		self.rect.centery = self.pos.y

	def update( self, dt ):
		self.input()
		self.get_status()
		self.update_timers()

		self.move( dt )
		self.animate( dt )
