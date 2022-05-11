# Weighted Metapath2vec

Weighted is a Python package to embed heterogenous graph nodes using a weighted alternative of Metapath2vec technique. The embedding can be used for downstream machine learning tasks.

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)


## Installation

```
pip install wmetapath2vec
```

## Usage

```python
from wmetapath2vec import WeightedMetapath2VecModel

...  # Load a networkx graph as G

metapaths = [
    ['Article', 'Author', 'Article'],
    ['Author', 'Article', 'Author']
]

model = WeightedMetapath2VecModel(G,
                                  metapaths,
                                  walk_length=3,
                                  n_walks_per_node=20,
                                  embedding_dim=128)

node_embeddings = model.fit_transform()

...  # downstream task
```
