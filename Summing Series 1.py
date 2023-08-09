from tkinter import *
import tkinter as tk


#Main window
root = Tk()
root.title("Summing Series")
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.state("zoomed")

c = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg = "Lavender")
c.place(x=0, y=0)

#Text
my_text = Text(root)


#Creating functions for arithmetic and geometric sum



#Creating labels
label = Label(root)

#Clear button
def clear():

    # e.delete(0, tk.END)

    # e2.delete(0, tk.END)

    # mylabel3.destroy()

    print('do nothing')




#Radio buttons
var = IntVar()
R1 = Radiobutton(root, text="Arithmetic", variable=var, value=1, command=sum)
R1.place(x=220, y=50)

R2 = Radiobutton(root, text="Geometric", variable=var, value=2, command=sum)
R2.place(x=220, y=80)

arithmetic
geometric

#Creating the entry widgets for arithmetic
first_term = Entry(root, width=20)
first_term.place(x=200, y=120)

common_difference = Entry(root, width=20)
common_difference.place(x=225, y=180)

number_of_terms = Entry(root, width=20)
number_of_terms.place(x=200, y=240)
                      
#Creating the entry widgets for geometric
if geometric == True:
    wjgedwoeufgwef
else:
    hide


#Error messages


#Creating menu
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Quit", menu = file_menu, command=root.destroy)

#Text size

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Text size", menu = file_menu)


#Colours


