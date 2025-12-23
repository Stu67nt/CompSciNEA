import customtkinter

from widgets import *

class App(customtkinter.CTk): # Inheriting CTk class
    def __init__(self, title: str="My App"):
        super().__init__() # Calls parent class

        # Initialising Window
        self.title(title)
        self.grid_rowconfigure((0,4), weight=1)
        self.grid_columnconfigure((0,1), weight=1)
        customtkinter.set_appearance_mode("dark") # light/dark/system (system is not functional on linux)

        SEARCH_MODES = ["Keyword", "Direct"]
        self.search_select_frame = RadioButtonFrame(self, title = "Select Search Mode:", values = SEARCH_MODES,
                                                    is_horizontal = True, title_sticky= "nsw")
        self.search_select_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nwe")

        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nwe")

        self.frame = CheckboxFrame(self, title = "Test", values = ["1", "2", "3"], is_scrollable = False )
        self.frame.grid(row=2, column=0, padx=10, pady=(10,10), sticky="swe")



app = App("Balls") # Creating app object
app.mainloop() # Needed to actually display the app.