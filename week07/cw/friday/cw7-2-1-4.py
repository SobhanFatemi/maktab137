class CustomDict(dict):
    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        return self.get(key)

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return f"No '{key}' found!"
    
    def __setitem__(self, key, value):
        if isinstance(value, int):
            value *= 2
        super().__setitem__(key, value)

    def __str__(self):
        return f"Dictionary: {dict(self)}\nNumber of keys: {len(self)} "
    
    def __repr__(self):
        return f"Dictionary: {dict(self)}\nNumber of keys: {len(self)}"


dict1 = CustomDict({"name": "Ali", "last_name": "heidari"})
dict1["name"] = "sobhan"
dict1.age = 25

print(dict1)
print(dict1["a"])
print(dict1.age)

    