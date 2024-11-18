
import time
import webbrowser as wb
import json




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


# really important variables <><> <><> <><> <><> <><> <><> <><> <><> <><> <><> <><> <><> <><> <><>

orders_list = []
current_note = None


# common tools

def get_glass_price(glass_type):

    try:
        price = glass_prices[glass_type]
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
        raise ValueError("proceso no encontrado")




def get_date():
    date = time.ctime(time.time())[:]
    return date[4:7] + date[-5:]


def open_powerbi_inform():
    link = "https://app.powerbi.com/view?r=eyJrIjoiYTY0ZDc3MTktMWFlZC00NjY1LTkzZGMtODllZjk0NjE4NDkzIiwidCI6IjZmMDM0OGYyLWU0OTgtNDVjOS04NGY0LWM2ZDgxZGNmZmRmZSIsImMiOjR9"
    wb.open(link)

# classes

class Pedido:

    def __init__(self,
                 # id_note: int,
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
        self.dimensions = str(length) + 'x' + str(width)
        self.m2 = length * width
        self.ml = 2 * length + 2 * width
        self.includes_glass = includes_glass
        self.barrenos = barrenos
        self.barrenos_type = barrenos_type
        self.sandblasted = sandblasted
        self.canteado = canteado
        self.extra = extra



    def calculate_price(self):

        total = 0
        if self.includes_glass == True: total += self.m2 * get_glass_price(self.glass_type)
        if self.sandblasted == True: total += self.m2 * get_process_price(self.glass_type,"arenado")
        if self.canteado == True: total += self.ml * get_process_price(self.glass_type,"canteado")
        total += self.barrenos * get_process_price(self.glass_type,self.barrenos_type)
        total += self.extra
        total *= self.quantity

        self.total = total





    def pack(self) -> list:
        return []






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
      resume = []
      # build up the description of the pedido , aka product (see resumen cotizacion on the mock up)
      for product in self.products:
          description = product.glass_type + product.dimensions
          if product.sandblasted: description += ' ,arenado'
          if product.canteado: description += ' ,canteado'
          if product.barrenos > 0:  description += ',' + str(product.barrenos) + 'barrenos'
          if not product.includes_glass: description += ', (maq)'
          # calculate unitary price of product
          # Creo que el problema es que estoy llamando self.total y self.quantity en vez de product.total y product.quantity    
          unit_price = product.total / product.quantity

          resume.append((product.quantity,description,unit_price,self.note_total))

      return (resume,self.note_total)

   def pack(Self) -> list :
        return [Self.date,Self.id,Self.client,Self.note_total,Self.type]




