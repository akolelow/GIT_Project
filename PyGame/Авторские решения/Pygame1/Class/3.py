import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption('Шахматная клетка')

    try:
        width, number = [int(i) for i in input().split()]
        if width % number != 0:
            print('Количество клеток не кратно размеру окна')
            return
    except ValueError:
        print("Неправильный формат ввода")
        return -1

    size = width, width
    screen = pygame.display.set_mode(size)
    draw(screen, number)

    while pygame.event.wait().type != pygame.QUIT:
        # Обновляем изображение в окне
        pygame.display.flip()
    pygame.quit()


def draw(screen, number):
    # Переменная cell_color используется для определения цвета квадрата
    cell_color = number % 2
    width, _ = screen.get_size()
    square_width = width // number
    # По очереди отрисовываем квадраты
    for i in range(0, width, square_width):
        for j in range(0, width, square_width):
            square_point = [(i, j), (square_width, square_width)]
            # Меняем цвет
            cell_color = (cell_color + 1) % 2
            if not cell_color:
                square_color = pygame.Color('black')
            else:
                square_color = pygame.Color('white')
            # Рисуем квадрат
            pygame.draw.rect(screen, square_color, square_point, 0)
        # Для чётного количества клеток, смещаем переменную счетчик
        if number % 2 == 0:
            cell_color += 1


if __name__ == '__main__':
    sys.exit(main())
