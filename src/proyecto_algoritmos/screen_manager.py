import tkinter as tk
from tkinter import ttk 
import gui
from gui import menu, finance, clients_prices, view_delete_client, client_management


class manager(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().self()
        container = ttk.Frame(self).pack(
            expand=True,
            fill = 'both',
            side = 'top',
            padx = 10,
            pady = 10,
            anchor = 'center'
            )
        

        #creamos un diccionario que contenga todas las pantallas
        self.screens = {}

        for ScreenClass in (gui.client_management,gui.clientes_precios,gui.clients_prices):
            screen = ScreenClass(container, self)
            self.screens[ScreenClass] = screen
            screen.grid(row=0,column=0,sticky=tk.NSEW)
            self.show_screen(menu)
    def show_screen(self,screen):
        if screen in self.screens:
            s = self.screens[screen]
            s.tkraise()

        


