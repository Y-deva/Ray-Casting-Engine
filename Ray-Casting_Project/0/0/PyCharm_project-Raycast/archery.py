import SETTINGS
import pygame
import text_map
import random
from math import cos, sin


class NPC:
    def __init__(self, screen, x, y):
        self.x, self.y = x, y
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, SETTINGS.BLUE, (self.x, SETTINGS.WIDTH // 2, 10, 10))


class ART:
    def __init__(self, x, y, anchor):
        self.x, self.y = x, y  # x // SETTINGS.tile_size * SETTINGS.tile_size, y // SETTINGS.tile_size * SETTINGS.tile_size

        self.anchor = anchor

    def go(self):
        try:
            for i in range(0, int(SETTINGS.tile_size * 25 // SETTINGS.FPS), int(SETTINGS.tile_size * 25 // SETTINGS.FPS // 7)):
                self.x += cos(self.anchor) * 1 * int(SETTINGS.tile_size * 25 // SETTINGS.FPS // 7)
                self.y += sin(self.anchor) * 1 * int(SETTINGS.tile_size * 25 // SETTINGS.FPS // 7)

                if text_map.text_map[round(self.y / SETTINGS.tile_size)][round(self.x / SETTINGS.tile_size)] != ' ':
                    # print(0, text_map.text_map[round(self.y / SETTINGS.tile_size)][round(self.x / SETTINGS.tile_size)],
                    #       self.x // SETTINGS.tile_size, self.y // SETTINGS.tile_size, i)
                    art_list.pop(self)
                    del self
                    break
                elif self.x < 0 or self.y < 0:
                    art_list.pop(self)
                    del self
                    break
                else:
                    n = False
                    for j in range(0, SETTINGS.tile_size // 16):
                        if n:
                            break
                        for k in range(0, SETTINGS.tile_size // 16):
                            if (round(self.x + j) // SETTINGS.tile_size,
                                round(self.y + k) // SETTINGS.tile_size) in npc_list.keys():
                                del npc_list[(round(self.x + j) // SETTINGS.tile_size,
                                              round(self.y + k) // SETTINGS.tile_size)]
                                # npc_list.pop((round(self.x + j), round(self.y + k)))
                                n = True
                                break
                    if n:
                        art_list.pop(self)
                        del self
                        break
                    art_list[self] = (self.x, self.y)
        except IndexError:
            del self


npc_list = {}
art_list = {}


def npc_take(screen, txt_map, n_to_width):
    npc_list.clear()
    for i in range(1, n_to_width + 1):
        for j in range(1, n_to_width + 1):
            x, y = None, 0
            while x is None or txt_map[y][x] != ' ':
                x, y = random.randrange(i * (len(txt_map[0]) - 1) // n_to_width,
                                        (i - 1) * (len(txt_map[0]) - 1) // n_to_width, -1), \
                       random.randrange(j * (len(txt_map) - 1) // n_to_width,
                                        (j - 1) * (len(txt_map) - 1) // n_to_width, - 1)
            npc_list[(int(x), int(y))] = NPC(screen, x * SETTINGS.tile_size,
                                             y * SETTINGS.tile_size)

    return npc_list
