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

Then, sign up on [OpenReview](https://openreview.net) if you haven't.

Next, run:
```
$ cp .env.example .env
```

Finally, fill in your Open Review username and password in the `.env` in order
to connect to the API using your account.

# Usage

Simply call the script with a path to your `*.bib` file:

```
./main.py path/to/references.bib
```

An example output is:

```
✅ [OK] (1/10) <paper title 1>
✅ [OK] (2/10) <paper title 2>
⛔️ [REJECTED] (3/40) <paper title 3>
    > https://openreview.net/forum?id=<ID>
✅ [OK] (4/10) <paper title 4>
...
✅ [OK] (10/10) <paper title 10>
```

> [!IMPORTANT]
> **Dislaimer:** Please note that this script aims at finding *any* rejected
> publication. This does not mean the latest work of the authors is rejected.
> Those that come up as rejected should *always* be manually confirmed through
> you—the developer who is utilizing this project—on Open Review. When
> hesitating about the state of publication, it is recommended to contact the
> authors of the paper for the most accurate information.
