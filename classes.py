import tkinter as tk
from tkinter import ttk

class frame_creation(ttk.Frame):
    def __init__(self,window,rows,columns,**kwargs):
        ttk.Frame.__init__(self,window,**kwargs)

        for column in range(columns): self.columnconfigure(column,weight=1)
        for row in range(rows): self.rowconfigure(row,weight=1)

class style_creation(ttk.Style):
    def __init__(self,name,theme,bg,items):
        ttk.Style.__init__(self)

        self.theme_use(theme)
        for item in items: self.configure(f"{name}.T{item}", background=bg)
