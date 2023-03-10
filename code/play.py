from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as font
import os
import random
import subprocess
import time
import threading
import sys
import tkinter.messagebox
import tkinter as tk
from move_comparison import compare_positions
import vlc


root = tk.Tk()
root.geometry("1960x1280")
root.configure(bg='black')
photo = PhotoImage(file = r"bg/LETS.png")
photo1 = PhotoImage(file = r"bg/1.png")
photo2 = PhotoImage(file = r"bg/2.png")
photo3 = PhotoImage(file = r"bg/3.png")
class App:
    var = IntVar()
    s=var.get()
    #p=vlc.MediaPlayer('audio/Lets.mp3')
    #p.play()
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        myfont=font.Font(size=300)

        def sel():
                
                selection = "You selected the option " + str(var.get())
                label.config(text = selection)
                self.s=var.get()
                

        var = IntVar()
        myfont=font.Font(size=20)
        
        l=Label(root,text="SELECT YOUR CHOICE",bg="black",fg="white",font=('ROG Fonts',30)).pack(pady=8)
        R1 = Radiobutton(root, text="EASY", variable=var, value=1,fg="red",height=40,width=10,image=photo3,activebackground='black',
                  command=sel)
        R1['font']=myfont
        R1.pack( fill=X,ipadx=2,ipady=2)

        R2 = Radiobutton(root, text="MEDIUM", variable=var, value=2,fg="red",height=40,width=10,image=photo2,activebackground='black',
                  command=sel)
        R2['font']=myfont
        R2.pack( anchor = W ,fill=X,ipadx=2,ipady=2)

        R3 = Radiobutton(root, text="HARD", variable=var, value=3,fg="red",height=40,width=10,image=photo1,activebackground='black',
                  command=sel)
        R3['font']=myfont
        R3.pack( anchor = W,fill=X,ipadx=2,ipady=2)
        

        label = Label(root)
        label.pack(pady=50)
        self.slogan = tk.Button(self.frame, text="START",height=710,width=1960,image=photo,fg="red",activebackground='black',command=self.write_slogan)
        self.slogan['font']=myfont
        self.slogan.pack(side=tk.LEFT)
    #p.stop()
       


    

    
    def write_slogan(self):
        if(self.s==0):
             return
        
        listv = ['dance/wrong_dance.mp4','dance/benchmark_dance.mp4','dance/right_dance.mp4']
        lists = ['audio/song.mp3','audio/ooo.mp3','audio/real.wav']
        p=vlc.MediaPlayer(lists[self.s-1])
        p.play()
        benchmark_video = (listv[self.s-1])
        user_video =0# 'dance_videos/wrong_dance.mp4' # replace with 0 for webcam
        compare_positions(benchmark_video, user_video)
        p.stop()
app = App(root)
#root.attributes('-fullscreen',True)
root.mainloop()
