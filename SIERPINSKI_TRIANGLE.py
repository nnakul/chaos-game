
import pygame
from random import randint
from timeit import default_timer as timer

pygame.init()
SCREEN_WIDTH = 500
BG_COLOR = (255, 255, 255)
COLOR = (255, 69, 0)
root = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

print('\nCHAOS GAME STARTED !')
print('CLICK ENTER TO WATCH THE STATUS .\n')

points = [
            (SCREEN_WIDTH/2, 0),
            (0, SCREEN_WIDTH),
            (SCREEN_WIDTH, SCREEN_WIDTH)
         ]

current_position = (SCREEN_WIDTH/2, SCREEN_WIDTH/2)

root.fill(BG_COLOR)

counter = 0
run = True

startTime = timer()

while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            print( '\nPROGRAM STOPPED AFTER {} ITERATIONS .'.format(counter) )
            print( 'PROGRAM RAN FOR {:.2f} SECONDS .'.format(timer()-startTime) )
            run = False
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_RETURN :
                print( '\n' + str(counter), 'ITERATIONS COMPLETED .' )
                print( round(timer()-startTime, 2), 'SECONDS PASSED .' )
    
    counter += 1
    
    i = randint(0,2)
    
    current_position = ( (current_position[0] + points[i][0])/2 , (current_position[1] + points[i][1])/2 )
    pygame.draw.line(root, COLOR, current_position, current_position)
    
    pygame.display.update()
    
pygame.quit()
