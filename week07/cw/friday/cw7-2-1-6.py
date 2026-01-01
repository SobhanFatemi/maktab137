class CustomDict(dict):
    def __add__(self, other):
        if not isinstance(other, dict):
            raise ValueError("Value must be a dict!")
        
        result = self.copy()

        for key, value in other.items():
            if key in result:
                if isinstance(value, str) and isinstance(self[key], str):
                    result[key] = f"{self[key]} - {value}"
                elif isinstance(value, int) and isinstance(self[key], int):
                    result[key] = self[key] + value
            else:
                result[key] = value
        return result
        

dict1 = CustomDict({"name": "sobhan", "age": 12})
dict2 = CustomDict({"name": "Harry Potter", "age": "209"})

dict3 = dict1 + dict2

print(dict3)