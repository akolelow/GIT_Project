import pygame


w, n = map(int, input().split())
x = n * w * 2

if __name__ == '__main__':
    pygame.init()
    size = width, height = x, x
    screen = pygame.display.set_mode(size)
    color = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]


    def draw():
        screen.fill((0, 0, 0))
        for i in range(n, 0, -1):
            pygame.draw.circle(screen, (color[-(i % 3)]), (n * w, n * w), (w * i))



    draw()


    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()