
import time
import webbrowser as wb
import json
import pandas as pd




with open(r'C:\Users\fofoy\OneDrive\clarovent\Base_de_datos\direcciones.json', 'r') as f:
    directions = json.load(f)


with open(directions["ruta_precios"], 'r') as f:
    price_table = json.load(f)


# Common variables

process_prices = price_table["proceso"]
process_names = list(process_prices.keys())

glass_prices = price_table["vidrio"]
glass_type_names = list(glass_prices.keys())

drill_types = ["barreno 19","barreno 37"]

pay_forms = ["efe","efe/maq","transf"]


clients = pd.read_csv(directions["ruta_clientes"])
clients = list(clients["cliente"].values)





# really important variables <><> <><> <><> <><> <><> <><> <><> <><> <><> <><> <><> <><> <><> <><>

orders_list = []
current_note = None


# common tools

def get_glass_price(glass_type):

    try:
        price = glass_prices[glass_type]
        return price
    except:
        raise ValueError("tipo de vidrio desconocido")


def get_process_price(glass_type,process):
    if process == "arenado": return process_prices[process]
    elif process == "barreno 19": return process_prices[process]
    elif process == "barreno 37": return process_prices[process]
    elif process == "canto":
        density = glass_type[-1]
        return process_prices[process][density] 
    else:
        raise ValueError(f"proceso no encontrado {glass_type},{process}")




def get_date():
    current_time = time.localtime()
    # Formatear la fecha en formato corto (DD/MM/AAAA)
    short_date = time.strftime("%d/%m/%Y", current_time)
    return short_date

def open_powerbi_inform():
    link = "https://app.powerbi.com/view?r=eyJrIjoiYTY0ZDc3MTktMWFlZC00NjY1LTkzZGMtODllZjk0NjE4NDkzIiwidCI6IjZmMDM0OGYyLWU0OTgtNDVjOS04NGY0LWM2ZDgxZGNmZmRmZSIsImMiOjR9"
    wb.open(link)

# classes

class Pedido:

    def __init__(self,
                 
                 quantity: int,
                 glass_type: str,
                 length: float,
                 width: float,
                 includes_glass: bool,
                 barrenos: int,
                 barrenos_type: str,
                 sandblasted: bool,
                 canteado: bool,
                 extra: float) -> None:
        self.id_note ='XXXXXX'
        self.quantity = quantity
        self.glass_type = glass_type
        self.dimensions = str(length) + 'm x' + str(width) +'m'
        self.m2 = length * width
        self.ml = 2 * length + 2 * width
        self.includes_glass = includes_glass
        self.barrenos = barrenos
        self.barrenos_type = barrenos_type
        self.sandblasted = sandblasted
        self.canteado = canteado
        self.extra = extra
        
    def __str__(self):
        return f"Pedido(id_note={self.id_note}, quantity={self.quantity}, glass_type={self.glass_type}, dimensions={self.dimensions},  "
        


    def calculate_price(self):
 
        total = 0
        if self.includes_glass: total += self.m2 * get_glass_price(self.glass_type)
        if self.sandblasted: total += self.m2 * get_process_price(self.glass_type,"arenado")
        if self.canteado: total += self.ml * get_process_price(self.glass_type,"canto")
        total += self.barrenos * get_process_price(self.glass_type,self.barrenos_type)
        total += self.extra
        total *= self.quantity

        self.total = total








    def pack(self) -> list:
        return [self.id_note.get(),self.quantity,self.glass_type,self.dimensions,self.m2,self.ml,self.includes_glass,self.barrenos,self.barrenos_type,self.sandblasted,self.canteado,self.extra,self.total]






class note :
   def __init__(self,products = []):
       if len(products) == 0:
           raise ValueError("No se puede crear una lista sin pedidos")
       
       if not all(isinstance(product,Pedido) for product in products):
            raise ValueError("Todos los elementos de la lista deben ser de tipo producto")

       else: 
        self.date = get_date()
        self.id = 'XXXXXX'
        self.client = 'client'
        self.type = 'efe'
        self.products = products
    # calcular el total de la lista
        note_total = 0
        for product in products:
            product.calculate_price()
            note_total += product.total


        self.note_total = note_total




   def get_resume(self) -> tuple :
      # build up the description of the pedido , aka product (see resumen cotizacion on the mock up)
      for product in self.products:
          description = product.glass_type + ' ' + product.dimensions
          if product.sandblasted: description += ' ,arenado'
          if product.canteado: description += ' ,canteado'
          if product.barrenos > 0:  description += ',' + str(product.barrenos) + ' barrenos'
          if not product.includes_glass: description += ', (maq)'

          product.description = description
          
          # calculate unitary price of product
          # Creo que el problema es que estoy llamando self.total y self.quantity en vez de product.total y product.quantity    
          if product.quantity != 0:
            product.unit_price = product.total / product.quantity
            
          else:
            raise ValueError("la cantidad no puede ser cero")
          


      

      

   def pack(Self) -> list :
        return [Self.date,Self.id.get(),Self.client.get(),Self.note_total,Self.type]




