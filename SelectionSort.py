#Het Patel
#Selection Sort Algorithm For Sorting Algorithm Visualizer
#26/10/20

from time import sleep

def Selection_Sort(data_set, drawData, speed):
    for start_pos in range(len(data_set)):
        min_pos=start_pos

        for current_pos in range(start_pos+1, len(data_set)):
            if (data_set[min_pos]>data_set[current_pos]):
                min_pos=current_pos

            if (speed!=0):
                drawData(data_set, ["SpringGreen" if current_block<start_pos else 'orange' if current_block==min_pos else "red" if current_block==current_pos else "orchid" for current_block in range(len(data_set))])
                sleep(speed)

        data_set[start_pos], data_set[min_pos] = data_set[min_pos], data_set[start_pos]

    drawData(data_set, ["SpringGreen" for current_block in range(len(data_set))])
