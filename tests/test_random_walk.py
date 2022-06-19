import numpy as np
import networkx as nx
from weighted_metapath2vec.random_walk import nx_random_walk, weighted_random_walk, match_metapath

import logging

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


def test_weighted_random_walk(walk_length=3, n_walks=10):

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

    walks = weighted_random_walk(G, walk_length, n_walks)

    assert len(walks) <= n_walks * len(G.nodes)


def test_nx_random_walk():
    weights = np.random.rand(5, 5)
    np.fill_diagonal(weights, 0)

    G = nx.from_numpy_array(weights)

    walks = nx_random_walk(G, walk_length=5, epochs=10)
    assert len(walks) == 50
