import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def is_fields_available(data, *keys):
    """Helper function to check if the searched field/parameters are existing in the data.
    If it exists return True."""
    new_data = data
    for key in keys:
        if key not in new_data:
            return False
        new_data = new_data[key]
    return True


def print_data_from_json(data):
    """Function take a loaded data from json file and print all fields, if they are existing"""
    for species in data:

        if 'name' in species:
            print(f"Name: {species['name']}")

        if is_fields_available(species, 'characteristics', 'diet'):
            print(f"Diet: {species['characteristics']['diet']}")

        if is_fields_available(species, 'locations'):
            print(f"Location: {', '.join(species['locations'])}")

        if is_fields_available(species, 'characteristics', 'type'):
            print(f"Type: {species['characteristics']['type']}")

        print()


def main():
    data = load_data('animals_data.json')
    print_data_from_json(data)


if __name__ == "__main__":
    main()