from yaml import load
from lsm import compare
from datetime import datetime
import sys
import os
import apps


def LSM(service, config, user1, user2):
    app = getattr(apps, "_" + service)
    text1, text2 = app(config, user1, user2)
    return compare(text1, text2)


def get_config(filepath="~/.nltk-lsm.yml"):
    try:
        with open(os.path.expanduser(filepath), 'r') as f:
            return load(f.read())
    except Exception as e:
        print "Couldn't read config:", e


def get_args(args):
    try:
        service, user1, user2 = args[1:4]
        return service, user1, user2
    except Exception as e:
        print "Couldn't parse input arguments:", e


def log(*args, **kwargs):
    filepath = kwargs.get('filepath', "~/.nltk-lsm.log")
    with open(os.path.expanduser(filepath), 'a') as f:
        now = str(datetime.now()).split(' ')
        now.extend([str(item) for item in args])
        line = ' '.join(now)
        f.write(line+'\n')
        return line


def main():
    args = get_args(sys.argv)
    if args:
        service, user1, user2 = args
        config = get_config()[service]
        if config:
            likeness = LSM(service, config, user1, user2)
            print log(service, user1, user2, likeness)

if __name__ == "__main__":
    main()
