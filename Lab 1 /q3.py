students={}

for i in range(3):
    name=input("Enter student's name : ")
    marks=int(input("Enter marks : "))
    students[name]=marks
    
print("Student Records:")
print(students)
