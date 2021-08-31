#Het Patel
#Cocktail Sort Algorithm For Sorting Algorithm Visualizer
#27/10/20

from time import sleep

def Cocktail_Sort(data_set, drawData, speed):
    end=len(data_set)
    start=0
    for pos1 in range(len(data_set)):
        flag=True
        for pos2 in range(start, end-1):
            if (data_set[pos2]>data_set[pos2+1]):
                data_set[pos2], data_set[pos2+1] = data_set[pos2+1], data_set[pos2]
                flag=False

            if (speed!=0):
                drawData(data_set, ['red' if current_block == pos2 else 'SpringGreen' if current_block>=end or current_block<start else 'orange' if current_block == pos2+1 and (pos2+1)<end else 'orchid' for current_block in range(len(data_set))])
                sleep(speed)

        end-=1
        if flag:
            break

        for pos2 in range(end-2, start-1, -1):
            if (data_set[pos2]>data_set[pos2+1]):
                data_set[pos2], data_set[pos2+1] = data_set[pos2+1], data_set[pos2]
                flag=False

            if (speed!=0):
                drawData(data_set, ['orange' if current_block == pos2 else 'SpringGreen' if current_block>=end or current_block<start else 'red' if current_block == pos2+1 and (pos2+1)<end else 'orchid' for current_block in range(len(data_set))])
                sleep(speed)

        start+=1
        if flag:
            break


    drawData(data_set, ['SpringGreen' for current_block in range(len(data_set))])
