import customtkinter as ctk

# Colors
color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

# Button layout
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

# Calculator state
A = "0"
operator = None
B = None

# Appearance
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Window setup
window = ctk.CTk()
window.title("Calculator")
window.resizable(False, False)

frame = ctk.CTkFrame(window)
label = ctk.CTkLabel(
    frame,
    text="0",
    font=("Arial", 45),
    fg_color=color_black,
    text_color=color_white,
    anchor="e",
    width=350,
    height=70
)
label.grid(row=0, column=0, columnspan=4, sticky="we")
frame.pack()

# Clear function


def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None
    label.configure(text="0")

# Button click handler


def button_clicked(value):
    global A, B, operator
    current_text = label.cget("text")

    if value == "AC":
        clear_all()

    elif value == "+/-":
        if current_text.startswith("-"):
            label.configure(text=current_text[1:])
        else:
            label.configure(text="-" + current_text)

    elif value == "%":
        try:
            percent = float(current_text) / 100
            if percent.is_integer():
                percent = int(percent)
            label.configure(text=str(percent))
        except:
            label.configure(text="Error")

    elif value == "√":
        try:
            result = float(current_text) ** 0.5
            if result.is_integer():
                result = int(result)
            label.configure(text=str(result))
        except:
            label.configure(text="Error")

    elif value in ["+", "-", "×", "÷"]:
        operator = value
        A = current_text
        label.configure(text="0")

    elif value == "=":
        B = current_text
        try:
            if operator == "+":
                result = float(A) + float(B)
            elif operator == "-":
                result = float(A) - float(B)
            elif operator == "×":
                result = float(A) * float(B)
            elif operator == "÷":
                result = float(A) / float(B)
            else:
                result = float(B)

            if result.is_integer():
                result = int(result)

            label.configure(text=str(result))
        except:
            label.configure(text="Error")

    else:
        if current_text == "0" and value != ".":
            new_text = value
        else:
            new_text = current_text + value

        if value == "." and "." in current_text:
            new_text = current_text

        label.configure(text=new_text)

    # Adjust font size
    length = len(label.cget("text"))
    if length <= 10:
        label.configure(font=("Arial", 45))
    elif length <= 15:
        label.configure(font=("Arial", 35))
    elif length <= 20:
        label.configure(font=("Arial", 25))
    else:
        label.configure(font=("Arial", 18))


# Button creation
for row in range(len(button_values)):
    for column in range(len(button_values[0])):
        value = button_values[row][column]
        bg = color_dark_gray
        fg = color_white
        if column == 3:
            bg = color_orange
        elif value in top_symbols:
            bg = color_light_gray
            fg = color_black

        button = ctk.CTkButton(
            frame,
            text=value,
            font=("Arial", 30),
            width=80,
            height=60,
            command=lambda value=value: button_clicked(value),
            fg_color=bg,
            text_color=fg
        )
        button.grid(row=row+1, column=column, padx=2, pady=2)

# Center window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(
    f"{window_width}x{window_height}+{int((screen_width-window_width)/2)}+{int((screen_height-window_height)/2)}")

# Start app
window.mainloop()
