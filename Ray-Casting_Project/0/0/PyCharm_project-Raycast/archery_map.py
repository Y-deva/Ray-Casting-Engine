from PIL import Image
import pygame
import threading


class Loading:
    def __init__(self, screen, file):
        self.sc = screen
        self.file = file
        self.n = 0
        self.ret, self.len = self.split_animated_gif()
        self.timer = threading.Timer(0.01, self.start)
        self.timer.start()

        #app = QApplication(sys.argv)

    def split_animated_gif(self):
        ret = []
        gif = Image.open(self.file)
        for frame_index in range(gif.n_frames):
            gif.seek(frame_index)
            frame_rgba = gif.convert("RGBA")
            pygame_image = pygame.image.fromstring(
                frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode
            )
            ret.append(pygame_image)
        return ret, gif.n_frames

    def start(self):
        # print(self.n)
        self.sc.blit(self.ret[self.n], (0, 0))
        self.n += 1
        self.n = self.n % self.len
        pygame.display.flip()
        self.timer = threading.Timer(0.1, self.start)
        self.timer.start()

    def stop(self):
        self.timer.cancel()


if __name__ == '__main__':
    load = Loading(pygame.display.set_mode((500, 500)), '../../load.gif')
    pygame.init()
    s = True
    while s:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                s = False
                load.stop()
        pygame.display.flip()
