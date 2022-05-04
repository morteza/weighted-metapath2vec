from wmp2vec.random_walk import weighted_random_walk

from sklearn.base import BaseEstimator, TransformerMixin


class WeightedMetapath2Vec(BaseEstimator, TransformerMixin):
    def __init__(self,
                 graph,
                 walk_length,
                 n_walks,
                 metapaths,
                 start_nodes=None, max_iters=1000):
        self.graph = graph
        self.metapaths = metapaths
        self.n_walks = n_walks
        self.walk_length = walk_length
        self.max_iters = max_iters
        self.start_nodes = start_nodes

        if self.start_nodes is None:
            self.start_nodes = self.graph.nodes

    def fit(self, X=None, y=None):
        return self

    def transform(self, X=None):
        walks = weighted_random_walk(self.graph,
                                     self.walk_length,
                                     self.n_walks,
                                     X or self.start_nodes,
                                     self.metapaths, self.max_iters)
        return walks
