import pygame, random
from pygame.locals import *

# init pygame
pygame.init()
# set display size
screen = pygame.display.set_mode((500, 400))
# title for window
pygame.display.set_caption('Bubble sort')
# allow control of FPS
clock = pygame.time.Clock()

l = []
dupeCheck = 0

# get 1000 non duplicate random values
for i in range(1000):
    dupeCheck = random.randrange(0, 390, 1)
    
    if dupeCheck in l:
        pass
    else:
        l.append(dupeCheck)

# print unsorted list
print(l)

# while loop run until window is quit
isRun = True
while isRun:

    # FPS set
    clock.tick(60)

    # stop while loop if quit
    for event in pygame.event.get():
        if event.type == QUIT:
            isRun = False

    # white background
    screen.fill((255, 255, 255))


    try:
        for i in l:
            # Displaying list on screen (color, location, size)
            pygame.draw.rect(screen, (50, 0, 200), (50 + l.index(i), 390, 2, -l[i]))
    except IndexError:
        pass
    
    for x in range(len(l)+1):
        try:
            # test if greater than neighbor
            if l[x] > l[x + 1]:
            
                # switch locations in list
                l[x],l[x+1] = l[x+1],l[x]

                # purely for visual, color the items being swapped
                pygame.draw.rect(screen, (0, 255, 0), (50 + l.index(x), 390, 2, -l[x+1]))
                pygame.draw.rect(screen, (255, 0, 0), (50 + l.index(x), 390, 2, -l[x]))
        
        # catch multiple errors
        except (IndexError, ValueError) as error:
            pass
    
    pygame.display.update()

# quit if while loop is broken 
pygame.quit()

# print ordered list in terminal
print(l)

if __name__ == "__main__":
    pass
