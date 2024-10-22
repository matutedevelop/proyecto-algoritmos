import tkinter as tk
from tkinter import ttk

app = tk.Tk()

app.geometry("800x600")

# Screen inicio







# ventana_1.mainloop

# btn1 = tk.Button(text="cotizar / crear pedido",command=ventana_1)
# btn2 = tk.Button(text="Datos y Finanzas",command=ventana_1)
# btn3 = tk.Button(text="clientes y precios",command=ventana_1)

selected = tk.BooleanVar()
check_button = tk.Checkbutton(app,text="test",variable=selected,command=lambda:print(selected.get()))

check_button.pack()
# btn1.pack()
# btn2.pack()
# btn3.pack()


# main screens

class menu(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)



    def init_screen(self):
        pass


class finance(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)

    
    def init_screen(self):
        pass


class clients_prices(ttk.Frame):
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
    
    def init_screen(self):
        pass

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


class client_management(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
    def init_screen(self):
        pass

class price_modifier(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
    def init_screen(self):
        pass



class cliente_creator(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
    def init_screen(self):
        pass

class view_delete_client(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
    
    def init_screen(self):
        pass









app.mainloop()