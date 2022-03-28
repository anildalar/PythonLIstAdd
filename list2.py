students = ["Vijay","Nandini"]

noofstudent = int(input("Please enter no of students you want to store :- "));

#students.append(name)
for x in range(noofstudent):
    students.append(input("Please enter the student name:- "))

for student in students:
    print(f"Hello {student}, How are you? ")