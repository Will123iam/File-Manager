import tkinter as tk
from tkinter import ttk
import os
from repeat_functions import file_load 
from pygame import mixer
from mutagen.mp3 import MP3
#from Login import win_canvas

class window_location():
    def __init__(self):
        #previous_layout=open("window_location.txt",'r')
        #self.previous_layout=previous_layout.readline()
        self.location=[0 for x in range(6)]

    def use_previous(self):
        print("Ooopsss!")    

windows=window_location()

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
    def __init__(self,window,file,file_images,style1,style2,view_container,previous_path,pass_through=None):

        #for item in pass_through:
        #    setattr(self,item,item)

        self.view_container=view_container
        self.file=file
        self.previous_path = previous_path
        self.file_images=file_images
        self.folder = False # Wheather it is a file or a folder

        if len(file) > 15: 
            file=file[:15] #Sets text size limit
            file+="..."

        self.end = self.file[-4:]

        if self.end == ".pdf": icon_image = file_images[1]
        elif self.end == ".png": icon_image = file_images[2]
        elif self.end == ".JPG" or self.end == ".jpg": icon_image = file_images[3]
        elif self.end == ".mp3": icon_image = file_images[4]
        else: 
            icon_image=file_images[0]
            self.folder = True

        
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
        if self.folder:
            self.detection()
            self.view_frame=scrollable_frame(self.view_container,"dark turquoise",450,350,"turquoise.TFrame",self.y,self.x,self.view_container,(self.previous_path+"/"+self.file),self.file_images,4,4)
            self.inner_files=self.view_frame.load_content(self.previous_path,self.file)
            self.view_frame.disply_file(self.inner_files,3)
        else:
            #media_frame.play_adio((self.previous_path+"/"+self.file),self.end)
            file_load((self.previous_path+"/"+self.file),self.end)

    def detection(self):
        count=0
        stop=False
        for pos in windows.location:
            if not stop:
                print("looking at x:",pos,count)
                if pos == 0 and count<3:
                    windows.location[count] = 1
                    self.x = count
                    self.y = 0
                    stop=True
                else:   
                    print("NOW AT Y!","looking at:",pos,count)
                    if pos == 0 and count>=3:
                        temp=count-3
                        print("Count:",count,temp)
                        windows.location[count] = 1
                        self.y = 2
                        self.x = temp
                        stop=True
                    else: 
                        print("No space!")
                        self.y,self.x = 0,0

                count+=1

        print(windows.location)



class scrollable_frame(ttk.Frame):
    def __init__(self,container_frame,bg,width,hight,style,row,column,view_container,pv_path,icon_images,scroll_row,scroll_column):
        ttk.Frame.__init__(self,container_frame,style=style,relief="ridge")
        self.grid(row=row,column=column,sticky="nw",padx=10,pady=10)
        self.grid_propagate(False)
        self.file_icon=icon_images
        self.view_container=view_container
        self.pv_path=pv_path

        self.canvas =tk.Canvas(self,bg=bg,width=width,height=hight)
        self.canvas.pack(side="left",fill="both",expand=True,padx=5,pady=5)

        scrollbar=ttk.Scrollbar(self,orient="vertical",command=self.canvas.yview)
        scrollbar.pack(side='right',fill='y')

        self.scroll_frame=frame_creation(self.canvas,scroll_row,scroll_column,style=style)
        self.canvas_win=self.canvas.create_window((0,0),window=self.scroll_frame,anchor='nw')

        #self.canvas.configure(scrollregion=self.scroll_frame.bbox("all"))
        self.canvas.bind("<Enter>", self.bind)
        self.canvas.bind("<Leave>", self.unbind)

    def load_content(self,pv_path,file):
        new_file=""
        for char in file:
            if char == " ":
                char="/"
            new_file+=char

        #path=open("path.txt",'r')
        if pv_path:path=pv_path+"/"+file
        else: path = pv_path
        files=os.listdir(path)
        print("Loaded!")

        return files
    
    def disply_file(self,files,rowLength):
        x,y=0,0
        for file in files:
            #print(file)
            icon=file_widget(self.scroll_frame,file,self.file_icon,"blue.TFrame","blue.TLabel",self.view_container,self.pv_path)
            icon.place(y,x)
            if x == rowLength: 
                x=0
                y+=1
            else: x+= 1
    
    def scroll(self,event): #Scrolles the window
        move = -1 if event.delta > 0 else 1 #Changes which way it scrolles
        self.canvas.yview_scroll(move, "units")

    def bind(self, event):
        self.canvas.bind_all("<MouseWheel>",self.scroll)
        #print("Binding")
        #self.configure(style=)
    def unbind(self, event):
        self.canvas.unbind_all("<MouseWheel>")
        #print("Unbinding")

    def update_size(self,width,hight):
        self.canvas.configure(width=width,height=hight)

class media_playback():
    def __init__(self,window,row,column,file):
       self.media_style=style_creation("blue","classic","light steel blue",items=["Frame","Label","Button"])

       self.time=tk.IntVar(value=mixer.music.get_pos())

       self.midea_controlls=frame_creation(window,2,1,width=200,height=100,style="blue.TFrame",relief="ridge")
       self.progress_frame=frame_creation(self.midea_controlls,2,1,relief="ridge")

       self.midea_controlls.grid_propagate(False)
       self.progress_frame.grid(row=1,column=0)

       self.count=1
       self.file = file

       self.play_pause_butt=ttk.Button(self.midea_controlls,text="PAUSE",command=self.play_pause_toggle)
       self.progress=ttk.Scale(self.progress_frame,from_=0,to=100,length=180,orient='horizontal')
       
       self.midea_controlls.grid(row=row,column=column,sticky='s')
       self.play_pause_butt.grid(row=0,column=0)
       self.progress.grid(row=0,column=0)
       #self.unpause_butt.grid(row=0,column=2)

    def play_pause_toggle(self):
        if self.count == 1:
            self.play_pause_butt.configure(text="PLAY")
            mixer.music.pause()
            self.count = 0
        else:
            self.play_pause_butt.configure(text="PAUSE")
            mixer.music.unpause()
            self.count = 1

    def update_length(self):
        self.audio=MP3(self.file)
        self.length=self.audio.info.length
        self.progress.configure(to=self.length)

    def play_adio(self,type,file):
        self.file=file
        if type == ".mp3": #Plays mp3 through pygame
            #Loads/playes file
            mixer.music.load(file)
            mixer.music.play()
            print("Playing mp3:",file)

        self.update_length()


class error_popup():
    def __init__(self,window):
        self.error_frame=frame_creation(window,2,2)
    