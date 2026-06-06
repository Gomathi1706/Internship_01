file = open("student_details.txt", "w")

file.write("Student Information\n")
file.write("-------------------\n")
file.write("Name: Gomathi\n")
file.write("Age: 19\n")
file.write("Department: AI & DS\n")
file.write("College: Kgisl Institute of Technology\n")

file.close()

print("Data written successfully!\n")

# Reading data from the text file

file = open("student_details.txt", "r")

content = file.read()

print("Student Details:")
print(content)

file.close()