def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

def main():
    try:
        shape = input("Enter :(triangle/circle/rectangle): ").lower()

        if shape == "triangle":
            base = float(input("Enter the base length of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = calculate_triangle_area(base, height)
        elif shape == "circle":
            radius = float(input("Enter the radius of the circle: "))
            area = calculate_circle_area(radius)
        elif shape == "rectangle":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = calculate_rectangle_area(length, width)
        else:
            print("Invalid shape entered.")
            return

        print("Area:", area)

        if area > 10:
            print("Area is bigger than 10.")
        elif area < 10:
            print("Area is smaller than 10.")
        else:
            print("Area is 10.")

    except ValueError:
        print("Invalid inputs.")
