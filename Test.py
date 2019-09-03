import os
import random
import time

sea = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def first_generation(sea,sim):
    for i in range(14):
        for j in range(40):
            sea[i][j] = random.randrange(0,4)
            if i == 0:
                sea[i][j] = 3
            elif i == 13:
                sea[i][j] = 3
            elif j == 0:
                sea[i][j] = 3
            elif j == 39:
                sea[i][j] = 3
                
    return sea

def update(sea):
    for i in range(14):
        for j in range(40):
            
            if sea[i][j]== 1 or sea[i][j] == 2:
                curr= sea[i][j]
                nearblocks = 0
                if sea[i+1][j] ==  curr:
                    nearblocks =+ 1 
                if sea[i+1][j+1] ==  curr:
                    nearblocks =+ 1
                if sea[i][j+1] ==  curr:
                    nearblocks =+ 1
                if sea[i][j-1] ==  curr:
                    nearblocks =+ 1
                if sea[i-1][j] ==  curr:
                    nearblocks =+ 1
                if sea[i-1][j-1] ==  curr:
                    nearblocks =+ 1
                if sea[i+1][j-1] ==  curr:
                    nearblocks =+ 1
                if sea[i-1][j+1] ==  curr:
                    nearblocks =+ 1

                if nearblocks < 2 or nearblocks > 3:
                    sea[i][j] = 0

                    
            if sea[i][j] == 0:
                curr= 1
                nearblocks = 0
                if sea[i+1][j] == curr:
                    nearblocks =+ 1 
                if sea[i+1][j+1] == curr:
                    nearblocks =+ 1
                if sea[i][j+1] == curr:
                    nearblocks =+ 1
                if sea[i][j-1] == curr:
                    nearblocks =+ 1
                if sea[i-1][j] == curr:
                    nearblocks =+ 1
                if sea[i-1][j-1] ==  curr:
                    nearblocks =+ 1
                if sea[i+1][j-1] ==  curr:
                    nearblocks =+ 1
                if sea[i-1][j+1] ==  curr:
                    nearblocks =+ 1

                if nearblocks == 3:
                    sea[i][j] = 1


            if sea[i][j] == 0:
                curr= 2
                nearblocks = 0
                if sea[i+1][j] ==  curr:
                    nearblocks =+ 1 
                if sea[i+1][j+1] == curr:
                    nearblocks =+ 1
                if sea[i][j+1] == curr:
                    nearblocks =+ 1
                if sea[i][j-1] == curr:
                    nearblocks =+ 1
                if sea[i-1][j]  == curr:
                    nearblocks =+ 1
                if sea[i-1][j-1] == curr:
                    nearblocks =+ 1
                if sea[i+1][j-1] == curr:
                    nearblocks =+ 1
                if sea[i-1][j+1] == curr:
                    nearblocks =+ 1

                if nearblocks == 3:
                    sea[i][j] = 2
                
    return sea

        
def show(sea,sim):
    for i in range(14):
        line = ""
        for j in range(40):
            line = line + sim[sea[i][j]]
        print(line)

sim = ["_","#","$","^"]
sea = first_generation(sea,sim)
show(sea,sim)
exit = 1


while exit == 1:
    update(sea)
    show(sea,sim)
    time.sleep(1)
    
    


    
    
