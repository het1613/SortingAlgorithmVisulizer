#Het Patel
#Merge Sort Algorithm For Sorting Algorithm Visualizer
#26/10/20

from time import sleep

def Merge_Sort(data_set, drawData, speed, left, right):
    if (left<right):

        centre=(left+right)//2
        Merge_Sort(data_set, drawData, speed, left, centre)
        Merge_Sort(data_set, drawData, speed, centre+1, right)

        L=data_set[left:centre+1]
        R=data_set[centre+1:right+1]

        for pos in range(left, right+1):
            if (len(L)>0) and (len(R)>0):
                if (L[0]>R[0]):
                    data_set[pos]=R[0]
                    R.pop(0)
                else:
                    data_set[pos]=L[0]
                    L.pop(0)

            elif (len(L)>0):
                data_set[pos]=L[0]
                L.pop(0)
            else:
                data_set[pos]=R[0]
                R.pop(0)

            if (speed!=0):
                if (left==0) and (right==len(data_set)-1):
                    drawData(data_set, ["springGreen" if current_block<=pos and current_block<=right else "red" if current_block==pos else "orchid" for current_block in range(len(data_set))])
                else:
                    drawData(data_set, ["red" if current_block==pos else "orange" if current_block>=left and current_block<=right else "orchid" for current_block in range(len(data_set))])
                sleep(speed)

        if (left==0) and (right==len(data_set)-1) and (speed==0):
            drawData(data_set, ["springGreen" for current_block in range(len(data_set))])
