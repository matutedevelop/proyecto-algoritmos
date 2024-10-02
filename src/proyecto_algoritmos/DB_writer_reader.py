
import pandas as pd

def csv_writer(arr,dir):
   df = pd.read_csv(dir)
   df.loc[len(df)] = arr
   df.to_csv(dir,index=False)
   

directions = pd.read_json(r'C:\Users\fofoy\OneDrive\clarovent\Base_de_datos\direcciones.json',typ='series').to_dict()


csv_writer(["eduardo"],directions['ruta_clientes'])

