import pygame 
from settings import *
from player import Player

class Level:
	def __init__( self ):

		# Get the Display Surface
		self.display_surface = pygame.display.get_surface()

		# Sprite Groups
		self.all_sprites = pygame.sprite.Group()

        # Setup the player and the level
		self.setup()

	def setup(self):
		# Player sprite setup
		self.player = Player( ( 640,360 ), self.all_sprites )

	def run( self, dt ):
		#  Run with relation to delta time and setup for the level
		self.display_surface.fill( 'black' )
		self.all_sprites.draw( self.display_surface )
		self.all_sprites.update( dt )