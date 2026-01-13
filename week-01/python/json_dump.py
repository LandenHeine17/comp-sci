import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)

print(json_string)

numbers = [2, 3, 4, 6, 7, 67]

FILENAME = "numbers.json"

try: 
    with open(FILENAME, "w") as file_handle:
        json.dump(numbers, file_handle)
    
    print("Successfully dumped")

except Exception as e:
    print(f"A file exception occurred. {e}")
