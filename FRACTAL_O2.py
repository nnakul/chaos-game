
import pygame
import math
from random import randint
from timeit import default_timer as timer

pygame.init()
SCREEN_WIDTH = 500
BG_COLOR = (255, 255, 255)
COLOR = (255, 69, 0)
root = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

print('\nCHAOS GAME STARTED !')
print('CLICK ENTER TO WATCH THE STATUS .\n')

w = SCREEN_WIDTH
theta = 2 * math.pi / 5

p1 = ( w/2, 0 )
p2 = ( w*0.5*(1+math.sin(theta)), w*0.5*(1-math.cos(theta)) )
p3 = ( w*0.5*(1+math.sin(theta/2)), w*0.5*(1+math.cos(theta/2)) )
p4 = ( w*0.5*(1-math.sin(theta/2)), w*0.5*(1+math.cos(theta/2)) )
p5 = ( w*0.5*(1-math.sin(theta)), w*0.5*(1-math.cos(theta)) )

points = [p1, p2, p3, p4, p5]

current_position = (SCREEN_WIDTH/2, SCREEN_WIDTH/2)
current_vertex = randint(0,4)
prev_vertex1 = -1
prev_vertex2 = -1

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
    
    current_position = ( (current_position[0] + points[current_vertex][0])/2, (current_position[1] + points[current_vertex][1])/2 )
    pygame.draw.line(root, COLOR, current_position, current_position)
    
    prev_vertex2 = prev_vertex1
    prev_vertex1 = current_vertex
    
    if prev_vertex1 == prev_vertex2 and prev_vertex1 != -1 and prev_vertex2 != -1 :
        
        sample = [0,1,2,3,4]
        if current_vertex == 0 :
            sample.remove(1)
            sample.remove(4)
        elif current_vertex == 1 :
            sample.remove(0)
            sample.remove(2)
        elif current_vertex == 2 :
            sample.remove(1)
            sample.remove(3)
        elif current_vertex == 3 :
            sample.remove(2)
            sample.remove(4)
        elif current_vertex == 4 :
            sample.remove(0)
            sample.remove(3)
        current_vertex = sample[randint(0,2)]
    
    else :  current_vertex = randint(0,4)
    
    pygame.display.update()
    
pygame.quit()
