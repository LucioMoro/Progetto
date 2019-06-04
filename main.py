import numpy as np
import DFN as dfn

# Settiamo i parametri del costruttore del DFN

N = 10
Xmin = 0
Xmax = 1
Ymin = 0
Ymax = 1
Zmin = 0
Zmax = 1
alpha_pl = 2
radius_l = 2
radius_u = 3
k = 1
mode_vector = np.array([[0.5], [2.], [1.]])
fixed_n_edges = 4

# Creiamo un network

network = dfn.DiscreteFractureNetwork(N, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax,
                                      alpha_pl, radius_l, radius_u, k, mode_vector, fixed_n_edges)

# Rimuoviamo delle fratture

v = [0, 0, 1]
# network.rimuovi(v)

# Aggiungiamo delle fratture

#network.genfrac(3)

# Chiamiamo i metodi di scrittura su file

network.scrittura1()
network.scrittura2()

# Visualizziamo il network con le sue fratture

network.visual3D()

# Salviamo l'oggetto in formato .pkl

network.save()

# Stampiamo le possibili intersezioni

# print(network.poss_intersezioni)
# print(network.possibili_intersezioni())
# print(network.intersezioni)
print(network.traces[0].estremi)
# print(network.inters_BB(network.fractures[0], network.fractures[2]))