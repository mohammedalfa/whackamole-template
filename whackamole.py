import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x = 0
        y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_pos = event.pos
                    if x < click_pos[0] < x + 32 and y < click_pos[1] < y + 32:
                        x = random.randrange(0, 20) * 32
                        y = random.randrange(0, 16) * 32
            screen.fill("light green")
            for i in range(1, 20):
                pygame.draw.line(screen, 0, (32 * i, 0), (32 * i, 512))
            for i in range (1, 16):
                pygame.draw.line(screen, 0, (0, 32 * i), (640, 32 * i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
