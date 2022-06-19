# Weighted-Metapath2Vec

**Weighted-Metapath2Vec** is a Python package to embed heterogeneous graphs.
The algorithm uses a weighted alternative to Metapath2vec to compute the embeddings.
The embeddings can be used for downstream machine learning.


[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)


## Installation

```bash
pip install weighted-metapath2vec
```

## Usage

```python
from weighted_metapath2vec import WeightedMetapath2VecModel

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

## Contributing

Use GitHub to fork and submit pull requests.

## License

MIT License. See the [LICENSE](LICENSE) file.
