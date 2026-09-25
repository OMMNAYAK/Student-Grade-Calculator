"""
Student Grade & Average Calculator

A Python module to manage student academic records, calculate subject averages,
and generate performance reports using Object-Oriented Programming (OOP).
"""

class Student:
    # Class Attribute
    college_name = "Institute of Technology"
    
    def __init__(self, name: str, marks: list[float]):
        """
        Initialize a new Student object.
        
        :param name: Student's full name
        :param marks: List of marks obtained in subjects
        """
        self.name = name
        self.marks = marks

    def calculate_average(self) -> float:
        """Calculates and returns the average marks."""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def get_grade(self) -> str:
        """Determines the performance grade based on average score."""
        avg = self.calculate_average()
        if avg >= 90:
            return "A+ (Outstanding)"
        elif avg >= 80:
            return "A (Excellent)"
        elif avg >= 70:
            return "B (Good)"
        elif avg >= 60:
            return "C (Satisfactory)"
        elif avg >= 50:
            return "D (Pass)"
        else:
            return "F (Fail)"

    def display_report(self):
        """Displays formatted student performance report."""
        avg = self.calculate_average()
        grade = self.get_grade()
        print("=" * 45)
        print(f"  STUDENT REPORT CARD - {Student.college_name}")
        print("=" * 45)
        print(f" Student Name : {self.name}")
        print(f" Marks        : {self.marks}")
        print(f" Average Score: {avg:.2f}")
        print(f" Grade        : {grade}")
        print("=" * 45 + "\n")

    @staticmethod
    def welcome_message():
        """Static utility method to print portal welcome message."""
        print("--- Student Performance Management Portal ---")


if __name__ == "__main__":
    Student.welcome_message()
    print()

    # Sample Student Entities
    student1 = Student("Omm Nayak", [92.5, 88.0, 95.0])
    student2 = Student("Rahul Sharma", [75.0, 82.5, 68.0])
    student3 = Student("Priya Singh", [55.0, 62.0, 58.5])

    # Display Reports
    student1.display_report()
    student2.display_report()
    student3.display_report()
