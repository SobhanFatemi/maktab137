def process(d1):
    d2 = {}
    for key, value in d1.items():
        if value in d2:
            if isinstance(d2[value], list):
                d2[value].append(key)
            else:
                d2[value] = [d2[value], key]
        else:
            d2[value] = key
    return d2

d1 = {
"apple": "fruit",
"banana": "fruit",
"carrot": "vegetable",
"tomato": "vegetable",
"laptop": "technology",
"orange": "fruit"
}

print(process(d1))