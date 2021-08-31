#Het Patel
#Bubble Sort Algorithm For Sorting Algorithm Visualizer
#26/10/20

from time import sleep

def Bubble_Sort(data_set, drawData, speed):
    temp=len(data_set)
    for pos1 in range(len(data_set)):
        flag=True
        for pos2 in range(temp-1):
            if (data_set[pos2]>data_set[pos2+1]):
                data_set[pos2], data_set[pos2+1] = data_set[pos2+1], data_set[pos2]
                flag=False

            if (speed!=0):
                drawData(data_set, ['red' if current_block == pos2 else 'SpringGreen' if current_block>=temp else 'orange' if current_block == pos2+1 and (pos2+1)<temp else 'orchid' for current_block in range(len(data_set))])
                sleep(speed)

        temp-=1
        if flag:
            break

    drawData(data_set, ['SpringGreen' for current_block in range(len(data_set))])
