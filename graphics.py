import main
from tkinter import *
from tkinter import ttk

## declaring root and name
root = Tk()
root.title("Calendar")

## content frame
## https://tkdocs.com/tutorial/firstexample.html

## creating a content frame
mainframe = ttk.Frame(root, padding = "50 5 0 100")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

## creating date entry buttons
date = StringVar()
date_entry = ttk.Entry(mainframe, width = 100, textvariable = date)
date_entry.grid(column = 2, row = 1, sticky = (W, E))

description = StringVar()
description_entry = ttk.Entry(mainframe, width = 100, textvariable = description)
description_entry.grid(column = 2, row = 2, sticky = (W, E))

## labels for buttons
ttk.Label(mainframe, text = "date : ").grid(column = 1, row = 1, sticky = E)
ttk.Label(mainframe, text = "description : ").grid(column = 1, row = 2, sticky = E)

## space between textboxes
for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

root.bind("<Return>", print("printing"))

root.mainloop()