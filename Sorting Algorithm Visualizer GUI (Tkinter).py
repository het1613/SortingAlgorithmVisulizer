#Het Patel
#Sorting Algorithm Visualizer Using Tkinter
#26/10/20

#Function to create all the rectangle blocks (represent the data)
def drawData(data_set, block_colours):
    global max_height, start
    Data_Bars.delete("all")
    c_height=380
    c_width=1195
    x_width=c_width/(len(data_set))

    if (len(data_set)<=30): spacing=10
    elif (len(data_set)<=60): spacing=7
    elif (len(data_set)<=100): spacing=5
    elif (len(data_set)<=200): spacing=3

    dataBlockHeight=[num/max_height for num in data_set]

    for current_block in range(len(dataBlockHeight)):
        height=dataBlockHeight[current_block]

        x0=current_block*x_width+spacing
        y0=c_height-height*340
        x1=(current_block+1)*x_width
        y1=c_height
        center_x=((x1+x0)//2)-4

        Data_Bars.create_rectangle(x0, y0, x1, y1, fill=block_colours[current_block])

        if len(data_set)<=60:
            Data_Bars.create_text(center_x, y0, anchor=SW, text=str(data_set[current_block]), font=('Fixedsys', 4))

    window.update_idletasks()

    if flag:
        Label(button_layout, text="Time: Start Sorting First       ", bg='DeepSkyBlue', fg='black', font=("Fixedsys", 12)).grid(row=0, column=2, padx=5, pady=5, sticky=W)
    else:
        stopwatch=time()-start
        Label(button_layout, text="Time So Far: {:.2f}s             ".format(stopwatch), bg='DeepSkyBlue', fg='black', font=("Fixedsys", 12)).grid(row=0, column=2, padx=5, pady=5, sticky=W)

#Function to create a random list of integers from some minimum and maximum value (function executed when 'Generate Data' button pressed)
def Generate():
    global data_set, max_height, flag
    minVal=int(minSlider.get())
    maxVal=int(maxSlider.get())
    size=int(sizeSlider.get())
    flag=True

    data_set=[randint(minVal, maxVal) for num in range(size)]

    max_height=max(data_set)

    drawData(data_set, ['orchid' for color in range(size)])

#Function to start the sorting of the data (function executed when 'Start Sorting' button pressed)
def ExecuteSort():
    global data_set, start, flag

    speed=speedSlider.get()
    flag=False

    start=time()

    if (Algorithm_DropDown.get()=='Bubble Sort'): Bubble_Sort(data_set, drawData, speed)

    elif (Algorithm_DropDown.get()=='Merge Sort'): Merge_Sort(data_set, drawData, speed, 0, len(data_set)-1)

    elif (Algorithm_DropDown.get()=='Selection Sort'): Selection_Sort(data_set, drawData, speed)

    elif (Algorithm_DropDown.get()=='Insertion Sort'): Insertion_Sort(data_set, drawData, speed)

    elif (Algorithm_DropDown.get()=='Shell Sort'): Shell_Sort(data_set, drawData, speed)

    elif (Algorithm_DropDown.get()=='Cocktail Sort'): Cocktail_Sort(data_set, drawData, speed)

    elif (Algorithm_DropDown.get()=='Comb Sort'): Comb_Sort(data_set, drawData, speed)

    elif (Algorithm_DropDown.get()=='Quick Sort'): Quick_Sort(data_set, 0, len(data_set)-1, drawData, speed)

    stopwatch=time()-start
    Label(button_layout, text="Time To Complete Sorting: {:.2f}s".format(stopwatch), bg='DeepSkyBlue', fg='black', font=("Fixedsys", 12)).grid(row=0, column=2, padx=5, pady=5, sticky=W)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Importing all nesseary functions from libraries/modules
from tkinter import *
from tkinter import ttk
from random import randint
from time import time
from algorithms/BubbleSort import Bubble_Sort
from MergeSort import Merge_Sort
from SelectionSort import Selection_Sort
from InsertionSort import Insertion_Sort
from ShellSort import Shell_Sort
from CocktailSort import Cocktail_Sort
from CombSort import Comb_Sort
from QuickSort import Quick_Sort

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Main GUI Initialization
window=Tk()
window.title('Sorting Algorithm Visualizer (By: Het Patel)')
window.maxsize(1225, 610)
window.config(bg='DeepSkyBlue')

#Frame For Title
title_layout=Frame(window, width=650, height=50, bg='DeepSkyBlue')
title_layout.grid(row=0, column=0, padx=10, pady=5)

#Frame For Sorting Algorithm Selection
alg_layout=Frame(window, width=650, height=50, bg='DeepSkyBlue')
alg_layout.grid(row=1, column=0, padx=10, pady=5)

#Frame For Value Sliders and Buttons
slider_layout=Frame(window, width=650, height=75, bg='DeepSkyBlue')
slider_layout.grid(row=2, column=0, padx=10, pady=5)

button_layout=Frame(window, width=650, height=75, bg='DeepSkyBlue')
button_layout.grid(row=3, column=0, padx=10, pady=5)

#Frame For Data Blocks
Data_Bars=Canvas(window, width=1200, height=380, bg='white')
Data_Bars.grid(row=4, column=0, padx=10, pady=8)

#Initializing Variables
algorithm=StringVar()
data_set=[]
start=0
flag=True

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#User Interface Area
#Title
Label(title_layout, text="Sorting Algorithm Visualizer By Het Patel", bg='DeepSkyBlue', fg='black', font=("Fixedsys", 17, 'bold')).grid(row=0, column=0, padx=5, pady=5, sticky=W)

#Algorithm Dropdown
Label(alg_layout, text="      Sorting Algorithm: ", bg='DeepSkyBlue', fg='black', font=("Fixedsys", 12)).grid(row=0, column=0, padx=5, pady=5, sticky=W)
Algorithm_DropDown=ttk.Combobox(alg_layout, textvariable=algorithm, values=['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Insertion Sort', 'Comb Sort', 'Shell Sort', 'Cocktail Sort', 'Selection Sort'], font=("Fixedsys", 8), width=17)
Algorithm_DropDown.grid(row=0, column=1, padx=5, pady=5)
Algorithm_DropDown.current(0)
Label(alg_layout, text=" "*37, bg='DeepSkyBlue', fg='black', font=("Fixedsys", 8)).grid(row=0, column=2, padx=5, pady=5, sticky=W)

#Data Size Slider
sizeSlider=Scale(slider_layout, from_=3, to=200, resolution=1, orient=HORIZONTAL, label="Data Size", font=("Fixedsys", 8), length=110)
sizeSlider.set(50)
sizeSlider.grid(row=0, column=0, padx=5, pady=5, sticky=W)

#Minimum Data Value Slider
minSlider=Scale(slider_layout, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value", font=("Fixedsys", 8), length=110)
minSlider.set(1)
minSlider.grid(row=0, column=1, padx=5, pady=5, sticky=W)

#Maximum Data Value Slider
maxSlider=Scale(slider_layout, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value", font=("Fixedsys", 8), length=110)
maxSlider.set(99)
maxSlider.grid(row=0, column=2, padx=5, pady=5, sticky=W)

#Sorting Speed Value Slider
speedSlider=Scale(slider_layout, from_=0.000, to=2.0, length=200, digits=4, resolution=0.002, orient=HORIZONTAL, label="Sorting Speed [s]", font=("Fixedsys", 8))
speedSlider.set(0.004)
speedSlider.grid(row=0, column=3, padx=5, pady=5)

#Buttons
Button(button_layout, text="Generate Data", command=Generate, bg='orange', font=("Fixedsys", 8)).grid(row=0, column=0, padx=5, pady=5)
Button(button_layout, text="Start Sorting", command=ExecuteSort, bg='SpringGreen', font=("Fixedsys", 8)).grid(row=0, column=1, padx=5, pady=5)
Label(button_layout, text=" "*19, bg='DeepSkyBlue').grid(row=0, column=3, padx=5, pady=5, sticky=W)

#Calls Generate() function to start the program with some random data. The user can generate the data again if they wish later
Generate()

window.mainloop()
