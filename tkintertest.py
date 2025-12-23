# Use this as a quick reference guide for how to do basic things in customTkinter!
# If you need more refer to here: https://customtkinter.tomschimansky.com/tutorial/beginner

import customtkinter
from customtkinter import CTkFrame

# Use OOP for tkinter stuff to make the code much cleaner

# Often there is something in CustonTkinter you should inherit when making a widget.
# You can then build upon it yourself.
# This is an example of a Check Box you should make classes for each of the main widgets.
class CheckboxFrame(customtkinter.CTkFrame):  # Inheriting CTkFrame class
    # self and master are standard idk why they are there tbh.

    # Title is the name of this specific checkbox frame you are creating.
        # titling it as "my_frame_1" would allow you to refer to this specifc frame as "my_frame_1" when using for CTk fucntions.

    # values is a list of all the checkboxes you want and their names.
        # ["value1", "value2", "value3"] creates a frame holding 3 checkboxes named respectively
    def __init__(self, master, title: str, values: list):
        super().__init__(master) # Calls/runs parent class. This is necessary so it initialises the inherited class.

        # This line below is there so the frame scales to take up the free space
        self.grid_columnconfigure(0, weight=1)

        # initialising variables
        self.values = values
        self.checkboxes = []
        self.title = title

        # Creating and positioning title in frame
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new")

        # Iterating through each item in values and creating a checkbox for it.
        # Each checkbox is then added to a list of checkboxes so we can track their state.
        for i, value in enumerate(self.values):
            self.checkbox = customtkinter.CTkCheckBox(self, text=value)
            self.checkbox.grid(row=i+1, column=0, padx=20, pady=20, sticky="w")
            self.checkboxes.append(self.checkbox)

    # Returning which checkboxes have been ticked.
    def get_checkboxes(self):
        checked = []
        for box in self.checkboxes:
            if box.get() == 1:
                checked.append(box.cget("text"))
        return checked


class RadiobuttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title: str, values: list):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.values = values
        self.title = title
        self.var = customtkinter.StringVar(value = "")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new")

        for i, value in enumerate(self.values):
            self.radio_button = customtkinter.CTkRadioButton(self, text=value, variable=self.var, value=value)
            self.radio_button.grid(row=i + 1, column=0, padx=20, pady=20, sticky="w")

    def get_radio_val(self):
        return self.var.get()


class App(customtkinter.CTk): # Inheriting CTk class
    def __init__(self, title: str="My App"):
        super().__init__() # Calls parent class

        # Initialising Window
        self.title(title)
        self.grid_rowconfigure((0,4), weight=1)
        self.grid_columnconfigure((0,1), weight=1)
        customtkinter.set_appearance_mode("dark") # light/dark/system (system is not functional on linux)

        # Creating different objects in window
        self.checkbox_frame = CheckboxFrame(self, "HI", ["Pick me!", "No Pick Me!", "No I'm better!"])
        self.checkbox_frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nswe")

        self.checkbox_frame1 = CheckboxFrame(self, "I'M DAISY!", ["Pick me!", "No Pick Me!"])
        self.checkbox_frame1.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nswe")

        self.radiobutton_frame = RadiobuttonFrame(self, "What is the meaning of life", ["1", "2"])
        self.radiobutton_frame.grid(row=3, column=1, padx=(10, 10), pady=(10, 10), sticky="nswe")

        # Lambda function used here to allow for arguments into function
        self.button = customtkinter.CTkButton(self, text="Print L column", command=lambda: self.button_pressed(self.checkbox_frame))
        self.button.grid(row=1, column=0, padx=(10,10), pady=(10,10), sticky="nwe")

        self.button1 = customtkinter.CTkButton(self, text="Print R column", command=lambda: self.button_pressed(self.checkbox_frame1))
        self.button1.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="nwe")

        self.button2 = customtkinter.CTkButton(self, text="Print B columns",command=self.print_all)
        self.button2.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="nwe", columnspan=2)

        self.button3 = customtkinter.CTkButton(self, text="Print Radio L column", command=self.print_radio_val)
        self.button3.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="nw")

    def button_pressed(self, frame):
        print(frame.get_checkboxes())

    def print_all(self):
        print(self.checkbox_frame.get_checkboxes())
        print(self.checkbox_frame1.get_checkboxes())

    def print_radio_val(self):
        print(self.radiobutton_frame.get_radio_val())

app = App("My Little Pony") # Creating app object
app.mainloop() # Needed to actually display the app.