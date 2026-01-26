import tkinter as tk
from tkinter import ttk, font
from classes import *
from repeat_functions import *
from pygame import mixer
#from PIL import Image, ImageTk

# - - - - - - - - - - - Section one - - - - - - - - - - -

def pathsave(file,item):
    data=open(file,'w')
    data.write(str(item))
    data.close()

def load_canvas(): #Checks if input given, moves onto next screen
    if device_input.get():
        try:
            os.listdir(device_input.get())
            login_win.destroy()
            pathsave("path.txt",device_input.get())
        except:
            error_message(login_win,"Location not found!",2,1)

    else: error_message(login_win,"No location given!",2,1)

#Main window
login_win=tk.Tk()
login_win.geometry("400x200")
login_win.resizable(False,False)
login_win.title("File Manager - Login")
login_win.config(bg="lemon chiffon")
rows_colums(login_win,3,3) #Adds a grid

old_path=open("path.txt",'r')
old_path=old_path.readline()

white_style=style_creation("white","classic","white",items=["Label","Frame"]) #White style
device_input=tk.StringVar(value=old_path) #Input varible for where to look for loading files

mixer.init() #starts pygames mixer for audio

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

login_win.bind("<Return>",lambda event: load_canvas())

login_win.mainloop()

# - - - - - - - - Section two - - - - - - - - - 

#Loads path
path=device_input.get()
files=os.listdir(path)

#Main window
win_canvas=tk.Tk()
win_canvas.geometry("1200x800")
win_canvas.title(f"File Manager - {path}")
win_canvas.config(bg="gray")
rows_colums(win_canvas,0,2)
win_canvas.minsize(600,300)

def update_winsize(side_selection,view_container): #Updates sizing / placemnts on screen
    #global win_size_hight
    win_canvas.update_idletasks()
    win_size_hight = win_canvas.winfo_height()
    win_size_width = win_canvas.winfo_width()

    #Updates widgets
    side_selection.update_size(220,(win_size_hight-63))
    view_container.configure(width=(win_size_width-270))

    win_canvas.after(500,lambda: update_winsize(side_selection,view_container)) #Runs loop again


#Load file icon
file_images=[]
file_images.append(load_image("images/icon_file.png",48,48))
file_images.append(load_image("images/pdf.png",48,48))
file_images.append(load_image("images/PNG.png",48,48))
file_images.append(load_image("images/JPG.png",48,48))
file_images.append(load_image("images/mp3.png",48,48))

#Styles
blue_style=style_creation("blue","classic","light steel blue",items=["Frame","Label"])
turquoise_style=style_creation("turquoise","classic","dark turquoise",items=["Frame"])

#counts number of files
count=0
for file in files: count+=1

#Finder like windows
view_container=frame_creation(win_canvas,3,2,width=950)
view_container.grid(row=0,column=1,sticky="nsew")
view_container.grid_propagate(False)

media_frame=media_playback(view_container,2,2,None)

#File selection
side_selection_container = frame_creation(win_canvas,2,2)
side_selection_container.grid(row=0,column=0,sticky='w')

side_selection=scrollable_frame(side_selection_container,"dark turquoise",220,793,"turquoise.TFrame",0,0,view_container,path,file_images,int(count/2),2)
side_selection.disply_file(files,1)

#side_select_canvas = tk.Canvas(side_selection_container,bg="dark turquoise",width=220,height=793)
#side_selection_container.grid_columnconfigure(0,weight=3)
#side_select_canvas.grid(row=0,column=0,sticky="nesw")

#scrollbar = ttk.Scrollbar(side_selection_container,orient="vertical",command=side_select_canvas.yview)
#scrollbar.grid(row=0,column=1,sticky='nes')

#ide_select_canvas.configure(yscrollcommand=scrollbar.set)

#scroll_frame = frame_creation(side_select_canvas,int(count/2),2,style="turquoise.TFrame")
#side_select_canvas.create_window((0,0),window=scroll_frame,anchor='nw')

def shrink(event):
    label = event
    print(label)

    f = font.nametofont("pathFont")
    text = label.cget("text")
    len=235

    for size in range(20,5,-1):
        f.configure(size=size)
        if f.measure(text) <= len:
            print(f.measure(text),":",len)
            break

pathFont=font.Font(family="Helvetica",size=15,name="pathFont")

#Show path
path_frame=frame_creation(side_selection_container,1,1,style="white.TFrame",relief="groove")
path_frame.grid(row=1,column=0,sticky='wes')
path_frame.grid_propagate(False)

path_label=ttk.Label(path_frame,text=path,font="pathFont",style="white.TLabel")
path_label.pack(side='left',pady=3)
shrink(path_label)

#ttk.Label(side_selection_container,text="rtj5e6je56j").grid(row=1,column=1)
#path_label.bind("<Configure>",shrink)

update_winsize(side_selection,view_container)

win_canvas.mainloop()