# Travelling salesman problem
Let `G` be an undirected connected graph. Find a quick path to visit all nodes. The algorithm must finish in
a given time.

## Input format
The `input` variable is a tuple `graph. Where `graph` is the graph successors
dictionary: `g[x][y] = distance between x and y`.

## Output format
You should return a list of the nodes visited during your traversal.


# [FR] Problème du voyageur de commerce
Soit `G` un graphe complet non orienté. Trouver un bon chemin (ie le plus court possible)
pour visiter tous les autres noeuds, en un temps donné.

## Données d'entrée
L'entrée est un couple `graph` où `graph` est un graphe non orienté complet sous
forme de dictionnaire de successeurs: `g[x][y] = distance entre x et y`.

## Données de sortie
Votre algorithme doit retourner le chemin du parcours: liste de
noeuds visités en partant et finissant au noeud `s`.
