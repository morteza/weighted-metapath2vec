import numpy as np
import networkx as nx
import csrgraph as cg


def weighted_metapath_random_walk(graph,
                                  n: int = None,
                                  length: int = None,
                                  metapaths=None):
  _g = cg.csrgraph(graph)

  # TODO assert length == len(metapaths[0]) == len(metapaths[1]) == ...
  # TODO walks of length>len(metapaths[0]) are also valid if it uses the same methapath

  valid_walks = []
  while len(valid_walks) < n:
    walks = _g.random_walks(length, n, start_nodes=None)
    types = [[graph.nodes[node]['type'] for node in walk]
             for walk in walks]
    walks = [walks[i].tolist()
             for i, t in enumerate(types)
             if t in metapaths and len(set(walks[i])) == len(walks[i])  # no loop
             ]
    valid_walks.extend(walks)

  return valid_walks[:n]


def nx_random_walk(G, walk_length, epochs, start_nodes=None, max_iter=1000):

  if start_nodes is None:
    start_nodes = G.nodes

  walks = []
  _walk_weights = []

  epoch = 0

  while epoch < epochs:
    epoch += 1

    for i_src, src in enumerate(start_nodes):
      iteration = 0

      while (iteration < max_iter
             and len(walks) < epochs * (i_src + 1)):

        iteration += 1
        walk = np.random.choice(G.nodes(),
                                walk_length - 1,
                                replace=True)
        walk = np.append(src, walk)
        # node_types = [G.nodes[node]['type'] for node in walk]

        walk_weights = []
        for i, _ in enumerate(walk[:-1]):
          ws = walk[i - 1]
          wd = walk[i]
          wgt = G.get_edge_data(ws, wd, {'weight': 0.0})['weight']
          walk_weights.append(wgt)

        if 0.0 not in walk_weights:
          walks.append(walk)
          _walk_weights.append(walk_weights)

  return walks
