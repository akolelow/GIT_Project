import pygame
from random import randrange


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 10:
                    pygame.draw.rect(screen, pygame.color.Color("red"),
                                     (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                                     self.cell_size, self.cell_size))
                elif self.board[y][x] != -1:
                    count = self.board[y][x]
                    coord = (x, y)
                    font = pygame.font.Font(None, 25)
                    number = font.render(str(count), True, pygame.Color("green"))
                    screen.blit(number, (coord[0] * self.cell_size + self.left + number.get_width(),
                                         coord[1] * self.cell_size + self.top + number.get_height() // 2))
                pygame.draw.rect(screen, (255, 255, 255), (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                                 self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        if mouse_pos[0] < self.left or mouse_pos[0] > self.left + self.cell_size * self.width \
                or mouse_pos[1] < self.top or mouse_pos[1] > self.top + self.cell_size * self.height:
            return None
        return ((mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size)

    def on_click(self, cell_coords):
        pass

    def get_click(self, mouse_pos):
        answer = self.get_cell(mouse_pos)
        if answer:
            self.on_click(answer)


class Minesweeper(Board):
    def __init__(self, width, height, count_mines):
        super().__init__(width, height)
        self.set_mines(count_mines)

    def set_mines(self, count_mines):
        coords = []
        for y in range(self.height):
            for x in range(self.width):
                coords.append((y, x))
        mines = []
        for _ in range(count_mines):
            mines.append(coords.pop(randrange(len(coords))))
        for el in mines:
            self.board[el[0]][el[1]] = 10


    def on_click(self, cell_coords):
        if self.board[cell_coords[1]][cell_coords[0]] == -1:
            self.open_cell(cell_coords)

    def open_cell(self, coord):
        count = self.around_count(coord)
        self.board[coord[1]][coord[0]] = count

    def around_count(self, coord):
        count = 0
        for y in range(coord[1] - 1, coord[1] + 2):
            if y < 0 or y >= self.height:
                continue
            for x in range(coord[0] - 1, coord[0] + 2):
                if x < 0 or x >= self.width or (y, x) == coord:
                    continue
                if self.board[y][x] == 10:
                    count += 1
        return count


if __name__ == '__main__':
    pygame.init()
    size = width, height = 350, 700
    screen = pygame.display.set_mode(size)

    sweeper = Minesweeper(10, 20, 15)
    running = True
    speed = 10
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                sweeper.get_click(event.pos)
        screen.fill((0, 0, 0))
        sweeper.render(screen)
        clock.tick(speed)
        pygame.display.flip()
