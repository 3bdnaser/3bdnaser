def calculate_square_area(side):
    return side ** 2

def calculate_square_perimeter(side):
    return 4 * side

def main():
    try:
        side = float(input("Enter the length of the square's side: "))

        area = calculate_square_area(side)
        perimeter = calculate_square_perimeter(side)

        print("Area:", area)
        print("Perimeter:", perimeter)
