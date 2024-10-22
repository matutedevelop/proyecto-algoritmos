"""Creo que este modulo no deberia de ser tan simple, quizas deberia de hacer un type checker y una funcion para escribir a cada tabla, 
asi queda hardcodeadeada la direccion y se hace mas segura la comunicacion"""




import pandas as pd

def csv_writer(arr,dir):
   df = pd.read_csv(dir)
   df.loc[len(df)] = arr
   df.to_csv(dir,index=False)
   

directions = pd.read_json(r'C:\Users\fofoy\OneDrive\clarovent\Base_de_datos\direcciones.json',typ='series').to_dict()


csv_writer(["eduardo"],directions['ruta_clientes'])

