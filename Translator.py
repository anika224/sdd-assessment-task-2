from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox


root = Tk()
root.title("translator")
root.geometry("550x280")

c = Canvas(root, width = 550, height = 280, bg = "Lavender")
c.place(x=0, y=0)

def translate_it():
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
           
   
def clear():
    # Clear the text boxes
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

#language_list = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40)

# Grab Language list from GoogleTrans
languages = googletrans.LANGUAGES

# Convert to list
language_list = list(languages.values())

# Text Boxes
original_text = Text(root, height=8, width=20)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate!", font=("Arial", 19), fg = "white", bg = "#87b3fa", command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=8, width=20)
translated_text.grid(row=0, column=2, padx=10)

# Combo Boxes
original_combo = ttk.Combobox(root, width=20, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=20, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)

# Clear Button
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()
