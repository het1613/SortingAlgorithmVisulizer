#Het Patel
#Shell Sort Algorithm For Sorting Algorithm Visualizer
#27/10/20

from time import sleep

def Shell_Sort(data_set, drawData, speed):
    space=len(data_set)//2

    while (space>0):
        for pos1 in range(space, len(data_set)):
            current=data_set[pos1]

            for pos2 in range(pos1-1, -1, -1):
                if (current>=data_set[pos2]):
                    data_set.pop(pos1)
                    data_set=data_set[:pos2+1]+[current]+data_set[pos2+1:]
                    break

                if (speed!=0):
                    drawData(data_set, ['orange' if current_block == pos1 else 'red' if current_block==pos2+1 else 'orchid' for current_block in range(len(data_set))])
                    sleep(speed)
            else:
                data_set.pop(pos1)
                data_set=[current]+data_set
        space//=2

    if (speed!=0):
        for pos1 in range(len(data_set)):
            drawData(data_set, ['SpringGreen' if current_block<=pos1 else 'orchid' for current_block in range(len(data_set))])
            sleep(0.001)
    else:
            drawData(data_set, ['SpringGreen' for current_block in range(len(data_set))])
