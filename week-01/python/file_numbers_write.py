FILE_NAME = "numbers.txt"

try:
    with open(FILE_NAME, "w") as file_handle:

        number1 = int(input("Enter a whole number: "))
        number2 = int(input("Enter a whole number: "))
        number3 = int(input("Enter a whole number: "))

        file_handle.write(f"{number1}\n")
        file_handle.write(f"{number2}\n")
        file_handle.write(f"{number3}\n")

        print("Data written successfully.")


except Exception as e:
    print(f"Bro, u had an error. {e}")