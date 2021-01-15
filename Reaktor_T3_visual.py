f = open("Reaktor_T3_data", "r")
lines = f.readlines()
coordslist = [] # ARRAY OF SAFE COORDINATES
start = None
finish = None
walls = []

for line in lines:
    first = (line.split(' '))[0].split(',')
    coords = [[int(first[0]),int(first[1])]]

    if len(line.split(' ')) > 1:
        commands = (line.split(' '))[1].split(',')
        if '\n' in commands[-1]: commands[-1] = commands[-1][0]

        for c in commands:
            if c in ['D','U','R','L']:
                if c == 'D': new = [coords[-1][0],coords[-1][1]+1]
                elif c == 'U': new = [coords[-1][0],coords[-1][1]-1]
                elif c == 'R': new = [coords[-1][0] + 1,coords[-1][1]]
                elif c == 'L': new = [coords[-1][0] - 1,coords[-1][1]]

                coords.append(new)

            elif c == 'X': 
                wall = coords.pop()
                walls.append(wall)
            elif c == 'S' and start == None: start = coords[-1]
            elif c == 'F' and finish == None: finish = coords[-1]

    for i in coords:
        if i not in coordslist:
            coordslist.append(i)

print("Starting coordinates: {}".format(start))
print("Finishing coordinates: {}".format(finish))

minX = min(i[0] for i in (coordslist + walls))
maxX = max(i[0] for i in (coordslist + walls))
minY = min(i[1] for i in (coordslist + walls))
maxY = max(i[1] for i in (coordslist + walls))

print(minX,maxX,minY,maxY) # DIMENSIONS OF THE MAZE

# VISUALISATION
for y in range(128):
    line = ""
    for x in range(128):
        q = [x,y]
        if q == finish: line += 'F'
        elif q == start: line += 'S'
        elif q in coordslist: line += 'O' # SAFE COORDINATES
        elif q in walls: line += 'X'
        else: line += ' '
    print(line)

