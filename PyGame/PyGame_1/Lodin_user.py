import sys
import pygame


def draw():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    red = (255, 0, 0)
    pygame.draw.rect(screen, red, (1, 1, int(w) - 2, int(h) - 2))


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    pygame.display.set_caption('Прямоугольник')
    # размеры окна:
    try:
        w, h = map(int, input().split())
        size = (int(w), int(h))
        screen = pygame.display.set_mode(size)
        draw()
        pygame.display.flip()
    except ValueError:
        print('Неправильный формат ввода')
        sys.exit()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
