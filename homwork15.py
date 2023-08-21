user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_dob = input("Enter your date of birth (YYYY-MM-DD): ")


with open("user_info.txt", "w") as file:
    file.write(f"User Name: {user_name}\n")
    file.write(f"Age: {user_age}\n")
    file.write(f"Date of Birth: {user_dob}\n")

print("User information has been saved to 'user_info.txt'.")






