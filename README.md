# http-scots

[![CI](https://github.com/blfpd/http-scots/actions/workflows/ci.yaml/badge.svg)](https://github.com/blfpd/http-scots/actions/workflows/ci.yaml)
[![PyPI](https://img.shields.io/pypi/v/http-scots)](https://pypi.org/project/http-scots/)
[![Python](https://img.shields.io/pypi/pyversions/http-scots)](https://pypi.org/project/http-scots/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

HTTP methods and status codes, translated into Scots. It is a drop-in sibling of
the standard library's `http.HTTPStatus` and `http.HTTPMethod`, except every
status has opinions.

> **Content warning:** this package contains strong language, and quite a lot of
> it. If your logs are read aloud in stand-up, or your compliance team has a
> sense of humour deficit, maybe stick with `http`.

## Why

Because `404 Not Found` is polite, and `404 No fuckin here pal` is accurate.

Also because a well-typed enum is a perfectly good vehicle for a joke, and
because someone, somewhere, will put `HTTPStatus.GET_TAE_FUCK` in a demo and
not realise their client is watching.

## Credit where it is due

This package was totally inspired by
[HTTP status codes in Scots](https://underwood.network/http/scots.html) on
underwood.network. Go and have a look at the original, it is very funny.

## Install

```sh
pip install http-scots
# or
uv add http-scots
```

Needs Python 3.11 or newer (we lean on `StrEnum`, and we are not sorry).

## Usage

```python
from http_scots import HTTPMethod, HTTPStatus
# or, if you like it explicit: from http_scots.http import HTTPMethod, HTTPStatus

HTTPStatus(404)
# <HTTPStatus.NO_FUCKIN_HERE_PAL: 404>

HTTPStatus.NAE_BOTHER == 200
# True, it is a real IntEnum, so it compares like one

HTTPStatus.AHM_A_FUCKIN_TEAPOT.phrase
# 'Ahm a fuckin teapot'

HTTPStatus.SLOW_DOON.description
# 'ALRIGHT. PACK IT IN. Ye've asked aboot a thoosand times. ...'

HTTPStatus.THE_COUNCIL_SAYS_NAW.is_server_error
# True

HTTPMethod.GIES == "GET"
# True, it is a real StrEnum too

HTTPMethod.SKIP_IT.description
# "Richt, that's goin' in the skip. Dinnae come lookin' fur it."
```

Every member carries a `phrase` (the reason phrase) and a `description` (what
the server is actually thinking). Status codes also come with the usual
`is_informational`, `is_success`, `is_redirection`, `is_client_error` and
`is_server_error` helpers.

## A small sample

| Code | Standard name         | Scots                               |
| ---- | --------------------- | ----------------------------------- |
| 200  | OK                    | `NAE_BOTHER`                        |
| 301  | Moved Permanently     | `WEVE_FLITTED`                      |
| 403  | Forbidden             | `GET_TAE_FUCK`                      |
| 418  | I'm a teapot          | `AHM_A_FUCKIN_TEAPOT`               |
| 429  | Too Many Requests     | `SLOW_DOON`                         |
| 500  | Internal Server Error | `THE_COUNCIL_SAYS_NAW`              |

| Method | Scots        |
| ------ | ------------ |
| GET    | `GIES`       |
| POST   | `HAWDES`     |
| PUT    | `AWAWI`      |
| DELETE | `SKIP_IT`    |

The full list lives in [`src/http_scots/http.py`](src/http_scots/http.py).

## Is it serious?

The code is. It is typed (`py.typed` ships in the wheel), tested, has no
runtime dependencies, and follows the same RFCs as the standard library. The
translations are not serious, and are not an authoritative guide to the Scots
language. Spelling is deliberately loose and phonetic. If you are a Scots
speaker with better ideas, please open an issue, we would love the help.

## Development

```sh
uv sync
uv run pytest
uv build
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the details, including how releases
are cut.

## Licence

MIT. See [LICENSE](LICENSE).
