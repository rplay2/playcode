__author__ = 'Ross'

from tkinter import *
from tkinter import ttk

root = Tk()

mainFrame = ttk.Frame(root, padding=(3,3,12,12))
menuFrame = ttk.Frame(mainFrame, borderwidth=5,relief="sunken", width=100, height=200)
pictureFrame = ttk.Frame(mainFrame, borderwidth=5, relief="sunken", width=200, height=200)

menuLabel = ttk.Label(menuFrame, text="Menu")
pictureLabel = ttk.Label(pictureFrame, text="Picture")

mainFrame.grid(column=0, row=0, sticky=(N,S,E,W))
pictureFrame.grid(column=2, row=0, columnspan=3, sticky=(N,S,E,W))
menuFrame.grid(column=0,row=0, columnspan=2, sticky=(N,S,W))



root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainFrame.columnconfigure(0,weight=1)
mainFrame.rowconfigure(0,weight=1)
mainFrame.columnconfigure(1,weight=1)
mainFrame.rowconfigure(1,weight=1)


root.mainloop()