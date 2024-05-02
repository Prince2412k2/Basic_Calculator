import tkinter as tk

# Function to handle button click event
def greet():
    name = entry.get()  # Get the text entered in the entry widget
    greeting_label.config(text=f"Hello, {name}!")  # Update the label text with the greeting

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Tkinter Tutorial")

# Create an entry widget for user input
entry = tk.Entry(root, width=30)
entry.pack()

# Create a button widget to trigger the greeting
button = tk.Button(root, text="Greet", command=greet)
button.pack()

# Create a label widget to display the greeting
greeting_label = tk.Label(root, text="")
greeting_label.pack()

# Run the Tkinter event loop
root.mainloop()