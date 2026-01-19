import tkinter as tk
from tkinter import ttk

def rows_colums(window,rows,columns):
    for column in range(columns): window.columnconfigure(column,weight=1)
    for row in range(rows): window.rowconfigure(row,weight=1)

def error_message(window,text,row,colum):
    error=tk.Label(window,text=text,font=("Arial",15),fg="red",bg="white")
    error.grid(row=row,column=colum)
    error.after(3000,error.destroy)