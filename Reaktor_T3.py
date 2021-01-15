import numpy as np

# THIS CODE EVALUATES THE OPTIMAL ROUTE FROM START TO FINISH.

f = open("Reaktor_T3_data", "r")
lines = f.readlines() # A list of strings containing the neural link fractions.

# All 'safe' coordinates are obtained from the given strands. These are saved into coords as 0 (unsafe/wall: -1).
coords = np.full((128, 128), -1) # Dimensions of the maze were previously evaluated in Reaktor_T3_visual.
start = None
finish = None

for line in lines:
    first = (line.split(' '))[0].split(',') # Gets the first coordinate of the neural link fractin.
    current = [int(first[0]),int(first[1])] 

    coords[current[0]][current[1]] = 0 # The first coordinate of a strand is safe.

    if len(line.split(' ')) > 1:
        commands = (line.split(' '))[1].split(',') # Array of commands (D,U,R,L). 
        if '\n' in commands[-1]: commands[-1] = commands[-1][0] # Accounts for line break.

        for c in commands: # Deals with one command at a time.
            if c in ['D','U','R','L']:
                if c == 'D': new = [current[0],current[1]+1]
                elif c == 'U': new = [current[0],current[1]-1]
                elif c == 'R': new = [current[0]+1,current[1]]
                elif c == 'L': new = [current[0]-1,current[1]]

                current = new # Saves latest coordinate to determine the next one.
                coords[current[0]][current[1]] = 0 # Denote that the coordinate is safe.

            elif c == 'X': 
                coords[current[0]][current[1]] = -1 # Turn the coordinate back to -1, as it is unsafe.
            elif c == 'S' and start == None: start = current
            elif c == 'F' and finish == None: finish = current


print("Starting coordinates: {}".format(start))
print("Finishing coordinates: {}".format(finish))

# Makes sure the coordinate does not exceed the dimensions of the matrix (i.e. the maze).
def inBounds(coord):
    if coord[0] < 128 and coord[0] >= 0:
        if coord[1] < 128 and coord[1] >= 0:
            return True
    
    return False

# Finds all neighboring coordinates (wihtout diagonals) that are safe.
def validNeighbors(coordslist):
    collect = []
    for c in coordslist:
        for xy in [[c[0]-1,c[1]], [c[0]+1,c[1]], [c[0],c[1]-1], [c[0],c[1]+1]]:
            if inBounds(xy) and xy not in collect and coords[xy[0]][xy[1]] != -1:
                collect.append(xy)
    return collect


coords[finish[0]][finish[1]] = -2 # Finish is now denotes as -2 in the 'coords' matrix.

# The length of shortest path to finish is evaluated and saved into coords for each safe coordinate. 
current = [finish] 
counter = 0
while(start not in current): 
    counter += 1
    current = filter(lambda xy: coords[xy[0]][xy[1]] == 0, validNeighbors(current))
    # filter: excludes coordinates that have already been assigned a shortest path length.

    for xy in current:
        coords[xy[0]][xy[1]] = counter

print("It takes {} steps from start to finish.").format(int(coords[start[0]][start[1]]))

current = start
counter = coords[start[0]][start[1]]

solution = ""

# Starting at 'start', we move to the neighbor with the shortest path length until 'finish' is reached.
while current != finish: # Writes commands into 'solution'.
    counter -= 1
    for xy in validNeighbors([current]):
        if coords[xy[0]][xy[1]] == counter:
            if xy[0] == current[0] + 1:
                solution = solution + 'R'
            elif xy[0] == current[0] - 1:
                solution = solution + 'L'
            elif xy[1] == current[1] + 1:
                solution = solution + 'D'
            elif xy[1] == current[1] - 1:
                solution = solution + 'U'
            current = xy
            break

print(solution)




        
