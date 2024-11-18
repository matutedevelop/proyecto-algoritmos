"""Creo que este modulo no deberia de ser tan simple, quizas deberia de hacer un type checker y una funcion para escribir a cada tabla, 
asi queda hardcodeadeada la direccion y se hace mas segura la comunicacion"""

import pandas as pd
directions = pd.read_json(r'C:\Users\fofoy\OneDrive\clarovent\Base_de_datos\direcciones.json',typ='series').to_dict()

def csv_writer(dir,arr):
   df = pd.read_csv(dir)
   df.loc[len(df)] = arr
   df.to_csv(dir,index=False)
   
def csv_deleter(dir,column,value):
   df = pd.read_csv(dir)
   df = df[df[column] != value]
   df = df.reset_index(drop=True)
   df.to_csv(dir, index=False)





csv_writer(directions['ruta_clientes'],['gonzalo'])
csv_deleter(directions['ruta_notas'],'id nota',1)
