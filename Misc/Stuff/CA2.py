students = {}

def addStudent():
    name = input("Enter the name: ")
    name = name.lower()
    marks1 = int(input("Enter marks for English: "))
    marks2 = int(input("Enter marks for Maths: "))
    marks3 = int(input("Enter marks for Science: "))
    
    students[name] = {
        "english": marks1,
        "maths": marks2,
        "science": marks3
    }
    
def updateMarks(name, subject, newMarks):
    name = name.lower()
    if name not in students:
        print(f"Student with name {name} does not exist")
        return
    
    subject = subject.lower()
    if subject == "english" or subject == "maths" or subject == "science":
        student = students[name]
        student[subject] = newMarks
    else:
        print("Invalid subject")
        return
    
def deleteStudent(name):
    name = name.lower()
    if name not in students:
        print(f"Student with name {name} does not exist")
        return
    
    print(f"Student record for {name} deleted")
    students.pop(name)
    
def displayDetails(name):
    name = name.lower()
    if name not in students:
        print(f"Student with name {name} does not exist")
        return
    
    student = students[name]
    print(f"Name: {name}")
    print("Marks -")
    print(f"English - {student['english']}")
    print(f"Maths - {student['maths']}")
    print(f"Science - {student['science']}")
    
def calculateAverage():
    total = len(students)
    if total == 0:
        print("No students added")
        return
    
    sum = [0, 0, 0]
    
    for student in students.values():
        sum[0] += student["english"]
        sum[1] += student["maths"]
        sum[2] += student["science"]
    
    print("Average Marks -")
    print(f"English - {sum[0] / total}")
    print(f"Maths - {sum[1] / total}")
    print(f"Science - {sum[2] / total}")
    


# addStudent()
# print()
# addStudent()
# print()
# addStudent()
# print()

# updateMarks("vikram", "science", 90)
# print()

# displayDetails("vikram")
# print()

# calculateAverage()
# print()

# deleteStudent("vikram")
# print()

# displayDetails("vikram")
# print()



newStudents = {}
student_id = 1000

def addStudent2():
    global student_id
    name = input("Enter the name - ")
    marks1 = int(input("Enter marks for Subject 1 - "))
    marks2 = int(input("Enter marks for Subject 2 - "))
    marks3 = int(input("Enter marks for Subject 3 - "))
    
    newStudents[student_id] = {
        "name": name,
        "marks": {
            "english": marks1,
            "maths": marks2,
            "science": marks3
        }
    }
    
    student_id += 1
    
def printDetails2(i):
    if i not in newStudents:
        print(f"student with id {i} does not exist")
        return
    
    student = newStudents[i]
    print(f"Name - {student['name']}")

    subjets = student["marks"]
    for key, val in subjets.items():
        print(f"{key}: {val}")


addStudent2()
printDetails2(1000)
