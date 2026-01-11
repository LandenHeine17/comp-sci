try:
    with open("mathematicians.txt", "w") as file_handle:
        file_handle.write("Freidrich Gauss\n")
        file_handle.write("Leonard Euler\n")
        file_handle.write("Isaac Newton\n")
        file_handle.write("Landen Heine\n")

    print("File written successfully.")

except Exception as e:
    print(f"Bro, it didn't work: {e}")