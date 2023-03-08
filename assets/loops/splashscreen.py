"""
The window test is a game loop for testing development features coming to the custard class
"""
# - Modules necessary for testing operation
import os
import pygame
from assets import Pause, Developer

# - This loop is used for testing the responsiveness of the game window
def splashscreen(game):
    "This game loop stores tests for me to trial frame rate and other features"
    # - Create a variable for time keeping
    game.get_prev_time()
    developer_obj = Developer(game)
    pause_obj = Pause(game, [4, 4])

    # - Load splashscreen
    screen = pygame.image.load(os.path.join(game.path + 'screens/splashscreen.png')).convert()
    screen = pygame.transform.scale(screen, [game.width, game.height])

    while game.loop == 'splashscreen':
        # - Delta time clock
        game.delta_clock()

        # - Events are caught and processed here
        for event in pygame.event.get():
            game.events(event)
            developer_obj.events(event)
            pause_obj.events(event, game)

            if event.type == 768:
                game.loop = 'window test'



        # - Game logic is processed here
        developer_obj.update(game)
        pause_obj.update(game)



        # - Apply all normal pygame functions to the offscreen_surface
        game.surface.blit(screen, [0, 0])
        game.surface.fill([0, 0, 0])

        # - Draw the screen
        developer_obj.draw(game.surface)
        pause_obj.draw(game.surface)
        game.draw()
