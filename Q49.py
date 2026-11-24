# Create student_marks.py in this folder with a function such as:
# def percentage(marks):
#     return sum(marks) / len(marks)
try:
    from student_marks import percentage
    marks = list(map(float, input("Enter marks separated by spaces: ").split()))
    print("Percentage/average:", percentage(marks))
except ImportError:
    print("Create student_marks.py with percentage(marks) first.")
