# NLTK-LSM

Language Style Matching (LSM), using the NLTK. LSM indicates the likeness of two text bodies by comparing use of function words, or words that relate solely to the syntactic and grammatical structure of a sentence, like conjunctions and articles, but not nouns or verbs.

## Install

    git clone git@github.com:garbados/nltk-lsm.git
    cd nltk-lsm
    virtualenv venv
    source venv/bin/activate
    make

At this time it is unclear how to install globally. Attempting `sudo make` outside the virtualenv yields a SandboxError.

## Usage

From command line, running...

    python -m lib [service] [user1] [user2]

...will yield this:

    # [date] [time] [service] [user1] [user2] [likeness]
    2013-06-30 23:58:06.443966 twitter BarackObama MichelleObama 0.894578663515

...and write something like that second line to `~/.nltk-lsm.log`

## Config

To be written :(