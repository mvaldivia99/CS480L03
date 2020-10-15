# !/usr/bin/python3
import tkinter as tk
from functools import partial
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


def foo(thisButton):
    print(thisButton)

# main window frame
window = tk.Tk()

# add a button to window 
button = tk.Button(window, text="9", command=partial(foo, "9"))
button.place(x=0, y=0)

#show input to user/enter input via keyboard?
string = tk.StringVar()
entry = tk.Entry(window, textvariable=string)
entry.place(x=50, y=50)


"""
# parse 
def foo():
    print("foo now")

# main window 
window = tk.Tk()
window.geometry("225x300")
#window.maxsize(400, 400)

# input box
"""display_text = tk.StringVar()
displayWndw = tk.Entry(window,
                       width=100,
                       textvariable=display_text)
displayWndw.place(x=0, y=0)"""

# number buttons
#button_0 = tk.Button(window, text="0", command=foo)
#button_0.place(x=0, y=0)
#button_0.grid(column=5, row=5)

#button_1 = tk.Button(window, text="1", command=foo)
#button_2 = tk.Button(window, text="2", command=foo)
#button_3 = tk.Button(window, text="3", command=foo)
#button_4 = tk.Button(window, text="4", command=foo)
#button_5 = tk.Button(window, text="5", command=foo)



button_9 = tk.Button(window,
                    text="9",
                    width=4,
                    height=2,
                    command=foo)
button_9.place(x=20, y=50)

button_8 = tk.Button(window,
                     text="8",
                     width=4,
                     height=2,
                     command=foo)
button_8.place(x=65, y=50)

button_7 = tk.Button(window,
                     text="7",
                     width=4,
                     height=2,
                     command=foo)
button_7.place(x=110, y=50)


button_4 = tk.Button(window,
                     text="4",
                     width=4,
                     height=2,
                     command=foo)
button_4.place(x=20, y=105)

button_5 = tk.Button(window,
                     text="5",
                     width=4,
                     height=2,
                     command=foo)
button_5.place(x=65, y=105)

button_6 = tk.Button(window,
                     text="6",
                     width=4,
                     height=2,
                     command=foo)
button_6.place(x=110, y=105)

button_1 = tk.Button(window,
                     text="1",
                     width=4,
                     height=2,
                     command=foo)
button_1.place(x=20, y=160)

button_2 = tk.Button(window,
                     text="2",
                     width=4,
                     height=2,
                     command=foo)
button_2.place(x=65, y=160)

button_3 = tk.Button(window,
                     text="3",
                     width=4,
                     height=2,
                     command=foo)
button_3.place(x=110, y=160)

button_0 = tk.Button(window,
                     text="0",
                     width=4,
                     height=2,
                     command=foo)
button_0.place(x=65, y=210)

button_negPos = tk.Button(window,
                     text="+/-",
                     width=4,
                     height=2,
                     command=foo)
button_negPos.place(x=20, y=210)

button_decimal = tk.Button(window,
                     text=".",
                     width=4,
                     height=2,
                     command=foo)
button_decimal.place(x=110, y=210)




