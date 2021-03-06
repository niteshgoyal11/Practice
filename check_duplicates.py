#
# Your previous Plain Text content is preserved below:
#
# This is just a simple shared plaintext pad, with no execution capabilities.
#
#
# Enjoy your interview!
#
# Problem Statement:
# -----
#
# Below is a piece of code which we want to run to get the output similar to as mentioned after the code as comment.
# Read the code and understand the requirement.
# Write all the required code which is missing here. Don;t
# The code will be evaluated on below aspects:
# 1. Output correctness.
# 2. Usage of OOPs concepts
# 3. Code should be divided in smaller and meaningfull modules.
# 4. Code should be self understandable. No comments are required. No docstrings required.
# 4. No code changes should be made to the code provided here.
# 5. Python coding standards should be maintained.
# 6. Time elapsed to complet. the code.
#
# Brief intro:
# There are students and there is professor. Professor include students in his subject lecture.
# Students will get only those assignments which are floated after their admission.

### Best of Luck!!!


###### Your code starts here ######

class Assignment:

    def __init__(self,assignment_name):
        self.assignment_name = assignment_name


class Student:

    def __init__(self,student_name):
        self.student_name = student_name

    def retreive_details(self):
        new_lis = []
        for key in self.total_students:
            new_str = f"{key}:{self.total_students[key]}"
            new_lis.append(new_str)
        return new_lis


class Professor(Student):

    def __init__(self, prof_name):
        self.prof_name = prof_name
        self.total_students = {}


    def add_students(self, student_obj):
        self.total_students[student_obj.student_name] = [list]

    def float_assignment(self,assignment_obj):
        for key in self.total_students.keys():
            self.total_students[key] = self.total_students[key].append(assignment_obj.assignment_name)





###### Your code ends here ######


if __name__ == "__main__":
    my_prof = Professor("Prof. Ajit Singh")

    students = [
        Student("Nikhil"),
        Student("Suresh"),
        Student("Aaditya"),
        Student("Ajay"),
    ]

    my_prof.add_students(students[0])
    my_prof.add_students(students[1])

    my_prof.float_assignment(Assignment("Motion"))
    my_prof.float_assignment(Assignment("Thermodynamics"))

    my_prof.add_students(students[2])
    my_prof.float_assignment(Assignment("Quantam Physics"))

    my_prof.add_students(students[3])
    my_prof.float_assignment(Assignment("Heat"))

    for stud in students:
        print(stud)

    """
    The output should be in below format:

    Nikhil: Motion, Thermodynamics, Quantam Physics, Heat
    Suresh: Motion, Thermodynamics, Quantam Physics, Heat
    Aaditya: Quantam Physics, Heat
    Ajay: Heat

    """
#