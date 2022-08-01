# Conway's game of life

import random
import copy
import time
import os

WIDTH = 10
HEIGHT = 8
BORDER = ' '
DEAD = '.'
ALIVE = '#'

def init_grid() -> list:
    grid = []
    for i in range(HEIGHT + 2):
        grid.append([])
        for j in range(WIDTH + 2):
            grid[i].append(ALIVE)
    return grid

def random_init_grid() -> list:
    grid = []

    grid.append([])
    for i in range(WIDTH + 2):
        grid[0].append(DEAD)

    for i in range(1, HEIGHT + 1):
        grid.append([])
        grid[i].append(DEAD)
        for j in range(1, WIDTH + 1):
            if random.randint(0, 1) == 0:
                grid[i].append(DEAD)
            else:
                grid[i].append(ALIVE)
        grid[i].append(DEAD)

    grid.append([])
    for i in range(WIDTH + 2):
        grid[len(grid) - 1].append(DEAD)

    return grid

def display(grid: list) -> None:
    print(BORDER * (WIDTH + 2))
    for i in range(1, HEIGHT + 1):
        print(BORDER, end = '')
        for j in range(1, WIDTH + 1):
            print(grid[i][j], sep = '', end = '')
        print(BORDER)
    print(BORDER * (WIDTH + 2))

def alive(grid: list, coords: tuple) -> bool:
    x, y = coords
    return grid[y][x] == ALIVE

def state(grid: list, coords: tuple) -> bool:
    ''' Evaluate state of the cell in next generation.
    
        Return True if cell will be alive, False otherwise.'''

    x, y = coords
    living_neighbors = 0

    if alive(grid, (x + 1, y)):     living_neighbors += 1
    if alive(grid, (x - 1, y)):     living_neighbors += 1
    if alive(grid, (x, y + 1)):     living_neighbors += 1
    if alive(grid, (x, y - 1)):     living_neighbors += 1
    if alive(grid, (x + 1, y + 1)): living_neighbors += 1
    if alive(grid, (x + 1, y - 1)): living_neighbors += 1
    if alive(grid, (x - 1, y + 1)): living_neighbors += 1
    if alive(grid, (x - 1, y - 1)): living_neighbors += 1

    if alive(grid, coords) and (living_neighbors == 2 or living_neighbors == 3):
        return True

    if not alive(grid, coords) and living_neighbors == 3:
        return True
    
    return False

def next_generation(grid: list) -> list:
    next = copy.deepcopy(grid)
    for y in range(1, HEIGHT + 1):
        for x in range(1, WIDTH + 1):
            if state(grid, (x, y)):
                next[y][x] = ALIVE
            else:
                next[y][x] = DEAD
    return next

def run():
    grid = random_init_grid()
    gen_number = 1

    while True:
        time.sleep(0.2)
        print('Generation: ', gen_number, sep = '')
        display(grid)
        next_gen = next_generation(grid)
        if grid == next_gen:
            break
        grid = next_gen
        gen_number += 1

if __name__ == '__main__':
    run()