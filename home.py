def main():
    num_students = int(input("Enter the number of students: "))

    for student in range(1, num_students + 1):
        num_marks = int(input(f"Enter the number of marks for student {student}: "))
        marks = []

        for mark_num in range(1, num_marks + 1):
            mark = float(input(f"Enter mark {mark_num} for student {student}: "))
            marks.append(mark)

        average = sum(marks) / num_marks
        max_mark = max(marks)
        min_mark = min(marks)

        print(f"Student {student}:")
        print(f"Average: {average:.2f}")
        print(f"Max Mark: {max_mark}")
        print(f"Min Mark: {min_mark}")
        print()

if __name__ == "__main__":
    main()
