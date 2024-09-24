import tkinter as tk


app = tk.Tk()

app.geometry("800x600")

# Screen inicio

def main_screen():

    ventana_1 = tk.Tk()
    label = tk.Label(master=ventana_1,text="eduardo se la come")
    label.pack()

    ventana_1.mainloop

# btn1 = tk.Button(text="cotizar / crear pedido",command=ventana_1)
# btn2 = tk.Button(text="Datos y Finanzas",command=ventana_1)
# btn3 = tk.Button(text="clientes y precios",command=ventana_1)

selected = tk.BooleanVar()
check_button = tk.Checkbutton(app,text="test",variable=selected,command=lambda:print(selected.get()))

check_button.pack()
# btn1.pack()
# btn2.pack()
# btn3.pack()





app.mainloop()