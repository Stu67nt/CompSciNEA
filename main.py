import customtkinter
import tkinter as tk
from widgets import *
from Components import *


class Home(customtkinter.CTk): # Inheriting CTk class
    def __init__(self, master):
        super().__init__() # Calls parent class

        # Creating Home Bar
        HOMEBAR = [["Home", self.hi], ["Tracks", self.hi], ["Playlists", self.hi], ["Music Finder", self.hi],
                   ["Favourites", self.hi], ["Settings", self.hi]]

        BUTTONS = [["Scan Music", self.hi], ["Add Folder", self.hi]]

        # Creating To Do List
        self.todo = ToDoList(master)
        self.todo.grid(row=1, column=0, padx=(10,10), pady=(10,10), sticky="nwe", rowspan = 2)

        # Creating timer
        self.timer = TimerCreate(master)
        self.timer.grid(row=1, column=1, padx=(10,10), pady=(10,10), sticky = "nwse")

        self.buttons = ButtonFrame(master, button_values=BUTTONS, is_horizontal=True)
        self.buttons.grid(row=2, column=1, padx=10, pady=(10, 10), sticky="new")

    def hi(self):
        print("hi")

class Tracks(customtkinter.CTk): # Inheriting CTk class
    def __init__(self, master, title: str="My App"):
        super().__init__() # Calls parent class

        TOPBAR = [["Select Multiple", self.hi]]
        song_count = 50

        self.topbar = customtkinter.CTkLabel(master)
        self.topbar.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="new")

    def hi(self):
        print("hi")

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master)

		# create tabs
        self.add("Home")
        self.add("Tracks")

		# add widgets on tabs
        self.home = Home(master=self.tab("Home"))
        self.home.grid()

        self.tracks = Tracks(master=self.tab("Tracks"))
        self.tracks.grid()

class App(customtkinter.CTk):
    def __init__(self, title="My App"):
        super().__init__()

        # Initialising Window
        self.title(title)
        customtkinter.set_appearance_mode("dark")  # light/dark/system (system is not functional on linux)

        self.tab_view = MyTabView(self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


app = App("Balls")
app.mainloop()