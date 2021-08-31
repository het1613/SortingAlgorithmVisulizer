#Het Patel
#Comb Sort Algorithm For Sorting Algorithm Visualizer
#27/10/20

from time import sleep

def Comb_Sort(data_set, drawData, speed):
    space=len(data_set)

    while (True):
        flag=True
        space=max((space*10)//13, 1)

        for pos in range(len(data_set)-space):
            if data_set[pos]>data_set[pos+space]:
                data_set[pos], data_set[pos+space]=data_set[pos+space], data_set[pos]
                flag=False

            if (speed!=0):
                drawData(data_set, ['red' if current_block == pos else 'orange' if current_block == pos+space else 'orchid' for current_block in range(len(data_set))])
                sleep(speed)

        if flag:
            break

    if (speed!=0):
        for pos1 in range(len(data_set)):
            drawData(data_set, ['SpringGreen' if current_block<=pos1 else 'orchid' for current_block in range(len(data_set))])
            sleep(0.001)
    else:
            drawData(data_set, ['SpringGreen' for current_block in range(len(data_set))])
