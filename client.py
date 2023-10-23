import socket
from  threading import Thread
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT = 8050
IP_ADDRESS = "127.0.0.1"
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():
    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg="LightSkyBlue")

    selectLabel =   Label(window , text="select song" , bg="LightSkyBlue" , font=('Calibri' , 8))
    selectLabel.place(x=2 , y=1)

    listBox = Listbox(window , height=10 , width=39 , activestyle="dotbox" , bg="LightSkyBlue" , borderwidth=2 , font=("Calibri" , 10))
    listBox.place(x = 10 , y=20)

    scrollbar = Scrollbar(listBox)
    scrollbar.place(relheight=1 , relx=1)
    scrollbar.config(command=listBox.yview)

    playButton = Button(window , text="play" , width=10 , bd=1 , bg="SkyBlue" , font=('Calibri' , 10))
    playButton.place(x=30 , y=200)

    stopButton = Button(window , text="stop" , width=10 , bd=1 , bg="SkyBlue" , font=('Calibri' , 10))
    stopButton.place(x=200 , y=200)

    uploadButton = Button(window , text="upload" , width=10 , bd=1 , bg="SkyBlue" , font=('Calibri' , 10))
    uploadButton.place(x=30 , y=250)

    downloadButton = Button(window , text="download" , width=10 , bd=1 , bg="SkyBlue" , font=('Calibri' , 10))
    downloadButton.place(x=200 , y=200)

    infoLabel = Label(window , text="" , fg = "blue" , font=("Calibri" , 8))
    infoLabel.place(x=4 , y=280)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS , PORT))

    musicWindow()
setup()
