import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Rule The Space!")
        self.clock = pygame.time.Clock()

        self.bg = pygame.image.load("images/space.png")
        self.bg = pygame.transform.scale(self.bg,(1200,800))

        self.rocket = pygame.image.load("images/rocket-1.png")
        self.rocket = pygame.transform.scale(self.rocket, (100,120))
        self.rocket_rect = self.rocket.get_rect(center=(100,600))

    def run(self):
        while True:
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.rocket, self.rocket_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and self.rocket_rect.right < 1200:
                self.rocket_rect.x += 3
            if keys[pygame.K_LEFT] and self.rocket_rect.left > 0:
                self.rocket_rect.x -= 3
            if keys[pygame.K_UP] and self.rocket_rect.top > 0:
                self.rocket_rect.y -= 3
            if keys[pygame.K_DOWN] and self.rocket_rect.bottom < 800:
                self.rocket_rect.y += 3

            pygame.display.update()
            self.clock.tick(60)

Game().run()