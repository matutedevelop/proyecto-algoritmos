import tkinter as tk
from tkinter import ttk 
from gui import *


class manager(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        container = ttk.Frame(self)
        #creamos un diccionario que contenga todas las pantallas
        self.title('clarovent accounting tool')
        self.geometry('1000x600')
        container.pack(
            expand=True,
            fill = 'both',
            side = 'top',
            padx = 10,
            pady = 10,
            anchor = 'center'
            )
        self.frames = {}
        screen_classes = [
            menu, finance,cotization_view,
            expense_input, delete_note,add_client, 
            add_abono,note_summary,clients
        ]

        
        for ScreenClass in screen_classes:
            screen = ScreenClass(container, self)
            screen.grid(row=0,column=0,sticky=tk.NSEW)
            self.frames[ScreenClass.__name__] = screen
        

        
        self.show_screen('menu')
        

    def show_screen(self,screen):
        if screen in self.frames.keys():
            s = self.frames[screen]
            s.tkraise()
        else: raise ValueError('no se puede encontrar la pantalla especificada')

    def reset_app(self):
        bl.orders_list.clear()
        bl.current_note = None
        self.show_screen('menu')
