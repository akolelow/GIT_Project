import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption('Прямоугольник')
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

    # Задаем размер отступа от границ холста
    step = 1
    # Задаем параметры прямоугольника
    rect_color = pygame.Color('red')
    rect_width = 0
    rect_point = [(step, step), (width - step * 2, height - step * 2)]
    # Рисуем прямоугольник
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)


if __name__ == '__main__':
    sys.exit(main())
