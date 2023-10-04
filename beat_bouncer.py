#**************************************************************************
#Programmer Names: Abhusha Ghimire
#Program Name: Beat Bouncer
#Date: Jan.19 2023
#Description: A Beat mixing program that allows the user to create their own
#             music track by selecting pre-made audio beats of their choice and
#             setting start time, end time, number of loops and volume for each
#             beat. After they save the sound it will turn into a layer. The user
#             can create upto 6 layers, delete layers and edit layers. The track
#             info can be saved in a text file. The track can be played/stopped.
#             the user can open up an existing track and listen to it through the
#             program.
#**************************************************************************

import tkinter as tk
import pygame
from Layer import *
from File import *
from Music import *

def r_click(event=" "):

    global title, entry_title, title_text
#Gets string from entry to create new file name
    if (entry_title == True):
        title_text = title.get()
        if (title_text.isalpha()):
            title.destroy() #Deletes entry
            #Creates button again
            title = tk.Button(title_frame, text=title_text, bg=BKG
                      ,font=("Times new", 18), command = title_click,
                      width=20, relief="flat")
            title.grid(row=0, column=0)
            entry_title = False

def title_click():
    
    global title, entry_title

    entry_title = True
    title.destroy() #Destorys button once pressed creates entry field
    title = tk.Entry(title_frame, bg="White", width=20, font=("Times new", 15))
    title.grid(row=0, column=0)
    
# Saves all the different beat layers in a text file
def save_file():
    
    global entry_title, first_layer, title_text, all_music
    file_name = title_text
    all_music = first_layer.get_music()
    print(all_music)
    file = File(file_name, all_music)
    file.save()
     
def back_click(): #Destroys frames after back is pressed

    global logo_frame, music_frame, title_frame, all_layers

    music.stop() 
    logo_frame.destroy()
    all_layers = [[],[],[],[],[],[]]
    if (fp == True):
        title_frame.destroy()
    music_frame.destroy()
    home_page()

def create_click():
   
    global logo_frame, open_frame

    logo_frame.destroy()
    open_frame.destroy()
    first_page()

#Plays the music
def play_music():
    global all_layers, music
    music = Music(all_layers)
    music.play()

#Stops the music
def stop_music():
    global music
    music.stop()

#Function that helps create a layer
def layer_label(Text, a, b, c, d, e):
    label = tk.Label(music_frame, text=Text, anchor=d,
                    height=2, bg="White", width=e,
                relief="flat", font=("Times new", c))
    label.grid(row=a, column=b)

#Opens an existing file so that it can be listened to
def opening_file():

    global logo_frame, open_frame, open_files_entry, all_layers, clear
    global music_frame

    file_name = open_files_entry.get()
    logo_frame.destroy()
    open_frame.destroy()
    second_page()
    file = File(file_name, all_layers)
    file.open_file() #File is opened
    all_layers = file.get_file()

    music_frame = tk.Frame(window, bg=BKG) #Frame with layers + buttons
    music_frame.grid(row=2, column=0)
    play = tk.Button(music_frame, text="Play",font=("Times new",10),
             bg="#7c9c5d", width = 10, relief="raised",
                     command=play_music, fg="White")
    play.grid(row=1,column=1)
    stop = tk.Button(music_frame, text="Stop",font=("Times new",10),
                bg="Red", width = 10, relief="raised",
                     command=stop_music, fg="White")
    stop.grid(row=1,column=3)
    
    title = tk.Button(music_frame, text=file_name, bg=BKG,
                      font=("Times new", 18), width=20, relief="flat")
    title.grid(row=1, column=2)

    empty_label(music_frame, 10, 2, 0, 2)
    empty_label(music_frame, 10, 2, 2, 2)
    
    for i in range(6): #Creates labels with values and intruments
        if (all_layers[i] != ['nothing']):
            name = INVT[all_layers[i][0]]
            layer_label(" ", (i+3), 1, 15, "e", 17)
            layer_label(" ", (i+3), 3, 6, "e", 17)
            layer_label(name+":", (i+3), 1, 16, "e", 17)
            layer_label(("Loops: " + str(all_layers[i][3]) + "   Start: " +
             str(all_layers[i][1])+"   End: "+str(all_layers[i][2])+"   Volume: "
                     + str(all_layers[i][3])), (i+3), 2, 14, "center", 39)        
    clear = True
   
def open_click(): #Page after open is clicked

    global logo_frame, open_frame, open_files_entry

    logo_frame.destroy()
    open_frame.destroy()

#---------------------------------------------------------------------
    logo_frame = tk.Frame(window, bg=BKG)
    logo_frame.grid(row=0, column=0)
    empty_label(logo_frame, 15, 1, 0, 0)
    empty_label(logo_frame, 1, 35, 0, 1)
    logo = tk.Label(logo_frame, bg=BKG, text=NAME,
                    font=("Century 50 bold"), anchor="center")
    logo.grid(row=0, column=1)

#---------------------------------------------------------------------
    open_frame = tk.Frame(window, bg=BKG)
    open_frame.grid(row=1, column=0)
    open_files_text = tk.Label(open_frame, text="Enter the name\nof your file:"
                            ,font=("Times New", 17), anchor="center", bg=BKG)
    open_files_text.grid(row=0, column=1)

    empty_label(open_frame, 9, 1, 0, 0)
    empty_label(open_frame, 3, 1, 0, 2)
    empty_label(open_frame, 7, 1, 0, 4)

    open_files_entry = tk.Entry(open_frame, width=27,
                                font=("Times new", 15), bg=BKG)
    open_files_entry.grid(row=0, column=3)

    open_files_button = tk.Button(open_frame, width=10, text="Open", font=(16),
                                       anchor="center", command=opening_file,
                                  bg = "light blue")
    open_files_button.grid(row=0, column=5)

def empty_label(a, b, c, d, e): #Creates empty labels
   
    empty = tk.Label(a, bg=BKG, width=b, height=c)
    empty.grid(row=d, column=e)

def second_page(): #Page after file is opened
   
    global logo_frame, hp, fp, sp, tp
    hp, fp, sp, tp = False, False, True, False

#---------------------------------------------------------------------
    logo_frame = tk.Frame(window, bg=BKG)
    logo_frame.grid(row=0, column=0)
    back_button = tk.Button(logo_frame, text="\u2190", anchor="center",
                            width=3, font=("Times new", 18), bg=BKG,fg="Black",
                            command=back_click, relief="flat")
    back_button.grid(row=0, column=0)
    
    empty_label(logo_frame, 38, 1, 0, 1)
    logo = tk.Label(logo_frame, text=NAME, font=("Century 17 bold"),
                    bg=BKG, anchor="center")
    logo.grid(row=0, column=2)    
    empty_label(logo_frame, 30, 1, 0, 3)
    
def first_page(): #Page after create new is clicked

    global logo_frame, hp, fp, sp, tp, title, title_frame
    global all_layers, music_frame, first_layer
    global entry_title, title_text
    hp, fp, sp, tp, entry_title = False, True, False, False, False

#---------------------------------------------------------------------
    logo_frame = tk.Frame(window, bg=BKG)
    logo_frame.grid(row=0, column=0)
    back_button = tk.Button(logo_frame, text="\u2190", anchor="center",
                            width=3, font=("Times new", 18), bg=BKG,fg="Black",
                            command=back_click, relief="flat")
    back_button.grid(row=0, column=0)
    empty_label(logo_frame, 38, 1, 0, 1)
    logo = tk.Label(logo_frame, bg=BKG, text=NAME, font=("Century 17 bold"),
                    anchor="center")
    logo.grid(row=0, column=2)
    empty_label(logo_frame, 30, 1, 0, 3)
    
#---------------------------------------------------------------------
    title_frame = tk.Frame(window, bg=BKG)
    title_frame.grid(row=1, column=0)
    empty_label(title_frame, 27, 5, 0, 1)
    title_text = "New Recording"
    title = tk.Button(title_frame, text=title_text, bg=BKG
                      ,font=("Times new", 18), command = title_click,
                      width=20, relief="flat")
    title.grid(row=0, column=0)

# Save button---------------------------------------------------------
    save = tk.Button(title_frame, text="Save File",font=("Times new",13),
                     command=save_file, width=15, relief="raised",
                     bg="Grey", fg="White")
    save.grid(row=0, column=1)
    
# Play button---------------------------------------------------------
    space = tk.Label(title_frame,text="",bg=BKG,width=5)
    space.grid(row=0,column=2)
    play = tk.Button(title_frame, text="Play",font=("Times new",10),
             bg="#7c9c5d", width = 10, relief="raised",
                     command=play_music, fg="White")
    play.grid(row=0,column=3)

# Stop button---------------------------------------------------------
    stop = tk.Button(title_frame, text="Stop",font=("Times new",10),
                bg="Red", width = 10, relief="raised",
                     command=stop_music, fg="White")
    stop.grid(row=0,column=4)
#---------------------------------------------------------------------
    
    music_frame = tk.Frame(window, bg=BKG)
    music_frame.grid(row=2, column=0)
    editing = False
    #Creates a Layer object
    first_layer = Layer(music_frame, 0, 0, 1, DICT, all_layers, editing)

def home_page(): #Home screen
   
    global logo_frame, open_frame, hp, fp, sp, tp, create_button, open_button
    hp, fp, sp, tp = True, False, False, False
   
#---------------------------------------------------------------------
    logo_frame = tk.Frame(window, bg=BKG)
    logo_frame.grid(row=0, column=0)
    empty_label(logo_frame, 17, 1, 0, 0)
    empty_label(logo_frame, 1, 35, 0, 1)
    logo = tk.Label(logo_frame, bg=BKG, text=NAME,
                    font=("Century 50 bold"), anchor="center")
    logo.grid(row=0, column=1)

#---------------------------------------------------------------------
    open_frame = tk.Frame(window, bg=BKG)
    open_frame.grid(row=1, column=0)
    empty_label(open_frame, 15, 1, 0, 0)
    create_button = tk.Button(open_frame, text="Create New",
                              font=("Times new", 15,"bold"), anchor="center",
                              bg="#6B2012", command=create_click, width=20,
                              fg=BKG)
    create_button.grid(row=0, column=1)
    empty_label(open_frame, 10, 1, 0, 2)
    open_button = tk.Button(open_frame, text="Open File",
                            font=("Times new", 15,"bold"), anchor="center",
                            bg="#093535", command=open_click, width=20, fg=BKG)
    open_button.grid(row=0, column=3)

def main():

    global window, NAME, BKG, DIM, hp, fp, sp, tp, DICT, all_layers, clear, INVT

    NAME, BKG, DIM = "Beat Bouncer", "White", "800x800"
    hp, fp, sp, tp = False, False, False, False
    DICT = {"Trap Drums": "d1.mp3", #All instruments that match with their names
            "Top Drums": "d2.mp3",
            "Watery Drums": "d3.mp3",
            "Pressurized Drums": "d4.mp3",
            "Heavy Trap Drums": "d5.mp3",
            "Drill Drums": "d6.mp3",
            "Melodic Drums": "d7.mp3",
            "Bass Drums": "d8.mp3",
            "Perc Guitar": "g1.mp3",
            "Intro Guitar": "g2.mp3",
            "Smooth Guitar": "g3.mp3",
            "Sunset Guitar": "g4.mp3",
            "Rock Guitar": "g5.mp3",
            "Melody Guitar": "g6.mp3",
            "Trap Guitar": "g7.mp3",
            "Chill Guitar": "g8.mp3",
            "Tunnel Piano": "p1.mp3",
            "Waves Piano": "p2.mp3",
            "Electric Piano": "p3.mp3",
            "Trap Piano": "p4.mp3",
            "Hiphop Piano": "p5.mp3",
            "Mellow Piano": "p6.mp3",
            "Powerful Piano": "p7.mp3",
            "Echo Trap Piano": "p8.mp3"}
    all_layers = [[],[],[],[],[],[]]
    INVT = dict(map(reversed, DICT.items())) #Reverse dictionary
    window = tk.Tk()
    window.title(NAME)
    window.geometry(DIM)
    window.configure(bg=BKG)
    window.bind("<Return>", r_click)

    pygame.mixer.init()
 
    home_page()
   
    window.mainloop()

main()
