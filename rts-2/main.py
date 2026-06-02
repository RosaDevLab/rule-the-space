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

        self.rock = pygame.image.load("images/rock-1.png")
        self.rock = pygame.transform.scale(self.rock, (200,200))
        self.rock_rect = self.rock.get_rect(center = (400,-200))
        self.rock_rect_2 = self.rock.get_rect(center = (800,-400))

        self.energy = pygame.image.load("images/energy_blue.png")
        self.energy = pygame.transform.scale(self.energy, (100,100))
        self.energy_rect = self.energy.get_rect(center = (600, -300))


    def run(self):
        while True:
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.rocket, self.rocket_rect)
            self.screen.blit(self.rock, self.rock_rect)
            self.screen.blit(self.rock, self.rock_rect_2)
            self.screen.blit(self.energy, self.energy_rect)

            self.rock_rect.y += 4
            if self.rock_rect.y > 900:
                self.rock_rect.y = -200

            self.rock_rect_2.y += 2
            if self.rock_rect_2.y > 900:
                self.rock_rect_2.y = -400

            self.energy_rect.y += 3
            if self.energy_rect.y > 900:
                self.energy_rect.y = -300

            if self.rocket_rect.colliderect(self.energy_rect):
                print("you gained 1 point!")
                self.energy_rect.y = -300

            if self.rocket_rect.colliderect(self.rock_rect) or self.rocket_rect.colliderect(self.rock_rect_2):
                print("you lost!")
                pygame.quit()
                sys.exit()


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