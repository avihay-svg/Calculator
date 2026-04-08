import tkinter
from constants import *
import logic


# The ma# The main calculator function
def button_clicked(value):
    global label
    if value in right_symbols:
        if value == "=":
            if logic.operator is not None:
                logic.B = label["text"]
                numA = float(logic.A)
                numB = float(logic.B)

                if logic.operator == "+":
                    label["text"] = logic.remove_zero_decimal(numA + numB)
                elif logic.operator == "-":
                    label["text"] = logic.remove_zero_decimal(numA - numB)
                elif logic.operator == "×":
                    label["text"] = logic.remove_zero_decimal(numA * numB)
                elif logic.operator == "÷":
                    if numB == 0:
                        label["text"] = "Error"
                    else:
                        label["text"] = logic.remove_zero_decimal(numA / numB)
                logic.is_result = True
                logic.clear_all()

        elif value in "+-×÷":
            logic.A = label["text"]
            label["text"] = "0"
            logic.B = "0"
            logic.operator = value

    elif value in top_symbols:
        if value == "AC":
            logic.clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = logic.remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = logic.remove_zero_decimal(result)
            logic.is_result = True

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
                label["text"] = logic.remove_zero_decimal(result)
        elif value in "0123456789":
            if logic.is_result:
                label["text"] = value
                logic.is_result = False
            elif label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value


# Window setup
window = tkinter.Tk()
window.title("calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_blue,
                      foreground=color_white, anchor="e", width=column_count)
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

# Layout Building
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,
                                command=lambda v=value: button_clicked(v))
        if value in top_symbols:
            button.config(foreground=color_white, background=color_black)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_dark_gray)
        else:
            button.config(foreground=color_white, background=color_gray)
        button.grid(row=row+1, column=column)

frame.pack()

# Center window logic
window.update()
window_width, window_height = window.winfo_width(), window.winfo_height()
screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
