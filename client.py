import socket
from  threading import Thread
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from pathlib import Path

import ftplib
import os
import ntpath
import time
from ftplib import FTP



from playsound import playsound
import pygame
from pygame import mixer

PORT = 8050
IP_ADDRESS = "127.0.0.1"
SERVER = None
BUFFER_SIZE = 4096
songCounter = 0
listBox = None
songSelected = None
infoLabel = None

textArea=None
filePathLabel=None #to show the file path


def play():
    global songSelected
    global infoLabel
    songSelected = listBox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load("shared_files/"+ songSelected)
    mixer.music.play()

    if(songSelected != ""):
        infoLabel.configure(text="NOW PLAYING: "+ songSelected)
    else:
        infoLabel.configure(text="")

def stop():
    global songSelected
    global infoLabel
    pygame
    mixer.init()
    mixer.music.load("shared_files/"+songSelected)
    mixer.music.pause()
    infoLabel.configure(text="")

def resume():
    global songSelected
    pygame
    mixer.init()
    mixer.music.load("shared_files/"+ songSelected)
    mixer.music.play()
def pause():
    global songSelected
    pygame
    mixer.init()
    mixer.music.load("shared_files/"+songSelected)
    mixer.music.pause()
def browseFile():
    global textArea
    global filePathLabel
    global songSelected
    global songCounter
    global listBox

    try:
        filename = filedialog.askopenfilename()
        HOSTNAME = "127.0.0.1"
        USERNAME = "admin"
        PASSWORD = "admin"

        ftpServer = FTP(HOSTNAME , USERNAME , PASSWORD)
        ftpServer.encoding = "utf-8"
        ftpServer.cwd("shared_files")
        fname = ntpath.basename(filename)
        with open(filename , "rb") as f:
            ftpServer.storbinary(f"STOR {fname}" , f)
        ftpServer.dir()
        ftpServer.quit()
    except FileNotFoundError:
        print("Cancel button pressed")


def musicWindow():
    global listBox
    global infoLabel
    global songCounter
    window = Tk()
    window.title("Music Window")
    window.geometry("300x350")
    window.configure(bg="LightSkyBlue")

    selectLabel =   Label(window , text="select song" , bg="LightSkyBlue" , font=('Calibri' , 8))
    selectLabel.place(x=2 , y=1)

    listBox = Listbox(window , height=10 , width=39 , activestyle="dotbox" , bg="LightSkyBlue" , borderwidth=2 , font=("Calibri" , 10))
    listBox.place(x = 10 , y=20)

    scrollbar = Scrollbar(listBox)
    scrollbar.place(relheight=1 , relx=1)
    scrollbar.config(command=listBox.yview)


    playButton = Button(window , text="play" , width=10 , bd=1 , bg="SkyBlue" , font=('Calibri' , 10) , command=play)
    playButton.place(x=30 , y=200)

    stopButton = Button(window , text="stop" , width=10 , bd=1 , bg="SkyBlue" , font=('Calibri' , 10) , command=stop)
    stopButton.place(x=200 , y=200)

    uploadButton = Button(window , text="upload" , width=10 , bd=1 , bg="SkyBlue" , font=('Calibri' , 10) , command=browseFile)
    uploadButton.place(x=30 , y=250)

    downloadButton = Button(window , text="download" , width=10 , bd=1 , bg="SkyBlue" , font=('Calibri' , 10))
    downloadButton.place(x=200 , y=250)

    resumeButton = Button(window , text="Resume" ,width=10 , bd=1 , bg="SkyBlue" , font=('Calibri' , 10)  , command=resume)
    resumeButton.place(x=30 , y=300)

    pauseButton = Button(window , text="Pause" , width=10 , bd=1 , bg="SkyBlue" , font=('Calibri' , 10) , command= pause )
    pauseButton.place(x=200 , y=300)

    infoLabel = Label(window , text="" , fg = "blue" , font=("Calibri" , 8))
    infoLabel.place(x=4 , y=330)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS , PORT))

    musicWindow()

setup()

for file in os.listdir("shared_files"):
        filename = os.fsdecode(file)
        listBox.insert(songCounter , filename)
        songCounter += 1
