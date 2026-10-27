students = [] #list of all students

def add_student(name, age, department):
    student = {
        "name" : name,
        "age" : age,
        "department" : department
    }
    students.append(student)

add_student("Benjamin", 22, "Computer Science")
add_student("Michael", 19, "Mathematics")
add_student("Favour", 25, "Business Administration")
add_student("Essence", 19, "Physics")
add_student("Wisdom", 25, "Chemisty")

def show_all_students():
    for student in students:
        print(
            f'{student["name"]} - '
            f'{student["age"]} - '
            f'{student["department"]}'
        )

def search_for_student(name_1):
     for student in students:
          if student["name"].lower() == name_1.strip().lower():
               print("Student found:")
               print(f"Name: {student["name"]}")
               print(f"Age: {student["age"]}")
               print(f"Department: {student["department"]}")
               return
          
     print(f"Sorry, {name_1} was not found.")

#show_all_students()

search_for_student("Daniel")
search_for_student("FAVour")
