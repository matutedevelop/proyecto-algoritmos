import pandas as pd
import time
import csv

# common tools

directions = pd.read_json(r'C:\Users\fofoy\OneDrive\clarovent\Base_de_datos\direcciones.json',typ='series').to_dict()
price_table = pd.read_json(directions["ruta_precios"]).to_dict()

process_prices = price_table["proceso"]
glass_prices = price_table["vidirio"]



def get_date():
    return time.ctime(time.time())[:10]
# def calculate_price(price_table,):

# classes

class note :
   def __init__(self, id:int, client:str, amount=0 , typ="efectivo" ) -> None:
       self.date = get_date()
       self.id = id
       self.client = client
       self.amount = amount
       self.type = typ
   def pack(Self) -> list :
      
        return [Self.date,Self.id,Self.client,Self.amount,Self.type]


class Pedido:



    def __init__(self, id_nota: int, cantidad: int, tipo_de_vidrio: str, largo: float, ancho: float, vidrio: bool, barrenos: int, tipo_barrenos: str , arenado: bool, canteado: bool, extra: float) -> None:
        self.id_nota = id_nota
        self.cantidad = cantidad
        self.tipo_de_vidrio = tipo_de_vidrio
        self.dimensiones = str(largo) + 'x' + str(ancho)
        self.m2 = largo * ancho
        self.ml = 2 * largo + 2 * ancho
        self.vidrio = vidrio
        self.barrenos = barrenos
        self.tipo_barrenos = tipo_barrenos
        self.arenado = arenado
        self.canteado = canteado
        self.extra = extra

# Tipo de vidrio es un string que se nos da por una combo box, y debe ser igual a los del json

    def calculate_price(self):

        total = 0
        if self.vidrio == True: total += self.m2 * glass_prices[self.tipo_de_vidrio]
        if self.arenado == True: total += self.m2 * process_prices["arenado"]
        if self.canteado == True: total += self.ml * process_prices["canto"][self.tipo_de_vidrio[-1]]
        total += self.barrenos * process_prices[self.tipo_barrenos]
        total += self.extra
        total *= self.cantidad

        self.total = total





    def pack(self) -> list:
        return []
