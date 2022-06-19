import numpy as np
import networkx as nx
import re


def match_metapath(G, walk, metapaths: list[list[str]]):

    node_types = [G.nodes.data('type')[node] for node in walk]

    for metapath in metapaths:

        metapath_encoding, encoded_metapath = np.unique(metapath, return_inverse=True)

        # skip empty metapaths
        if len(encoded_metapath) == 0:
          continue

        encoded_walk = ''.join([str(np.where(metapath_encoding == x)[0][0]) for x in node_types])

        metapath_pattern = '(?=(' + ''.join([str(nt) for nt in encoded_metapath]) + '))'

        n_matched = len(re.findall(metapath_pattern, encoded_walk))
        n_expected = (len(encoded_walk) - 1) / (len(encoded_metapath) - 1)

        if n_matched > 0 and n_matched == n_expected:
            return True

    return False


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

    node_walks = []

    node_iter_num = 0
    while len(node_walks) < n_walks:

      node_iter_num += 1
      if node_iter_num > max_iters:
        break

      walk = [start_node]
      current_node = start_node

      iter_num = 0
      while len(walk) < walk_length:

        iter_num += 1
        if node_iter_num > max_iters:
          break

        neighbors = list(graph.neighbors(current_node))
        weights = [graph[current_node][next_node]['weight'] for next_node in neighbors]

        if np.sum(weights) == 0.0:
          break

        weights = np.array(weights) / np.sum(weights)
        current_node = np.random.choice(neighbors, p=weights)
        walk.append(current_node)

      if (metapaths is None) or match_metapath(graph, walk, metapaths):
        node_walks.append(walk)

    walks.extend(node_walks)

  # remove duplicate walks
  walks = list(set(map(tuple, walks)))

  return walks


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
