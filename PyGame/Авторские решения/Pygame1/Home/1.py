import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption('Сфера')
    # Считываем количество эллипсов
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


def draw(screen, number):
    ellipse_color = pygame.Color('white')
    ellipse_width = 1
    width, _ = screen.get_size()

    # Определяем шаг
    step = (width // 2) // number
    for i in range(0, width // 2, step):
        # Рисуем эллипсы, вытянутые по высоте
        ellipse_rect = [(i, 0), (width - i * 2, width)]
        pygame.draw.ellipse(screen, ellipse_color, ellipse_rect, ellipse_width)
        # Рисуем эллипсы, вытянутые по ширине
        ellipse_rect = [(0, i), (width, width - i * 2)]
        pygame.draw.ellipse(screen, ellipse_color, ellipse_rect, ellipse_width)


if __name__ == '__main__':
    sys.exit(main())
