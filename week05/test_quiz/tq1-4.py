d1 = {'a': 1, 'b': 2}

d2 = dict(map(lambda x: (x[1], x[0]), d1.items()))

print(d2)