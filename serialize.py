import json

FILENAME = "Landen-info.txt"

def write():

    personal_info = {
        "name": {
            "First":"Landen",
            "Last":"Heine"
        },
        "sports":["Tennis", "Swim", "Track"],
        "social_security_number": "Just kidding, I won't put that"
    }

    # I left this because it is worth noting
    # it "double encodes" it when I do json.dump(json_string)
    # and if I look at the json file with cat, I can see it is
    # not the expected json object
    json_string = json.dumps(personal_info)

    try:
        with open(FILENAME, "w") as file_handle:
            json.dump(personal_info, file_handle)
        
        print("json dump successful!")

    except Exception as e:
        print(f"Something went wrong, information did not write. {e}")

def read():

    try:
        with open(FILENAME) as file_handle:
            personal_info = json.load(file_handle)

        print(personal_info)
    
    except Exception as e:
        print(f"Something went wrong, Information did not read. {e}")

if __name__ == "__main__":
    write()
    read()