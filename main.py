from tkinter import W
import pygame
from Agent import Agent
from Field import Field 

width = 640
height = 480

SCREENRECT = pygame.Rect(0, 0, width, height)

def main():
    # Initialize pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print('Warning, no sound')
        pygame.mixer = None

    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # Screen setup
    pygame.display.set_caption('Celesta')
    # pygame.mouse.set_visible(0)
    # player = load_player_image()
    # background = load_background_image()
    # screen.blit(background, (0, 0))
    screen.fill((234, 212, 252))
    pygame.display.flip()
    
    # Timer / fps
    clock = pygame.time.Clock()
    player1 = Agent()
    player2 = Agent()
    field = Field("map.txt")
    tiles = field.get_field()
    
    scroll = {"x": 0, "y": 0}
    while True:
        # Get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                return
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            player1.move(key="jump")
        if keys[pygame.K_s]:
            player1.move(key="down")
        if keys[pygame.K_a]:
            player1.move(key="left")
        if keys[pygame.K_d]:
            player1.move(key="right")
        if keys[pygame.K_t]:
            player1.move(key="dash")

        if keys[pygame.K_RSHIFT]:
            player2.move(key="jump")
        if keys[pygame.K_DOWN]:
            player2.move(key="down")
        if keys[pygame.K_LEFT]:
            player2.move(key="left")
        if keys[pygame.K_RIGHT]:
            player2.move(key="right")
        if keys[pygame.K_RCTRL]:
            player2.move(key="dash")

        # screen.blit(background, position, position) #erase
        screen.fill((234, 212, 252))

        player1.update()
        player2.update()

        for tile in tiles:
            tile.draw(screen, scroll)
        
        x1, y1 = player1.get_location()
        x2, y2 = player2.get_location()
        
        if field.is_colliding(x1, y1): 
            player1.kill_life()
            print("Player 1 is Colliding")
        if field.is_colliding(x2, y2):
            player2.kill_life()
            print("Player 2 is Colliding")
        
        # Scrolling
        facing = player1.get_facing()
        scroll["x"] = int(x1)
        scroll["y"] = int(-y1)

        player1.draw(screen, scroll)
        player2.draw(screen, scroll)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
	main()
