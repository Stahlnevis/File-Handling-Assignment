def create_file():
    try:
        # Create a new text file named "my_file.txt" in write mode
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Line 1: Hello, world!\n")
            file.write("Line 2: 12345\n")
            file.write("Line 3: Python file handling is awesome!\n")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File creation process completed.")

def read_and_display():
    try:
        # Open "my_file.txt" in read mode
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        # Open "my_file.txt" in append mode
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("Line 4: Appending some more text!\n")
            file.write("Line 5: 54321\n")
            file.write("Line 6: Python file handling is versatile!\n")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File appending process completed.")

# Task 1: File Creation
create_file()

# Task 2: File Reading and Display
read_and_display()

# Task 3: File Appending
append_to_file()
