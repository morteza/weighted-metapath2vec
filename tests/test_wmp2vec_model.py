import numpy as np
import networkx as nx

from wmp2vec.wmp2vec_model import WeightedMetapath2Vec


def test_wmp2vec_model():
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

    WeightedMetapath2Vec(G, 3, 20, metapaths).transform()
