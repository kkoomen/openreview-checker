# OpenReview Checker

Verifies all entries in a `.bib` file on [OpenReview](https://openreview.net)
whether they have ever been rejected.

# Getting Started

```
$ git clone https://github.com/kkoomen/openreview-checker && cd openreview-checker
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

# Usage

Simply call the script with a path to your `*.bib` file:

```
./main.py path/to/references.bib
```
