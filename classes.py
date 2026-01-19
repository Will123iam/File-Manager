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

class file_widget():
    def __init__(self,window,file,icon_image,style1,style2):
        if len(file) > 15: 
            file=file[:15] #Sets text size limit
            file+="..."

        self.icon_fram=frame_creation(window,2,0,style=style1,relief="groove",width=108,height=85)
        self.file_name=ttk.Label(self.icon_fram,text=file,style=style2,font=("Ariles",10))
        self.file_icon=ttk.Label(self.icon_fram,image=icon_image,style=style2)

        self.icon_fram.grid_propagate(False)
        self.file_icon.grid(row=0,padx=10,pady=5,sticky='n')
        self.file_name.grid(row=1,padx=5,pady=5,sticky='n')

    def place(self,row,column):
        self.icon_fram.grid(row=row,column=column,padx=3,pady=3)

