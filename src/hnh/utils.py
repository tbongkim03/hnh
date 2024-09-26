def get_max_score(p):
    from random import choice
    label = choice(p)['label']
    score = choice(p)['score']
    return label