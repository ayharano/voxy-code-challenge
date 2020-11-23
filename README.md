# Code Challenge

by [Alexandre Harano] (mailto:email@ayharano.dev)

"Code Challenge" provides a solution to a code challenge which requires to display the word count of a non-empty text input provided by a user through a web page.

You are free to copy, modify, and distribute "Code Challenge" with attribution under the terms of the MIT license. See the [LICENSE file](./LICENSE) for details.

## System requirements

- A Web browser that supports EMCAScript 6+
- Python 3.8+
- [Poetry](https://python-poetry.org/) 1.0.10+

## Installation

Using a terminal, change current directory to the directory containing this README file.

After that, run

```sh
poetry install
```

## Usage

Using a terminal, change current directory to the directory containing this README file.

After that, run

```sh
poetry run manage.py runserver
```

and in a Web browser open the URL http://127.0.0.1:8000/

If port 8000 is being used, run command

```sh
poetry run manage.py runserver <PORT>
```

and in a Web browser open the URL `http://127.0.0.1:<PORT>/`

This project Web site can be only accessed in the server local machine, as it is only using default development settings for now.

## Run test suite

Using a terminal, change current directory to the directory containing this README file.

After that, run

```sh
poetry run manage.py test
```

to run included tests.
