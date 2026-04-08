# Creating the button layout with list to group them
button_values = [
    ["AC", "+/-", "%", "+"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "÷"],
    ["0", ".", "√", "="]
]

# Operators
right_symbols = ["÷", "×", "-", "+", "="]

# Calculators function
top_symbols = ["AC", "+/-", "%"]

# In case we want to change the button layout in the future
row_count = len(button_values)
column_count = len(button_values[0])

# Colors that was used
color_dark_gray = "#5F6368"
color_gray = "#80868B"
color_black = "#202124"
color_blue = "#4285F4"
color_white = "white"
