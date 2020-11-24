
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

p1 = (0,0)
p2 = (SCREEN_WIDTH,0)
p3 = (0,SCREEN_WIDTH)
p4 = (SCREEN_WIDTH,SCREEN_WIDTH)
p5 = (SCREEN_WIDTH/2, SCREEN_WIDTH/2)

points = [p1, p2, p3, p4, p5]

current_position = p5

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
    
    i = randint(0,4)
        
    current_position = ( (current_position[0] + 2*points[i][0])/3 , (current_position[1] + 2*points[i][1])/3 )
    pygame.draw.line(root, (255,0,0), current_position, current_position)
        
    pygame.display.update()
    
pygame.quit()
