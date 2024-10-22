from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Relogio Digital')
def time():
    string_time = strftime('%H:%M:%S %p')
    lbl.config(text = string_time)
    lbl.after(1000, time)
lbl = Label(root, font= ('open-sans', 50, 'bold'), background= 'black', foreground= 'white')
lbl.pack(anchor='center')
time()
mainloop()
