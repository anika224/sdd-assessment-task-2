from tkinter import *
import tkinter as tk
import googletrans
import textblob
from tkinter import ttk, messagebox

root = Tk()
root.title("Arithmetic Operations")
root.geometry("400x400")

c = Canvas(root, width = 500, height = 500, bg = "Lavender")
c.place(x=0, y=0)

#Create Functions
def add():
    global mylabel3
    sum = int(e1.get()) + int(e2.get())
    mylabel3 = Label(root, text = "Sum of two numbers is : " + str(sum))
    mylabel3.place(x=120, y=250)

def subtract():
    global mylabel3
    difference = int(e1.get()) - int(e2.get())
    mylabel3 = Label(root, text = "Difference of two numbers is : " + str(difference))
    mylabel3.place(x=120, y=250)
    
def divide():
    global mylabel3
    quotient = int(e1.get()) / int(e2.get())
    mylabel3 = Label(root, text = "Quotient of two numbers is : " + str(quotient))
    mylabel3.place(x=120, y=250)

def multiply():
    global mylabel3
    product = int(e1.get()) * int(e2.get())
    mylabel3 = Label(root, text = "Product of two numbers is : " + str(product))
    mylabel3.place(x=120, y=250)

def clear():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    mylabel3.place_forget()


#Create Labels
my_label = Label(root, text = "Enter Number 1:", relief = GROOVE, fg = "white", bg = "#87b3fa")
my_label.place(x=75, y=50)

my_label2 = Label(root, text = "Enter Number 2:", relief = GROOVE, fg = "white", bg = "#87b3fa")
my_label2.place(x=75, y=90)

my_label4 = Label(root, text = "Choose an option: ", relief = GROOVE, fg = "white", bg = "#87b3fa")
my_label4.place(x=75, y=180)

#Create entry widget
e1 = Entry(root, width=20)
e1.place(x=200, y=50)

e2 = Entry(root,width=20)
e2.place(x=200, y=90)

#Clear button
my_button1 = Button(root, text = "Clear", command = clear)
my_button1.place(x=150, y=350)

#radio button
var = IntVar()
R1 = Radiobutton(root, text="Sum", variable=var, value=1, command=add)
R1.place(x=220, y=150)

R2 = Radiobutton(root, text="Subtract", variable=var, value=2, command=subtract)
R2.place(x=220, y=170)

R3 = Radiobutton(root, text="Divide", variable=var, value=3, command=divide)
R3.place(x=220, y=190)

R4 = Radiobutton(root, text="Multiply", variable=var, value=4, command=multiply)
R4.place(x=220, y=210)


#Create a function for translator
def translate_command():
     # Delete Any Previous Translations
    translated_text.delete(1.0, END)
   
    try:
        # Get Languages From Dictionary Keys
        # Get the From Language Key
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key

        # Get the To Language Key
        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key
               
        # Turn Original Text into a TextBlob
        words = textblob.TextBlob(original_text.get(1.0, END))

        # Translate Text
        words = words.translate(from_lang=from_language_key , to=to_language_key)

        # Output translated text to screen
        translated_text.insert(1.0, words)
        
    except Exception as e:
        messagebox.showerror("Translator", e)
b

#Create menu for translator
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu = file_menu)
file_menu.add_command(label="Translator", command=translate_command)
file_menu.add_separator()



root.mainloop()
