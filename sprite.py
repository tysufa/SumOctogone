import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))


class StaticFrame:
    """Single static sprite from a spritesheet.

    image: surface representing the spritesheet
    row: row in the spritesheet where the sprite is located
    col: column in the spritesheet where the sprite is located
    nrows: number of rows of sprites
    ncols: number of columns of sprite
    """

    def __init__(self, image, row, col, nrows, ncols):
        self.image = image
        rect = image.get_rect()
        framewidth = rect.width // ncols
        frameheight = rect.height // nrows
        self._xoffset = col * framewidth
        self._yoffset = row * frameheight
        self._rect = pygame.Rect(self._xoffset, self._yoffset,
                                 framewidth, frameheight)

    def update(self, dt):
        pass

    @property
    def rect(self):
        "The Rectangle in the spritesheet delimiting the desired sprite."
        return self._rect


class AnimatedFrame(StaticFrame):
    """Animated sprite from a spritesheet.

    The animation is supposed to be contained on a row. It can start at a
    column different than column 0 in which case the animation will loop from
    the starting column until the last column sprite.

    duration: frame duration expressed in seconds.
    """

    def __init__(self, image, row, col, duration, nrows, ncols):
        super().__init__(image, row, col, nrows, ncols)
        self.duration = duration
        self.time = 0
        self._anim_frames_width = (ncols - col) * self._rect.width

    def update(self, dt):
        self.time += dt / 1000
        while self.time > self.duration:
            self.time -= self.duration
            left = self._rect.left
            step = self._rect.width
            left = (left - self._xoffset + step) % self._anim_frames_width
            self._rect.left = left + self._xoffset


class Gompa:
    "Gompa is an animated sprite."
    image = pygame.image.load("image/Luffy.png").convert_alpha()

    def __init__(self, x, y):
        NROWS = 4
        NCOLS = 5
        self._frames = {
            "STATIC": {
                "DOWN": StaticFrame(self.image, 0, 0, NROWS, NCOLS),
                "LEFT": StaticFrame(self.image, 1, 0, NROWS, NCOLS),
                "RIGHT": StaticFrame(self.image, 2, 0, NROWS, NCOLS),
                "UP": StaticFrame(self.image, 3, 0, NROWS, NCOLS),
            },
            "ANIMATED": {
                "DOWN": AnimatedFrame(self.image, 0, 1, 0.2, NROWS, NCOLS),
                "LEFT": AnimatedFrame(self.image, 1, 1, 0.2, NROWS, NCOLS),
                "RIGHT": AnimatedFrame(self.image, 2, 1, 0.2, NROWS, NCOLS),
                "UP": AnimatedFrame(self.image, 3, 1, 0.2, NROWS, NCOLS),
            }
        }
        self.status = "STATIC"
        self.facing = "LEFT"
        self._frame = self._frames[self.status][self.facing]
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y), self._frame.rect)

    def update(self, dt):
        self._frame.update(dt)
        dt_sec = dt / 1000
        self.x += self.vx * dt_sec
        self.y += self.vy * dt_sec

    def react(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.vx -= 70
                elif event.key == K_RIGHT:
                    self.vx += 70
                elif event.key == K_DOWN:
                    self.vy += 70
                elif event.key == K_UP:
                    self.vy -= 70

                self._update_frame()

            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    self.vx += 70
                elif event.key == K_RIGHT:
                    self.vx -= 70
                elif event.key == K_DOWN:
                    self.vy -= 70
                elif event.key == K_UP:
                    self.vy += 70

                self._update_frame()

    def _update_frame(self):
        if self.vy < 0:
            self.status = "ANIMATED"
            self.facing = "UP"
        elif self.vx < 0:
            self.status = "ANIMATED"
            self.facing = "LEFT"
        elif self.vx > 0:
            self.status = "ANIMATED"
            self.facing = "RIGHT"
        elif self.vy > 0:
            self.status = "ANIMATED"
            self.facing = "DOWN"
        else:
            self.status = "STATIC"
        self._frame = self._frames[self.status][self.facing]


bg = pygame.image.load("image/background.jpg").convert()
gompa = Gompa(x=200, y=100)
clock = pygame.time.Clock()

continuer = True
while continuer:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = False

    gompa.react(events)

    dt = clock.tick(60)
    gompa.update(dt)

    screen.blit(bg, (0, 0))
    gompa.draw(screen)
    pygame.display.flip()

pygame.quit()