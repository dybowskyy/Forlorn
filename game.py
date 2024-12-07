import pygame
import sys

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        self.image_r = None
        pygame.init()
        pygame.display.set_caption("Forlorn")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False, False, False]
        # TODO: Optimize self.assets loading.
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        self.tilemap = Tilemap(self)

    def run(self):
        while True:
            self.display.fill((14, 219, 248))
            self.tilemap.render(self.display)

            self.player.update(self.tilemap, (self.movement[2] - self.movement[3], self.movement[1] - self.movement[0]))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                    key_state = event.type == pygame.KEYDOWN
                    key_map = {pygame.K_UP: 0, pygame.K_DOWN: 1, pygame.K_RIGHT: 2, pygame.K_LEFT: 3}
                    if event.key in key_map:
                        self.movement[key_map[event.key]] = key_state
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -2

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()