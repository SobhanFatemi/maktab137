import random

def random_sentence(names, verbs, adverbs):
    print(f"{random.choice(names)} {random.choice(verbs)} {random.choice(adverbs)}")

names = ["Sobhan", "Arman", "Fateme"]
verbs = ["went", "fell", "ate"]
adverbs = ["quickly.", "suddenly.", "loudly."]

random_sentence(names, verbs, adverbs)