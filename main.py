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
    # background = load_background_image()
    # screen.blit(background, (0, 0))
    screen.fill((234, 212, 252))
    pygame.display.flip()
    
    # Timer / fps
    clock = pygame.time.Clock()

    # Entities
    player1 = Agent()
    player2 = Agent()
    field = Field("map.txt")
    tiles = field.get_tiles()
    
    scroll = {"x": 0, "y": 0, "offsetX": 0}

    # Game loop
    while True:
        # Get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                return
        keys = pygame.key.get_pressed()

        # Player 1 controls
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

        # Player 2 controls
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

        # Background
        screen.fill((234, 212, 252))
        # Update player position
        player1.update()
        player2.update()
        
        # Draw tiles
        for tile in tiles:
            tile.draw(screen, scroll)
        
        # Player collision
        x1, y1 = player1.get_location()
        x2, y2 = player2.get_location()
        # conditions = field.check_conditions(x1, y1)
        # if conditions == "Wall":
        #     pass
        # elif conditions == "Bomb":
        #     pass
        
        # s1: check bomb conditions
        field_tiles = field.get_field()
        i1 = int(y1/50)
        j1 = int(x1/50)
        i2 = int(y2/50)
        j2 = int(x2/50)
        try: 
            if field_tiles[i1][j1] == "+":
                player1.kill_life()
            if field_tiles[i2][j2] == "+":
                player2.kill_life()
        except: 
            pass 

        # s2: check collision in y
        # if field_tiles[i1][j1] == "x":
        #     pass
        # if field_tiles[i2][j2] == "x":
        #     pass
        
        # if field.check_conditions(x1, y1): 
        #     player1.kill_life()
        #     print("Player 1 is Colliding")
        # if field.check_conditions(x2, y2):
        #     player2.kill_life()
        #     print("Player 2 is Colliding")
        
        # Camera / Scrolling
        facing = player1.get_facing()
        if facing == "right" and scroll["offsetX"] > width/2 - 100:
            scroll["offsetX"] -= 3
        elif facing == "left" and scroll["offsetX"] < width/2 - 100:
            scroll["offsetX"] += 3
        scroll["x"] += int((x1 - scroll["x"] - scroll["offsetX"]) / 20)
        scroll["y"] += int((y1 - scroll["y"] - 300) / 20)

        # Draw players
        player1.draw(screen, scroll)
        player2.draw(screen, scroll)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
	main()
