import tkinter as tk
from tkinter import ttk
from tkinter import font
from functools import partial






#create main window

root = tk.Tk()
root.geometry("400x500")
root.title("Summing Series")



def hide_widgets():
    arithmetic_frame.pack_forget()
    geometric_frame.pack_forget()
   

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
        result = ((float(arith_num_of_terms))/2)*((2*(float(arith_first_term)))+(float(arith_num_of_terms)-1)*(float(arith_common_diff)))

       
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
    arith_first_term_entry.delete(0, tk.END)
    arith_common_diff_entry.delete(0, tk.END)
    arith_num_of_terms_entry.delete(0, tk.END)
   
    geo_first_term_entry.delete(0, tk.END)
    geo_common_ratio_entry.delete(0, tk.END)
    geo_num_of_terms_entry.delete(0, tk.END)
   
    arith_result_label.config(text="")
    geo_result_label.config(text="")



def change_font(font_name, widgets_to_configure):
    global text_size
    text_font = (font_name, text_size)
    for widget in widgets_to_configure:
        widget.config(font=text_font)



def change_theme(theme_name, widgets_to_configure):
    theme = theme_colors.get(theme_name)
    if theme:
        for widget in widgets_to_configure:
            widget.config(bg=theme["bg"], fg=theme["fg"])
    if theme:
        root.config(bg=theme["bg"])
        radio_frame.config(bg=theme["bg"])
        arithmetic_frame.config(bg=theme["bg"])
        geometric_frame.config(bg=theme["bg"])
        arith_first_term_label.config(bg=theme["bg"], fg=theme["fg"])

def set_text_size(size, widgets_to_configure):
    global text_size
    text_size = size
    for widget in widgets_to_configure:
        widget.config(font=(widget.cget("font")[0], text_size))

#def change_theme(theme_name):
    #theme = theme_colors.get(theme_name)
   

def create_menu(root):
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
   
   
    parent_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Edit", menu=parent_menu)
   
   
    font_menu = tk.Menu(parent_menu, tearoff=0)
    parent_menu.add_cascade(label="Font", menu=font_menu)
   
    font_families = font.families()
   
    for font_name in font_families:
        font_menu.add_command(label=font_name, command=partial(change_font, font_name, widgets_to_configure))
   
   
    theme_menu = tk.Menu(parent_menu, tearoff=0)
    parent_menu.add_cascade(label="Themes", menu=theme_menu)
   
    for theme_name in theme_colors:
        theme_menu.add_command(label=theme_name, command=lambda theme_name=theme_name: change_theme(theme_name, widgets_to_configure))

    text_size_menu = tk.Menu(parent_menu, tearoff=0)
    parent_menu.add_cascade(label="Text Size", menu=text_size_menu)
   
    text_sizes = [10, 12, 14, 16]  # Define text size options
    for size in text_sizes:
        text_size_menu.add_command(label=str(size), command=lambda size=size: set_text_size(size, widgets_to_configure))



   



def quit_app():
    root.quit()              


text_size = 12

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



#hide widget/s

hide_widgets()


#clear and quit button
clear_button = tk.Button(root, text="Clear", command=clear_entries)
clear_button.pack(side=tk.BOTTOM, padx=5, pady=20)

quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack(side=tk.BOTTOM, padx=5, pady=20)



#making a list of all the widgets to configure for fonts
widgets_to_configure = [arith_first_term_label,
    arith_common_diff_label,
    arith_num_of_terms_label,
    arithmetic_radio,
    geometric_radio,
    arith_first_term_entry,
    arith_common_diff_entry,
    arith_num_of_terms_entry,
    arith_calculate_button,
    arith_result_label,
    geo_common_ratio_label,
    geo_num_of_terms_label,
    geo_first_term_entry,
    geo_common_ratio_entry,
    geo_num_of_terms_entry,
    geo_calculate_button,
    geo_result_label,
    clear_button,
    quit_button]


theme_colors = {
    "Default": {"bg": "white", "fg": "black"},
    "Dark": {"bg": "black", "fg": "white"},
    "Blue": {"bg": "blue", "fg": "red"},
    # Add more themes here
}
















create_menu(root)

root.mainloop()
