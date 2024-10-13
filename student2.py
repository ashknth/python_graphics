import random

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, ID: {self.student_id})"

    def __lt__(self, other):
        """Compare students based on their names."""
        return self.name < other.name

def main():
    # Create a list of Student objects with different names
    students = [
        Student("Alice", 20, 1001),
        Student("Bob", 22, 1002),
        Student("Charlie", 21, 1003),
        Student("David", 19, 1004),
        Student("Eve", 23, 1005)
    ]

    # Shuffle the list of students
    random.shuffle(students)

    # Display the shuffled list
    print("Shuffled List of Students:")
    for student in students:
        print(student)

    # Sort the list of students
    students.sort()

    # Display the sorted list
    print("\nSorted List of Students:")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()