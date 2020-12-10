import os
import random

import pygame

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()


def load_image(name, color_key=None):
    fullname = os.path.join('', name)
    image = pygame.image.load(fullname).convert()

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("data/bomb2.png")
    image_boom = load_image("data/boom.png")

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно !!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

for i in range(20):
    # нам уже не нужно даже имя объекта!
    Bomb(all_sprites)

running = True
while running:
    all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)

    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
