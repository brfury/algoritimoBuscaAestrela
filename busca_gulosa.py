from cityMap import Grafo
from vetor_ordenado import VetorOrdenado 

class Gulosa:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
    print('----------------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado == True
          vetor_ordenado.insere(adjacente)
      vetor_ordenado.imprime()

      if not isinstance(vetor_ordenado.vetor[0], float):
        self.buscar(vetor_ordenado.vetor[0].vertice) 
    
grafo = Grafo()
busca_gulosa = Gulosa(grafo.curitiba)
busca_gulosa.buscar(grafo.paulo_frontin)