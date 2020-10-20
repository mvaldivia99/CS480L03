# Michell Valdivia
# CS 480 Lab 3


# This file contains the UI for the calculator

import tkinter as tk
from MyParser import MyParser 

# throwaway filler function to be changed
def foo():
    print(foo)


class Application(tk.Frame):
    # set up the main window
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("275x400")
        self.mathParser = MyParser()
        self.create_widgets()        
        
    def create_widgets(self):

        # set up the entry, where user input will be captured
        appStr = tk.StringVar()
        appEntry = tk.Entry(self.master)
        appEntry.place(x=20, y=25)

        # for user validation
        # If the call was due to an insertion or deletion
        # %S argument will be the text being inserted or deleted.
        reg = self.master.register(self.mathParser.callback)
        appEntry.config(validate="key", validatecommand=(reg, '%S'))

        # set up the calculator buttons inside the main window
        button_sin = tk.Button(self.master,
                               text="sin",
                               width=4,
                               height=2,
                               command=foo)
        button_sin.place(x=20, y=60)

        button_cos = tk.Button(self.master,
                               text="cos",
                               width=4,
                               height=2,
                               command=foo)
        button_cos.place(x=65, y=60)

        button_tan = tk.Button(self.master,
                               text="tan",
                               width=4,
                               height=2,
                               command=foo)
        button_tan.place(x=110, y=60)


        
        button_pths = tk.Button(self.master,
                               text="( )",
                               width=4,
                               height=2,
                               command=foo)
        button_pths.place(x=20, y=110)
        
        button_exp = tk.Button(self.master,
                               text="^",
                               width=4,
                               height=2,
                               command=foo)
        button_exp.place(x=65, y=110)
        
        button_sqrt = tk.Button(self.master,
                                text="sqrt",
                                width=4,
                                height=2,
                                command=foo)
        button_sqrt.place(x=110, y=110)
        
        button_clr = tk.Button(self.master,
                               text="clear",
                               width=4,
                               height=2,
                               command=foo)
        button_clr.place(x=155, y=60)
        
        button_mult = tk.Button(self.master,
                               text="x",
                               width=4,
                               height=2,
                               command=foo)
        button_mult.place(x=155, y=110)
        
        button_equals = tk.Button(self.master,
                                  text="=",
                                  width=4,
                                  height=2,
                                  command=foo)
        button_equals.place(x=155, y=310)

        button_divide = tk.Button(self.master,
                                  text="/",
                                  width=4,
                                  height=2,
                                  command=foo)
        button_divide.place(x=155, y=160)
        
        button_plus = tk.Button(self.master,
                                text="+",
                                width=4,
                                height=2,
                                command=foo)
        button_plus.place(x=155, y=260)

        button_minus = tk.Button(self.master,
                                 text="-",
                                width=4,
                                height=2,
                                command=foo)
        button_minus.place(x=155, y=210)

        button_negPos = tk.Button(self.master,
                             text="+/-",
                             width=4,
                             height=2,
                             command=foo)
        button_negPos.place(x=20, y=310)

        button_decimal = tk.Button(self.master,
                             text=".",
                             width=4,
                             height=2,
                             command=foo)
        button_decimal.place(x=110, y=310)
                
        self.button_9 = tk.Button(self.master,
                                  text="9",
                                  width=4,
                                  height=2,
                                  command=foo)
        self.button_9.place(x=20, y=160)

        button_8 = tk.Button(self.master,
                             text="8",
                             width=4,
                             height=2,
                             command=foo)
        button_8.place(x=65, y=160)

        button_7 = tk.Button(self.master,
                             text="7",
                             width=4,
                             height=2,
                             command=foo)
        button_7.place(x=110, y=160)


        button_4 = tk.Button(self.master,
                             text="4",
                             width=4,
                             height=2,
                             command=foo)
        button_4.place(x=20, y=210)

        button_5 = tk.Button(self.master,
                             text="5",
                             width=4,
                             height=2,
                             command=foo)
        button_5.place(x=65, y=210)

        button_6 = tk.Button(self.master,
                             text="6",
                             width=4,
                             height=2,
                             command=foo)
        button_6.place(x=110, y=210)

        button_1 = tk.Button(self.master,
                             text="1",
                             width=4,
                             height=2,
                             command=foo)
        button_1.place(x=20, y=260)

        button_2 = tk.Button(self.master,
                             text="2",
                             width=4,
                             height=2,
                             command=foo)
        button_2.place(x=65, y=260)

        button_3 = tk.Button(self.master,
                             text="3",
                             width=4,
                             height=2,
                             command=foo)
        button_3.place(x=110, y=260)

        button_0 = tk.Button(self.master,
                             text="0",
                             width=4,
                             height=2,
                             command=foo)
        button_0.place(x=65, y=310)

                


mainWindow = tk.Tk()
app = Application(master=mainWindow)
app.mainloop()


