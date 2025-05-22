with open("output.txt", "w") as f:
    f.write(input("Enter text to write to the file: "))
    print("Data successfully written to 'output.txt'.\n")

with open("output.txt", "a") as f:
    f.write("\n" + input("Enter additional text to append: "))
    print("Data successfully appended\n")

with open("output.txt", "r") as f:
    print("Final content of output.txt:")
    print(f.read())