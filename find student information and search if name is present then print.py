#Create a dictionary to represent a student's information


students_info = {
    'Priyesh': {'age': 23, 'grade': 'A'},
    'Aditya': {'age': 22, 'grade': 'B'},
    'Priya': {'age': 21, 'grade': 'C'}
}
name = input("Enter the student's name: ")
if name in students_info:
    print(students_info[name])
else:
    print("Student not found.")
