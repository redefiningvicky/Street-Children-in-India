from turtle import *

# Function to read dataset
def readData():
    with open(r"C:/Users/redef/OneDrive/Desktop/Github - Vicky/Street_Children_in_India/02_Dataset/NCPCR_2023_Dataset.TXT", 'r') as file:
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
    
    # Calculate the positions for the labels
    label_x = start_x + (width / 2)
    name_y = start_y + height + 250
    height_y = start_y + height + 50

    # Move to the correct position for the name and write it
    penup()
    goto(label_x, name_y)
    write(f"{name}", align="center", font=("Arial", 10, "bold"))
    # Move to the correct position for the height and write it
    goto(label_x, height_y)
    write(f"{height}", align="center", font=("Arial", 10, "normal"))
    # Return the turtle to the starting point of the next bar
    goto(start_x + width + 10, start_y)
    pendown()

# Function to sort data by value
def sortData(data):
    return sorted(data, key=lambda x: x[1])

# Function to draw graph on a given screen
def drawGraph(data, title, screen):
    numBars = len(data)
    maxheight = max([height for _, height in data])
    top_margin = maxheight * 0.3 + 50
    bottom_margin = 50
    
    # Clear previous drawing
    screen.clearscreen()  
    
    # Calculate the total width of the bars and add extra space for the title
    bar_width = 60
    gap_width = 15
   
    # Calculate the total width of the graph dynamically
    bars_total_width = (bar_width + gap_width) * numBars
    graph_width = bars_total_width + 150
    
    # Set coordinates so the bars and title fit proportionally
    screen.setworldcoordinates(-graph_width / 2, 0, graph_width / 2, maxheight + top_margin + bottom_margin)
    screen.title(title)
    speed('fastest')
    penup()
    
    # Draw title centered horizontally at the top of the window
    goto(0, maxheight + bottom_margin + top_margin - 20)
    write(title, align="center", font=("Arial", 16, "bold"))
    
    # Draw bars
    goto(-(bars_total_width / 2), bottom_margin)
    pendown()
    for name, height in data:
        drawBar(name, height, width=bar_width)
        penup()
        forward(gap_width)
        pendown()

def main():
    data, total_line = readData()
    print("Unsorted data:")
    for name, height in data:
        print(f"{name}: {height}")
    print(total_line)
    
    # Create one screen for both graphs
    screen = Screen()

    # Draw unsorted graph
    drawGraph(data, "Children Living on the Streets With or Without Parents in Select States of India, 2023 (Unsorted)", screen)

    # Automatically switch to sorted graph
    sorted_data = sortData(data)
    print("\nSorted data:")
    for name, height in sorted_data:
        print(f"{name}: {height}")

    # Draw sorted graph immediately after
    drawGraph(sorted_data, "Children Living on the Streets With or Without Parents in Select States of India, 2023 (Sorted)", screen)

    # Keep window open until user closes
    screen.mainloop()

if __name__ == "__main__":
    main()