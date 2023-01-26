if __name__ == '__main__':
    map1 = map
    import multiprocessing
    from multiprocessing import Pool

    multiprocessing.freeze_support()
    import pygame
    import tkinter as tk
    import sys
    import os
    import map
    import SETTINGS
    import player
    import raycast_mp
    import render
    import npc
    import render_menu, text_map
    import df_maze
    from df_maze import Maze

    # start new code
    import archery
    import archery_map
    from archery_map import Loading
    import random
    import tkinter.filedialog
    import main2
    # from PyQt5.QtWidgets import QApplication, QFileDialog
    # end new code


    def prompt_file():
        """Create a Tk file dialog and cleanup when finished"""
        top = tk.Tk()
        top.withdraw()  # hide window
        file_name = tkinter.filedialog.askopenfilename(parent=top)
        top.destroy()
        return file_name


    if __name__ == '__main__':
        # app = QApplication(sys.argv)
        pygame.init()

        # sys.exit(app.exec())

        sc = pygame.display.set_mode(SETTINGS.SIZE)
        f = pygame.font.Font(None, 20)

        running = True
        txt = '''
         левый Ctrl - проявление курсора
         W
        A D - управление, движение мышкой - изменение направления
         S
         insert - выход
         esc - свертывание экрана
         tab - выстрел
         нажмите tab для продолжения'''
        n = 0
        for i in txt.split('\n'):
            txt = f.render(i, True, (0, 255, 255))
            sc.blit(txt, (10, 25 + 20 * n))
            n += 1
        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        running = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.display.iconify()
                    elif event.key == pygame.K_INSERT:
                        pygame.quit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
        sc.fill('black')
        load = Loading(sc, '../../load.gif')
        # pygame.display.flip()
        tk1 = tk.Tk()

        os.environ['SDL_VIDEO_WINDOW_POS'] = f'{(tk1.winfo_screenwidth() - SETTINGS.WIDTH) // 2},' \
                                             f'{(tk1.winfo_screenheight() - SETTINGS.HEIGHT) // 4}'

        tk1.destroy()
        del tk1

        # pygame.init()

        pygame.mixer.music.load('lo-fi1.mp3')
        pygame.mixer.music.play(-1)
        mus = True
        map_hide = 0
        pygame.display.set_caption('Ray casting')

        # sc = pygame.display.set_mode(SETTINGS.SIZE)
        sc_map = pygame.Surface(SETTINGS.map_size)
        sc_menu = pygame.Surface(SETTINGS.menu_size)

        clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)

        map = map.Map()
        render = render.Render(sc, sc_map)
        rend = render_menu.Menu(sc, sc_menu)

        player = player.Player(npc, clock, map.flat_map)
        ray_cast = raycast_mp.RayCast(map.map)  # , sc, render)
        code = 0
        is_open = False
        archery.npc_take(sc, text_map.text_map, 2)
        x, y = 0, 0
        for s in text_map.text_map:
            if x == -1:
                break
            x = 0
            for p in s:
                if p == 'N':
                    archery.npc_list[(x, y)] = archery.NPC(sc, x * SETTINGS.tile_size,
                                                           y * SETTINGS.tile_size)
                x += 1
            y += 1
        archer = 0
        # pygame.draw.rect(sc, SETTINGS.LIGHTGRAY, (0, 0, 50, 50))
        # im = pygame.image.load('../../image2.admin.png')
        # sc.blit(im, (0, 0))
        # pygame.display.flip()

        with Pool(processes=4) as pool:
            game = True

            while game:
                for event in pygame.event.get():
                    if is_open:
                        pygame.mouse.set_visible(True)
                    else:
                        if code == 0:
                            pygame.mouse.set_visible(False)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.display.iconify()
                        elif event.key == pygame.K_INSERT:
                            game = False

                        elif event.key == pygame.K_LCTRL:
                            code = 1
                            pygame.mouse.set_visible(True)
                        elif event.key == pygame.K_TAB:
                            archery.art_list[archery.ART(player.real_x, player.real_y, player.angle)] = \
                                (player.real_x,
                                 player.real_y)
                            archer = 1
                        elif event.key == pygame.K_9:
                            print(*list(map1(lambda x: (x.x, x.y), archery.art_list)))
                            print(archery.npc_list)
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LCTRL:
                            code = 0
                            pygame.mouse.set_visible(False)
                    elif event.type == pygame.MOUSEBUTTONDOWN:


                        def _1(a, b, c):
                            return a[0] < b[0] < c[0] and a[1] < b[1] < c[1]

                        b = is_open

                        if _1((0, 0), event.pos, (SETTINGS.WIDTH // 20, 15 + SETTINGS.WIDTH // 20)):
                            is_open = not is_open
                        elif not is_open:
                            pass

                        elif _1((3 * SETTINGS.WIDTH // 40, 0),
                                event.pos, (3 * SETTINGS.WIDTH // 40 + SETTINGS.WIDTH // 24, 15 + SETTINGS.WIDTH // 24)):
                            if mus:
                                pygame.mixer.music.stop()
                            else:
                                pygame.mixer.music.play(-1)
                            mus = not mus
                        elif _1((4 * SETTINGS.WIDTH // 40 + SETTINGS.WIDTH // 24, 0),
                                event.pos, (4 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24, 15 + SETTINGS.WIDTH // 24)):
                            map_hide += 1
                            map_hide %= 3
                            render.sc_map.fill(SETTINGS.BLACK)
                        elif 15 + SETTINGS.WIDTH // 24 < event.pos[1] < 15 + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 20:
                            text_map.n = 0
                        elif 15 + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 20 \
                                < event.pos[1] < 15 + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 20 * 2:
                            text_map.n = 1
                        elif 15 + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 20 * 2 \
                                < event.pos[1] < 15 + SETTINGS.WIDTH // 24 + SETTINGS.WIDTH // 20 * 3:
                            text_map.n = 2
                        elif _1((SETTINGS.WIDTH - SETTINGS.WIDTH // 20 - 10, 15), event.pos,
                                (SETTINGS.WIDTH - SETTINGS.WIDTH // 20 - 10 + SETTINGS.WIDTH // 24,
                                 15 + SETTINGS.WIDTH // 24)):
                            game = False
                        elif _1((6 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24 + 9 * SETTINGS.WIDTH // 24, 15),
                                event.pos,
                                (6 * SETTINGS.WIDTH // 40 + 12 * SETTINGS.WIDTH // 24, 15 + SETTINGS.WIDTH // 24)):
                            f = prompt_file()
                            if f != '':
                                main2.return_sheet(f, 'player_map.txt', step=2,
                                                   wall=random.choice(list('12345678P')),
                                                   floor=' ', sep='')
                                if 'player_map.txt' not in text_map.files:
                                    text_map.files.append('player_map.txt')
                                with open('player_map.txt', 'r') as file:
                                    x, y = 0, 0
                                    for s in file.readlines():
                                        if x == -1:
                                            break
                                        x = 0
                                        for p in s:
                                            if p == 'P':
                                                text_map.pos.append((x, y))
                                                x = -1
                                                break
                                            x += 1
                                        y += 1
                                if x != -1:
                                    with open('player_map.txt', 'r') as file:
                                        x, y = 0, 0
                                        for s in file.readlines():
                                            if x == -1:
                                                break
                                            x = 0
                                            for p in s:
                                                if p == ' ':
                                                    text_map.pos.append((x, y))
                                                    x = -1
                                                    break
                                                x += 1
                                            y += 1

                        elif _1((7 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                                 + 10 * SETTINGS.WIDTH // 24, 15), event.pos,
                                (7 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24
                                 + 11 * SETTINGS.WIDTH // 24,
                                 15 + SETTINGS.WIDTH // 24)):
                            # file = open(QFileDialog.getOpenFileName()[0])
                            file1 = prompt_file()
                            if file1 != '':
                                text_map.files.append(file1)
                                with open(file1, 'r') as file:
                                    x, y = 0, 0
                                    for s in file.readlines():
                                        if x == -1:
                                            break
                                        x = 0
                                        for p in s:
                                            if p == 'P':
                                                text_map.pos.append((x, y))
                                                x = -1
                                                break
                                            x += 1
                                        y += 1
                                if x != -1:
                                    with open(file1, 'r') as file:
                                        x, y = 0, 0
                                        for s in file.readlines():
                                            if x == -1:
                                                break
                                            x = 0
                                            for p in s:
                                                if p == ' ':
                                                    text_map.pos.append((x, y))
                                                    x = -1
                                                    break
                                                x += 1
                                            y += 1
                            # file.close()
                            # file_selection = UIFileDialog(rect=Rect(0, 0, 300, 300), manager=manager,
                            #                               initial_file_path='C:\\')
                            # if event.ui_element == file_selection.ok_button:
                            #     file_path = file_selection.current_file_path
                        elif _1((5 * SETTINGS.WIDTH // 40 + 2 * SETTINGS.WIDTH // 24, 15), event.pos,
                                (5 * SETTINGS.WIDTH // 40 + 7 * SETTINGS.WIDTH // 24, 15 + SETTINGS.WIDTH // 24)):
                            Maze1 = Maze(40, 40, 0, 0)
                            file = open('generate_map.txt', 'w')
                            Maze1.make_maze()
                            maz = str(Maze1)
                            w = random.choice(list('12345678P'))
                            for i in maz.split('\n'):
                                s = ''
                                for j in i:
                                    if j == ' ':
                                        s += j
                                    else:
                                        s += w
                                # print(s)
                                print(s, file=file)
                            file.close()
                            if 'generate_map.txt' not in text_map.files:
                                text_map.files.append('generate_map.txt')
                                text_map.pos.append((1, 1))
                        else:
                            if (event.pos[1] - 15 - SETTINGS.WIDTH // 24) // (SETTINGS.WIDTH // 20) >= 0:
                                text_map.n = (event.pos[1] - 15 - SETTINGS.WIDTH // 24) // (SETTINGS.WIDTH // 20)
                        if b and not is_open:
                            # print(open(text_map.files[text_map.n]))
                            if text_map.n != n1:
                                text_map.text_map = list(map1(lambda x: x.strip('\n'),
                                                              open(text_map.files[text_map.n]).readlines()))
                                text_map.start = text_map.pos[text_map.n]
                                # tryi = ['map.text_map', 'player.flat_map', 'ray_cast.map']
                                # els = map.text_map, player.flat_map, ray_cast.map
                                SETTINGS.re_map()
                                map.text_map = SETTINGS.text_map
                                map.map_of_tiles, map.map, map.flat_map = map.create_map()
                                sc_map.fill(SETTINGS.BLACK)
                                sc_map = pygame.Surface(SETTINGS.map_size)
                                render.sc_map = sc_map
                                render.sc_map.fill(SETTINGS.BLACK)
                                player.flat_map = map.flat_map
                                player.real_x, player.real_y = SETTINGS.player_pos
                                ray_cast.map = map.map
                                ray_cast.map_rows, ray_cast.map_cols = SETTINGS.map_rows, SETTINGS.map_cols
                                # print(text_map.text_map, text_map.start)
                                archery.npc_take(sc, text_map.text_map, 2)
                                x, y = 0, 0
                                for s in text_map.text_map:
                                    if x == -1:
                                        break
                                    x = 0
                                    for p in s:
                                        if p == 'N':
                                            archery.npc_list[(x, y)] = archery.NPC(sc, x * SETTINGS.tile_size,
                                                                                   y * SETTINGS.tile_size)
                                        x += 1
                                    y += 1
                                # print('trying', 'els')
                                # for i in tryi:
                                #     print(i, eval(f'{i}') == els[tryi.index(i)])
                                # print()
                        elif not b and is_open:
                            n1 = text_map.n
                if code != 1 and not is_open:
                    player.movement()
                load.stop()
                sc.fill(SETTINGS.GREEN2)

                render.draw_background(player.angle_inf, player.real_x, player.real_y)
                a = list(map1(lambda x: (round(x[0] / SETTINGS.tile_size), round(x[1] / SETTINGS.tile_size)), archery.art_list.values()))

                res_1 = pool.apply_async(ray_cast.raycasting, (list(archery.npc_list.keys()), a,
                                                               player.angle, player.real_x, player.real_y, 0))
                res_2 = pool.apply_async(ray_cast.raycasting, (list(archery.npc_list.keys()), a,
                                                               player.angle, player.real_x, player.real_y, 1))
                res_3 = pool.apply_async(ray_cast.raycasting, (list(archery.npc_list.keys()), a,
                                                               player.angle, player.real_x, player.real_y, 2))
                res_4 = pool.apply_async(ray_cast.raycasting, (list(archery.npc_list.keys()), a,
                                                               player.angle, player.real_x, player.real_y, 3))

                walls_1, floor_1 = res_1.get()
                walls_2, floor_2 = res_2.get()
                walls_3, floor_3 = res_3.get()
                walls_4, floor_4 = res_4.get()

                walls_1.update(walls_2); floor_1.update(floor_2)
                walls_1.update(walls_3); floor_1.update(floor_3)
                walls_1.update(walls_4); floor_1.update(floor_4)

                render.draw_world(walls_1, floor_1)

                render.draw_map(map.map_of_tiles, player.real_x, player.real_y, player.sin_a, player.cos_a, map_hide)
                render.display_fps(clock)
                rend.draw_menu(is_open=is_open, mus=mus, map_hide=map_hide)
                if round(archer):
                    pygame.draw.rect(sc, SETTINGS.DGRAY, (2 * SETTINGS.WIDTH // 3, 5.5 * SETTINGS.HEIGHT // 7,
                                                          SETTINGS.WIDTH // 12, 1.5 * SETTINGS.HEIGHT // 7))
                    archer -= 0.2

                # pygame.display.update()
                pygame.display.flip()

                for el in list(archery.art_list.keys()):
                    el.go()
                    # print(el.x // SETTINGS.tile_size, el.y // SETTINGS.tile_size)
                    # print(archery.npc_list.keys())

                # clock.tick()
        pygame.quit()
        sys.exit()