a = {"Alice": 85,"Bob": 90,"Chandler": 78,"Dravid": 92,"Eleven": 88}

b = input("Enter the student's name: ").title()
if b in a:
    print(f"{b}'s marks: {a[b]}")
else:
    print("Student not found.")