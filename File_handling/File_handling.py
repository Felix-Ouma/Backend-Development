try:
    with open('test.txt', 'r') as file:
        file.writelines(["Hello this is a new file created", "\nThis is now another line of the codes"])
except FileNotFoundError as e:
    print("File is not found", e)