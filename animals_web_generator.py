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


def generate_animals_string(data):
    """Generates a string with all animals' data"""
    output = ""
    for species in data:
        if 'name' in species:
            output += f"Name: {species['name']}\n"

        if is_fields_available(species, 'characteristics', 'diet'):
            output += f"Diet: {species['characteristics']['diet']}\n"

        if is_fields_available(species, 'locations'):
            output += f"Location: {', '.join(species['locations'])}\n"

        if is_fields_available(species, 'characteristics', 'type'):
            output += f"Type: {species['characteristics']['type']}\n"

        output += "\n"
    return output


def read_template(file_path):
    """Reads the HTML template file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    """The main function"""
    data = load_data('animals_data.json')

    generate_animals_string(data)

    template = read_template("animals_template.html")


if __name__ == "__main__":
    main()