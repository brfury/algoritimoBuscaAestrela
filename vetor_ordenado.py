
import cityMap as ct

class VetorOrdenado:
    def __init__(self, capacity):
        self.capacity = capacity
        self.vetor = self.creat_vetor()
        self.count = 0
        
    
    def creat_vetor(self):
        vetor = []
        for i in range(self.capacity):
            vetor.append(ct.Grafo.infinito.adjacentes[0])
        
        return vetor
   

    def insere(self, value):
        for i in range(self.capacity, 0, -1):
            
            if self.count == 0:
                self.vetor[-1] = value
                self.count += 1
                
            elif value.distancia_aestrela < self.vetor[i-1].distancia_aestrela:
                if self.vetor[i-1].distancia_aestrela == self.vetor[-1].distancia_aestrela:
                    self.vetor[i-1], self.vetor[i] = value, self.vetor[i-1]
                    
                    
                else: 
                    self.vetor[i], self.vetor[i-1] = self.vetor[i-1], value
        self.count = 0
                    
    def imprime(self):
        
        for i in range(len(self.vetor)):
            if self.vetor[i].vertice.rotulo == 'inf':
                pass
            else:
                print(f'''
                ---------------------------------------------
                {i} - {self.vetor[i].vertice.rotulo} 
                custo: {self.vetor[i].custo} 
                distancia reta: {self.vetor[i].vertice.distancia_objetivo}
                distancia A*: {self.vetor[i].distancia_aestrela}'''
                  )
            
    

