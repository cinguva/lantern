# lantern

[![Inline docs](https://readthedocs.org/projects/crypto-lantern/badge/?version=latest)](https://crypto-lantern.readthedocs.io/en/latest/)

TODO: Logo

TODO: Jenkins auto builds

TODO: Coveralls

**lantern** is a cryptanalysis library to assist with the identification and breaking of classical ciphers. The library provides general purpose analysis tools, aswell as premade modules to break well known classic ciphers.

```python
from lantern.modules import caesar
from lantern.score_functions import english_scorer

ciphertext = """iodj{EuxwhIrufhLvEhvwIrufh}"""

decryptions = caesar.crack(ciphertext, [english_scorer.quadgrams()])
best_decryption = decryptions[0]
print(best_decryption.plaintext)
```

In short, lantern can be used to:

* **Identify** ciphers from ciphertext
* **Auotomatically crack** well known ciphers
* **Analyze** ciphertext to assist in the breaking of custom crypto systems

## Installation

```
git clone git@github.com:CameronLonsdale/lantern.git
pip install -e ./lantern
```

## Documentation

Full documentation available at [https://crypto-lantern.readthedocs.io/](https://crypto-lantern.readthedocs.io/en/latest/)

## Requirements

| Supported Python Implementations |
| ---------------------------------|
| Python 2.7                       |
| Python 3.5                       |
| PyPy                             |

lantern has no external dependencies outside of the Python standard library.

## Usage

lanterns's usage is for it's modules to be imported into custom scripts written by the user. The modules aim to be generalised cryptoanalysis functions which the user can extend / modify / combine with other changes to solve particular problems.

Recommended usage with PyPy for maximum speed.

[Example programs](examples)

## Development

### Testing

Setup a virtual environment with your favourite version of python

```
virtualenv -p python3.5 venv
source ./venv/bin/activate
```

Install testing requirements

`pip install -r test_requirements`

Use `py.test` to run tests using your current working environment

Use `tox -r` to build a new environment for each python version and run all tests

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request.
