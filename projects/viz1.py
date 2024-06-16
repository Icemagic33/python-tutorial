import tkinter as tk

# Function to change the background color


def change_color():
    global color_index
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    if color_index >= len(colors):
        color_index = 0
    color_label.config(bg=colors[color_index])
    color_index += 1


# Setting up the main window
root = tk.Tk()
root.title('Color Changer')

# Initial color index
color_index = 0

# Create a label with initial background color
color_label = tk.Label(root, text='Click the button to change my color!', font=(
    'Helvetica', 16), width=80, height=5)
color_label.pack(pady=20)

# Create a button that changes the color of the label
change_button = tk.Button(root, text='Change Color',
                          command=change_color, font=('Helvetica', 14))
change_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
