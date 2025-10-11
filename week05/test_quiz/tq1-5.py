def read_file(file_name):
    with open(file_name) as f:
        for line in f:
            yield line


for line in read_file("somefile.txt"):
    print(line.strip())