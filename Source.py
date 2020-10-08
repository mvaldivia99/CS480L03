# !/usr/bin/python3
import tkinter as tk
#import compiler

"""
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
"""

def foo(thisButton):
    print("click me")

# main window frame
window = tk.Tk()

# add a button to window 
button = tk.Button(window, text="9", command=foo)
button.place(x=0, y=0)

#show input to user/enter input via keyboard?
string = tk.StringVar()
entry = tk.Entry(window, textvariable=string)
entry.place(x=50, y=50)
