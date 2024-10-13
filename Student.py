class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        """Compare if two students are equal based on their names."""
        return self.name == other.name

    def __lt__(self, other):
        """Compare if one student's name is less than another student's name."""
        return self.name < other.name

    def __ge__(self, other):
        """Compare if one student's name is greater than or equal to another student's name."""
        return self.name >= other.name

def main():
    # Create some Student objects
    student1 = Student("Alice")
    student2 = Student("Bob")
    student3 = Student("Alice")

    # Test for equality
    print(f"Is {student1.name} equal to {student2.name}? {student1 == student2}")
    print(f"Is {student1.name} equal to {student3.name}? {student1 == student3}")

    # Test for less than
    print(f"Is {student1.name} less than {student2.name}? {student1 < student2}")
    print(f"Is {student2.name} less than {student1.name}? {student2 < student1}")

    # Test for greater than or equal to
    print(f"Is {student1.name} greater than or equal to {student2.name}? {student1 >= student2}")
    print(f"Is {student1.name} greater than or equal to {student3.name}? {student1 >= student3}")

if __name__ == "__main__":
    main()