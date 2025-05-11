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
✅ [OK] (1/10) Realtoxicityprompts: Evaluating neural toxic degeneration in language models
✅ [OK] (2/10) JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models
⛔️ [REJECTED] (3/40) Jailbreaking Black Box Large Language Models in Twenty Queries
    > https://openreview.net/forum?id=hkjcdmz8Ro
✅ [OK] (4/10) Universal and Transferable Adversarial Attacks on Aligned Language Models
...
✅ [OK] (10/10) Emergence of human-like polarization among large language model agents
```
