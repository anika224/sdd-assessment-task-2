from tkinter import *

from tkinter import ttk

 

def sel():

   selection = "You selected the option " + str(var.get())

   label.config(text = selection)

 

 

 

# PART1: Crate master window

root = Tk()

frm = ttk.Frame(root, padding=50)

frm.grid()



# Create radio buttons for selection

var = IntVar()

R1 = Radiobutton(root, text="Arithmetic", variable=var, value=1,

                  command=sel)

R1.grid(column=0,row=1)

# R1.pack( anchor = W )

 

R2 = Radiobutton(root, text="Geometric", variable=var, value=2,

                  command=sel)

# R2.pack( anchor = W )

R2.grid(column=1,row=1)

 

 

# PART2:based on the selection get input and show output

 

labelFirstTerm = Label(root, text="Enter The First term", fg="black", bg="#BE93D4", relief="groove", font=("Arial", 12),)

labelFirstTerm.grid(column=1,row=2)

 

labelCommonDiff = Label(root, text="cd", fg="black", bg="#BE93D4", relief="groove", font=("Arial", 12),)

labelCommonDiff.grid(column=3,row=2)

 

labelNumTerms = Label(root, text="n", fg="black", bg="#BE93D4", relief="groove", font=("Arial", 12),)

labelNumTerms.grid(column=5,row=2)

 

 

 

# PART3: Crate  clear and quit button at the end

def clear():

    # e.delete(0, tk.END)

    # e2.delete(0, tk.END)

    # mylabel3.destroy()

    print('do nothing')

 

qtButton = ttk.Button(frm, text="Quit", command=root.destroy)

qtButton.grid(column=0, row=5)

 

clrButton = ttk.Button(frm, text="Clear", command=clear)

clrButton.grid(column=3, row=5)

 

 

 

label = Label(root)

# label.pack()

root.mainloop()
