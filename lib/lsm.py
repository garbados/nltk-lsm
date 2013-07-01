import nltk
from collections import Counter

NON_FUNCTION_TAGS = [
    'FW',
    'JJ', 'JJR', 'JJS', 'JJT',
    'NN', 'NNS', 'NNP', 'NNPS',
    'POS',
    'RB', 'RBR', 'RBS',
    'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'
]


def intersection(c1, c2):
    return set(c1).intersection(set(c2))


def is_function_tag(tag):
    if tag in NON_FUNCTION_TAGS:
        return False
    else:
        return True


def abs_diff(preps1, preps2):
    return 1 - (abs(preps1 - preps2) / float(preps1 + preps2 + .0001))


def compare(text1, text2):
    styles = []
    for text in [text1, text2]:
        tokens = nltk.word_tokenize(text)
        tags = [item[1] for item in nltk.pos_tag(text)]
        counter = Counter(tags)
        total = sum(counter.values())
        style = {}
        for tag, count in counter.iteritems():
            if is_function_tag(tag):
                style[tag] = float(count) / total
        styles.append(style)
    comparisons = []
    common_tags = intersection(styles[0].keys(), styles[1].keys())
    for tag in common_tags:
        # weight = (styles[0][tag] + styles[1][tag]) / 2
        diff = abs_diff(styles[0][tag], styles[1][tag])
        comparisons.append(diff)
    return float(sum(comparisons)) / len(comparisons)
