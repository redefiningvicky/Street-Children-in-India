from turtle import *
import time

# Function to read dataset
def readData():
    with open(r"C:\Users\redef\OneDrive\Desktop\Street_Children_in_India\BSCiSS_2023_Dataset.TXT", 'r') as file:
        lines = file.readlines()
    myList = []
    # Loop through each line in the file
    for line in lines:
        line = line.strip()
        # Check if the line is not empty and contains data in the expected format
        if line and '(' in line and ')' in line:
            name, value_str = line.split('(')
            # Remove the closing parenthesis and comma, then convert to integer
            value = int(value_str.replace(')', '').replace(',', ''))
            myList.append((name.strip(), value))
    return myList

def drawBar(name, height, width=40, font_size=8):
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
    name_y = start_y + height + 1000  # Reduced margin
    height_y = start_y + height + 100  # Place the height closer to the bar
    # Move to the correct position for the name and write it
    penup()
    goto(label_x, name_y)
    write(f"{name}", align="center", font=("Arial", font_size, "bold"))
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
    bar_width = 300
    gap_width = 100
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
        # Pass a smaller font size to drawBar for the names
        drawBar(name, height, width=bar_width, font_size=8)
        penup()
        forward(gap_width)
        pendown()

def main():
    data = readData()
    print("Unsorted data:")
    for name, height in data:
        print(f"{name}: {height}")

    # Create one screen for both graphs
    screen = Screen()

    # Draw unsorted graph
    drawGraph(data, "Street Children in India by Living Situation, 2023 (Unsorted)", screen)

    # Automatically switch to sorted graph
    sorted_data = sortData(data)
    print("\nSorted data:")
    for name, height in sorted_data:
        print(f"{name}: {height}")

    # Draw sorted graph immediately after
    drawGraph(sorted_data, "Street Children in India by Living Situation, 2023 (Sorted)", screen)

    # Keep window open until user closes
    screen.mainloop()

if __name__ == "__main__":
    main()