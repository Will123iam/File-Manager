import tkinter as tk
from tkinter import ttk
from classes import *#frame_creation, style_creation
from repeat_functions import *#rows_colums, error_message

def pathsave(file,item):
    data=open(file,'w')
    data.write(str(item))
    data.close()

def load_canvas(): #Checks if input given, moves onto next screen
    if device_input.get():
        login_win.destroy()
        pathsave("path.txt",device_input.get())
        #exec(open("canvas.py").read()) #Opens / runs main app
    else: error_message(login_win,"No location given!",2,1)

#Main window
login_win=tk.Tk()
login_win.geometry("400x200")
login_win.resizable(False,False)
login_win.title("File Manager - Login")
login_win.config(bg="lemon chiffon")
rows_colums(login_win,3,3) #Adds a grid

white_style=style_creation("white","classic","white",items=["Label"]) #White style
device_input=tk.StringVar(value=None) #Input varible for where to look for loading files


#File / Device location input
connection_frame = frame_creation(login_win,2,2,relief="groove")
connection_frame.grid(row=1,column=1)

devNam=ttk.Label(connection_frame,text="Path Name:",font=("Ariles",15))
devNam.grid(row=0,column=0,padx=5,pady=5,sticky='w')

device=ttk.Entry(connection_frame,textvariable=device_input)
device.grid(row=1,column=0,padx=5,pady=5)

continue_butt=ttk.Button(connection_frame,text="Ok",command=load_canvas)
continue_butt.grid(row=1,column=1,padx=5,pady=5)
#Input End


login_win.mainloop()

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

def update_winsize(side_select_canvas,view_container): #Updates sizing / placemnts on screen
    #global win_size_hight
    win_canvas.update_idletasks()
    win_size_hight = win_canvas.winfo_height()
    win_size_width = win_canvas.winfo_width()
    #print("y=",win_size_hight,"x=",win_size_width)
    #Updates widgets
    side_select_canvas.configure(height=(win_size_hight-7))
    view_container.configure(width=(win_size_width-240))

    win_canvas.after(500,lambda: update_winsize(side_select_canvas,view_container))


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

side_select_canvas = tk.Canvas(side_selection_container,bg="dark turquoise",width=220,height=793)
side_select_canvas.pack(side="left",fill="both",expand=True)

scrollbar = ttk.Scrollbar(side_selection_container,orient="vertical",command=side_select_canvas.yview)
scrollbar.pack(side='right',fill='y')

side_select_canvas.configure(yscrollcommand=scrollbar.set)

scroll_frame = frame_creation(side_select_canvas,int(count/2),2,style="turquoise.TFrame")
side_select_canvas.create_window((0,0),window=scroll_frame,anchor='nw')

#Finder like windows
view_container=frame_creation(win_canvas,2,2,width=950)
view_container.grid(row=0,column=1,sticky="nsew")
view_container.grid_propagate(False)


#Loads files into selection menu
def disply_files(files):
    x,y=0,0
    for file in files:
        icon=file_widget(scroll_frame,file,file_icon,"blue.TFrame","blue.TLabel",view_container,path)
        icon.place(y,x)
        if x == 1: 
            x=0
            y+=1
        else: x+= 1

disply_files(files)
update_winsize(side_select_canvas,view_container)

win_canvas.mainloop()