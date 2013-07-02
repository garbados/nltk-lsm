# NLTK-LSM

Language Style Matching (LSM), using the NLTK. LSM indicates the likeness of two text bodies by comparing use of function words, or words that relate solely to the syntactic and grammatical structure of a sentence, like conjunctions and articles, but not nouns or verbs.

## Install

    git clone git@github.com:garbados/nltk-lsm.git
    cd nltk-lsm
    sudo make # to install globally

`nltk-lsm` exposes itself to global uses by aliasing itself in a profile. If your machine doesn't do UNIX-ish aliasing, or doesn't user `~/.bashrc` for profiles, edit `Makefile` accordingly.

## Usage

From command line, running...

    nltk-lsm [service] [user1] [user2]

...will yield this:

    # [date] [time] [service] [user1] [user2] [likeness]
    2013-06-30 23:58:06.443966 twitter BarackObama MichelleObama 0.894578663515

...and write something like that second line to `~/.nltk-lsm.log`

## Config

To be written :(