#Ormiston Computing Project
#Version 1
#Author: Ron Ruaro

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.geometry("1920x1080")
root.iconbitmap('OSC_Icon.ico')
root.title("Ormiston Computing")

class Get_Info:

    def __init__(self, master):
        landing_frame = Frame(master)
        landing_frame.pack(anchor='center')

        self.Label_1 = Label(master, text="Ormiston Computing", font=('Mati', 40))
        self.Label_1.pack()

        self.label_2 = Label(master, text='Before we begin, pelase eneter your name:', font=('Calibri', 15))
        self.label_2.pack(padx=(10, 10), pady=(10, 10))

        self.name_entry = Entry(master)
        self.name_entry.pack(ipady=10, ipadx=50)

        self.next_button = Button(master, text='Next', command=self.select_diff)
        self.next_button.pack()

    def select_diff(self):
        print("Select difficulty.")



e = Get_Info(root)

root.mainloop()