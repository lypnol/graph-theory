# Travelling salesmann problem
Let `G` be an undirected connected graph. Given a starting node `s`, what is the shortest path to visit all other nodes and get back to `s`.

## Input format
The `input` variable is a tuple `graph, start`. Where `graph` is the graph successors dictionary: `g[x][y] = distance between x and y`. and `start` is the starting node.

## Output format
You should return a list of the nodes visited during your traversal starting end ending with `s`.


# [FR] Problème du voyageur de commerce
Soit `G` un graphe complet non orienté. En commençant par un noeud `s`, quel est le plus court chemin à prendre pour visiter tous les autres noeuds et revenir à `s`.

## Données d'entrée
L'entrée est un couple `graph, start` où `graph` est un graphe non orienté complet sous forme de dictionnaire de successeurs: `g[x][y] = distance entre x et y`, et `start` est un noeud de `graph`.

## Données de sortie
Votre algorithme doit retourner le chemin du parcours: liste de noeuds visités en partant et finissant au noeud `s`.
