# main.py
#none of the handling errors are done right
from mathematics import whoami as math_whoami
from mathematics.numbers import whoami as num_whoami
from mathematics.numbers import series, simple
from mathematics.geometry import whoami as geo_whoami
from mathematics.geometry import circle, cube, rectangle

def main():
    print(math_whoami.getname())  # Output: mathematics
    print(num_whoami.getname())    # Output: mathematics.numbers
    print(geo_whoami.getname())    # Output: mathematics.geometry

    # Test series
    values = [1, 2, 3, 4, 5]
    print(f"Sum: {series.total_sum(number_list=values)}")             # Output: 15
    print(f"Average: {series.average(number_list=values)}")     # Output: 3.0

    # Test simple operations
    print(f"Addition: {simple.addition(left=5, right=3)}")  # Output: 8
    print(f"Subtraction: {simple.subtraction(left=5, right=3)}")  # Output: 2
    print(f"Multiplication: {simple.multiplication(left=5, right=3)}")  # Output: 15
    print(f"Division: {simple.division(left=6, right=3)}")  # Output: 2.0

    # Test geometry
    print(f"Circle Area: {circle.area(radius=5)}")             # Output: 78.53981633974483
    print(f"Circle Circumference: {circle.circumference(radius=5)}")  # Output: 31.41592653589793
    print(f"Cube Volume: {cube.volume(side=3)}")               # Output: 27
    print(f"Cube Surface Area: {cube.surface_area(side=3)}")   # Output: 54
    print(f"Rectangle Area: {rectangle.area(length=5, width=3)}")  # Output: 15
    print(f"Rectangle Perimeter: {rectangle.perimeter(length=5, width=3)}")  # Output: 16

if __name__ == "__main__":
    main()

