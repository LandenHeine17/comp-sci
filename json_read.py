import json
FILENAME = "numbers.json"

try:
    with open(FILENAME) as file_handle:
        numbers = json.load(file_handle)

    print(numbers)

except Exception as e:
    print(f"An exception occured, you gotta fix something. {e}")