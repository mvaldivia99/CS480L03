# Michell Valdivia
# CS 480 Lab 3
# This file contains the UI for the calculator

import tkinter as tk
import simpleParser
from functools import partial
        
class Application(tk.Frame):
    # set up the main window
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("275x400")
        self.master.title("Lab 03: Calculator")
        #mathParser = MyParser()

        # set up the entry, where user input will be captured
        self.appStr = tk.StringVar()
        self.appEntry = tk.Entry(self.master, textvariable=self.appStr, width=27, font=("Calibri 12"))
        self.appEntry.place(x=20, y=25)

        # for user validation
        # If the call was due to an insertion or deletion
        # %S argument will be the text being inserted or deleted.
        self.reg = self.master.register(self.callback)
        self.appEntry.config(validate="key", validatecommand=(self.reg, '%S'))

    # keyboard input validation
    def callback(self, a):

        letterInput = ["", "s", "i", "n", "c", "o", "t", "a", "q",
                       "r", "l", "p", "g", "e"]

        #print(a)
        if a.isdigit():
            return True
        elif a == "*" or a == "+" or a == "-" or a == "/":
            return True
        elif a == "." or a == ")" or a == "(":
            return True
        elif a in letterInput:
            return True
        else:
            return False
        
    # capture input from buttons
    def buttonText(self, text):
        currStr = self.appEntry.get()
        currStr = currStr + text
        self.appStr.set(currStr)
        #print(self.appEntry.get())       

    # called on clicking enter 
    def mathEval(self):
        currStr = self.appEntry.get()
        answer = simpleParser.evaluate(currStr)
        
        if answer == None:
            self.appStr.set("<Error Encountered>")
        else:
            self.appStr.set(answer)

        #print(answer)
        
    def clear(self):
        self.appStr.set("")
        #print("cleared")
        
    def create_widgets(self):       
        # set up the calculator buttons inside the main window
        button_sin = tk.Button(self.master,
                               text="sin",
                               width=4,
                               height=2,
                               command=partial(self.buttonText, "sin(")) 
        button_sin.place(x=20, y=60)

        button_cos = tk.Button(self.master,
                               text="cos",
                               width=4,
                               height=2,
                               command=partial(self.buttonText, "cos(")) 
        button_cos.place(x=65, y=60)

        button_tan = tk.Button(self.master,
                               text="tan",
                               width=4,
                               height=2,
                               command=partial(self.buttonText, "tan(")) 
        button_tan.place(x=110, y=60)


        
        button_pths1 = tk.Button(self.master,
                               text="(",
                               height=2,
                               command=partial(self.buttonText, "(")) 
        button_pths1.place(x=20, y=110)

        button_pths2 = tk.Button(self.master,
                               text=")",
                               height=2,
                               command=partial(self.buttonText, ")"))
        button_pths2.place(x=40, y=110)
        
        
        button_exp = tk.Button(self.master,
                               text="^",
                               width=4,
                               height=2,
                               command=partial(self.buttonText, "^("))
        button_exp.place(x=65, y=110)
        
        button_sqrt = tk.Button(self.master,
                                text="sqrt",
                                width=4,
                                height=2,
                                command=partial(self.buttonText, "sqrt("))
        button_sqrt.place(x=110, y=110)
        
        button_clr = tk.Button(self.master,
                               text="cot",
                               width=4,
                               height=2,
                               command=partial(self.buttonText, "cot("))
        button_clr.place(x=155, y=60)


        button_ln = tk.Button(self.master,
                               text="ln",
                               width=4,
                               height=2,
                               command=partial(self.buttonText, "ln("))
        button_ln.place(x=200, y=60)

        button_log = tk.Button(self.master,
                               text="log",
                               width=4,
                               height=2,
                               command=partial(self.buttonText, "log("))
        button_log.place(x=200, y=110)


        button_clr = tk.Button(self.master,
                               text="clear",
                               width=4,
                               height=12,
                               command=self.clear)
        button_clr.place(x=200, y=160)

        
        
        button_mult = tk.Button(self.master,
                               text="x",
                               width=4,
                               height=2,
                               command=partial(self.buttonText, "*"))
        button_mult.place(x=155, y=110)
        
        button_equals = tk.Button(self.master,
                                  text="=",
                                  width=4,
                                  height=2,
                                  command=self.mathEval)
        button_equals.place(x=155, y=310)

        button_divide = tk.Button(self.master,
                                  text="/",
                                  width=4,
                                  height=2,
                                  command=partial(self.buttonText, "/"))
        button_divide.place(x=155, y=160)
        
        button_plus = tk.Button(self.master,
                                text="+",
                                width=4,
                                height=2,
                                command=partial(self.buttonText, "+"))
        button_plus.place(x=155, y=260)

        button_minus = tk.Button(self.master,
                                 text="-",
                                width=4,
                                height=2,
                                command=partial(self.buttonText, "-"))
        button_minus.place(x=155, y=210)

        button_negPos = tk.Button(self.master,
                             text="+/-",
                             width=4,
                             height=2,
                             command=partial(self.buttonText, "-"))
        button_negPos.place(x=20, y=310)

        button_decimal = tk.Button(self.master,
                             text=".",
                             width=4,
                             height=2,
                             command=partial(self.buttonText, ".")) 
        button_decimal.place(x=110, y=310)
                
        self.button_9 = tk.Button(self.master,
                                  text="9",
                                  width=4,
                                  height=2,
                                  command=partial(self.buttonText, "9"))
        self.button_9.place(x=20, y=160)

        button_8 = tk.Button(self.master,
                             text="8",
                             width=4,
                             height=2,
                             command=partial(self.buttonText, "8"))
        button_8.place(x=65, y=160)

        button_7 = tk.Button(self.master,
                             text="7",
                             width=4,
                             height=2,
                             command=partial(self.buttonText, "7"))
        button_7.place(x=110, y=160)


        button_4 = tk.Button(self.master,
                             text="4",
                             width=4,
                             height=2,
                             command=partial(self.buttonText, "4"))
        button_4.place(x=20, y=210)

        button_5 = tk.Button(self.master,
                             text="5",
                             width=4,
                             height=2,
                             command=partial(self.buttonText, "5"))
        button_5.place(x=65, y=210)

        button_6 = tk.Button(self.master,
                             text="6",
                             width=4,
                             height=2,
                             command=partial(self.buttonText, "6"))
        button_6.place(x=110, y=210)

        button_1 = tk.Button(self.master,
                             text="1",
                             width=4,
                             height=2,
                             command=partial(self.buttonText, "1"))
        button_1.place(x=20, y=260)

        button_2 = tk.Button(self.master,
                             text="2",
                             width=4,
                             height=2,
                             command=partial(self.buttonText, "2"))
        button_2.place(x=65, y=260)

        button_3 = tk.Button(self.master,
                             text="3",
                             width=4,
                             height=2,
                             command=partial(self.buttonText, "3"))
        button_3.place(x=110, y=260)

        button_0 = tk.Button(self.master,
                             text="0",
                             width=4,
                             height=2,
                             command=partial(self.buttonText, "0"))
        button_0.place(x=65, y=310)

                


mainWindow = tk.Tk()
app = Application(master=mainWindow)
app.create_widgets()
app.mainloop()


