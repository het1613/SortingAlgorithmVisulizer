#Het Patel
#Insertion Sort Algorithm For Sorting Algorithm Visualizer
#27/10/20

from time import sleep

def Insertion_Sort(data_set, drawData, speed):
    for pos1 in range(1, len(data_set)):
        current=data_set[pos1]

        for pos2 in range(pos1-1, -1, -1):
            if (current>=data_set[pos2]):
                data_set.pop(pos1)
                data_set=data_set[:pos2+1]+[current]+data_set[pos2+1:]
                break

            if (speed!=0):
                drawData(data_set, ['orange' if current_block == pos1 else 'red' if current_block==pos2+1 else 'SpringGreen' if current_block<pos1 else 'orchid' for current_block in range(len(data_set))])
                sleep(speed)
        else:
            data_set.pop(pos1)
            data_set=[current]+data_set

    drawData(data_set, ['SpringGreen' for current_block in range(len(data_set))])


# def Insertion_Sort(data_set, drawData, speed):
#     for pos1 in range(1, len(data_set)):
#         current=data_set[pos1]
#
#         for pos2 in range(pos1-1, -1, -1):
#             if (current>=data_set[pos2]):
#                 data_set.pop(pos1)
#                 data_set=data_set[:pos2+1]+[current]+data_set[pos2+1:]
#                 break
#
#             drawData(data_set, ['orange' if current_block == pos1 else 'red' if current_block==pos2+1 else 'orchid' for current_block in range(len(data_set))])
#             sleep(speed)
#         else:
#             data_set.pop(pos1)
#             data_set=[current]+data_set
#
#     for pos1 in range(len(data_set)):
#         drawData(data_set, ['SpringGreen' if current_block<=pos1 else 'orchid' for current_block in range(len(data_set))])
#         sleep(0.006)

# def Insertion_Sort(data_set, drawData, speed):
#     for pos1 in range(1, len(data_set)):
#         pos2=pos1-1
#         temp=data_set[pos1]
#         while (pos2>=0) and (temp<data_set[pos2]):
#             data_set[pos2+1]=data_set[pos2]
#             pos2-=1
#             drawData(data_set, ['orange' if current_block == pos1 else 'red' if current_block==pos2 else 'SpringGreen' if current_block<pos1 else 'orchid' for current_block in range(len(data_set))])
#             sleep(speed)
#
#         data_set[pos2+1]=temp
#
#     drawData(data_set, ['SpringGreen' for current_block in range(len(data_set))])
