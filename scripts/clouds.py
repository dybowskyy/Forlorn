import random
import datetime as dt

class Cloud:
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth


    def update(self):
        self.pos[0] += self.speed

    def render(self, surf, offset=(0, 0)):
        render_pos = (self.pos[0]- offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)

        adjusted_x = (render_pos[0] + self.img.get_width()) % (surf.get_width() + self.img.get_width()) - self.img.get_width()
        adjusted_y = render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()

        surf.blit(self.img, (adjusted_x, adjusted_y))


class Clouds:
    def __init__(self, cloud_images, count=16, surf=None):
        self.clouds = []

        for i in range(count):
            self.clouds.append(Cloud(
                (random.random() * 9999,
                 random.random() * 9999),
                 random.choice(cloud_images),
                 random.random() * 0.1 + 0.02,
                 random.random() * 0.3 + 0.7,
            ))

        self.clouds.sort(key=lambda cloud_object: cloud_object.depth)

    def update(self):
        for cloud in self.clouds:
            cloud.update()

    def render(self, surf, offset=(0, 0)):
        for cloud in self.clouds:
            cloud.render(surf, offset)