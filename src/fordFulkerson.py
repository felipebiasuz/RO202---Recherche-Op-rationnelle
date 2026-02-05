import numpy as np
import graph
import sys

def main():

    # Le poids des arcs de ce graphe correspondent aux capacités
    g = example()

    # Le poids des arcs de ce graphe correspondent au flot
    flow = fordFulkerson(g, "s", "t")

    print(flow)
    
# Fonction créant un graphe sur lequel sera appliqué l'algorithme de Ford-Fulkerson
def example():
        
    g = graph.Graph(np.array(["s", "a", "b", "c", "d", "e", "t"]))

    g.addArc("s", "a", 8)
    g.addArc("s", "c", 4)
    g.addArc("s", "e", 6)
    g.addArc("a", "b", 10)
    g.addArc("a", "d", 4)
    g.addArc("b", "t", 8)
    g.addArc("c", "b", 2)
    g.addArc("c", "d", 1)
    g.addArc("d", "t", 6)
    g.addArc("e", "b", 4)
    g.addArc("e", "t", 2)
    
    return g

# Fonction appliquant l'algorithme de Ford-Fulkerson à un graphe
# Les noms des sommets sources est puits sont fournis en entrée
def fordFulkerson(g, sName, tName):

    """
    Marquage des sommets du graphe:
     - mark[i] est égal à +j si le sommet d'indice i peut être atteint en augmentant le flot sur l'arc ji
     - mark[i] est égal à  -j si le sommet d'indice i peut être atteint en diminuant le flot de l'arc ji
     - mark[i] est égal à sys.float_info.max si le sommet n'est pas marqué
    """
    mark = [0] * g.n
    
    # Récupérer l'indice de la source et du puits
    s = g.indexOf(sName)
    t = g.indexOf(tName)
    
    # Créer un nouveau graphe contenant les même sommets que g
    flow = graph.Graph(g.nodes)

    # Récupérer tous les arcs du graphe 
    arcs = g.getArcs()

    sommet_actuel = s

    poi_du_chemin = 
    while (marque == True & destination != t):
        mark = [0] * g.n
        marque = False
        destinations = flow.adjacency[sommet_actuel]
        for destination in destinations:
            if flow.adjacency[sommet_actuel][destination] < g.adjacency[sommet_actuel, destination]:
                mark[destination] = sommet_actuel
                marque = True
                poi_du_chemin = min()
                sommet_actuel = destination
                break
        if (not(marque)):
            for destination in destinations:
                if (flow.adjacency[sommet_actuel][destination] > g.adjacency[sommet_actuel, destination]):
                    mark[destination] = (-1)*sommet_actuel
                    marque = True
                    sommet_actuel = destination
                    break
        if (destination == t):
            for i,j in enumerate(mark):
                flow.adjacency[i,abs(j)] += 
    
    return flow
   
if __name__ == '__main__':
    main()
