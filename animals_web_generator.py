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
    """Generates HTML string with all animals' data as styled cards"""
    output = ""
    for species in data:
        # Start card
        output += '<li class="cards__item">\n'

        # Add title (name)
        if 'name' in species:
            output += f'  <div class="card__title">{species["name"]}</div>\n'

        # Start text paragraph
        output += '  <p class="card__text">\n'

        # Add diet if available
        if is_fields_available(species, 'characteristics', 'diet'):
            output += f'    <strong>Diet:</strong> {species["characteristics"]["diet"]}<br/>\n'

        # Add location if available
        if is_fields_available(species, 'locations'):
            locations = ', '.join(species['locations'])
            output += f'    <strong>Location:</strong> {locations}<br/>\n'

        # Add type if available
        if is_fields_available(species, 'characteristics', 'type'):
            output += f'    <strong>Type:</strong> {species["characteristics"]["type"]}<br/>\n'

        # Close text paragraph and card
        output += '  </p>\n'
        output += '</li>\n\n'

    return output


def read_template(file_path):
    """Reads the HTML template file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_html_file(content, output_file="animals.html"):
    """Writes the HTML content to a file"""
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)


def main():
    """The main function"""
    data = load_data('animals_data.json')
    animals_string = generate_animals_string(data)
    template = read_template("animals_template.html")
    new_content_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_string)
    write_html_file(new_content_html)


if __name__ == "__main__":
    main()