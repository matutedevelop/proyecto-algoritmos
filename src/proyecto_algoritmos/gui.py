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
        self.mebu_background_image = PhotoImage(file=relative_to_assets("fondo.png"))
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
            command=lambda: self.controller.show_screen("clients"),
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
            command=lambda: self.controller.show_screen("finance"),
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
        self.controller = controller
        
        # Configure frame grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        self.init_screen()

    
    def init_screen(self):
        self.canvas = Canvas(
        self,
        bg = "#FFFFFF",
        height = 627,
        width = 1003,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
            )

        self.canvas.place(x = 0, y = 0)
        self.finance_background_image = PhotoImage(
            file=relative_to_assets("fondo.png"))
        image_1 = self.canvas.create_image(
            515.0001220703125,
            314.0,
            image=self.finance_background_image
        )

        self.canvas.create_text(
            63.0,
            71.0,
            anchor="nw",
            text="Datos y finanzas",
            fill="#000000",
            font=("JetBrainsMono Regular", 48 * -1)
        )

        self.finance_button_image_1 = PhotoImage(
            file=relative_to_assets("finance_button_1.png"))
        self.button_1 = Button(
            self,
            image=self.finance_button_image_1,
            borderwidth=0,
            bg="#ffffff",
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=144.0,
            y=313.0,
            width=271.395263671875,
            height=80.97615051269531
        )

        self.finance_button_image_2 = PhotoImage(
            file=relative_to_assets("finance_button_2.png"))
        self.button_2 = Button(
            self,
            image=self.finance_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            bg="#ffffff",
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=144.0,
            y=213.0,
            width=271.395263671875,
            height=80.97615051269531
        )

        self.finance_button_image_3 = PhotoImage(
            file=relative_to_assets("finance_button_3.png"))
        self.button_3 = Button(
            self,
            image=self.finance_button_image_3,
            command=lambda: print("button_3 clicked"),
            bg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_3.place(
            x=143.0,
            y=413.4884033203125,
            width=271.395263671875,
            height=80.97615051269531
        )

        self.canvas.create_rectangle(
            65.9984130859375,
            130.69003295898438,
            520.0010070800781,
            131.69003295898438,
            fill="#000000",
            outline="")

        self.finance_button_image_4 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        self.button_4 = Button(
            self,
            image=self.finance_button_image_4,
            command=lambda: print("button_4 clicked"),
            bg="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_4.place(
            x=29.0,
            y=27.0,
            width=38.0,
            height=32.0
        )


class clients(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        
        # Configure frame grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        self.init_screen()

    
    def init_screen(self):
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 627,
            width = 1012,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.background_image = PhotoImage(
            file=relative_to_assets("fondo.png"))
        image_1 = self.canvas.create_image(
            515.0001220703125,
            314.0,
            image=self.background_image
        )

        self.canvas.create_text(
            72.0,
            72.0,
            anchor="nw",
            text="Administrar Clientes",
            fill="#000000",
            font=("JetBrainsMono Regular", 48 * -1)
        )

        self.clients_button_image_1 = PhotoImage(
            file=relative_to_assets("clientes_button_1.png"))
        self.button_1 = Button(
            self,
            bg= "#ffffff",
            image=self.clients_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=123.0,
            y=368.0,
            width=271.395263671875,
            height=80.97615051269531
        )

        self.clientes_button_image_2 = PhotoImage(
            file=relative_to_assets("clientes_button_2.png"))
        self.button_2 = Button(
            self,
            bg= "#ffffff",
            image=self.clientes_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=123.0,
            y=268.0,
            width=271.395263671875,
            height=80.97615051269531
        )

        self.canvas.create_rectangle(
            74.9984130859375,
            131.69003295898438,
            529.0010070800781,
            132.69003295898438,
            fill="#000000",
            outline="")



# pa   ntallas secundarias / datos y finanzas 

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


