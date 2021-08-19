#import random, sys, time
import copy, random, sys, time

#set width and height for the screen
width = 79
height = 20

#set constants for empty or occupied
ALIVE = 'X'
DEAD = '0'


#set cells and next cells functions
next_cells = {}


#put random cells in random place to start with
for x in range(width):
    for y in range(height):
        if random.randint(0,1) == 'X':
            next_cells[(x,y)] = ALIVE #start with alive cell
        else:
            next_cells[(x,y)] = DEAD #start with dead cell

#create the main game loop
while True:

    print('\n'*50) # total newlines
    cells = copy.deepcopy(next_cells)
    #print cells on screen


    for y in range(height):
        for x in range(width):
            print(cells[(x,y)], end = '')
        print()
    print('Enter Ctrl-C to quit.')


    #calculate next steps based on current steps

    for x in range(width):
        for y in range(height):

            left = (x-1)%width
            right = (x+1)%width
            up = (y+1)%height
            down = (y-1)%height

            #count the number of living neighbours

            numNeighbours = 0

            if cells[(left, up)] == ALIVE: #top left neighbour is alive
                numNeighbours += 1
            if cells[(x, up)] == ALIVE: #top neighbour is alive
                numNeighbours += 1
            if cells[(right, up)] == ALIVE: #top right is alive
                numNeighbours += 1
            if cells[(right, y)] == ALIVE: #right neighbour is alive
                numNeighbours += 1
            if cells[(left, y)] == ALIVE: #left neighbour is alive
                numNeighbours += 1
            if cells[(left, down)] == ALIVE:
                numNeighbours += 1
            if cells[(x, down)] == ALIVE:
                numNeighbours += 1
            if cells[(right, down)] == ALIVE:
                numNeighbours += 1
            

            #set cell based on Conway's Game of life rules

            if cells[(x,y)] == ALIVE and (numNeighbours == 2 or numNeighbours == 3):
                #living cells with 2 or 3 neighbours stay alive
                next_cells[(x,y)] == ALIVE
            elif cells[(x,y)] == DEAD and numNeighbours == 3:
                #dead cells with 3 neighbours become alive
                next_cells[(x,y)] == ALIVE
            else:
                next_cells[(x,y)] == DEAD #all spaces are dead
    
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print('Conway\'s game of life.')
        sys.exit()