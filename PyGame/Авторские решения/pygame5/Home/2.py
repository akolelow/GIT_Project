import os

import pygame

size = width, height = 600, 95
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


class Car(pygame.sprite.Sprite):
    image_right = load_image("car2.png")
    image_left = pygame.transform.flip(image_right, True, False)

    def __init__(self):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite
        super().__init__(all_sprites)
        self.image = Car.image_right
        self.rect = self.image.get_rect()
        self.vx = 1
        # считаем количество тиков для замедления
        self.ticks = 0

    def update(self):
        if self.rect.left + self.rect.width > width or self.rect.left < 0:
            self.vx = -self.vx
            if self.vx > 0:
                self.image = Car.image_right
            else:
                self.image = Car.image_left
        self.rect.left = self.rect.left + self.vx
        self.ticks = 0


# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

car = Car()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
