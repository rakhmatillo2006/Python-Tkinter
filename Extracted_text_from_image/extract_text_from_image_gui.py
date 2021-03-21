from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tooltips_2 import CreateToolTip
from ttkthemes import ThemedTk, THEMES
from PIL import Image
from pytesseract import pytesseract
import os

root = ThemedTk(themebg=True)
root.set_theme('plastik')
root.title('Extract text from image')
root.iconbitmap('D:/python_dars/coding.ico')
root.geometry('500x300+300+200')
root.resizable(False,False)


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def limitsize(*args):
    length = len(kirit.get())
    ga = kirit.index(INSERT)
    if length > 100:
        ending = kirit.index(END)
    if length > 100 and ga!= ending:
        msg.showwarning('Ogohlantirish','Buncha ko\'p nomli faylning manzili bo\'lmaydi!Iltimos qisqa faylning manzilini kiriting@')        
        ga_1 = kirit.index(INSERT)
        kirit.delete(ga_1, ga_1 + 1)
    if length > 100 and ga == ending:
        msg.showwarning('Ogohlantirish','Buncha ko\'p nomli faylning manzili bo\'lmaydi!Iltimos qisqa faylning manzilini kiriting@')
        kirit.delete(100,END)       

def uchirish(e):
    kirit.delete(first=0, last=1245)

def buyruq():       
    if kirit.get() == '':
        msg.showerror('Xato','Fayl manzilini yozmagansiz!')
        kirit.focus()
    elif not os.path.exists(kirit.get()):
        msg.showerror('Xato', 'Bunday fayl mavjud emas, iltimos fayl nomini tekshirib yozing!')
        kirit.delete(first=0, last=1245)
        kirit.focus()    
    else:
        img = Image.open(kirit.get())
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)
        with open('extracted_text_from_image.txt', 'w') as file:
            file.write(text[:-1])

            
    
        
        

kiritish_e = StringVar()
kiritish_e.trace('w', limitsize)

kirit = ttk.Entry(root, style='C.TEntry', textvariable=kiritish_e)
kirit.place(x=250, y=59, width=230)
kirit.focus()
# The Binding section
kirit.bind("<Button-3>", uchirish)

ta = ttk.Label(root, text='Fayl joylashuvini kiriting:', style='C.TLabel', font=("Serif", 12))
ta.place(x=35, y=59)

tugma = ttk.Button(root, text="Olish", style='C.TButton', command=buyruq)
tugma.place(x=290, y=100)
CreateToolTip(tugma, "Rasmdan tekstni olish")






root.mainloop()