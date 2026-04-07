import tkinter

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

color_dark_gray = "#5F6368"
color_gray = "#80868B"
color_black = "#202124"
color_blue = "#4285F4"
color_white = "white"


# Window setup
window = tkinter.Tk()
window.title("calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)

# Defining the lable properties
label = tkinter.Label(frame, text="0", font=(
    "Arial", 45), background=color_blue, foreground=color_white, anchor="e", width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

# Going through each row and column and creating the button layout
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=color_white,
                          background=color_black)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_dark_gray)
        else:
            button.config(foreground=color_white, background=color_gray)
        button.grid(row=row+1, column=column)
frame.pack()

A = 0
operator = None
B = None


# Clear all function
def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None


# Removing decimal in case the number has none
def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


# The main calculator function
def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    if numB == 0:
                        label["text"] = "Error"
                    else:
                        label["text"] = remove_zero_decimal(numA / numB)

                clear_all()

        elif value in "+-×÷":
            A = label["text"]
            label["text"] = "0"
            B = "0"
            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    else:  # digits or . or √
        if value == ".":
            if value not in label["text"]:
                label["text"] += value

        elif value == "√":
            num = float(label["text"])
            if num < 0:
                label["text"] = "Error"
            else:
                result = float(label["text"]) ** 0.5
                label["text"] = remove_zero_decimal(result)

        elif value in "0123456789":
            if label["text"] == "0":  # In case 0 is first
                label["text"] = value  # replace 0
            else:
                label["text"] += value  # append digit


# Center the window
window.update()  # Update window with new measurements
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculating the correct screen measurement
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# Format "(w) x (h) +(x) + (y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()
