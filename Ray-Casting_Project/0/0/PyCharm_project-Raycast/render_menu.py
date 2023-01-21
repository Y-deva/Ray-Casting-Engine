import SETTINGS
import pygame
import text_map
from math import pi


class Menu:
    def __init__(self, true_screen, screen):
        self.w, self.h = SETTINGS.menu_size
        self.screen = screen
        self.sc = true_screen

    def draw_menu(self, is_open=False, mus=True, map_hide=False):
        if is_open:
            self.sc.fill(SETTINGS.DARKGRAY)
            for i in range(0, len(text_map.files)):
                font = pygame.font.Font(None, 24)
                text = font.render(text_map.files[i], True, (100, 255, 100))
                self.sc.blit(text, (10, 15 + self.h + i * SETTINGS.WIDTH // 20))
            pygame.draw.rect(self.sc, SETTINGS.LIGHTGRAY, (5, 12 + self.h + text_map.n * SETTINGS.WIDTH // 20,
                                                           SETTINGS.WIDTH - 10, SETTINGS.WIDTH // 30), 3)
            self.screen.fill(SETTINGS.GRAY)
            for i in range(3):
                pygame.draw.line(self.screen, SETTINGS.BLACK, (7, self.h // 4 * (i + 1)),
                                 (self.w - 7, self.h // 4 * (i + 1)), width=self.h // 20)
            self.sc.blit(self.screen, (3, 15))

            pygame.draw.rect(self.sc, SETTINGS.GREEN, (3 * SETTINGS.WIDTH // 40, 15,
                                                       SETTINGS.WIDTH // 24, SETTINGS.WIDTH // 24))
            pygame.draw.polygon(self.sc, SETTINGS.DARKGREEN, ((7 * SETTINGS.WIDTH // 96,
                                                               15 + SETTINGS.WIDTH // 48), (9 * SETTINGS.WIDTH // 96,
                                                               15 + SETTINGS.WIDTH // 320), (9 * SETTINGS.WIDTH // 96,
                                                               15 + SETTINGS.WIDTH // 24 - SETTINGS.WIDTH // 320)))
            if mus:
                pygame.draw.arc(self.sc, SETTINGS.DARKGREEN, (10 * SETTINGS.WIDTH // 96, 20,
                                                              SETTINGS.WIDTH // 96, SETTINGS.WIDTH // 24 - 10),
                                6 * pi / 5, 4 * pi / 5)
            pygame.draw.rect(self.sc, SETTINGS.BROWN, (4 * SETTINGS.WIDTH // 40 + SETTINGS.WIDTH // 24, 15,
                                                       SETTINGS.WIDTH // 24, SETTINGS.WIDTH // 24))
            if not map_hide:
                pygame.draw.lines(self.sc, SETTINGS.LIGHTGRAY, False, ((4 * SETTINGS.WIDTH // 40
                                                                       + SETTINGS.WIDTH // 24 + 10,
                                                                       SETTINGS.WIDTH // 24 + 5),
                                                                       (4 * SETTINGS.WIDTH // 40
                                                                       + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 36,
                                                                        SETTINGS.WIDTH // 48 + 15),
                                                                       (4 * SETTINGS.WIDTH // 40
                                                                       + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 48
                                                                        - 10, 25), (4 * SETTINGS.WIDTH // 40
                                                                       + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 24
                                                                       - 10, 20)), 3)
                pygame.draw.line(self.sc, SETTINGS.RED, (4 * SETTINGS.WIDTH // 40
                                                         + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 24
                                                         - 12, 17), (4 * SETTINGS.WIDTH // 40
                                                                     + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 24
                                                                     - 12 + SETTINGS.WIDTH // 156,
                                                                     17 + SETTINGS.WIDTH // 156), 3)
                pygame.draw.line(self.sc, SETTINGS.RED, (4 * SETTINGS.WIDTH // 40
                                                         + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 24
                                                         - 12, 17 + SETTINGS.WIDTH // 156),
                                                        (4 * SETTINGS.WIDTH // 40
                                                         + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 24
                                                         - 12 + SETTINGS.WIDTH // 156,
                                                         17), 3)
            pygame.draw.rect(self.sc, SETTINGS.DARKGREEN, (5 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24, 15,
                                                           SETTINGS.WIDTH // 24 * 5, SETTINGS.WIDTH // 24))
            font = pygame.font.Font(None, 24)
            text = font.render('GENERATE MAP 40x40', True, (100, 255, 100))
            self.sc.blit(text, (5 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24 + 10, 15 + SETTINGS.WIDTH // 60))
            font = pygame.font.Font(None, 24)
            text = font.render('map --> generate_map.txt', True, (100, 100, 100))
            self.sc.blit(text, (5 * SETTINGS.WIDTH // 40 + 7 * SETTINGS.WIDTH // 24 + 10, 15 + SETTINGS.WIDTH // 60))
            pygame.draw.rect(self.sc, SETTINGS.RED, (SETTINGS.WIDTH - SETTINGS.WIDTH // 20 - 10, 15,
                                                     SETTINGS.WIDTH // 24, SETTINGS.WIDTH // 24))
            pygame.draw.line(self.sc, SETTINGS.DARKRED, (SETTINGS.WIDTH - SETTINGS.WIDTH // 20 - 5, 20),
                             (SETTINGS.WIDTH - SETTINGS.WIDTH // 20 - 15 + SETTINGS.WIDTH // 24,
                              SETTINGS.WIDTH // 24 + 10), width=3)
            pygame.draw.line(self.sc, SETTINGS.DARKRED, (SETTINGS.WIDTH - SETTINGS.WIDTH // 20 - 5,
                                                         SETTINGS.WIDTH // 24 + 10),
                             (SETTINGS.WIDTH - SETTINGS.WIDTH // 20 - 15 + SETTINGS.WIDTH // 24,
                              20), width=3)
            pygame.draw.rect(self.sc, SETTINGS.DGRAY, (6 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                                                       + 9 * SETTINGS.WIDTH // 24, 15, SETTINGS.WIDTH // 24,
                                                       SETTINGS.WIDTH // 24))
            pygame.draw.line(self.sc, SETTINGS.LIGHTGREEN, (6 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                                                            + 9 * SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 36, 15),
                             (6 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                              + 9 * SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 36, 15 + SETTINGS.WIDTH // 60), width=4)
            pygame.draw.line(self.sc, SETTINGS.LIGHTGREEN, (6 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                                                            + 9 * SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 36
                                                            - SETTINGS.WIDTH // 120, 15
                                                            + SETTINGS.WIDTH // 24 - SETTINGS.WIDTH // 36 - 8),
                             (6 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                              + 9 * SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 36 + SETTINGS.WIDTH // 120,
                              15 + SETTINGS.WIDTH // 24 - SETTINGS.WIDTH // 36 - 8), width=4)
            pygame.draw.rect(self.sc, SETTINGS.LIGHTGRAY, (6 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                                                           + 9 * SETTINGS.WIDTH // 24 + 2, 17, SETTINGS.WIDTH // 36 - 4,
                                                           SETTINGS.WIDTH // 36 - 4))

            pass
            pygame.draw.rect(self.sc, SETTINGS.DGRAY, (7 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                                                       + 10 * SETTINGS.WIDTH // 24, 15, SETTINGS.WIDTH // 24,
                                                       SETTINGS.WIDTH // 24))
            pygame.draw.line(self.sc, SETTINGS.LIGHTGREEN, (7 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                                                            + 10 * SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 36, 15),
                             (7 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                              + 10 * SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 36, 15 + SETTINGS.WIDTH // 60), width=4)
            pygame.draw.line(self.sc, SETTINGS.LIGHTGREEN, (7 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                                                            + 10 * SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 36
                                                            - SETTINGS.WIDTH // 120, 15
                                                            + SETTINGS.WIDTH // 24 - SETTINGS.WIDTH // 36 - 8),
                             (7 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                              + 10 * SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 36 + SETTINGS.WIDTH // 120,
                              15 + SETTINGS.WIDTH // 24 - SETTINGS.WIDTH // 36 - 8), width=4)
        else:
            self.screen.fill(SETTINGS.GRAY)
            for i in range(3):
                pygame.draw.line(self.screen, SETTINGS.BLACK, (7, self.h // 4 * (i + 1)),
                                 (self.w - 7, self.h // 4 * (i + 1)), width=self.h//20)
            self.sc.blit(self.screen, (3, 15))
