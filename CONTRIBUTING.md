# Contributing

Thanks for wanting to help make a computer swear in Scots. A few notes.

## Setup

You need [uv](https://docs.astral.sh/uv/).

```sh
git clone https://github.com/blfpd/http-scots
cd http-scots
uv sync
uv run pytest
```

## What we would like

- Better, more authentic Scots. If something reads like a tourist wrote it, say
  so, and say what a local would say instead.
- Missing HTTP status codes or methods, with a link to the RFC.
- Bug fixes, tests, and typing improvements.

## What we would rather avoid

- Changing a member's numeric code or an enum's public behaviour. Names can
  change in a major release, codes cannot.
- Anything that targets or demeans real people. The rude words are aimed at
  servers, clients and teapots only.
- New runtime dependencies. The list is empty and we would like to keep it that
  way.

## Pull requests

1. Add or update tests in `tests/`.
2. Run `uv run pytest`.
3. Add a line to `CHANGELOG.md` under `Unreleased`.

## Releasing (maintainers)

Releases are published to PyPI by `.github/workflows/publish.yaml` using
[trusted publishing](https://docs.pypi.org/trusted-publishers/), so there are
no API tokens to leak.

One-time setup:

1. On PyPI, add a trusted publisher for the project `http-scots` with owner
   `blfpd`, repository `http-scots`, workflow `publish.yaml`, environment
   `pypi`. For a first release, use a
   [pending publisher](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/).
2. Optionally do the same on TestPyPI with environment `testpypi`.
3. In the GitHub repository settings, create the environments `pypi` and
   `testpypi`. Adding a required reviewer to `pypi` is a good idea.

To cut a release:

1. Move the `Unreleased` notes in `CHANGELOG.md` under a new version heading.
2. Bump `version` in `pyproject.toml`.
3. Commit, then tag and push: `git tag v0.1.1 && git push --tags`.
4. Create a GitHub release from the tag. Publishing the release triggers the
   workflow. The workflow refuses to publish if the tag and
   `pyproject.toml` disagree.

To rehearse against TestPyPI, run the `Publish` workflow manually from the
Actions tab.
