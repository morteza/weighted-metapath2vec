import numpy as np
import networkx as nx
from wmp2vec.random_walk import weighted_metapath_random_walk
from wmp2vec.random_walk import nx_random_walk


def test_weighted_metapath_random_walk():

    weights = np.random.rand(5, 5)
    np.fill_diagonal(weights, 0)

    G = nx.from_numpy_array(weights)
    G.nodes[0]['type'] = 'task'
    G.nodes[1]['type'] = 'task'
    G.nodes[2]['type'] = 'construct'
    G.nodes[3]['type'] = 'construct'
    G.nodes[4]['type'] = 'construct'
    # G[0][2]['weight'] = 10

    metapaths = [
        ['task', 'construct', 'task'],
        ['construct', 'task', 'construct'],
    ]

    walks = weighted_metapath_random_walk(G, 30, 3, metapaths)
    print(walks)
    # G.edges.data()


def test_nx_random_walk():
    weights = np.random.rand(5, 5)
    np.fill_diagonal(weights, 0)

    G = nx.from_numpy_array(weights)

    walks = nx_random_walk(G, walk_length=5, epochs=10)
    assert len(walks) == 50
