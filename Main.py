# air on higher value squares will try to flow to lower value squares
# a square can only hold a certain amount of air ( Depends on square value ). If square is full, air will not flow into it.

import random, pygame, time
from noise import pnoise2
noise_X = random.randint(-1000,1000)
noise_Y = random.randint(-1000,1000)
#Modifiers. Chage these to chage window size, zoom, and particle size
noise_zoom = 0.05
mapsize = 150
size = 7

##noise_zoom = float(input("Noise? "))
##mapsize = int(input("Mapsize? "))
##size = int(input("Paritlcesize? "))

pygame.init()
screen = pygame.display.set_mode((mapsize*size,mapsize*size))

air = []
heightmap = []

def update_air_index(i,j):
    if i == 0 or i == (mapsize-1) or j == 0 or j == (mapsize-1):
        d1 = [255,255,255,255]
        
    else:
        d1 = [heightmap[i][j-1], heightmap[i][j+1], heightmap[i-1][j], heightmap[i+1][j]]

        target = min(d1)
        target_location = d1.index(min(d1))
        if target < 14:
            target_location = random.randint(0,3)
            
        if air[i][j] >= 1:
            if heightmap[i][j] >= target:
                if air[i-1][j] <= 4: 
                    if target_location == 2:
                        air[i][j] -= 1
                        air[i-1][j] += 1

                if air[i+1][j] <= 4:
                    if target_location == 3:
                        air[i][j] -= 1
                        air[i+1][j] += 1
                        
                if air[i][j-1] <= 4:
                    if target_location == 0:
                        air[i][j] -= 1
                        air[i][j-1] += 1

                if air[i][j+1] <= 4:
                    if target_location == 1:
                        air[i][j] -= 1
                        air[i][j+1] += 1


            
                
                
def update_air():
    for i in range(mapsize):
        for j in range(mapsize):
            update_air_index(i,j)
        

def generate_map():
    for i in range(mapsize):
        air.append([])
        heightmap.append([])
        for j in range(mapsize):
            height = pnoise2((i + (noise_X))*noise_zoom, (j + (noise_Y))*noise_zoom)*10
            height += 15
            heightmap[i].append(abs(height))
            air[i].append(random.randint(0,5))

            
def render():
    
    for i in range(mapsize):
        for j in range(mapsize):
            aircolor = air[j][i]*25
            heightcolor = int(heightmap[j][i]*3)
            if aircolor > 255:
                aircolor=255
            pygame.draw.rect(screen,(heightcolor,heightcolor,aircolor),(j*size,i*size,size,size))

            
            
generate_map()     
while True:
    update_air()
    render()
    pygame.display.flip()
    
