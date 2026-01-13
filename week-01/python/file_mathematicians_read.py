try:
    with open("mathematicians.txt", "r") as file_handle:
        lines = []
        for line in file_handle:
            lines.append(line)
    
    for mathematician in lines:
        print(mathematician.rstrip("\n"))
    print("File read successfully.")
except Exception as e:
    print(f"Bro, it didn't work: {e}")