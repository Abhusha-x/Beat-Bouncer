#**************************************************************************
#Programmer Name: Abhusha Ghimire
#Program Name: File Class
#Date: Jan.19 2023
#Description: Creates file objects that saves all the music data & writes it in
#             a text file. It can also open a file, read the contents and write
#             it to a record.
#***************************************************************************

class File():

    def __init__(self, name, layers):
        self.name = name
        self.layers = layers
        self.open_layers = []
        
    # Writes the user's music selections and settings to a file
    def save(self):
        self.file = open(self.name + ".txt", "w")
        for sound in self.layers:
            if(len(sound) != 0):
                for i in range(5):
                    self.file.write(str(sound[i])+ " ")
                self.file.write("\n")
            else:
                self.file.write("nothing")
                self.file.write("\n")

        self.file.close()
        
    # Reads the user's file of choice and stores the info in a list
    def open_file(self):
        self.file = open(self.name + ".txt", "r")
        self.row = self.file.readline()

        while (self.row != ""):
            if (self.row == "nothing"):
                self.open_layers.append(self.row)
            else:
                self.row = self.row.split()
                self.open_layers.append(self.row)
            self.row = self.file.readline()
        
            
        self.file.close()

    def get_file(self):

        return self.open_layers

