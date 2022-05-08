import numpy as np
import networkx as nx

from wmetapath2vec.model import WeightedMetapath2VecModel


def test_wmetapath2vec_model(embedding_dim=128):
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

    model = WeightedMetapath2VecModel(G, metapaths, 3, 20, embedding_dim=embedding_dim)
    embeddings = model.fit_transform()

    assert embeddings.shape == (len(G.nodes.keys()), embedding_dim)
