# ProdManager API

`prod-manager` is a Python package providing access to the [ProdManager][prodmanager] API.

## Features

`prod-manager` enables you to:

- write Pythonic code to manage your [ProdManager][prodmanager] resources.
- pass arbitrary parameters to the [ProdManager][prodmanager] API. Simply follow [ProdManager][prodmanager]’s docs on what parameters are available.
- access arbitrary endpoints as soon as they are available on [ProdManager][prodmanager], by using lower-level API methods.
- use persistent requests sessions for authentication, proxy and certificate handling.
- flexible handling of paginated responses, including lazy iterators.

## Installation

`prod-manager` is compatible with Python 3.7+.

Use `pip` to install the latest stable version of `prod-manager`:

```bash
$ pip install --upgrade prod-manager
```

The current development version is available on GitLab.com, and can be installed directly from the git repository:

```bash
$ pip install git+https://gitlab.com/prod-manager/prod-manager-api.git
```

## Bug reports

Please report bugs and feature requests at <https://gitlab.com/prod-manager/prod-manager-api/-/issues>.

## Documentation

The full documentation for CLI and API is available on [GitLab Pages][documentation-url].

### Build the docs

We use `mkdocs` to manage our environment and build the documentation :

```bash
$ poetry install --only docs
$ mkdocs build
```

## Contributing

For guidelines for contributing to `prod-manager`, refer to [CONTRIBUTING.md](./CONTRIBUTING.md).


<!-- Links -->
[documentation-url]: https://prod-manager-api.tiwabbit.fr
[prodmanager]: https://gitlab.com/prod-manager/prod-manager