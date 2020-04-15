from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

def main():
    root= Tk()
    app = screen1(root)


class screen1:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurante Login Manager")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='black')
        self.frame.pack()

        self.Username= StringVar()
        self.Password= StringVar()

        self. lblTitle= Label(self.frame, text= 'Restaurant Login Manager', font=('arial', 50,'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, Column=0, columnspan=2, pady=40)


        self.btnLogin = Button(self.frame, text= 'Login',width= 17, command=self.new_screen)
        self.btnLogin.grid(row=3, column=0)

        self.btnReset = Button(self.frame, text='Reset', width=17, command=self.new_screen)
        self.btnReset.grid(row=3, column=1)

        self.btnExit = Button(self.frame, text='Exit', width=17, command=self.new_screen)
        self.btnExit.grid(row=3, column=3)



    def new_screen(self):
        self.newscreen = Toplevel(self.master)
        self.app = screen2(self.newscreen)

class screen2:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurante Manager")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='cadet blue')
        self.frame = Frame(self.master, bg='black')
        self.frame.pack()


if main == '__main__':
    main()