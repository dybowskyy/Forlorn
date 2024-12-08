import pygame

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}

class Tilemap():
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(20):
            self.tilemap[str(i) + ';13'] = {'type': 'grass', 'variant': 1, 'pos': (i, 13)}
            self.tilemap[str(i) + ';14'] = {'type': 'stone', 'variant': 1, 'pos': (i, 14)}
        for i in range(5):
            self.tilemap['12;' + str(i + 11)] = {'type': 'stone', 'variant': 1, 'pos': (12, i + 11)}
            self.tilemap['14;' + str(i + 10)] = {'type': 'stone', 'variant': 1, 'pos': (14, i + 10)}
            self.tilemap['16;' + str(i + 9)] = {'type': 'stone', 'variant': 1, 'pos': (16, i + 9)}
            self.tilemap['18;' + str(i + 8)] = {'type': 'stone', 'variant': 1, 'pos': (18, i + 8)}


    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    def physics_recs_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects


    def render(self, surf, offset=(0, 0)):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))

        for location in self.tilemap:
            tile = self.tilemap[location]
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))


