import tkinter as tk
from tkinter import ttk
from classes import file_widget, style_creation, frame_creation
from repeat_functions import rows_colums
import os

#Loads path
path=open("path.txt",'r')
path=path.readline()
files=os.listdir(path)

#Main window
win_canvas=tk.Tk()
win_canvas.geometry("1200x800")
win_canvas.title(f"File Manager - {path}")
win_canvas.config(bg="gray")
rows_colums(win_canvas,0,2)

#Load file icon
file_icon=tk.PhotoImage(file="images/icon_file.png")

#Styles
blue_style=style_creation("blue","classic","light steel blue",items=["Frame","Label"])
turquoise_style=style_creation("turquoise","classic","dark turquoise",items=["Frame"])

#counts number of files
count=0
for file in files: count+=1

#File selection
side_selection_container = ttk.Frame(win_canvas)
side_selection_container.grid(row=0,column=0,sticky='w')

side_select_canvas = tk.Canvas(side_selection_container,width=220,height=800)
side_select_canvas.pack(side="left",fill="both",expand=True)

scrollbar = ttk.Scrollbar(side_selection_container,orient="vertical",command=side_select_canvas.yview)
scrollbar.pack(side='right',fill='y')

side_select_canvas.configure(yscrollcommand=scrollbar.set)

scroll_frame = frame_creation(side_select_canvas,int(count/2),2,style="turquoise.TFrame")
side_select_canvas.create_window((0,0),window=scroll_frame,anchor='nw')

#Loads files into selection menu
all_icons=[]
x=0
y=0

for file in files:
    icon=file_widget(scroll_frame,file,file_icon,"blue.TFrame","blue.TLabel")
    icon.place(y,x)
    all_icons.append(icon)
    if x == 1: 
        x=0
        y+=1
    else: x+= 1
        


print(all_icons)


win_canvas.mainloop()