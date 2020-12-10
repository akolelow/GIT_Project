import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption('Ромбики')
    # Вводим количество ромбиков
    try:
        number = int(input())
    except ValueError:
        print("Неправильный формат ввода")
        return -1
    size = (300, 300)
    screen = pygame.display.set_mode(size)
    draw(screen, number)
    while pygame.event.wait().type != pygame.QUIT:
        # Обновляем изображение в окне
        pygame.display.flip()
    pygame.quit()


def draw(screen, n):
    # Устанавливаем жёлтый цвет фона
    screen.fill(pygame.Color('yellow'))
    width, height = screen.get_size()
    polygon_width = 0
    polygon_color = pygame.Color('orange')
    # Шаг пригодится для определения координат вершин ромба
    step = n // 2
    # в цикле рисуем ромбики по одному
    for i in range(0, width - n + 1, n):
        for j in range(0, height - n + 1, n):
            # Координаты вершин ромба
            polygon_points = [(i, j + step), (i + step, j + 2 * step), (i + 2 * step, j + step),
                              (i + step, j)]
            pygame.draw.polygon(screen, polygon_color, polygon_points, polygon_width)


if __name__ == '__main__':
    sys.exit(main())
