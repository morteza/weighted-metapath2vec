import numpy as np
import networkx as nx
from wmp2vec.random_walk import match_metapath


def test_match_metapath():

    weights = np.random.rand(5, 5)
    np.fill_diagonal(weights, 0)

    G = nx.from_numpy_array(weights)
    G.nodes[0]['type'] = 'task'
    G.nodes[1]['type'] = 'task'
    G.nodes[2]['type'] = 'construct'
    G.nodes[3]['type'] = 'construct'
    G.nodes[4]['type'] = 'construct'
    # G[0][2]['weight'] = 10

    metapaths = [['task', 'construct', 'task']]

    assert match_metapath(G, [0, 2, 1, 4, 1], metapaths)
