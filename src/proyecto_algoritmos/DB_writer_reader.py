
import pandas as pd

def csv_writer(arr,dir):

   df = pd.read_csv(dir)
   

   df.loc[len(df)] = arr

   # print(df)
   df.to_csv(directions['ruta_pedidos'],index=False)
   

directions = pd.read_json(r'C:\Users\fofoy\OneDrive\clarovent\Base_de_datos\direcciones.json',typ='series').to_dict()



csv_writer([1,1,1,'eduardo se la come'],directions['ruta_pedidos'])
