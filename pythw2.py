import json

def main():
    original_file = r"X:\File\Path\Goes\Here\CSC226\student.json"
    # Uncomment the next line to allow the user to specify the new file name and location
    # new_file = input("Please enter the path for the new JSON file: ")
    new_file = r"X:\File\Path\Goes\Here\CSC226\Newstudent.json"
    with open(original_file, "r") as f:
        ogfile_contents = f.read()
    data_dict = json.loads(ogfile_contents)
    data_dict["name"] = "Aleksandr"
    data_dict["email"] = "aleksandr.gritsayuk@gmail.com"
    with open(new_file, "w") as f:
        json.dump(data_dict, f) 
        #Could add indent for readibility, i.e. json.dump(data_dict, f, indent=4)

if __name__ == "__main__":
    main()

#I ran the program once with legitimate file paths to generate the Newstudent.json file.