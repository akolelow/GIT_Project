import pygame
import sys

COLORS = (pygame.Color('blue'), pygame.Color('red'), pygame.Color('green'))


def main():
    pygame.init()
    pygame.display.set_caption('Мишень')
    # Считываем количество колец и их толщину
    try:
        circle_width, number = [int(i) for i in input().split()]
    except ValueError:
        print("Неправильный формат ввода")
        return -1

    size = (2 * circle_width * number, 2 * circle_width * number)
    screen = pygame.display.set_mode(size)

    draw(screen, circle_width, number)

    while pygame.event.wait().type != pygame.QUIT:
        # Обновляем изображение в окне
        pygame.display.flip()
    pygame.quit()


# Кольца рисуем как круги с наслаиванием друг на друга
def draw(screen, circle_width, number):
    circle_radius = circle_width * number
    circle_pos = (circle_radius, circle_radius)
    while number > 0:
        # Отрисовываем круг
        pygame.draw.circle(screen, COLORS[number % 3], circle_pos, circle_radius, 0)
        # Уменьшаем радиус
        circle_radius -= circle_width
        # Смещаем коэффициент цвета
        number -= 1


if __name__ == '__main__':
    sys.exit(main())
