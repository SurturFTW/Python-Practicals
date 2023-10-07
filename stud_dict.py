# Create a dictionary for 5 students
students = {
    'student1': {
        'name': 'ABC',
        'address': 'MU',
        'age': 18,
        'class': '11th',
        'marks': {
            'Mathematics': 85,
            'science': 92,
            'history': 78,
            'english': 88,
            'Drawing': 95
        }
    },
    
    'student2': {
        'name': 'DEF',
        'address': 'NA',
        'age': 17,
        'class': '6th',
        'marks': {
            'Mathematics': 90,
            'science': 88,
            'history': 76,
            'english': 91,
            'Drawing': 84
        }
    },
    
    'student3': {
        'name': 'GHI',
        'address': 'CH',
        'age': 19,
        'class': '10th',
        'marks': {
            'Mathematics': 78,
            'science': 85,
            'history': 92,
            'english': 80,
            'Drawing': 89
        }
    },

    'student4': {
        'name': 'JKL',
        'address': 'MP',
        'age': 17,
        'class': '8th',
        'marks': {
            'Mathematics': 92,
            'science': 84,
            'history': 76,
            'english': 90,
            'Drawing': 82
        }
    },
    
    'student5': {
        'name': 'MNO',
        'address': 'AG',
        'age': 18,
        'class': '9th',
        'marks': {
            'Mathematics': 88,
            'science': 90,
            'history': 85,
            'english': 87,
            'Drawing': 91
        }
    }
}

print("Details of All the Students :")
# Display the information for each student
for student_id, student_info in students.items():
    print(f"Student ID: {student_id}")
    print(f"Name: {student_info['name']}")
    print(f"Address: {student_info['address']}")
    print(f"Age: {student_info['age']}")
    print(f"Class: {student_info['class']}")
    print("Marks:")

for subject, marks in student_info['marks'].items():
    print(f"{subject}: {marks}")
    print()

# Search for a student by ID
search_id = 'student3'
if search_id in students:
    print(f"Student ID: {search_id}")
    student_info = students[search_id]
    print(f"Name: {student_info['name']}")
else:
    print(f"Student with ID '{search_id}' not found")

# Delete a student by ID
delete_id = 'student4'
if delete_id in students:
    del students[delete_id]
    print(f"Student with ID '{delete_id}' deleted from the dictionary")
else:
    print(f"Student with ID '{delete_id}' not found in the dictionary")
