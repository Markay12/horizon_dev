import pygame, sys
from settings import *
from level import Level

class Game: 
    ## Initialization setup
    def __init__( self ):

        # Initialize the game
        pygame.init()

        #  Set window name
        pygame.display.set_caption( "Homestead Horizons" )

        self.screen = pygame.display.set_mode ( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )
        self.clock  = pygame.time.Clock()

        # Level attribute for what level we are on
        self.level = Level()

    ## General Commands Used to Run the Game
    def run( self ):
        while True:
            for event in pygame.event.get():

                # Exit / Quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # delta time; get the change in time
            dt = self.clock.tick() / 1000
            self.level.run( dt )
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()