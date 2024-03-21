# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Line 1: This is a string\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: 3.14159\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error creating file: {e}")
finally:
    print("File creation completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error reading file: {e}")
finally:
    print("File reading completed.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Appended string\n")
        file.write("Line 5: 67890\n")
        file.write("Line 6: 2.71828\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error appending to file: {e}")
finally:
    print("File appending completed.")
