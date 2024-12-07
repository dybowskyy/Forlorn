import pygame
import sys

class Game:
    def __init__(self):
        self.image_r = None
        pygame.init()
        pygame.display.set_caption("Forlorn")
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.image = pygame.image.load("data/images/entities/player.png")
        self.image.set_colorkey((0, 0, 0))
        self.image_pos = [160, 260]
        self.movement = [False, False, False, False]

        self.collision_area = pygame.Rect(50, 50, 540, 50)

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            self.image_r = pygame.Rect(*self.image_pos, *self.image.get_size())

            if self.image_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 255, 0), self.collision_area)
                #self.movement = [False, False, False, False]
            else:
                pygame.draw.rect(self.screen, (255, 0, 0), self.collision_area)

            self.image_pos[1] += (self.movement[1] - self.movement[0]) * 3
            self.image_pos[0] += (self.movement[2] - self.movement[3]) * 3
            self.screen.blit(self.image, self.image_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                    key_state = event.type == pygame.KEYDOWN
                    key_map = {pygame.K_UP: 0, pygame.K_DOWN: 1, pygame.K_RIGHT: 2, pygame.K_LEFT: 3}
                    if event.key in key_map:
                        self.movement[key_map[event.key]] = key_state
            pygame.display.update()
            self.clock.tick(60)


Game().run()