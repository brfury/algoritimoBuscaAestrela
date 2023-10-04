
class Vertice:
    def __init__(self, rotulo:str, distancia_objetivo:int) -> None:
        self.rotulo = rotulo
        self.distancia_objetivo = distancia_objetivo
        self.visitado = False
        self.adjacentes = []

    def adiciona_adjacente(self, adjacentes):
        self.adjacentes.append(adjacentes)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)


class Adjacente():
    def __init__(self, vertice, custo) -> None:
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + custo

class Grafo:
    
    infinito =  Vertice('inf', float('inf'))
    
    porto_uniao = Vertice('Porto União', 203 )
    paulo_frontin = Vertice('Paulo Frontin', 172 )
    canoinhas = Vertice('canoinhas', 141 )
    tres_barras = Vertice('Três Barras', 131 )
    sao_mateus = Vertice('São Mateus do Sul', 123 )
    irati = Vertice('Irati', 139 )
    curitiba = Vertice('Curitiba', 0 )
    palmeira = Vertice('Palmeira', 59 )
    mafra = Vertice('Mafra', 94 )
    campo_largo = Vertice('Campo Largo', 27 )
    balsa_nova = Vertice('Balsa Nova',41 )
    lapa = Vertice('Lapa', 74 )
    tijucas = Vertice('Tijucas do Sul', 56 )
    araucaria = Vertice('Araucária', 23 )
    sao_jose = Vertice('São José dos Pinhais', 13 )
    contenda = Vertice('contenda', 29 )
    
    infinito.adiciona_adjacente(Adjacente(infinito, float('inf')))
    
    porto_uniao.adiciona_adjacente(Adjacente(paulo_frontin, 46))
    porto_uniao.adiciona_adjacente(Adjacente(canoinhas, 78))
    porto_uniao.adiciona_adjacente(Adjacente(sao_mateus, 87))

    paulo_frontin.adiciona_adjacente(Adjacente(porto_uniao, 46))
    paulo_frontin.adiciona_adjacente(Adjacente(irati, 75))

    canoinhas.adiciona_adjacente(Adjacente(porto_uniao, 78))
    canoinhas.adiciona_adjacente(Adjacente(tres_barras, 12))
    canoinhas.adiciona_adjacente(Adjacente(mafra, 66))

    tres_barras.adiciona_adjacente(Adjacente(canoinhas, 12))
    tres_barras.adiciona_adjacente(Adjacente(sao_mateus, 43))

    sao_mateus.adiciona_adjacente(Adjacente(tres_barras, 43))
    sao_mateus.adiciona_adjacente(Adjacente(porto_uniao, 87))
    sao_mateus.adiciona_adjacente(Adjacente(irati, 57))
    sao_mateus.adiciona_adjacente(Adjacente(palmeira, 77))

    irati.adiciona_adjacente(Adjacente(paulo_frontin, 75))
    irati.adiciona_adjacente(Adjacente(palmeira, 75))
    irati.adiciona_adjacente(Adjacente(sao_mateus, 57))

    curitiba.adiciona_adjacente(Adjacente(campo_largo, 29))
    curitiba.adiciona_adjacente(Adjacente(balsa_nova, 51))
    curitiba.adiciona_adjacente(Adjacente(araucaria, 37))
    curitiba.adiciona_adjacente(Adjacente(sao_jose, 15))

    palmeira.adiciona_adjacente(Adjacente(irati, 75))
    palmeira.adiciona_adjacente(Adjacente(sao_mateus, 77))
    palmeira.adiciona_adjacente(Adjacente(campo_largo, 55))

    mafra.adiciona_adjacente(Adjacente(canoinhas, 78))
    mafra.adiciona_adjacente(Adjacente(lapa, 57))
    mafra.adiciona_adjacente(Adjacente(tijucas, 99))

    campo_largo.adiciona_adjacente(Adjacente(palmeira, 55))
    campo_largo.adiciona_adjacente(Adjacente(balsa_nova, 22))
    campo_largo.adiciona_adjacente(Adjacente(curitiba, 29))

    balsa_nova.adiciona_adjacente(Adjacente(campo_largo, 22))
    balsa_nova.adiciona_adjacente(Adjacente(contenda, 19))
    balsa_nova.adiciona_adjacente(Adjacente(curitiba, 51))

    lapa.adiciona_adjacente(Adjacente(contenda, 26))
    lapa.adiciona_adjacente(Adjacente(sao_mateus, 60))
    lapa.adiciona_adjacente(Adjacente(mafra, 57))

    tijucas.adiciona_adjacente(Adjacente(mafra, 99))
    tijucas.adiciona_adjacente(Adjacente(sao_jose, 49))

    araucaria.adiciona_adjacente(Adjacente(curitiba, 37))
    araucaria.adiciona_adjacente(Adjacente(contenda, 18))

    sao_jose.adiciona_adjacente(Adjacente(curitiba, 15))
    sao_jose.adiciona_adjacente(Adjacente(tijucas, 49))

    contenda.adiciona_adjacente(Adjacente(balsa_nova, 19))
    contenda.adiciona_adjacente(Adjacente(araucaria, 18))
    contenda.adiciona_adjacente(Adjacente(lapa, 26))

    