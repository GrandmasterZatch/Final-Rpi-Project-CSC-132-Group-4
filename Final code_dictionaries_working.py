#################################################################
# Name: group 4 
# Date:
# Description:
#################################################################
from Tkinter import *
from random import randint 
# the room class
class Room(object):
    # the constructor
    def __init__(self, name):
# rooms have a name, an image (the name of a file),
# exits (e.g., south), exit locations
# (e.g., to the south is room n), items (e.g., table),
# item descriptions (for each item), and grabbables
# (things that can be taken into inventory)
        self.name = name
        self.exits = {}
        self.storys = {}
        self.options_s = {}

        
# getters and setters for the instance variables
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def storys(self):
        return self._storys
    @storys.setter
    def storys(self, value):
        self._storys = value
    @property
    def options_s(self):
        return self._options_s
    @options_s.setter
    def options_s(self, value):
        self._options_s = value
###########################################
 
    @property
    def exits(self):
            return self._exits
    @exits.setter
    def exits(self, value):
            self._exits = value
###########################################
    def addstory(self,story,desc):
        self._storys[story] = desc
#
    def addoptions(self,options , desc):
        self._options_s[options] = desc
###########################################
 
    def addExit(self, exit, room):
    # append the exit and room to the appropriate
    # dictionary
        self._exits[exit] = room
###########################################
# returns a string description of the room
    def __str__(self):
        s = ""
# next, the items in the room
        for story in self.storys.keys():
            s += "{}\n".format(story)
            
        for options  in self.options_s.keys():
            s += self.options_s[options] + ","
        
        s += "\n"
# next, the exits from the room
        return s
# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
# the constructor
    def __init__(self, parent):
# call the constructor in the superclass
        Frame.__init__(self, parent)
# creates the rooms
    def createRooms(self):
        # r1 through r4 are the four rooms in the mansion
# currentRoom is the room the player is currently in (which
# can be one of r1 through r4)
# create the rooms and give them meaningful names and an
# image in the current directory
        r1 = Room("level 1") 
        r2 = Room ("2") 
        r3 = Room("3") 
        r4 = Room("4") 
        r5 = Room("5") 
        r6 = Room("6") 
        r7 = Room("7") 
        
        # can use this to keep track of the levels ans groups of the qustions 
        r1.addstory(1,"")#1
        r1.addoptions("1.1.1","A:")#1.1.1
        r1.addoptions("1.1.2","B:")#1.1.2
        r1.addoptions("1.1.3","C:")#1.1.3
        r1.addExit("down",r2)
    #
        R2 = randint(1,6)
        if R2 == 1:
            r2.addstory("2.1","")
            r2.addoptions("2.1.1 ","A:")
            r2.addoptions("2.1.2 ","B:")
            r2.addoptions("2.1.3 ","C:")
        if R2 ==2:
            r2.addstory("2.2","")
            r2.addoptions("2.2.1 ","A:")
            r2.addoptions("2.2.2 ","B:")
            r2.addoptions("2.2.3 ","C:")
        if R2 ==3:
            r2.addstory("2.3","")
            r2.addoptions("2.3.1 ","A:")
            r2.addoptions("2.3.2 ","B:")
            r2.addoptions("2.3.3 ","C:")
        if R2 ==4:
            r2.addstory("2.4","")
            r2.addoptions("2.4.1 ","A:")
            r2.addoptions("2.4.2 ","B:")
            r2.addoptions("2.4.3 ","C:")
        if R2 ==5:
            r2.addstory("2.5","")
            r2.addoptions("2.5.1 ","A:")
            r2.addoptions("2.5.2 ","B:")
            r2.addoptions("2.5.3 ","C:")
        r2.addExit("down",r3)

        R3= randint(1,6)
        if R3 == 1:
            r3.addstory("3.1","")
            r3.addoptions("3.1.1 ","A:")
            r3.addoptions("3.1.2 ","B:")
            r3.addoptions("3.1.3 ","C:")
        if R3 ==2:
            r3.addstory("3.2","")
            r3.addoptions("3.2.1 ","A:")
            r3.addoptions("3.2.2 ","B:")
            r3.addoptions("3.2.3 ","C:")
        if R3 ==3:
            r3.addstory("3.3","")
            r3.addoptions("3.3.1 ","A:")
            r3.addoptions("3.3.2 ","B:")
            r3.addoptions("3.3.3 ","C:")
        if R3 ==4:
            r3.addstory("3.4","")
            r3.addoptions("3.4.1 ","A:")
            r3.addoptions("3.4.2 ","B:")
            r3.addoptions("3.4.3 ","C:")
        if R3 ==5:
            r3.addstory("3.5","")
            r3.addoptions("3.5.1 ","A:")
            r3.addoptions("3.5.2 ","B:")
            r3.addoptions("3.5.3 ","C:")
        r3.addExit("down",r4)

        R4 = randint(1,6)
        if R4 == 1:
            r4.addstory("4.1","")
            r4.addoptions("4.1.1 ","A:")
            r4.addoptions("4.1.2 ","B:")
            r4.addoptions("4.1.3 ","C:")
        if R4 ==2:
            r4.addstory("4.2","")
            r4.addoptions("4.2.1 ","A:")
            r4.addoptions("4.2.2 ","B:")
            r4.addoptions("4.2.3 ","C:")
        if R4 ==3:
            r4.addstory("4.3","")
            r4.addoptions("4.3.1 ","A:")
            r4.addoptions("4.3.2 ","B:")
            r4.addoptions("4.3.3 ","C:")
        if R4 ==4:
            r4.addstory("4.4","")
            r4.addoptions("4.4.1 ","A:")
            r4.addoptions("4.4.2 ","B:")
            r4.addoptions("4.4.3 ","C:")
        if R4 ==5:
            r4.addstory("4.5","")
            r4.addoptions("4.5.1 ","A:")
            r4.addoptions("4.5.2 ","B:")
            r4.addoptions("4.5.3 ","C:")
        r4.addExit("down",r5)

        R5= randint(1,6)
        if R5 == 1:
            r5.addstory("5.1","")
            r5.addoptions("5.1.1 ","A:")
            r5.addoptions("5.1.2 ","B:")
            r5.addoptions("5.1.3 ","C:")
        if R5 ==2:
            r5.addstory("5.2","")
            r5.addoptions("5.2.1 ","A:")
            r5.addoptions("5.2.2 ","B:")
            r5.addoptions("5.2.3 ","C:")
        if R5 ==3:
            r5.addstory("5.3","")
            r5.addoptions("5.3.1 ","A:")
            r5.addoptions("5.3.2 ","B:")
            r5.addoptions("5.3.3 ","C:")
        if R5 ==4:
            r5.addstory("5.4","")
            r5.addoptions("5.4.1 ","A:")
            r5.addoptions("5.4.2 ","B:")
            r5.addoptions("5.4.3 ","C:")
        if R5 ==5:
            r5.addstory("5.5","")
            r5.addoptions("5.5.1 ","A:")
            r5.addoptions("5.5.2 ","B:")
            r5.addoptions("5.5.3 ","C:")
        r5.addExit("down",r6)

        R6= randint(1,6)
        if R6 == 1:
            r6.addstory("6.1","")
            r6.addoptions("6.1.1 ","A:")
            r6.addoptions("6.1.2 ","B:")
            r6.addoptions("6.1.3 ","C:")
        if R6 ==2:
            r6.addstory("6.2","")
            r6.addoptions("6.2.1 ","A:")
            r6.addoptions("6.2.2 ","B:")
            r6.addoptions("6.2.3 ","C:")
        if R6 ==3:
            r6.addstory("6.3","")
            r6.addoptions("6.3.1 ","A:")
            r6.addoptions("6.3.2 ","B:")
            r6.addoptions("6.3.3 ","C:")
        if R6 ==4:
            r6.addstory("6.4","")
            r6.addoptions("6.4.1 ","A:")
            r6.addoptions("6.4.2 ","B:")
            r6.addoptions("6.4.3 ","C:")
        if R6 ==5:
            r6.addstory("6.5","")
            r6.addoptions("6.5.1 ","A:")
            r6.addoptions("6.5.2 ","B:")
            r6.addoptions("6.5.3 ","C:")
        r6.addExit("down",r6)

        R7= randint(1,6)
        if R7 == 1:
            r7.addstory("7.1","")
            r7.addoptions("7.1.1 ","A:")
            r7.addoptions("7.1.2 ","B:")
            r7.addoptions("7.1.3 ","C:")
        if R7 ==2:
            r7.addstory("7.2","")
            r7.addoptions("7.2.1 ","A:")
            r7.addoptions("7.2.2 ","B:")
            r7.addoptions("7.2.3 ","C:")
        if R7 ==3:
            r7.addstory("7.3","")
            r7.addoptions("7.3.1 ","A:")
            r7.addoptions("7.3.2 ","B:")
            r7.addoptions("7.3.3 ","C:")
        if R7 ==4:
            r7.addstory("7.4","")
            r7.addoptions("7.4.1 ","A:")
            r7.addoptions("7.4.2 ","B:")
            r7.addoptions("7.4.3 ","C:")
        if R6 ==5:
            r6.addstory("7.5","")
            r6.addoptions("7.5.1 ","A:")
            r6.addoptions("7.5.2 ","B:")
            r6.addoptions("7.5.3 ","C:")
        # just in case we add more rooms: r6.addExit("down",r6)

### this is 31 options 
# game
        Game.currentRoom = r1
# initialize the player's inventory
        Game.inventory = []


# sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)
        # the widget is a Tkinter Entry
# set its background to white and bind the return key to the
# function process in the class
# push it to the bottom of the GUI and let it fill
# horizontally
# give it focus so the player doesn't have to click on it
        Game.player_input = Entry(bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        #Game.player_input.focus()
# setup the image to the left of the GUI
# the widget is a Tkinter Label
# don't let the image control the widget's size
        
        # setup the text to the right of the GUI
# first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH )
# the widget is a Tkinter Text
# disable it by default
# don't let the widget control the frame's size
        Game.text = Text(bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=TOP, fill=X)
        text_frame.pack_propagate(False)

# setup the player input at the bottom of the GUI


# sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        
# otherwise, display the appropriate status
        Game.text.insert(END, str(Game.currentRoom)  +"\n \n" + status)
        Game.text.config(state=DISABLED)
# play the game
    def play(self):
# add the rooms to the game
        self.createRooms()
# configure the GUI
        self.setupGUI()
# set the current room
     
# set the current status
        self.setStatus("")

# processes the player's input
########################################################################################
    def process(self, event):
# grab the player's input from the input at the bottom of
# the GUI
        action = Game.player_input.get()
# set the user's input to lowercase to make it easier to
# compare the verb and noun to known values
        action = action.lower()
# set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, use and take"
# if the player is dead if goes/went south from room 4
        if (Game.currentRoom == None):
# clear the player's input
            Game.player_input.delete(0, END)
            return
# exit the game if the player wants to leave (supports quit,exit, and bye)
        if (action  == "quit" or action   == "exit" or action  == "bye" or action  == "sionara!"):
                exit (0)
# split the user input into words (words are separated by spaces) and store the words in a list the game only understands two word inputs
        words = action.split()
        if (len(words) == 2  ):
# isolate the verb and noun
            verb = words[0]
            noun = words[1]
# the verb is: go
            if (verb == "go"):
# set a default response
                response = "Invalid exit."
# check for valid exits in the current room
                if (noun in Game.currentRoom.exits):
# if one is found, change the current room to the one that is associated with the specified exit
                    Game.currentRoom = Game.currentRoom.exits[noun]
                    
                    response = "went down a level"
# the verb is: look
            elif (verb == "look"):
# set a default response
                response = "I don't see that item."
# check for valid items in the current room
                if (noun in Game.currentRoom.options_s):
# if one is found, set the response to the item's description
                    response = Game.currentRoom.options_s[noun]

##############################################################################
# the verb is: take
            elif (verb == "take"):
# set a default response
                response = "I don't see that item."
# check for valid grabbable items in the current room
                if noun in Game.currentRoom.options_s:
                    Game.inventory.append(noun)
                  
              
###############################################################################

         
##############################################################################################################
# display the response on the right of the GUI
# display the room's image on the left of the GUI
# clear the player's input
        self.setStatus(response)
        Game.player_input.delete(0, END)
##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 800
# create the window
window = Tk()
window.title("Room Adventure")
# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()
# wait for the window to close
window.mainloop()

