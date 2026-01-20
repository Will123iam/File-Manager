import tkinter as tk
from tkinter import ttk
import os

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
    def __init__(self,window,file,icon_image,style1,style2,view_container,previous_path):

        self.view_container=view_container
        self.file=file
        self.detection_valuex=-1
        self.previous_path = previous_path

        if len(file) > 15: 
            file=file[:15] #Sets text size limit
            file+="..."
        
        self.icon_fram=frame_creation(window,2,0,style=style1,relief="groove",width=108,height=85)
        self.file_name=ttk.Label(self.icon_fram,text=file,style=style2,font=("Ariles",10))
        self.file_icon=ttk.Label(self.icon_fram,image=icon_image,style=style2)

        self.icon_fram.grid_propagate(False)
        self.file_icon.grid(row=0,padx=10,pady=5,sticky='n')
        self.file_name.grid(row=1,padx=5,pady=5,sticky='n')

        self.icon_fram.bind("<Button-1>",self.when_clicked)
        self.file_icon.bind("<Button-1>",self.when_clicked)
        self.file_name.bind("<Button-1>",self.when_clicked)

    def update_loop(self):
        self.view_container.update_idletasks()
        win_size_hight = self.view_container.winfo_height()
        win_size_width = self.view_container.winfo_width()

        self.view_frame.configure(width=win_size_width-100,height=win_size_hight-400)

        self.view_container.after(500,self.update_loop)


    def place(self,row,column):
        self.icon_fram.grid(row=row,column=column,padx=3,pady=3)

    def when_clicked(self,event):
        self.detection()
        self.view_frame=scrollable_frame(self.view_container,"dark turquoise",450,350,"turquoise.TFrame",0,self.detection_valuex,self.view_container,(self.previous_path+"/"+self.file))
        self.inner_files=self.view_frame.load_content(self.previous_path,self.file)
        self.view_frame.disply_file(self.inner_files)

    def detection(self):
        self.detection_valuex += 1
        if self.detection_valuex > 3: self.detection_valuex = 0
        


class scrollable_frame(ttk.Frame):
    def __init__(self,container_frame,bg,width,hight,style,row,column,view_container,pv_path):
        ttk.Frame.__init__(self,container_frame,style=style,relief="ridge")
        self.grid(row=row,column=column,sticky="nw",padx=10,pady=10)
        self.grid_propagate(False)
        self.file_icon=tk.PhotoImage(file="images/icon_file.png")
        self.view_container=view_container
        self.pv_path=pv_path

        canvas =tk.Canvas(self,bg=bg,width=width,height=hight)
        canvas.pack(side="left",fill="both",expand=True,padx=5,pady=5)

        scrollbar=ttk.Scrollbar(self,orient="vertical",command=canvas.yview)
        scrollbar.pack(side='right',fill='y')

        self.scroll_frame=frame_creation(canvas,3,3,style=style)
        canvas.create_window((0,0),window=self.scroll_frame,anchor='nw')

    def load_content(self,pv_path,file):
        new_file=""
        for char in file:
            if char == " ":
                char="/"
            new_file+=char

        #path=open("path.txt",'r')
        path=pv_path+"/"+file
        files=os.listdir(path)
        print("Loaded!")

        return files
    
    def disply_file(self,files):
        x,y=0,0
        for file in files:
            icon=file_widget(self.scroll_frame,file,self.file_icon,"blue.TFrame","blue.TLabel",self.view_container,self.pv_path)
            icon.place(y,x)
            if x == 4: 
                x=0
                y+=1
            else: x+= 1
