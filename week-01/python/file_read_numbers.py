FILE_NAME = "numbers.txt"

try:
    with open(FILE_NAME, "r") as file_handle:
        
        numbers = []

        for line in file_handle:
            numbers.append(int(line))
        
        total = sum(numbers)

        print("The numbers are: ", end="")

        for number in numbers:
            print(f"{number} ", end="")
        
        print(f"\nThe total is: {total}")


except Exception as e:
    print(f"Bro, u had an error. {e}")