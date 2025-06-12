
import os
import json

student = []
subjects = ["maths", "english", "science", "computer science"]

def add_student():
    num = int(input("Enter the number of students you want to enter: "))
    for index in range(num):
        name = input("Enter the name of the student: ")
        student.append([name])
        avgt = 0
        for subject in subjects:
            while True:
                try:
                    marks = int(input(f"Enter the marks of {subject}: "))
                    if marks > 100 or marks < 0:
                        print("Please enter a number between 0 to 100 inclusive.")
                    else:
                        break
                except ValueError:
                    print("Invalid input! Please enter a number.")

            student[index].append(marks)
            avgt += marks

        student[index].append(avgt)
        student[index].append(avgt / len(subjects))

        percent = avgt / (100 * len(subjects)) * 100
        if percent >= 80:
            grade = "A"
        elif percent >= 70:
            grade = "B"
        elif percent >= 60:
            grade = "C"
        else:
            grade = "F"
        student[index].append(grade)

    if exsist:
        with open("student_record.json", "r+") as file:
            temp = json.load(file)
            temp.extend(student)
            file.seek(0)
            json.dump(temp, file)
    else:
        with open("student_record.json", "w") as file:
            json.dump(student, file)

def view_student():
    if exsist:
        name = input("Enter the name of the student: ")
        with open("student_record.json", "r") as file:
            student_data = json.load(file)
        found = False
        for row in student_data:
            if name.lower() == row[0].lower():
                found = True
                sub = input("For total marks press 1\nFor subject marks enter subject name\nFor average press 2\nYour Option: ").lower()
                if sub in subjects:
                    print(f"The marks for {sub} are {row[subjects.index(sub) + 1]}")
                elif sub == "1":
                    print(f"Total marks: {row[len(subjects) + 1]}")
                elif sub == "2":
                    print(f"Average marks: {row[len(subjects) + 2]}")
                else:
                    print("Invalid option or subject.")
        if not found:
            print("Student not found.")
    else:
        print("No student data available.")

def main():
    global exsist
    exsist = os.path.isfile("student_record.json")

    while True:
        option = input("\n1. Add Student\n2. View Student Record\n0. Exit\nYour Option: ")
        if option == "1":
            add_student()
        elif option == "2":
            view_student()
        elif option == "0":
            print("Thank you for using the program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
