# 🧸 Street Children in India
## 🎯 Objective <br>
This project uses data from the National Commission for Protection of Child Rights (NCPCR) and the Child in Street Situations (CISS) Portal on the Baalswaraj platform to analyze the number of street children in India by state and living situation. It processes the dataset in Python and generates bar graphs (unsorted and sorted) using Turtle graphics for clear visualization. <p>
## 🛠️ Tools <br>
• <b>Language:</b> Python <p>
## 📊 Bar Graphs <br>
<img src="https://github.com/redefiningvicky/Street-Children-in-India/blob/e5de99d2a122c11cfbb70276cd74c50e45232add/04_Graph/NCPCR_2023_Graph.png" width="900" />

```
from turtle import *
```
```
# Function to read dataset
def readData():
    with open(r"NCPCR_2023_Dataset.TXT", 'r') as file:
        lines = file.readlines()
    myList = []
    total_line = None
    for line in lines:
        line = line.strip()
        if line:
            if line.startswith("Total"):
                total_line = line
            elif '(' in line and ')' in line:
                name, value = line.split('(')
                value = value.replace(')', '').replace(',', '')
                myList.append((name.strip(), int(value)))
    return myList, total_line
```
<img src="https://github.com/redefiningvicky/Street-Children-in-India/blob/5ccf0fe1f59171fe307bc2b16170e18da303e8f5/04_Graph/BSCiSS_2023_Graph.png" width="900" />

```
def drawBar(name, height, width=40):
    # Get the current position of the turtle before drawing the bar
    start_x, start_y = pos()
    # Draw the bar
    begin_fill()
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)
    end_fill()
```
```
# Function to sort data by value
def sortData(data):
    return sorted(data, key=lambda x: x[1])
```
