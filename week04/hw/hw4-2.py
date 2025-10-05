def to_string(func):
    def wrapper(*args, **kwargs):
        str_args = []
        str_kwargs = {}
        for arg in args:
            str_args.append(str(arg))
        for key, value in kwargs.items():
            str_kwargs[str(key)] = str(value)
        result = func(*str_args, **str_kwargs)
        return result
    return wrapper

def get_length(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f"length of '{arg}' -> {len(arg)}")
        for key, value in kwargs.items():
            print(f"length of '{key}' -> {len(key)}")
            print(f"length of '{value}' -> {len(value)}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@to_string
@get_length
def do_something(*args, **kwargs):
    print(args, kwargs)

do_something("sobhan", 2, 40.2, x="abc", y=5)