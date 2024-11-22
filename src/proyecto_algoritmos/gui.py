# gui.py

import tkinter as tk
from tkinter import ttk, Canvas, Button, PhotoImage,Entry
from pathlib import Path
from tkinter.ttk import  Treeview, Combobox,Checkbutton
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
            command=lambda: bl.open_powerbi_inform(),
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
            command=lambda: self.controller.reset_app(),
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

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("cli_button_ver_clientes.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
            bg="#FFFFFF"
        )
        self.button_1.place(
            x=143.0,
            y=328.0,
            width=271.395263671875,
            height=80.97615051269531
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("cli_button_add_abono.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat",
            bg="#FFFFFF"
        )
        self.button_2.place(
            x=143.0,
            y=428.0,
            width=271.395263671875,
            height=80.97615051269531
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("cli_button_create.png"))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat",
            bg="#FFFFFF"
        )
        self.button_3.place(
            x=143.0,
            y=228.0,
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

            
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        self.button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.reset_app(),
            relief="flat",
            bg="#FFFFFF"
        )
        self.button_4.place(
            x=38.0,
            y=38.0,
            width=38.0,
            height=32.0
        )



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

        ''' Logic for treeview  and variables'''

        # Declaration
        self.qty = tk.IntVar()
        self.glass_type = tk.StringVar()
        self.width = tk.DoubleVar()
        self.length = tk.DoubleVar()
        self.includes_glass = tk.BooleanVar()
        self.num_drills = tk.IntVar()
        self.drills_type = tk.StringVar()
        self.is_sandblasted = tk.BooleanVar()
        self.aditional_fee = tk.DoubleVar()
        self.is_canteado = tk.BooleanVar()

        # Set variables

        self.qty.set(0)
        self.glass_type.set("lun 3")
        self.width.set(1)
        self.length.set(1)
        self.includes_glass.set(True)
        self.num_drills.set(0)
        self.drills_type.set("barreno 19")
        self.is_sandblasted.set(False)
        self.aditional_fee.set(0)
        self.is_canteado.set(False)

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
        image_image_1 = PhotoImage(
        file=relative_to_assets("fondo_clean.png"))
        image_1 = self.canvas.create_image(
            506.0,
            313.0,
            image=image_image_1
            )


        self.canvas.create_text(
            402.0015869140625,
            46.0,
            anchor="nw",
            text="Cotizar",
            fill="#000000",
            font=("JetBrainsMono Regular", 48 * -1)
            )

        self.canvas.create_rectangle(
            278.0,
            108.69003295898438,
            732.0025939941406,
            109.69003295898438,
            fill="#000000",
            outline="")

        self.entry_image_1 = PhotoImage(
        file=relative_to_assets("cot_entry.png"))
        entry_bg_1 = self.canvas.create_image(
            240.0,
            453.5,
            image=self.entry_image_1
            )
        self.combobox_glass_type = Combobox(
            self,
            values = bl.glass_type_names,
            textvariable=self.glass_type

        )
        self.combobox_glass_type.place(
            x=207.0,
            y=436.0,
            width=66.0,
            height=33.0
        )

        self.canvas.create_text(
        130.0,
        419.0,
        anchor="nw",
        text="Cantidad",
        fill="#000000",
        font=("JetBrains Mono", 12 * -1)
        )

        self.canvas.create_text(
            210.0,
            419.0,
            anchor="nw",
            text="Tipo",
            fill="#000000",
            font=("JetBrainsMono Regular", 12 * -1)
        )

        self.canvas.create_text(
            331.0,
            419.0,
            anchor="nw",
            text="Ancho",
            fill="#000000",
            font=("JetBrainsMono Regular", 12 * -1)
        )

        self.canvas.create_text(
            409.0,
            419.0,
            anchor="nw",
            text="Largo",
            fill="#000000",
            font=("JetBrainsMono Regular", 12 * -1)
        )

        self.canvas.create_text(
            484.0,
            419.0,
            anchor="nw",
            text="Vidrio",
            fill="#000000",
            font=("JetBrainsMono Regular", 12 * -1)
        )

        self.canvas.create_text(
            636.0,
            419.0,
            anchor="nw",
            text="Tipo Ø",
            fill="#000000",
            font=("JetBrainsMono Regular", 12 * -1)
        )

        self.canvas.create_text(
            715.0,
            419.0,
            anchor="nw",
            text="Arenado",
            fill="#000000",
            font=("JetBrainsMono Regular", 12 * -1)
        )

        self.canvas.create_text(
            786.0,
            419.0,
            anchor="nw",
            text="Adicional",
            fill="#000000",
            font=("JetBrainsMono Regular", 12 * -1)
        )
        self.canvas.create_text(
            875.0,
            419.0,
            anchor="nw",
            text="Canteado",
            fill="#000000",
            font=("JetBrainsMono Regular", 12 * -1)
        )

        self.canvas.create_text(
            562.0,
            419.0,
            anchor="nw",
            text="Num. Ø",
            fill="#000000",
            font=("JetBrainsMono Regular", 12 * -1)
        )

        # Treeview declaration
        columns = ["CANTIDAD","TIPO","ANCHO","LARGO","VIDRRIO","NUM. Ø","TIPO Ø","ARENADO","CANTEADO","ADICIONAL"]

        self.table = Treeview(
            self,
            columns=columns,
            selectmode= "browse",
            show="headings"

        )

        for c in columns:
            self.table.heading(c, text=c)
            self.table.column(c, width=0)
            self.table.column(c, stretch=True)


        self.table.place(
            x=100,
            y=150,
            width=800,
            height=250


        )


        self.table.bind("<BackSpace>",self.delete_selection)



        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("cot_entry.png"))
        entry_bg_2 = self.canvas.create_image(
            157.0,
            453.5,
            image=self.entry_image_2
        )
        self.quantity_entry = tk.Entry(
            self,
            textvariable = self.qty,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.quantity_entry.place(
            x=124.0,
            y=436.0,
            width=66.0,
            height=33.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("cot_entry.png"))
        entry_bg_3 = self.canvas.create_image(
            348.5,
            453.5,
            image=self.entry_image_3
        )
        self.width_entry = tk.Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.width
        )
        self.width_entry.place(
            x=315.0,
            y=436.0,
            width=67.0,
            height=33.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("cot_entry.png"))
        entry_bg_4 = self.canvas.create_image(
            427.5,
            453.5,
            image=self.entry_image_4
        )
        self.length_entry = tk.Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.length
        )
        self.length_entry.place(
            x=394.0,
            y=436.0,
            width=67.0,
            height=33.0
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("cot_entry.png"))
        entry_bg_5 = self.canvas.create_image(
            506.0,
            453.5,
            image=self.entry_image_5
        )
        self.includes_glass_checkbtn = Checkbutton(
            self,
            variable=self.includes_glass
        )
        self.includes_glass_checkbtn.place(
            x=495.0,
            y=442.0,
            width=20.0,
            height=25.0
        )

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("cot_entry.png"))
        entry_bg_6 = self.canvas.create_image(
            584.0,
            453.5,
            image=self.entry_image_6
        )
        self.drill_num_entry = tk.Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.num_drills
        )
        self.drill_num_entry.place(
            x=551.0,
            y=436.0,
            width=66.0,
            height=33.0
        )

        self.entry_image_7 = PhotoImage(
            file=relative_to_assets("cot_entry.png"))
        entry_bg_7 = self.canvas.create_image(
            662.0,
            453.5,
            image=self.entry_image_7
        )
        self.drill_type_combobox = Combobox(
            self,
            values = bl.drill_types,
            textvariable= self.drills_type
        )
        self.drill_type_combobox.place(
            x=622.0,
            y=436.0,
            width=79,
            height=33
        )

        self.entry_image_8 = PhotoImage(
            file=relative_to_assets("cot_entry.png"))
        entry_bg_8 = self.canvas.create_image(
            741.0,
            453.5,
            image=self.entry_image_8
        )
        self.sandblasted_checkbox = Checkbutton(self,variable=self.is_sandblasted)
        self.sandblasted_checkbox.place(
            x=730.0,
            y=442.0,
            width=20.0,
            height=25.0
        )

        self.entry_image_9 = PhotoImage(
            file=relative_to_assets("cot_entry.png"))
        entry_bg_9 = self.canvas.create_image(
            820.0,
            453.5,
            image=self.entry_image_9
        )
        self.aditional_fee_entry = tk.Entry(

            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.aditional_fee
        )
        self.aditional_fee_entry.place(
            x=785.0,
            y=436.0,
            width=66.0,
            height=33.0
        )

        self.entry_image_10 = PhotoImage(
            file=relative_to_assets("cot_entry.png"))
        entry_bg_5 = self.canvas.create_image(
            900.0,
            453.5,
            image=self.entry_image_5
        )
        self.canteado_check_btn = Checkbutton(
            self,
            variable=self.is_canteado
        )
        self.canteado_check_btn.place(
            x=889.0,
            y=442.0,
            width=20.0,
            height=25.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("cot_button_1.png"))
        cot_btn_cotizar = Button(
            self,
            bg="#FFFFFF",
            fg="#000000",
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.append_to_list_switch_screen(),
            relief="flat"
        )
        cot_btn_cotizar.place(
            x=391.99998474121094,
            y=506.0,
            width=110.52107238769531,
            height=32.97615051269531
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("cot_button_2.png"))
        self.cot_button_add_to_table = Button(
            self,
            bg="#FFFFFF",
            fg="#000000",
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_to_table(),
            relief="flat"
        )
        self.cot_button_add_to_table.place(
            x=509.99998474121094,
            y=506.0,
            width=110.52107238769531,
            height=32.97615051269531
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        self.cot_button_back = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.reset_app(),
            relief="flat"
        )
        self.cot_button_back.place(
            x=38.0,
            y=28.0,
            width=38.0,
            height=32.0
        )


    def add_to_table(self):
        data = [self.qty.get(),self.glass_type.get(),
                self.width.get(),self.length.get(),
                self.includes_glass.get(),self.num_drills.get(),
                self.drills_type.get(),self.is_sandblasted.get(),
                self.is_canteado.get(),self.aditional_fee.get()]

        self.table.insert(parent='',index=tk.END,values=data)

    def delete_selection(self,_):
        selection = self.table.selection()

        self.table.delete(selection[0])


    def convert_to_orders(self):
        items = self.table.get_children()
        values = [self.table.item(i)['values'] for i in items ]
        
        # esta parte castea los valores a lo que deberian de ser, 
        # pues en las tablas de tkinter todo es texto
        for v in values:
            v[0] = int(v[0])
            v[2] = float(v[2])
            v[3] = float(v[3])
            v[4] = bool(v[4])
            v[5] = int(v[5])
            v[7] = bool(v[7])
            v[8] = bool(v[8])
            v[9] = float(v[9])


        try:
            pass
            return [bl.Pedido(*v) for v in values]

        except:
             raise ValueError("error al convertir a pedido")



    def append_to_list_switch_screen(self):
        orders = self.convert_to_orders()
        for o in orders:
            bl.orders_list.append(o)

        # Convertir  pedidos a nota
        bl.current_note = bl.note(bl.orders_list)
        bl.current_note.get_resume()

        self.controller.frames["note_summary"].add_total_text()
        self.controller.frames["note_summary"].add_to_table()
        self.controller.show_screen("note_summary")


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
        
        
class note_summary(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.id = tk.IntVar()
        self.id.set(0)
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
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("fondo_clean.png"))
        image_1 = self.canvas.create_image(
            506.0,
            313.0,
            image=self.image_image_1
        )
        
        self.image_image_2 = PhotoImage(
            file=relative_to_assets("logo.png"))
        image_2 = self.canvas.create_image(
            875.0,
            84.0,
            image=self.image_image_2
        )
        
        self.canvas.create_text(
            272.0,
            46.0,
            anchor="nw",
            text="Confirmar pedido",
            fill="#000000",
            font=("JetBrainsMono Regular", 48 * -1)
        )
        
        self.canvas.create_rectangle(
            278.0,
            108.69003295898438,
            732.0025939941406,
            109.69003295898438,
            fill="#000000",
            outline="")
        
        self.canvas.create_text(
            751.0,
            158.0,
            anchor="nw",
            text="ID",
            fill="#000000",
            font=("JetBrainsMono Regular", 12 * -1)
        )
        # crear treeview

        columns = ["CANTIDAD", "Descripcion","P. UNITARIO", "IMPORTE"]
        self.table = Treeview(
                self,
                columns=columns,
                selectmode= "browse",
                show="headings"

                )

        for c in columns:
            self.table.heading(c, text=c)
            self.table.column(c, width=0)
            self.table.column(c, stretch=True)

            self.table.place(

            x=100,
            y=170,
            width=400,
            height=300


            )

        



        
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("cot_entry.png"))
        entry_bg_1 = self.canvas.create_image(
            786.5,
            191.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=753.0,
            y=174.0,
            width=67.0,
            height=33.0
        )
        
        self.canvas.create_text(
            751.0,
            218.0,
            anchor="nw",
            text="Cliente",
            fill="#000000",
            font=("JetBrainsMono Regular", 12 * -1)
        )
        
        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("cot_entry.png"))
        entry_bg_2 = self.canvas.create_image(
            795.5,
            251.5,
            image=self.entry_image_2
        )
        self.entry_2 = Combobox(
            self,
            values= bl.clients
        )
        self.entry_2.place(
            x=753.0,
            y=236.0,
            width=85.0,
            height=33.0
        )
        
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("conf_confirmar.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
            bg="#FFFFFF"
        )
        self.button_1.place(
            x=696.9999847412109,
            y=382.0,
            width=198.65003967285156,
            height=59.02384948730469
        )
        
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat",
            bg="#FFFFFF"
        )
        self.button_2.place(
            x=38.0,
            y=28.0,
            width=38.0,
            height=32.0
        )
        
        self.canvas.create_rectangle(
            76.0,
            159.0,
            92.0,
            504.0,
            fill="#D9D9D9",
            outline="")
        
        self.canvas.create_rectangle(
            712.0,
            335.0,
            892.0,
            338.0,
            fill="#FF0909",
            outline="")
        
        
        

    def add_total_text(self):
        total = bl.current_note.note_total
        self.canvas.create_text(
            712.0,
            309.0,
            anchor="nw",
            text=f"Total:$ {total}",
            fill="#FF0909",
            font=("JetBrainsMono Regular", 24 * -1)
        )



    def add_to_table(self):
       orders = bl.orders_list
       for o in orders:
            
            data = [o.quantity,o.description,o.unit_price,o.total]
            self.table.insert(parent='',index = tk.END,values=data)


