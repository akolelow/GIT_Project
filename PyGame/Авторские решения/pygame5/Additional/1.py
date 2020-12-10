import os

import pygame

size = width, height = 600, 300
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Gameover(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite
        super().__init__(all_sprites)
        self.image = Gameover.image
        self.rect = Gameover.image.get_rect()
        self.rect.left = -600

    def update(self):
        global width, height
        if self.rect.left < 0:
            self.rect.left += 8


# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

Gameover = Gameover()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("blue"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
