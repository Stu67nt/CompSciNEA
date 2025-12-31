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

        self.frame = customtkinter.CTkFrame(self)

        self.frame.grid(row=2, column=0, sticky="nsew") # Master frame to Place to do list in
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        todo_checkboxes = ["Task 1", "Task 2", "Task 3"]
        self.todo = CheckboxFrame(self.frame, title="To Do List:", values= todo_checkboxes) # Make Transparent
        self.todo.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nwe")

        self.input = customtkinter.CTkEntry(self.frame)
        self.input.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nwe")

        self.buttons = ButtonFrame(self.frame, [["Create Task", self.balls], ["Delete Tasks", self.balls]], is_horizontal = True)
        self.buttons.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="nwe")

    def balls(self):
        print("Balls")

class TimerCreate(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # This line below is there so the frame scales to take up the free space
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.BUTTON = [["Start Timer", self.test]]

        self.title_label = customtkinter.CTkLabel(self, text="Timer", fg_color="gray30", corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new")


    def test(self):
        print("test")