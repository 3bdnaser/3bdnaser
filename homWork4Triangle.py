import math

def calculate_triangle_area(s1,s2):

    return 0.5*s1*s2

def calculate_triangle_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter
s1=float(input("Enter the base:"))
s2=float(input("Enter the height:"))



side1 =float( input("Enter the length of the first side: "))
side2 =float( input("Enter the length of the second side: "))
side3 =float( input("Enter the length of the third side: "))

area = calculate_triangle_area(s1,s2)
perimeter = calculate_triangle_perimeter(side1, side2, side3)

print("Area:", area)
print("Perimeter:", perimeter)


def main():
    pass


if __name__ == "__main__":
    main()
