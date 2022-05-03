import numpy as np
import networkx as nx


def weighted_random_walk(graph: nx.Graph,
                         walk_length,
                         n_walks,
                         start_nodes: list = None,
                         metapaths: list = None,
                         max_iters=1000):

  if start_nodes is None:
    start_nodes = graph.nodes

  walks = []
  for start_node in start_nodes:
    assert start_node in graph.nodes
    for _ in range(n_walks):

      walk = [start_node]
      current_node = start_node

      iter_num = 0
      while len(walk) < walk_length:

        iter_num += 1
        if iter_num > max_iters:
          break

        neighbors = list(graph.neighbors(current_node))
        weights = [graph[current_node][next_node]['weight'] for next_node in neighbors]

        if np.sum(weights) == 0.0:
          break

        weights = np.array(weights) / np.sum(weights)
        current_node = np.random.choice(neighbors, p=weights)
        walk.append(current_node)

      walks.append(walk)

  return walks


# def weighted_random_walk_deprecated(graph,
#                                     n: int = None,
#                                     length: int = None,
#                                     metapaths=None):

  # _g = cg.csrgraph(graph)

  # TODO assert length == len(metapaths[0]) == len(metapaths[1]) == ...
  # TODO walks of length>len(metapaths[0]) are also valid if it uses the same methapath

  # valid_walks = []
  # while len(valid_walks) < n:
  #   walks = _g.random_walks(length, n, start_nodes=None)
  #   types = [[graph.nodes[node]['type'] for node in walk]
  #            for walk in walks]
  #   walks = [walks[i].tolist()
  #            for i, t in enumerate(types)
  #            if t in metapaths and len(set(walks[i])) == len(walks[i])  # no loop
  #            ]
  #   valid_walks.extend(walks)

  # return valid_walks[:n]


def nx_random_walk(graph, walk_length, epochs, start_nodes=None, max_iter=1000):

  if start_nodes is None:
    start_nodes = graph.nodes

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
        walk = np.random.choice(graph.nodes(),
                                walk_length - 1,
                                replace=True)
        walk = np.append(src, walk)
        # node_types = [graph.nodes[node]['type'] for node in walk]

        walk_weights = []
        for i, _ in enumerate(walk[:-1]):
          ws = walk[i - 1]
          wd = walk[i]
          wgt = graph.get_edge_data(ws, wd, {'weight': 0.0})['weight']
          walk_weights.append(wgt)

        if 0.0 not in walk_weights:
          walks.append(walk)
          _walk_weights.append(walk_weights)

  return walks
