# gui.py

import tkinter as tk
from tkinter import ttk, Canvas, Button, PhotoImage
from pathlib import Path
import business_logic as bl


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

def relative_to_assets( path: str) -> Path:
    return ASSETS_PATH / Path(path)


class menu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Configure frame grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        self.init_screen()

        
    def init_screen(self):
                # Canvas setup
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=627,
            width=1003,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Background image
        self.mebu_background_image = PhotoImage(file=relative_to_assets("menu_fondo.png"))
        self.canvas.create_image(
            502.80448150634766,
            313.98328971862793,
            image=self.mebu_background_image
        )

        # Button 1
        self.menu_clientes_button_image = PhotoImage(file=relative_to_assets("menu_button_1.png"))
        self.menu_button_clientes = Button(
            self.canvas,
            image=self.menu_clientes_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_screen("finance"),
            relief="flat",
            bg="#FFFFFF"
        )
        self.menu_button_clientes.place(
            x=154.9451904296875,
            y=403.9252014160156,
            width=218.34243774414062,
            height=89.51094055175781
        )

        # Button 2 
        self.menu_button_datos_image = PhotoImage(file=relative_to_assets("menu_button_2.png"))
        self.menu_button_datos = Button(
            self.canvas,
            image=self.menu_button_datos_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: bl.open_powerbi_inform(),
            relief="flat",
            bg="#FFFFFF"
        )
        self.menu_button_datos.place(
            x=154.0949249267578,
            y=276.8608703613281,
            width=218.34243774414062,
            height=89.51094055175781
        )

        # Button 3

        self.menu_button_cotizar_image = PhotoImage(
        file=relative_to_assets("menu_button_3.png"))
        self.menu_button_cotizar = Button(
            self.canvas,
            image=self.menu_button_cotizar_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_screen('cotization_view'),
            relief="flat",
            bg="#FFFFFF"
        )
        self.menu_button_cotizar.place(
            x=160.0949249267578,
            y=150.22360229492188,
            width=218.34243774414062,
            height=89.51094055175781
        )

        # Decorative rectangles
        self.canvas.create_rectangle(
            15.0,
            70.0000000049245,
            606.0000000757296,
            72.0,
            fill="#D8D8D9",
            outline=""
        )



class finance(ttk.Frame): 
    def __init__(self,parent,controller):
        super().__init__(parent)

    
    def init_screen(self):
        pass


class clients(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
    def init_screen(self):
        pass

# pantallas secundarias / datos y finanzas 

class summary_panel(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
    def init_screen(self):
        pass


class cotization_view(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        # Configure frame grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        self.init_screen()
    
    def init_screen(self):
        bt1 = ttk.Button(self,text='abjhdbjhsa')
        bt1.pack()

class expense_input(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
    def init_screen(self):
        pass


class delete_note(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
    def init_screen(self):
        pass

# pantallas secundarias administrar clientes y precios 


class view_delete_client(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
    def init_screen(self):
        pass

class create_order(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
    def init_screen(self):
        pass

class query_for_note(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
    def init_screen(self):
        pass


