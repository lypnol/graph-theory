# Realistic graph traversal
Let `G` be an undirected graph with multiple connected components. Produce a traversal path of what you can visit starting at a given node `s` without teleportation.

## Input format
The `input` variable is a tuple `graph, start`. Where `graph` is the graph successors dictionary and `start` is the starting node.

## Output format
You should return a list of the nodes visited during your traversal.


# [FR] Parcours réaliste d'un graphe non orienté
Soit `G` un graphe non orienté, avec plusieurs composantes connexes séparés. faites un parcours de la composante connexe de `G` à partir d'un noeud donné `s` sans se téléporter.

## Données d'entrée
L'entrée est un couple `graph, start` où `graph` est un graphe non orienté sous forme de dictionnaire de successeurs, et `start` est un noeud de `graph`.

## Données de sortie
Votre algorithme doit retourner un chemin de parcours: liste de noeuds visités en partant du noeud de départ.
