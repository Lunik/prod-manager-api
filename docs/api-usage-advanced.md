# Advanced usage

## Using a custom session

`prod-manager` relies on `requests.Session` objects to perform all the HTTP requests to the ProdManager servers.

You can provide your own `Session` object with custom configuration when you create a `ProdManager` object.

## Proxy configuration

The following sample illustrates how to define a proxy configuration when using `prod-manager` :

```python
import os
import prodmanager
import requests

session = requests.Session()
session.proxies = {
    'https': os.environ.get('https_proxy'),
    'http': os.environ.get('http_proxy'),
}
pm = prodmanager.ProdManager(url, token, session=session)
```

Reference: <https://requests.readthedocs.io/en/latest/user/advanced/#proxies>

## SSL certificate verification

`prod-manager` relies on the CA certificate bundle in the `certifi` package that comes with the requests library.

If you need `prod-manager` to use your system CA store instead, you can provide the path to the CA bundle in the `REQUESTS_CA_BUNDLE` environment variable.

Reference: <https://requests.readthedocs.io/en/latest/user/advanced/#ssl-cert-verification>

## Client side certificate

The following sample illustrates how to use a client-side certificate :

```python
import prodmanager
import requests

session = requests.Session()
session.cert = ('/path/to/client.cert', '/path/to/client.key')
pm = prodmanager.ProdManager(url, token, session=session)
```

Reference: <https://requests.readthedocs.io/en/latest/user/advanced/#client-side-certificates>
