import pandas as pd
import time
import webbrowser as wb


# common tools

directions = pd.read_json(r'C:\Users\fofoy\OneDrive\clarovent\Base_de_datos\direcciones.json',typ='series').to_dict()
price_table = pd.read_json(directions["ruta_precios"]).to_dict()

process_prices = price_table["proceso"]
glass_prices = price_table["vidrio"]



def get_date():
    return time.ctime(time.time())[:10]

def open_powerbi_inform():
    wb.open('https://app.powerbi.com/view?r=eyJrIjoiNWEwMjkxY2MtM2Q2Ny00MGI5LTk0YWUtN2VkZTA5MTVmYTg2IiwidCI6IjZmMDM0OGYyLWU0OTgtNDVjOS04NGY0LWM2ZDgxZGNmZmRmZSIsImMiOjR9')

# classes

class Pedido:

    def __init__(self,
                 id_note: int,
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
        self.id_note = id_note
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

# Tipo de vidrio es un string que se nos da por una combo box, y debe ser igual a los del json

    def calculate_price(self):

        total = 0
        if self.includes_glass == True: total += self.m2 * glass_prices[self.glass_type]
        if self.sandblasted == True: total += self.m2 * process_prices["arenado"]
        if self.canteado == True: total += self.ml * process_prices["canto"][self.glass_type[-1]]
        total += self.barrenos * process_prices[self.barrenos_type]
        total += self.extra
        total *= self.quantity

        self.total = total





    def pack(self) -> list:
        return []






class note :
   def __init__(self, id:int, client:str, products = [], typ="efectivo"  ) -> None:
       
       if len(products) == 0:
           raise ValueError("No se puede crear una lista sin pedidos")
       
       if not all(isinstance(product,Pedido) for product in products):
            raise ValueError("Todos los elementos de la lista deben ser de tipo producto")

       else: 
        self.date = get_date()
        self.id = id
        self.client = client
        self.type = typ
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


