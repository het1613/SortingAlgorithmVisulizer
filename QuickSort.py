#Het Patel
#Quick Sort Algorithm For Sorting Algorithm Visualizer
#27/10/20

from time import sleep

def partition(data_set, head, tail, drawData, speed):
    border=head
    pivot=data_set[tail]

    if (speed!=0):
        drawData(data_set, blockColours(len(data_set), head, tail, border, border))
        sleep(speed)

    for pos in range(head, tail):
        if data_set[pos]<pivot:
            if (speed!=0):
                drawData(data_set, blockColours(len(data_set), head, tail, border, pos))
                sleep(speed)

            data_set[border], data_set[pos]=data_set[pos], data_set[border]
            border+=1

        if (speed!=0):
            drawData(data_set, blockColours(len(data_set), head, tail, border, pos))
            sleep(speed)

    if (speed!=0):
        drawData(data_set, blockColours(len(data_set), head, tail, border, tail))
        sleep(speed)

    data_set[border], data_set[tail] = data_set[tail], data_set[border]

    return border

def Quick_Sort(data_set, head, tail, drawData, speed):
    if head<tail:
        partitionIdx=partition(data_set, head, tail, drawData, speed)

        Quick_Sort(data_set, head, partitionIdx-1, drawData, speed) #Left Partition
        Quick_Sort(data_set, partitionIdx+1, tail, drawData, speed) #Right Partition

    if (head==0 and tail==len(data_set)-1 and speed!=0):
        for pos1 in range(len(data_set)):
            drawData(data_set, ['SpringGreen' if current_block<=pos1 else 'orchid' for current_block in range(len(data_set))])
            sleep(0.001)

    elif (head==0 and tail==len(data_set)-1 and speed==0):
        drawData(data_set, ['SpringGreen' for current_block in range(len(data_set))])

def blockColours(dataLen, head, tail, border, currIdx):
    colourList=[]
    for current_block in range(dataLen):
        if current_block==tail:
            colourList.append('blue')

        elif current_block==border:
            colourList.append('red')

        elif current_block==currIdx:
            colourList.append('orange')

        elif current_block>=head and current_block <= tail:
            colourList.append('white')

        else:
            colourList.append('orchid')

    return colourList
