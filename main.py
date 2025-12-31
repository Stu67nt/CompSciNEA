import customtkinter
from widgets import *
from Components import *

class App(customtkinter.CTk): # Inheriting CTk class
    def __init__(self, title: str="My App"):
        super().__init__() # Calls parent class

        # Initialising Window
        self.title(title)
        self.grid_rowconfigure((0,4), weight=1)
        self.grid_columnconfigure((0,1), weight=1)
        customtkinter.set_appearance_mode("dark") # light/dark/system (system is not functional on linux)

        # Creating Home Bar
        BUTTONS = [["Home", self.hi], ["Tracks", self.hi], ["Playlists", self.hi], ["Music Finder", self.hi],
                   ["Favourites", self.hi], ["Settings", self.hi]]

        self.buttons = ButtonFrame(self, button_values = BUTTONS, is_horizontal = True)
        self.buttons.grid(row=0, column=0, padx=10, pady=(10,10), sticky="new", columnspan = 2)

        # Creating To Do List
        self.todo = ToDoList(self)
        self.todo.grid(row=1, column=0, padx=(10,10), pady=(10,10), sticky="nwe")

        # Creating timer
        self.timer = TimerCreate(self)
        self.timer.grid(row=1, column=1, padx=(10,10), pady=(10,10), sticky = "nwse")

    def hi(self):
        print("hi")



app = App("Balls") # Creating app object
app.mainloop() # Needed to actually display the app.