#**************************************************************************
#Programmer Names: Abhusha Ghimire
#Program Name: Layer Class
#Date: Jan.19 2023
#Description: The layer class creates an interactive layer object and allows
#           the user to create a layer of music.
#**************************************************************************
import tkinter as tk
import pygame

class Layer():

    def __init__(self, window, x, y, num, DICT, all_layers, editing):

        def exit_func(): #When X is clicked
            if (self.editing == False or self.can_exit):
                self.choice_frame.destroy()
                self.button = tk.Button(self.window, text=TEXT, anchor="center",
                                command=get_layer, width=10, height=2)
                self.button.grid(row=y, column=x)
                pygame.mixer.music.stop()

            #If X clicked while editing, keeps the previous layer
            elif (self.redo == True): 
                self.choice_frame.destroy()
                self.layer_frame = tk.Frame(self.window, bg="White")
                self.layer_frame.grid(row=y, column=x)
                layer_label(self.name+":", y, x, 16, "e", 17)
                layer_label(("Loops: " + str(self.loop) + "   Start: "
                             + str(self.start) +"   End: " + str(self.end) +
                             "   Volume: " + str(self.volume)),
                            y, (x+1), 14, "center", 39)
                self.edit = tk.Button(self.layer_frame, command=edit_func,
                      text="Edit", width=10)
                self.edit.grid(row=y, column=(x+2))

        #Creates frame for different pop ups (easy to destroy frames)
        def create_frame():
            self.choice_frame = tk.Frame(self.window)
            self.choice_frame.grid(row=y, column=x)
            exit_button = tk.Button(self.choice_frame, text="X", bg="Red",
                        fg="White", command=exit_func, width=3, anchor="center")
            exit_button.grid(row=0, column=0)

        #Creates frame + destorys window after a type of instrument is chosen
        def create_select():
            self.choice_frame.destroy()
            create_frame()
            select_label = tk.Label(self.choice_frame, width=30,anchor="center",
                font=("Times new", 17), text="\nSelect One:\t\n")
            select_label.grid(row=1, column=1)

        #Creates empty labels for design
        def empty_label(x, y):
            empty_label = tk.Label(self.choice_frame, width=1,anchor="center",
                font=("Times new", 13), text="")
            empty_label.grid(row=x, column=y)

        #Plays music when radiobutton clicks on it
        def play():
            pygame.mixer.music.load(self.beat)
            pygame.mixer.music.play(loops=self.loop)

        #Layers
        def layer_label(Text, a, b, c, d, e):
            self.label = tk.Label(self.layer_frame, text=Text, anchor=d,
                      height=2, bg="White", width=e,
                    relief="flat", font=("Times new", c))
            self.label.grid(row=a, column=b)

        #Deletes frame after delete layer is pressed creates new object
        def delete():
            self.choice_frame.destroy()
            self.all_layers[self.num - 1].clear()
            Layer(self.window,x,y,(self.num),self.DICT,self.all_layers,
                  self.editing)

        #When edit layer is pressed deletes frame uses get_layer function again
        def edit_func():
            self.editing = True
            self.redo = True
            self.can_exit = False
            self.layer_frame.destroy()
            get_layer()
            delete_button = tk.Button(self.choice_frame, text="Delete Layer!",
                anchor="center", command=delete, width=22,
                bg="Red", fg="White", font=("Times new", 11))
            delete_button.grid(row=10, column=1)
            empty_label(11, 1)

        #Validates all entry numbers
        def validation(w, x, y, z):
            valid = False
            def num_valid(n):
                try:
                    float(n)
                except ValueError:
                    return False
                return True
    
            if (num_valid(w) and num_valid(x) and num_valid(y)
                and num_valid(z)):
                valid = True
                if (float(x) >= float(y)): #Start time is greater than end time
                    valid = False
                if ((float(z) < 0) or (float(z) > 1)): #Not 0-1
                    valid = False
        
            return valid

        def save(): #Saves layer creates new Layer object
            pygame.mixer.music.stop()
            self.loop = self.loop_entry.get() #Gets entry values
            self.start = self.start_entry.get()
            self.end = self.end_entry.get()
            self.volume = self.volume_entry.get()
            
            if(self.editing and self.redo): #Clears list if editing
                self.all_layers[self.num - 1].clear()
                self.redo = False
            
            if (validation(self.loop, self.start, self.end, self.volume)):
                #Stores values in a list containing all layer data
                self.all_layers[self.num-1].extend((self.beat,self.start,
                                        self.end,self.loop,self.volume))
                self.loop = int(float(self.loop))
                self.start = float(self.start)
                self.end = float(self.end)
                self.choice_frame.destroy()
                self.layer_frame = tk.Frame(self.window, bg="White")
                self.layer_frame.grid(row=y, column=x)
                layer_label(" ", y, x, 15, "e", 17)
                layer_label(" ", y, (x+2), 6, "e", 17)
                layer_label(self.name+":", y, x, 16, "e", 17)
                #Displays the values in a label
                layer_label(("Loops: " + str(self.loop) + "   Start: "
                             + str(self.start) +"   End: " + str(self.end) +
                             "   Volume: " + str(self.volume)),
                            y, (x+1), 14, "center", 39)
                self.edit = tk.Button(self.layer_frame, command=edit_func,
                      text="Edit", width=10)
                self.edit.grid(row=y, column=(x+2)) #Edit button to edit layer

                #If layer is not the 6th layer, creates new Layer object
                if (self.num < 6 and self.editing == False):
                    Layer(self.window, x,(y+1),(self.num+1),self.DICT,
                          self.all_layers, self.editing)
                
            else:
                self.loop = 0
                self.soundbutton.configure(bg="Red")
    

        def sound_func(): #Pop up filled with GUI for values
            pygame.mixer.music.stop()
            self.choice_frame.destroy()
            create_frame()
            sound_label = tk.Label(self.choice_frame, width=14, anchor="center",
                font=("Times new", 18),text=("\n"+self.name+"\n"))
            sound_label.grid(row=2, column=2)
            tk.Label(self.choice_frame, width=7,anchor="e",
                text=("Start at:"), font=("Times new", 14)).grid(row=3,column=1)
            self.start_entry = tk.Entry(self.choice_frame, width=20)
            self.start_entry.grid(row=3, column=2)
            tk.Label(self.choice_frame, width=7,anchor="w",
                text=("secs"), font=("Times new", 14)).grid(row=3,column=3)
            tk.Label(self.choice_frame, width=7,anchor="e",
                text=("End at:"), font=("Times new", 14)).grid(row=4,column=1)
            self.end_entry = tk.Entry(self.choice_frame, width=20)
            self.end_entry.grid(row=4, column=2)
            tk.Label(self.choice_frame, width=7,anchor="w",
                text=("secs"), font=("Times new", 14)).grid(row=4,column=3)
            tk.Label(self.choice_frame, width=7,anchor="e",
                text=("Loop:"), font=("Times new", 14)).grid(row=5, column=1)
            self.loop_entry = tk.Entry(self.choice_frame, width=20)
            self.loop_entry.grid(row=5, column=2)
            tk.Label(self.choice_frame, width=7,anchor="w",
                text=("times"), font=("Times new", 14)).grid(row=5,column=3)
            tk.Label(self.choice_frame, width=9,anchor="e",
                text=("Volume:"), font=("Times new", 14)).grid(row=6, column=1)
            self.volume_entry = tk.Entry(self.choice_frame, width=20)
            self.volume_entry.grid(row=6, column=2)
            tk.Label(self.choice_frame, width=8,anchor="w",
                text=("0 - 1"), font=("Times new", 14)).grid(row=6,column=3)
            empty_label(8, 1)
            tk.Button(self.choice_frame, text="Play Sound", width=20,
                      command=play, bg="White", fg="Black").grid(row=9,column=2)
            self.soundbutton = tk.Button(self.choice_frame, text="Save Sound",
                          width=20,command=save, bg="Gray", fg="White")
            self.soundbutton.grid(row=10,column=2)
            empty_label(8, 1)

        def get_beat(x): #Gets beat and calls play() allows user to use sound
            self.name = x
            self.beat = self.DICT[x]
            self.loop = 0
            play()
            empty_label(9, 1)
            button = tk.Button(self.choice_frame, text="Add Sound", width=25,
                               bg="Black", fg="White", command=sound_func)
            button.grid(row=12, column=1)
            empty_label(11, 1)

        def drum_beats(): #Options for drum beats
            def drum_select(): #When a radiobutton gets clicked
                get_beat(self.drum_var.get())

            def drum_choices(w, x, y, z): #Creates drum radiobuttons
                radiobutton = tk.Radiobutton(self.choice_frame, text=w, width=30
                    ,anchor="w", variable=z, value=w, command=drum_select,
                                             font=("Times new", 13))
                radiobutton.grid(row=x, column=y)
                
            create_select()
            self.drum_var = tk.StringVar()
            for i in range(8): #Uses tuple created from dictionary to
                               #display all drum selection options
                drum_choices(self.TUP[i][0], (i+2), 1, self.drum_var)
                empty_label(12, 1)
                    
        def guitar_beats(): #Same thing as drums but with guitar          
            def guitar_select():
                get_beat(self.guitar_var.get())

            def guitar_choices(w, x, y, z):
                radiobutton = tk.Radiobutton(self.choice_frame, text=w, width=30
                    ,anchor="w", variable=z, value=w, command=guitar_select,
                                             font=("Times new", 13))
                radiobutton.grid(row=x, column=y)

            create_select()
            self.guitar_var = tk.StringVar()
            for i in range(8):
                guitar_choices(self.TUP[i+8][0], (i+2), 1, self.guitar_var)
                empty_label(12, 1)
                
        def piano_beats():#Same thing as drums but with piano
            def piano_select():
                get_beat(self.piano_var.get())

            def piano_choices(w, x, y, z):
                radiobutton = tk.Radiobutton(self.choice_frame, text=w, width=30
                    ,anchor="w", variable=z, value=w, command=piano_select,
                                             font=("Times new", 13))
                radiobutton.grid(row=x, column=y)
                
            create_select()
            self.piano_var = tk.StringVar()
            for i in range(8):
                piano_choices(self.TUP[i+16][0], (i+2), 1, self.piano_var)
                empty_label(12, 1)

        #Gives option for the different types of instruments
        def get_layer():
            self.button.destroy()
            create_frame()
            beats_label = tk.Label(self.choice_frame, width=30, anchor="center",
                font=("Times new", 17), text="\nPre-made Beats\t\n",)
            beats_label.grid(row=1, column=1)
            drums_button = tk.Button(self.choice_frame, text="+ Drums",
                anchor="w", command=drum_beats, width=20, relief="flat",
                font=("Times new", 14))
            drums_button.grid(row=2, column=1)
            guitar_label = tk.Button(self.choice_frame, text="+ Guitar",
                anchor="w", command=guitar_beats, width=20, relief="flat",
                font=("Times new", 14))
            guitar_label.grid(row=3, column=1)
            piano_label = tk.Button(self.choice_frame, text="+ Piano",
                anchor="w", command=piano_beats, width=20, relief="flat",
                font=("Times new", 14))
            piano_label.grid(row=4, column=1)
            empty_label(9, 1)

        pygame.mixer.init()

        #Instantiates variables
        self.redo, self.can_exit = False, True
        self.editing = editing
        self.all_layers = all_layers
        self.num, self.x, self.y = num, x, y
        self.window = window
        if (self.num == 1):
            TEXT = "Add music"
        else:
            TEXT = "Add layer"
        self.DICT = DICT
        self.TUP = list(self.DICT.items())
        self.button = tk.Button(self.window, text=TEXT, anchor="center",
                                command=get_layer, width=10, height=2)
        self.button.grid(row=y, column=x)

    #Gets music
    def get_music(self):
            return self.all_layers
