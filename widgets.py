import customtkinter
from customtkinter import CTkFrame

"""
TODO: Allow for fg_colour and corner radius to be scaled 
"""

class CheckboxFrame(customtkinter.CTkFrame):  # Inheriting CTkFrame class
    def __init__(self, master, title: str, values: list, is_horizontal: bool = False, is_scrollable: bool = False):
        super().__init__(master) # Calls/runs parent class. This is necessary so it initialises the inherited class.

        if is_scrollable:
            self.container = customtkinter.CTkScrollableFrame(self)
        else:
            self.container = customtkinter.CTkFrame(self)

        # This line below is there so the frame scales to take up the free space
        self.container.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.values = values
        self.checkboxes = []
        self.title = title

        # Creating and positioning title in frame
        self.title = customtkinter.CTkLabel(self.container, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new")

        # Iterating through each item in values and creating a checkbox for it.
        # Each checkbox is then added to a list of checkboxes so we can track their state.
        for i, value in enumerate(self.values):
            self.checkbox = customtkinter.CTkCheckBox(self.container, text=value)
            if is_horizontal:
                self.checkbox.grid(row=0, column=i+1, padx=20, pady=20, sticky="w")
            else:
                self.checkbox.grid(row=i + 1, column=0, padx=20, pady=20, sticky="w")
            self.checkboxes.append(self.checkbox)

    # Returning which checkboxes have been ticked.
    def get_checkboxes(self):
        checked = []
        for box in self.checkboxes:
            if box.get() == 1:
                checked.append(box.cget("text"))
        return checked


class RadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title: str, values: list, is_horizontal: bool = False, is_scrollable: bool = False,
                 title_sticky: str = "nesw", title_fg_color: str = "gray30", title_corner_radius:int = 6,
                 button_sticky: str = "nesw"):
        super().__init__(master)  # Initilising parent class

        if is_scrollable:
            self.container = customtkinter.CTkScrollableFrame(self)
        else:
            self.container = customtkinter.CTkFrame(self)

        self.container.grid(row=0, column=0, sticky="new")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Initialising vars
        self.values = values
        self.title = title
        self.var = customtkinter.StringVar(value = "")

        # Creating title label
        self.title = customtkinter.CTkLabel(self.container, text=self.title, fg_color=title_fg_color,
                                            corner_radius=title_corner_radius)
        self.title.grid(row=0, column=0, sticky=title_sticky)

        # Iterating thorugh each value
        for i, value in enumerate(self.values):
            self.radio_button = customtkinter.CTkRadioButton(self.container, text=value, variable=self.var, value=value)
            if is_horizontal:
                self.radio_button.grid(row=0, column=i+1, padx=20, pady=20, sticky=button_sticky)
            else:
                self.radio_button.grid(row=i + 1, column=0, padx=20, pady=20, sticky=button_sticky)

    def get_radio_val(self):
        return self.var.get()