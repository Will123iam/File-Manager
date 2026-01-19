import tkinter as tk
from tkinter import ttk
from classes import frame_creation, style_creation
from repeat_functions import rows_colums, error_message

def load_canvas(): #Checks if input given, moves onto next screen
    if device_input.get():
        login_win.destroy()
        exec(open("canvas.py").read()) #Opens / runs main app
    else: error_message(login_win,"No location given!",2,1)

#Main window
login_win=tk.Tk()
login_win.geometry("400x200")
login_win.title("File Manager - Login")
login_win.config(bg="lemon chiffon")
rows_colums(login_win,3,3) #Adds a grid

white_style=style_creation("white","classic","white",items=["Label"]) #White style
device_input=tk.StringVar(value=None) #Input varible for where to look for loading files


#File / Device location input
connection_frame = frame_creation(login_win,2,2,relief="groove")
connection_frame.grid(row=1,column=1)

devNam=ttk.Label(connection_frame,text="Device Name:",font=("Ariles",15),style="white.TLabel")
devNam.grid(row=0,column=0,padx=5,pady=5,sticky='w')

device=ttk.Entry(connection_frame,textvariable=device_input)
device.grid(row=1,column=0,padx=5,pady=5)

continue_butt=ttk.Button(connection_frame,text="Ok",command=load_canvas)
continue_butt.grid(row=1,column=1,padx=5,pady=5)
#Input End


login_win.mainloop()