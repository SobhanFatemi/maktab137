def file_io(input_file, output_file):
    def decorator(func):
        def wrapper(data):
            with open(input_file, 'w') as file:
                file.write(data)
            result = func(data)
            with open(output_file, 'w') as file:
                file.write(result)
            return result
        return wrapper
    return decorator


@file_io(input_file='input.txt', output_file='output.txt')
def process_data(data):
    return data.upper()

data = "hello world"
# data = input("Enter a sentence: ")
process_data(data)