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
