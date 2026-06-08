import tkinter as tk
from tkinter import ttk, font
from classes import *
from repeat_functions import *
from pygame import mixer
import socket
from threading import Thread
#from PIL import Image, ImageTk#

# - - - - - - - - - - - Section one - - - - - - - - - - -

class sendFile():
    def __init__(self):
        #Window setup
        self.win=tk.Tk()
        self.win.geometry("500x300")
        self.win.resizable(False,False)
        self.win.title("Send / Recive Files")
        self.win.configure(bg="lemon chiffon")

        self.HOST = "86.167.85.190"
        self.PORT = 1369

        try:
            print("connecting")
            self.server = socket.socket()
            self.server.connect((self.HOST,self.PORT))
        except:
            print(f"Error server not found! IP:{self.HOST} PORT:{self.PORT}")

        self.inner_frame = ttk.Frame(self.win,relief="groove")
        self.inner_frame.pack(anchor='center')

        self.inner_frame.columnconfigure(0)
        self.inner_frame.columnconfigure(1)
        self.inner_frame.columnconfigure(2)

        self.inner_frame.rowconfigure(0)
        self.inner_frame.rowconfigure(1)
        self.inner_frame.rowconfigure(2) 

        self.inputs(self.inner_frame,self.server)


        Thread(target=self.recive_messages,).start()



    def recive_messages(self):
        self.connected = True

        while self.connected:
            self.message = self.server.recv(1024).decode()

            self.message_label=tk.Label(self.win,text=self.message,fg="red")
            self.message_label.pack()
            self.win.after(5000,self.message_label.destroy)
            
            print(self.message)

            if self.message[0] == "1": self.inputs()
            elif self.message[0] == "2": 
                for widget in self.inner_frame.winfo_children(): widget.destroy()
                sendFile()

    def inputs(self):
        self.username=tk.StringVar()
        self.password=tk.StringVar()

        u_e=ttk.Entry(self.inner_frame,textvariable=self.username)
        p_e=ttk.Entry(self.inner_frame,textvariable=self.password)

        user_label=tk.Label(self.inner_frame,text="User Name:")
        pass_label=tk.Label(self.inner_frame,text="Password:")

        contin_but1 = ttk.Button(self.inner_frame,text="Log In",command=lambda:self.server.send(f"False,{self.username.get()},{self.password.get()},".encode()))
        contin_but2 = ttk.Button(self.inner_frame,text="Sign Up",command=lambda:self.server.send(f"True,{self.username.get()},{self.password.get()},".encode()))
        
        u_e.grid(column=1,row=0,padx=5,pady=10)
        p_e.grid(column=1,row=1,padx=5,pady=10)
        user_label.grid(column=0,row=0,padx=5,pady=10)
        pass_label.grid(column=0,row=1,padx=5,pady=10)
        contin_but1.grid(column=1,row=2,padx=5,pady=10)
        contin_but2.grid(column=0,row=2,padx=5,pady=10)

    def sendFile(self):

        def send():
            self.file = open(self.file_name.get(),'rb')
            self.server.send(self.file_name.get().encode())
            print("Sent name")

            data=file.read()
            self.server.sendall(data)
            self.file.close()
            self.server.send(b"<END>")

            for widget in self.inner_frame.winfo_children():
                widget.destroy()
        
            #print(server.recv(1024).decode())

        self.server.send("SENDING".encode())
        
        self.file_name=tk.StringVar()

        self.send_label=tk.Label(self.inner_frame,text="Upload a file")
        self.send_label2=tk.Label(self.inner_frame,text="File Path:")
        self.file_entry=ttk.Entry(self.inner_frame,textvariable=self.file_name)
        self.contin_but1 = ttk.Button(self.inner_frame,text="Upload File",command=send)

        self.send_label.grid(column=0,row=0,padx=5,pady=10)
        self.send_label2.grid(column=0,row=1,padx=5,pady=10)
        self.file_entry.grid(column=1,row=1,padx=5,pady=10)
        self.contin_but1.grid(column=1,row=2,padx=5,pady=10)


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


def threadSending():
    server=sendFile()
    Thread(target=server.sendFile,).start()

#Menu bar
topMenu = tk.Menu(login_win)

server_menu=tk.Menu(topMenu,tearoff=0)
server_menu.add_command(label="Send File",command=threadSending)

topMenu.add_cascade(label="Server",menu=server_menu)

login_win.configure(menu=topMenu)


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

side_selection=scrollable_frame(side_selection_container,"dark turquoise",220,793,"turquoise.TFrame",0,0,view_container,path,file_images,int(count/2),2,media_frame)
side_selection.disply_file(files,1)

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

update_winsize(side_selection,view_container)

win_canvas.mainloop()