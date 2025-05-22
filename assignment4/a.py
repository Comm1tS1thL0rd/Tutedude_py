try:
    with open("sample.txt", "r") as f:
        print("Reading file content:")
        i = 1
        line = f.readline()
        while line:
            print("Line", i, ":", line.rstrip())
            i += 1
            line = f.readline()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
