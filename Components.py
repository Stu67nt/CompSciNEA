from widgets import *
import customtkinter
from customtkinter import CTkFrame

class ToDoList(customtkinter.CTkFrame):
    """
    TODO:
        Tie todo_checkboxes list to the db
        Create the to_do db
        Pretty much make the thing functional
    """
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=0, sticky="nsew") # Master frame to Place to do list in
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_label = customtkinter.CTkLabel(self, text="To Do List:", fg_color="gray30", corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new", columnspan=2)

        todo_checkboxes = ["Task 1", "Task 2", "Task 3"]
        self.todo = CheckboxFrame(self, values= todo_checkboxes) # Make Transparent
        self.todo.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nwe")

        self.input = customtkinter.CTkEntry(self)
        self.input.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="nwe")

        self.buttons = ButtonFrame(self, [["Create Task", self.balls], ["Delete Tasks", self.balls]], is_horizontal = True)
        self.buttons.grid(row=3, column=0, padx=10, pady=(10, 10), sticky="nw")

    def balls(self):
        print("Balls")

class TimerCreate(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


        # This line below is there so the frame scales to take up the free space
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.BUTTON = [["Start Timer", self.test]]

        self.title_label = customtkinter.CTkLabel(self, text="Timer", fg_color="gray30", corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="new", columnspan=2)

        self.hours_label = customtkinter.CTkLabel(self, text="Enter Hours: ", fg_color="transparent", corner_radius=6)
        self.hours_label.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nw")

        self.mins_label = customtkinter.CTkLabel(self, text="Enter Miniutes: ", fg_color="transparent", corner_radius=6)
        self.mins_label.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="nw")

        self.secs_label = customtkinter.CTkLabel(self, text="Enter Seconds: ", fg_color="transparent", corner_radius=6)
        self.secs_label.grid(row=3, column=0, padx=10, pady=(10, 10), sticky="nw")

        self.button = ButtonFrame(self, self.BUTTON, is_horizontal = True, button_sticky = "nw")
        self.button.grid(row=4, column=0, padx=10, pady=(10, 10), sticky="nw")

    def test(self):
        print("test")