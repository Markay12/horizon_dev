import pygame, sys
from settings import *

class Game: 
    def __init__( self ):

        # Initialize the game
        pygame.init()

        #  Set window name
        pygame.display.set_caption( "Homestead Horizons" )

        self.screen = pygame.display.set_mode ( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )
        self.clock  = pygame.time.Clock()

    # Where most of the game is run 
    def run( self ):
        while True:
            for event in pygame.event.get():

                # Exit / Quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # datetime; get the time
            dt = self.clock.tick() / 1000
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()