title: Guidelines

When creating a new project or moving an existing one to the Jazzband
there are some guidelines to follow. They exist to make sure that
the Jazzband stays useful as a place to share responsibility for software
maintenance when a number of projects are created at or moved to it.

To initiate the transfer to Jazzband, you should use
[Github's Transfer Feature](https://help.github.com/en/github/administering-a-repository/transferring-a-repository)
to transfer the repository to the Jazzband organization. The Jazzband bot will
then open an issue in the
[Roadies help repo](https://github.com/jazzband/help/issues/38)
with a TODO list that you can work through to complete the transfer, which
is mainly to ensure the below guidelines are being followed. Please do read
the guidelines in full before initiating a transfer.

!!! warn "Please consider these guidelines carefully before deciding to transfer a repository to the Jazzband GitHub organization."

    The Jazzband [roadies](/roadies) will enforce the guidelines and won't hesitate to remove projects from the GitHub organization if required.

    The section about [frequently asked questions](/about/faq) may be
    interesting to you as well.

### Viability

There is no place in the Jazzband for proofs of concept or projects that
exist as one-off toys. The Jazzband expects projects to cover non-trivial
functionality and is not a code snippet hoster.

Established projects with a history of outside contributions that seek more
maintainers are best suited for transfer to the Jazzband.

Projects should have an orderly hand-over to Jazzband with agreement
from the previous maintainer(s). For example, forking a project to transfer
it to Jazzband is frowned upon.

### Documentation

Projects require prose documentation for end users **and** contributors.
Inline code documentation is considered an indicator for a high quality of
code and is also strongly recommended.

Document as much as possible and don't rely on autodoc alone. Write like you're
addressing yourself in a few years.

### Tests

Projects must have tests that are easy to run. Automatic testing based on
contributions (e.g. GitHub Actions) is also strongly encouraged. The test
coverage requirement follows the "perfect is the enemy of the good" motto
-- it's enough if the tests cover the core API of the project.

Test as much as needed to make maintenance a breeze. Don't be dogmatic.

### Conduct

Projects are required to adopt and follow the Jazzband code of conduct.
Please see the [Contributor Code of Conduct](/about/conduct) for more
information what that entails and how to report conduct violations.

Adhering to the contributor code of conduct is key in keeping the Jazzband
together.

### Contributing Guidelines

Projects have to add a `CONTRIBUTING.md` or `CONTRIBUTING.rst` file to their repository so it's
automatically displayed when new issues and pull requests are created.

A `CONTRIBUTING.md` ([Markdown]) file needs to contain this header:

```md
[![Jazzband](https://jazzband.co/static/img/jazzband.svg)](https://jazzband.co/)

This is a [Jazzband](https://jazzband.co/) project. By contributing you agree to abide by the [Contributor Code of Conduct](https://jazzband.co/about/conduct) and follow the [guidelines](https://jazzband.co/about/guidelines).
```

A `CONTRIBUTING.rst` ([reStructuredText]) file needs to contain this header:

```rst
.. image:: https://jazzband.co/static/img/jazzband.svg
   :target: https://jazzband.co/
   :alt: Jazzband

This is a `Jazzband <https://jazzband.co>`_ project. By contributing you agree to abide by the `Contributor Code of Conduct <https://jazzband.co/about/conduct>`_ and follow the `guidelines <https://jazzband.co/about/guidelines>`_.
```

See the default [contributing guideline] file for how it'd look like.
Feel free to add a similar paragraph to your `README` file.

Of course extending the contributing document with your project's contributing
guide is highly encouraged, too. See GitHub's documentation on [contributing
guidelines] for more information.

[contributing guidelines]: https://help.github.com/articles/setting-guidelines-for-repository-contributors/
[contributing guideline]: https://github.com/jazzband/.github/blob/main/CONTRIBUTING.md
[reStructuredText]: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
[Markdown]: https://daringfireball.net/projects/markdown/syntax

### Badges

You may also want to use Jazzband badges (following the [shields.io] spec) using the
following URL: `https://jazzband.co/static/img/badge.svg`. It looks like this:
![Jazzband](https://jazzband.co/static/img/badge.svg)

Markdown:

```md
[![Jazzband](https://jazzband.co/static/img/badge.svg)](https://jazzband.co/)
```

reStructuredText:

```rst
.. image:: https://jazzband.co/static/img/badge.svg
   :target: https://jazzband.co/
   :alt: Jazzband
```
