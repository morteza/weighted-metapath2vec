from wmetapath2vec.random_walk import weighted_random_walk

from sklearn.base import BaseEstimator, TransformerMixin

from gensim.models import Word2Vec


class WeightedMetapath2VecModel(BaseEstimator, TransformerMixin):
    def __init__(self,
                 graph,
                 metapaths,
                 walk_length=3,
                 n_walks_per_node=10,
                 embedding_dim=128,
                 word2vec_window_size=3,
                 start_nodes='all',
                 max_iters=1000):
        self.graph = graph
        self.metapaths = metapaths
        self.n_walks_per_node = n_walks_per_node
        self.walk_length = walk_length
        self.embedding_dim = embedding_dim
        self.word2vec_window_size = word2vec_window_size
        self.max_iters = max_iters
        self.start_nodes = start_nodes

        if self.start_nodes == 'all':
            self.start_nodes = self.graph.nodes

        self.walks_ = None
        self.embeddings_ = None

    def fit(self, X=None, y=None, **fit_params):
        self.walks_ = weighted_random_walk(
            self.graph,
            self.walk_length,
            self.n_walks_per_node,
            X or self.start_nodes,
            self.metapaths, self.max_iters)

        self.model_ = Word2Vec(
            self.walks_,
            vector_size=self.embedding_dim,
            min_count=0,
            window=self.word2vec_window_size,
            sg=1,
            workers=-1,
            epochs=10)

        # keys = model_.wv.key_to_index.keys()
        self.embeddings_ = self.model_.wv.vectors

        return self

    def transform(self, X=None):
        return self.embeddings_

    def fit_transform(self, X=None, y=None, **fit_params):
        return self.fit(X, y, **fit_params).transform(X)
