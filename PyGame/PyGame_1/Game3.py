import pygame
import sys

if __name__ == '__main__':
    try:
        a, n = map(int, input().split())
    except ValueError:
        print('Неверный формат ввода.')
        sys.exit()


    def draw():
        screen.fill((255, 255, 255))
        for i in range(n):
            for j in range(n):
                if (i + 1) % 2:
                    if (j + 1) % 2:
                        pygame.draw.rect(screen, (0, 0, 0), (j * x, i * x, a, a), 0)
                        pygame.display.flip()
                    else:
                        pygame.draw.rect(screen, (255, 255, 255), (j * x, i * x, a, a), 0)
                        pygame.display.flip()
                else:
                    if (j + 1) % 2:
                        pygame.draw.rect(screen, (255, 255, 255), (j * x, i * x, a, a), 0)
                        pygame.display.flip()
                    else:
                        pygame.draw.rect(screen, (0, 0, 0), (j * x, i * x, a, a), 0)
                        pygame.display.flip()


    size = (a, a)
    x = a // n
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Шахматная клетка')
    draw()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()