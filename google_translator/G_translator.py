# Import necessary modules from tkinter and googletrans
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Function to perform translation
def change(text="type", src="English", dest="Hindi"):
    # Set the text, source, and destination languages
    text1 = text
    src1 = src
    dest1 = dest
    
    # Initialize the Translator object
    trans = Translator()
    
    # Perform translation and return the translated text
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

# Function to get input from the user, perform translation, and display result
def data():
    # Get the selected source and destination languages from the comboboxes
    s = combo_sor.get()
    d = combo_dest.get()
    
    # Get the source text entered by the user
    msg = sor_txt.get(1.0, END)
    
    # Call the change function to translate the text
    textget = change(text=msg, src=s, dest=d)
    
    # Clear the destination text box and insert the translated text
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

# Initialize the Tkinter window
root = Tk()
root.title("Translator")  # Set the window title
root.geometry("500x700")  # Set the window size
root.config(bg='Red')  # Set the background color of the window

# Label to display the title "Translator"
lab_txt = Label(root, text="Translator", font=("Time New Roman", 40, "bold"))
lab_txt.place(x=100, y=40, height=50, width=300)

# Create a frame to hold the text boxes and buttons
frame = Frame(root).pack(side=BOTTOM)

# Label to indicate where the source text should be entered
lab_txt = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"), fg="black", bg='Red')
lab_txt.place(x=100, y=100, height=20, width=300)

# Text widget for the user to enter source text
sor_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)
sor_txt.place(x=10, y=130, height=150, width=480)

# List of supported languages from googletrans
list_txt = list(LANGUAGES.values())

# Combobox to select the source language
combo_sor = ttk.Combobox(frame, value=list_txt)
combo_sor.place(x=10, y=300, height=40, width=150)
combo_sor.set("English")  # Default source language is English

# Button to trigger the translation when clicked
button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=100)

# Combobox to select the destination language
combo_dest = ttk.Combobox(frame, value=list_txt)
combo_dest.place(x=360, y=300, height=40, width=150)
combo_dest.set("English")  # Default destination language is English

# Label to indicate where the translated text will be displayed
lab_txt = Label(root, text="Destination Text", font=("Time New Roman", 20, "bold"), fg="black", bg='Red')
lab_txt.place(x=100, y=360, height=20, width=300)

# Text widget to display the translated text
dest_txt = Text(frame, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

# Start the Tkinter main loop to display the window
root.mainloop()
