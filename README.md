# Weighted-Metapath2Vec

**Weighted-Metapath2Vec** is a Python package for embedding heterogeneous graphs.
It uses a weighted variant of [metapath2vec](https://ericdongyx.github.io/metapath2vec/m2v.html) to compute the node embeddings.
The embeddings can be used for downstream machine learning.

**The package is a work-in-progress**. There are bugs, and example notebooks are missing. If you want to use this package, expect to make changes.

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

## Acknowledgements

This project is supported by the Luxembourg National Research Fund (ATTRACT/2016/ID/11242114/DIGILEARN and INTER Mobility/2017-2/ID/11765868/ULALA).


## License

MIT License. See the [LICENSE](LICENSE) file.
