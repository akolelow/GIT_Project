import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption('Крест')
    try:
        # Считываем размер окна
        size = [int(i) for i in input().split()]
    except ValueError:
        print("Неправильный формат ввода")
        return -1

    screen = pygame.display.set_mode(size)
    draw(screen)
    while pygame.event.wait().type != pygame.QUIT:
        # Обновляем изображение в окне
        pygame.display.flip()

    pygame.quit()


def draw(screen):
    width, height = screen.get_size()
    # Задаем параметры линий
    lines_color = (255, 255, 255)
    lines_width = 5
    # Рисуем главную диагональ
    lines_points = [(0, 0), (width, height)]
    pygame.draw.line(screen, lines_color, *lines_points, width=lines_width)
    # Рисуем побочную диагональ
    lines_points = [(0, height), (width, 0)]
    pygame.draw.line(screen, lines_color, *lines_points, width=lines_width)


if __name__ == '__main__':
    sys.exit(main())
