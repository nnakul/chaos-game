
import pygame
from random import randint
from timeit import default_timer as timer

pygame.init()
WIDTH = 3
SCREEN_WIDTH = 600
FILL_COLOR = (255, 255, 255)
BG_COLOR = (0, 0, 0)
PEN_COLOR = (255, 0, 0)

root = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
root.fill(BG_COLOR) 
pygame.display.update()

print('\nCLICK ENTER TO START THE CHAOS GAME.')

def drawAt( coord, color, size ) :
    left = int(coord[0] / WIDTH) * WIDTH - size
    top = int(coord[1] / WIDTH) * WIDTH - size
    pygame.draw.rect( root, color, (left, top, WIDTH+2*size, WIDTH+2*size) )
    pygame.display.update()

    
def drawFractal() :
    current_position = (SCREEN_WIDTH/2, SCREEN_WIDTH/2)
    
    p1 = (0,0)
    p2 = (SCREEN_WIDTH,0)
    p3 = (0,SCREEN_WIDTH)
    p4 = (SCREEN_WIDTH,SCREEN_WIDTH)
    
    points = [p1, p2, p3, p4]
    
    current_vertex = randint(0,3)
    
    counter = 0
    run = True
    
    startTime = timer()
    
    while run :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                print( '\nGAME STOPPED AFTER {} ITERATIONS .'.format(counter) )
                print( 'GAME RAN FOR {:.2f} SECONDS .'.format(timer()-startTime) )
                return False
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_SPACE :
                    print( '\n' + str(counter), 'ITERATIONS COMPLETED .' )
                    print( round(timer()-startTime, 2), 'SECONDS PASSED .' )
                
        position_temp = ( (current_position[0]+points[current_vertex][0])/2 , (current_position[1]+points[current_vertex][1])/2 )
        position_temp = ( int(position_temp[0]), int(position_temp[1]) )
        
        if  tuple(root.get_at(position_temp)) != PEN_COLOR + (255, ) :
            current_position = ( (current_position[0] + points[current_vertex][0])/2, (current_position[1] + points[current_vertex][1])/2 )
            pygame.draw.line(root, FILL_COLOR, current_position, current_position)
            counter += 1
            pygame.display.update()
            
        current_vertex = randint(0,3)
    
    
run = True
 
while run :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_RETURN :
                print('\nCHAOS GAME STARTED !')
                print('CLICK SPACE TO WATCH THE STATUS .\n')
                if not drawFractal() : run = False
            if event.key == pygame.K_BACKSPACE :
                root.fill(BG_COLOR) 
                pygame.display.update()
            
    if pygame.mouse.get_pressed()[2] :
        drawAt(pygame.mouse.get_pos(), PEN_COLOR, 2*WIDTH)
        
    if pygame.mouse.get_pressed()[0] :
        drawAt(pygame.mouse.get_pos(), BG_COLOR, 2*WIDTH)
        
pygame.quit()
