import pygame
from settings import *
from circle import Circle
from state import State
import math

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.flip()

screen.fill((252, 186, 3))
state = State()


def update():
    pass

def draw_background_lines():
    for x in range(int(WIDTH/GRID)):
        pygame.draw.line(screen, BACKGROUND_LINES_COLOR, (x*GRID,0), (x*GRID, HEIGHT), BACKGROUND_LINES_WIDTH)
    for y in range(int(HEIGHT/GRID)):
        pygame.draw.line(screen, BACKGROUND_LINES_COLOR, (0, y*GRID), (WIDTH, y*GRID), BACKGROUND_LINES_WIDTH)
    
def draw_circles():
    for circle in circles:
        pygame.draw.circle(screen, (0, 0, 0), (circle.position['x'], circle.position['y']), CIRCLE_RADIUS, CIRCLE_WIDTH)

def draw_lines():
    if len(circles) >1 :
        for circle in circles:
            if circle.next:
                pygame.draw.line(screen, (25, 0, 255), (circle.position['x'], circle.position['y']), (circle.next.position['x'], circle.next.position['y']), LINE_WIDTH) 

def draw():
    draw_background_lines()
    draw_circles()
    draw_lines()
    
    
    pygame.display.update()

def add_circle(position: dict):
    instance = Circle({'x': position['x'], 'y': position['y']})
    circles.append(instance)
    if len(circles) > 1:
        state.last_circle.next = instance
    state.last_circle = instance
    
    return instance

def remove_circle(circle):
    index = circles.index(circle)
    print(f"index: {index}")
    print(f"len(circles): {len(circles)}")
    if not circle == circles[-1]:
        circles[index-1].next = circles[index+1]
    else:
        state.last_circle = circles[-2]
    circles[index-1].change_position({'x': circles[index-1].position['x'], 'y': circles[index-1].position['y']})
    circles.remove(circle)
    # del circle
    screen.fill((252, 186, 3))
    pygame.display.update()


def check_if_clicked_on_circle(x, y):
    """Returns True or False and circle instance or None"""
    for circle in circles:
        if x > circle.position['x'] - CIRCLE_RADIUS \
            and x < circle.position['x'] + CIRCLE_RADIUS \
            and y > circle.position['y'] - CIRCLE_RADIUS \
            and y < circle.position['y'] + CIRCLE_RADIUS:
                return True, circle
        else:
            print(f"nic nie jest ok")
    return (False, None)

def snap_to_grid(x, y):
    new_x = round(x / GRID) * GRID
    new_y = round(y / GRID) * GRID
    return new_x, new_y

circles = []

first_circle_x, first_circle_y = snap_to_grid(50, 50)
add_circle({'x': first_circle_x, 'y': first_circle_y})

    
is_moving_circle = False
moving_circle = None
running = True
while running:
    update()
    draw()
    if is_moving_circle:
        if moving_circle:
            screen.fill((252, 186, 3))
                    
            # pygame.display.flip()
            new_x, new_y = snap_to_grid(x,y)
            moving_circle.change_position({'x': new_x, 'y': new_y})

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if event.button == 1:
                clicked_on_circle, circle = check_if_clicked_on_circle(x, y)
                if clicked_on_circle:
                    is_moving_circle = True
                    moving_circle = circle
                else:
                    new_x, new_y = snap_to_grid(x, y)
                    add_circle({'x': new_x, 'y': new_y})
            elif event.button == 3:
                clicked_on_circle, circle = check_if_clicked_on_circle(x, y)
                if circle:
                    remove_circle(circle)


        elif event.type == pygame.MOUSEBUTTONUP:
            is_moving_circle = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print(f"all circles: {circles}")
            if event.key == pygame.K_b:
                for circle in circles:
                    print(f"circle.next: {circle.next}")
            if event.key == pygame.K_c:
                print(f"State.__dict__: {state.__dict__}")
                    

        x, y = pygame.mouse.get_pos()


