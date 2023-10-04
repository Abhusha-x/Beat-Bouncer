#**************************************************************************
#Programmer Names: Abhusha Ghimire
#Program Name: Music Class
#Date: Jan.19 2023
#Description: The music class that allows the user to play/stop the music
#**************************************************************************

import pygame
import time
from threading import Thread
from File import *
import sys

class Music():
    
    pygame.mixer.init()

    def __init__(self, layers):
        
        self.layers = layers
        self.go = True
        
        #Channels (the layers for each instrument)
        self.channel_one = pygame.mixer.Channel(0)
        self.channel_two = pygame.mixer.Channel(1)
        self.channel_three = pygame.mixer.Channel(2)
        self.channel_four = pygame.mixer.Channel(3)
        self.channel_five = pygame.mixer.Channel(4)
        self.channel_six = pygame.mixer.Channel(5)
        
    # If a layer is not empty then the audio will be played through the
    # respective channel
    def play(self):

        def run_channel_one():
            if(len(self.layers[0]) ==5):
                self.sound1 = pygame.mixer.Sound(self.layers[0][0])
                self.channel_one.set_volume(float(self.layers[0][4]))
                self.max = (int(self.layers[0][2])-int(self.layers[0][1]))*1000
                time.sleep(int(self.layers[0][1]))
                if (self.go == False):
                    return
                else:
                    self.channel_one.play(self.sound1, loops=int(self.layers[0][3])-1,
                                maxtime = self.max)  

        def run_channel_two():
            if(len(self.layers[1]) ==5):
                self.sound2 = pygame.mixer.Sound(self.layers[1][0])
                self.channel_two.set_volume(float(self.layers[1][4]))
                self.max = (int(self.layers[1][2])-int(self.layers[1][1]))*1000
                time.sleep(int(self.layers[1][1]))
                if (self.go == False):
                    return
                else:
                    self.channel_two.play(self.sound2, loops=int(self.layers[1][3])-1,
                                maxtime = self.max)

        def run_channel_three():
            if(len(self.layers[2]) ==5):
                self.sound3 = pygame.mixer.Sound(self.layers[2][0])
                self.channel_three.set_volume(float(self.layers[2][4]))
                self.max = (int(self.layers[2][2])-int(self.layers[2][1]))*1000
                time.sleep(int(self.layers[2][1]))
                if (self.go == False):
                    return
                else:
                    self.channel_three.play(self.sound3, loops=int(self.layers[2][3])-1,
                                maxtime = self.max)

        def run_channel_four():
            if(len(self.layers[3]) ==5):
                self.sound4 = pygame.mixer.Sound(self.layers[3][0])
                self.channel_four.set_volume(float(self.layers[3][4]))
                self.max = (int(self.layers[3][2])-int(self.layers[3][1]))*1000
                time.sleep(int(self.layers[3][1]))
                if (self.go == False):
                    return
                else:
                    self.channel_four.play(self.sound4, loops=int(self.layers[3][3])-1,
                                maxtime = self.max)

        def run_channel_five():
            if(len(self.layers[4]) == 5):
                self.sound5 = pygame.mixer.Sound(self.layers[4][0])
                self.channel_five.set_volume(float(self.layers[4][4]))
                self.max = (int(self.layers[4][2])-int(self.layers[4][1]))*1000
                time.sleep(int(self.layers[4][1]))
                if (self.go == False):
                    return
                else:
                    self.channel_five.play(self.sound5, loops=int(self.layers[4][3])-1,
                                maxtime = self.max)

        def run_channel_six():
            if(len(self.layers[5]) == 5):
                self.sound6 = pygame.mixer.Sound(self.layers[5][0])
                self.channel_six.set_volume(float(self.layers[5][4]))
                self.max = (int(self.layers[5][2])-int(self.layers[5][1]))*1000
                time.sleep(int(self.layers[5][1]))
                if (self.go == False):
                    return
                else:
                    self.channel_six.play(self.sound6, loops=int(self.layers[5][3])-1,
                                maxtime = self.max)
        
        # Assigning each channel to a thread so that they can run simultaneously
        self.first_channel = Thread(target = run_channel_one)
        self.second_channel = Thread(target = run_channel_two)
        self.third_channel = Thread(target = run_channel_three)
        self.fourth_channel = Thread(target = run_channel_four)
        self.fifth_channel = Thread(target = run_channel_five)
        self.sixth_channel = Thread(target = run_channel_six)

        self.first_channel.start()
        self.second_channel.start()
        self.third_channel.start()
        self.fourth_channel.start()
        self.fifth_channel.start()
        self.sixth_channel.start()

    # stops all playback on each channel
    def stop(self):
        self.go = False
        self.channel_one.stop()
        self.channel_two.stop()
        self.channel_three.stop()
        self.channel_four.stop()
        self.channel_five.stop()
        self.channel_six.stop()
        


