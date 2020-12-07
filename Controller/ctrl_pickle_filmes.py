import pickle

filmes = {}
arq_filmes = open('filmes.pkl', 'wb')

def metodo_dump():
  pickle.dump(filmes, arq_filmes)
  
def metodo_load():
  pickle.load(filmes,arq_filmes)
