import tkinter as tk
from tkinter import ttk 
import gui
from gui import *


class manager(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        container = ttk.Frame(self)
        #creamos un diccionario que contenga todas las pantallas
        self.frames = {}
        screen_classes = [
            menu, finance, summary_panel, cotization_view,
            expense_input, delete_note,view_delete_client, 
            create_order,query_for_note,clients
        ]
        for ScreenClass in screen_classes:
            screen = ScreenClass(container, self)
            screen.grid(row=0,column=0,sticky=tk.NSEW)
            self.frames[ScreenClass] = screen
            self.show_screen(menu)

        
        self.title("clarovent accounting tool")
        self.geometry("1600x1000")
        container.pack(
            expand=True,
            fill = 'both',
            side = 'top',
            padx = 10,
            pady = 10,
            anchor = 'center'
            )
        self.show_screen(menu)
        



    def show_screen(self,screen):
        if screen in self.frames.keys():
            s = self.frames[screen]
            s.tkraise()
        else: raise ValueError("no se puede encontrar la pantalla especificada")

        


