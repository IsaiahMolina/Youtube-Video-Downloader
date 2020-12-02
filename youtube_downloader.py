from pytube import YouTube
from tkinter import *
import os

screen = Tk(baseName=None,className=" YouTube Downloader",useTk=1)
screen.geometry("300x200")



Label(screen, text="URL").grid(row=1, column=1)
Label(screen, text="PATH").grid(row=2, column=1)

URL = Entry(screen, width=43)
URL.grid(row=1, column=2)

PATH = Entry(screen, width=43)
PATH.grid(row=2, column=2)




def SUBMIT():
	url = URL.get()
	path = PATH.get()
	yt = YouTube(url).streams.first().download(path)
	print(yt)

BTN = Button(screen, text="SUBMIT", command=SUBMIT).grid(row=3, column=2)
mainloop()








