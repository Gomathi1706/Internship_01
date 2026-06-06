file = open("students.txt", "w")

file.write("Student Records\n")
file.write("-----------------\n")
file.write("Name: Arun, Age: 20, Department: CSE\n")
file.write("Name: Priya, Age: 19, Department: IT\n")
file.write("Name: Kavin, Age: 21, Department: ECE\n")

file.close()

print("Student records saved successfully!")

file = open("students.txt", "r")

print("\nStored Student Records:")
print(file.read())

file.close()