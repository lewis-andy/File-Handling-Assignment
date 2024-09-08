

# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("This is the second line, with a number: 42\n")
        file.write("Finally, this is the third line.\n")
    print("File created and initial content written successfully.")

except (PermissionError, IOError) as e:
    print(f"Error writing to file: {e}")

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nFile contents:")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error reading file: {e}")

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Appending a new line of text.\n")
        file.write("Another line added to the end of the file.\n")
        file.write("And one more line to finish up.\n")
    print("\nAdditional content appended successfully.")

except (PermissionError, IOError) as e:
    print(f"Error appending to file: {e}")

# Final file read to display appended content
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nUpdated file contents:")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error reading file: {e}")

finally:
    print("\nFile handling operations are complete.")
