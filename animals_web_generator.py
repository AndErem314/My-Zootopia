import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

data = load_data('animals_data.json')


def print_data_from_json(data):
    """Function take a loaded data from json file and print it"""
    for species in data:
        print(f"Name: {species['name']}")

        if 'characteristics' in species and 'diet' in species['characteristics']:
            print(f"Diet: {species['characteristics']['diet']}")

        if 'locations' in species and species['locations']:
            print(f"Location: {', '.join(species['locations'])}")

        if 'characteristics' in species and 'type' in species['characteristics']:
            print(f"Type: {species['characteristics']['type']}")
        print()
