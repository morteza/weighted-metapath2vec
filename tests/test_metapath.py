# %%
import numpy as np
import re
import networkx as nx


def match_metapath(G, walk, metapath):

    node_types = [G.nodes.data('type')[node] for node in walk]

    metapath_encoding, encoded_metapath = np.unique(metapath, return_inverse=True)

    encoded_walk = ''.join([str(np.where(metapath_encoding == x)[0][0]) for x in node_types])

    metapath_pattern = '(?=(' + ''.join([str(nt) for nt in encoded_metapath]) + '))'

    metapath_pattern

    n_matched = len(re.findall(metapath_pattern, encoded_walk))

    n_expected = (len(encoded_walk) - 1) / (len(encoded_metapath) - 1)

    if n_matched > 0 and n_matched == n_expected:
        return True

    return False

# example use case


weights = np.random.rand(5, 5)
np.fill_diagonal(weights, 0)

G = nx.from_numpy_array(weights)
G.nodes[0]['type'] = 'task'
G.nodes[1]['type'] = 'task'
G.nodes[2]['type'] = 'construct'
G.nodes[3]['type'] = 'construct'
G.nodes[4]['type'] = 'construct'
# G[0][2]['weight'] = 10

metapath = ['task', 'construct', 'task']

match_metapath(G, [0, 2, 1, 4, 1], metapath)
