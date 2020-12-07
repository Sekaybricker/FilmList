from Model.series import Series
from View.serie_view import SerieView
import pickle

series = {}
arq_series = open('series.pkl', 'wb')

def metodo_dump():
  pickle.dump(series, arq_series)
  
def metodo_load():
  pickle.load(series,arq_series)
