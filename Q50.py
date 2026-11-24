# Package layout example:
# student_package/
#   __init__.py
#   module1.py (define add(a,b))
#   module2.py (define multiply(a,b))
try:
    from student_package.module1 import add
    from student_package.module2 import multiply
    print("Sum:", add(4, 5))
    print("Product:", multiply(4, 5))
except ImportError:
    print("Create the student_package folder and its two modules as shown in the comments.")
