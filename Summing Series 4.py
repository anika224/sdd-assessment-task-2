import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from ttkthemes import ThemedStyle
from tkinter import font



#create main window

root = tk.Tk()
root.geometry("400x500")
root.title("Summing Series")

#colour options
def colour_schemes():
    global colour1
    global colour2
    global colour3
    global def_colour
    global colour_options
    global size_options
    #all these variables are used from other functions
    if colour_options==True: #if its already open, clickng the button again closes the colour options
        colour1.place_forget()
        colour2.place_forget()
        colour3.place_forget()
        def_colour.place_forget()
        colour_options=False
    else: #if its not open, it will open now, making variable true
        colour_options=True
    if size_options==True:#if size options are open, close them
        T50.place_forget()
        T100.place_forget()
        T200.place_forget()
        size_options=False
    if language_options==True: #if language options are open, close them
        options.place_forget()
        language_options=False
    #display 4 colour option buttons (B&W, pastel, high con, & default)
    def_colour=Button(root, text="Default", command=def_colour)
    def_colour.place(x=30, y=122)
    colour1=Button(root, text="Black & White", command=colour1)
    colour1.place(x=30, y=40)
    colour2=Button(root, text="Pastel", command=colour2)
    colour2.place(x=30, y=67)
    colour3=Button(root, text="High Contrast", command=colour3)
    colour3.place(x=30, y=95)

def colour1():
    #changes all widgets to shades of white & black
    root.config(bg="black")
    arith_first_term_label.config(bg='#e0dada')
    arith_common_diff_label.config(bg='#e0dada')
    arith_num_of_terms_label.config(bg='#e0dada')
    arithmetic_result_label.config(bg='#e0dada')
    clear_button.config(bg='#e0dada')
    file.config(bg='#e0dada')
    arithmetic_radio.config(bg='#e0dada')
    geometric_radio.config(bg='#e0dada')
    geo_first_term_label.config(bg="White")
    geo_num_of_terms_label.config(bg="White")
    geo_common_ratio_label.config(bg="White")
    geometric_result_label.config(bg="White")


def colour2():
    root.config(bg="#3a393b")
    arith_first_term_label.config(bg='#e0dada')
    arith_common_diff_label.config(bg='#e0dada')
    arith_num_of_terms_label.config(bg='#e0dada')
    arithmetic_result_label.config(bg='#e0dada')
    clear_button.config(bg='#e0dada')
    file.config(bg='#e0dada')
    arithmetic_radio.config(bg='#e0dada')
    geometric_radio.config(bg='#e0dada')
    geo_first_term_label.config(bg="White")
    geo_num_of_terms_label.config(bg="White")
    geo_common_ratio_label.config(bg="White")
    geometric_result_label.config(bg="White")


def colour3():
    #changes all widgets to high contrast coloursroot.config(bg="#3a393b")
    arith_first_term_label.config(bg='White')
    arith_common_diff_label.config(bg='#e0dada')
    arith_num_of_terms_label.config(bg='#e0dada')
    arithmetic_result_label.config(bg='#e0dada')
    clear_button.config(bg='#e0dada')
    file.config(bg='#e0dada')
    arithmetic_radio.config(bg='#e0dada')
    geometric_radio.config(bg='#e0dada')
    geo_first_term_label.config(bg="White")
    geo_num_of_terms_label.config(bg="White")
    geo_common_ratio_label.config(bg="White")
    geometric_result_label.config(bg="White")


def def_colour():
    #changes all widgets to default colours
    root.config(bg="#3a393b")
    arith_first_term_label.config(bg='#e0dada')
    arith_common_diff_label.config(bg='#e0dada')
    arith_num_of_terms_label.config(bg='#e0dada')
    arithmetic_result_label.config(bg='#e0dada')
    clear_button.config(bg='#e0dada')
    file.config(bg='#e0dada')
    arithmetic_radio.config(bg='#e0dada')
    geometric_radio.config(bg='#e0dada')
    geo_first_term_label.config(bg="White")
    geo_num_of_terms_label.config(bg="White")
    geo_common_ratio_label.config(bg="White")
    geometric_result_label.config(bg="White")




def hide_widgets():
    arithmetic_frame.pack_forget()
    geometric_frame.pack_forget()

def quit_app():
    root.quit()


def change_color():
    color = askcolor()[1]
    root.config(bg=color)
    arithmetic_frame.config(bg=color)
    geometric_frame.config(bg=color)
   
    bg_rgb = root.winfo_rgb(color)
    luminance = (0.299 * bg_rgb[0] + 0.587 * bg_rgb[1] + 0.114 * bg_rgb[2]) / 65535
    text_color = "black" if luminance > 0.5 else "white"
   
    style = ThemedStyle(root)
    style.set_theme("clam")
   
    style.configure("TFrame", background=color)
    style.configure("TLabel", foreground=text_color, background=color)
    style.configure("TButton", background=color)
    style.configure("TRadiobutton", foreground=text_color, background=color)

def show_arithmetic_widget():
    hide_widgets()
    arithmetic_frame.pack()
   
def show_geometric_widget():
    hide_widgets()
    geometric_frame.pack()
   

   
def calculate_arithmetic():
    arith_first_term = arith_first_term_entry.get()
    arith_common_diff = arith_common_diff_entry.get()
    arith_num_of_terms = arith_num_of_terms_entry.get()
   
    try:
        result = ((float(arith_num_of_terms))/2)*((2*(float(arith_first_term)))+(float(arith_num_of_terms-1))*(float(arith_common_diff)))
        # result = ((float(arith_num_of_terms))/2)*((2*(float(arith_first_term)))+(float(arith_num_of_terms)-1)*(float(arith_common_diff)))
        arith_result_label.config(text=f"Result: {result}")
       

    except ValueError:
        arith_result_label.config(text= "Please enter valid numbers")
   


def calculate_geometric():
    geo_first_term = geo_first_term_entry.get()
    geo_common_ratio = geo_common_ratio_entry.get()
    geo_num_of_terms = geo_num_of_terms_entry.get()
   
    try:
        result = (float(geo_first_term))*((1-(float(geo_common_ratio))**(float(geo_num_of_terms)))/(1-(float(geo_common_ratio))))
        geo_result_label.config(text=f"Result: {result}")
       
    except ValueError:
            geo_result_label.config(text= "Please enter valid numbers")
   

def clear_entries():
    arith_first_term.delete(0, tk.END)
    arith_common_diff.delete(0, tk.END)
    arith_num_of_terms.delete(0, tk.END)
   
    geo_first_term.delete(0, tk.END)
    geo_common_ratio.delete(0, tk.END)
    geo_num_of_terms.delete(0, tk.END)
   
    arith_result_label.config(text="")
    geo_result_label.config(text="")
   

#def change_font(font_name):
    #text_font = (font_name, 12)
    #arith_first_term_label.config(font=text_font)
    #arith_common_diff_label.config(font=text_font)
    #arith_num_of_terms_label.config(font=text_font)
    #geo_first_term_label.config(font=text_font)
    #geo_common_ratio_label.config(font=text_font)
    #geo_num_of_terms_label.config(font=text_font)
    #arith_calculate_button.config(font=text_font)
    #geo_calculate_button.config(font=text_font)

   
def change_font(font_name):
    text_font = (font_name, 12)
    for label in label_list:
        label.config(font=text_font)






# create a frame for the radiobuttons
radio_var = tk.StringVar()


radio_frame = tk.Frame(root)
radio_frame.pack()

arithmetic_radio = tk.Radiobutton(radio_frame, text = "Arithmetic", variable=radio_var, value="arithmetic", command=show_arithmetic_widget)
geometric_radio = tk.Radiobutton(radio_frame, text = "Geometric", variable=radio_var, value="geometric", command=show_geometric_widget)


arithmetic_radio.pack()
geometric_radio.pack()


#create arithmetic series frame
arithmetic_frame = tk.Frame(root)
arithmetic_frame.pack(padx=20, pady=20)

arith_first_term_label = tk.Label(arithmetic_frame, text="Enter First Term")
arith_first_term_entry = tk.Entry(arithmetic_frame)

arith_common_diff_label = tk.Label(arithmetic_frame, text="Enter Common Difference")
arith_common_diff_entry = tk.Entry(arithmetic_frame)

arith_num_of_terms_label = tk.Label(arithmetic_frame, text="Enter Number of Terms")
arith_num_of_terms_entry = tk.Entry(arithmetic_frame)


arith_calculate_button = tk.Button(arithmetic_frame, text="Calculate", command=calculate_arithmetic)

arith_result_label = tk.Label(arithmetic_frame, text="")


arith_first_term_label.pack()  
arith_first_term_entry.pack(padx=15, pady=15)
                                 
arith_common_diff_label.pack()
arith_common_diff_entry.pack(padx=15, pady=15)
                                   
arith_num_of_terms_label.pack()
arith_num_of_terms_entry.pack(padx=15, pady=15)


arith_calculate_button.pack(padx=20, pady=20)

arith_result_label.pack()



#create geometric series frame
geometric_frame = tk.Frame(root)
geometric_frame.pack()



geo_first_term_label = tk.Label(geometric_frame, text="Enter First Term")
geo_first_term_entry = tk.Entry(geometric_frame)

geo_common_ratio_label = tk.Label(geometric_frame, text="Enter Common Ratio")
geo_common_ratio_entry = tk.Entry(geometric_frame)

geo_num_of_terms_label = tk.Label(geometric_frame, text="Enter Number of Terms")
geo_num_of_terms_entry = tk.Entry(geometric_frame)


geo_calculate_button = tk.Button(geometric_frame, text="Calculate", command=calculate_geometric)

geo_result_label = tk.Label(geometric_frame, text="")


geo_first_term_label.pack()  
geo_first_term_entry.pack(padx=15, pady=15)
                                 
geo_common_ratio_label.pack()
geo_common_ratio_entry.pack(padx=15, pady=15)
                                   
geo_num_of_terms_label.pack()
geo_num_of_terms_entry.pack(padx=15, pady=15)


geo_calculate_button.pack(padx=15, pady=15)

geo_result_label.pack()


#create a font menu

menu_bar_font = tk.Menu(root)
root.config(menu=menu_bar_font)
font_menu = tk.Menu(menu_bar_font, tearoff=0)
menu_bar_font.add_cascade(label="Font", menu=font_menu)


# Create a font menu
#menu_bar_font = tk.Menu(root)
#root.config(menu=menu_bar_font)
#font_menu = tk.Menu(menu_bar_font, tearoff=0)
#menu_bar_font.add_cascade(label="Font", menu=font_menu)
#font_menu.add_command(label="Change Font", command=change_font)

# List of font families
font_families = font.families()

# Create a list to store labels that should have their font changed
label_list = [arith_first_term_label, arith_common_diff_label, arith_num_of_terms_label,
              geo_first_term_label, geo_common_ratio_label, geo_num_of_terms_label,
              arith_calculate_button, geo_calculate_button]

# Add fonts to the menu
for font_name in font_families:
    font_menu.add_command(label=font_name, command=lambda font_name=font_name: change_font(font_name))

# Create a submenu for font selection
#font_submenu = tk.Menu(font_menu, tearoff=0)

# Add the submenu to the font menu
#font_menu.add_cascade(label="Font", menu=font_submenu)





#clear and quit button
clear_button = tk.Button(root, text="Clear", command=clear_entries)

quit_button = tk.Button(root, text="Quit", command=quit_app)

clear_button.pack(side=tk.BOTTOM, padx=5, pady=20)

quit_button.pack(side=tk.BOTTOM, padx=5, pady=20)


#hide widget/s

hide_widgets()








#menu with different colours
menu_bar_colour = tk.Menu(root)
root.config(menu=menu_bar_colour)

color_menu = tk.Menu(menu_bar_colour, tearoff=0)
menu_bar_colour.add_cascade(label="Colour", menu=color_menu)
color_menu.add_command(label="Choose Color", command=change_color)









root.mainloop()
