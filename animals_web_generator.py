import json

def load_data(file):
    """ Loads a JSON file """
    with open(file, "r") as fileobj:
        return json.load(fileobj)


def is_fields_available(data, *keys):
    """Helper function to check if the searched field/parameters are existing in the data.
    If it exists return True."""
    new_data = data
    for key in keys:
        if key not in new_data:
            return False
        new_data = new_data[key]
    return True


def serialize_animal(species):
    """Serialize a single animal object to HTML card format"""
    output = ''
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{species["name"]}</div>\n'
    output += '  <div class="card__text">\n'
    output += '   <ul>\n'

    if is_fields_available(species, 'characteristics', 'diet'):
        output += f'    <li><strong>Diet:</strong> {species["characteristics"]["diet"]}</li>\n'

    if is_fields_available(species, 'locations'):
        location = species["locations"][0] if species["locations"] else ""
        output += f'    <li><strong>Location:</strong> {location}</li>\n'

    if is_fields_available(species, 'characteristics', 'type'):
        output += f'    <li><strong>Type:</strong> {species["characteristics"]["type"]}</li>\n'

    if is_fields_available(species, 'taxonomy', 'scientific_name'):
        output += f'    <li><strong>Latin name:</strong> <em>{species["taxonomy"]["scientific_name"]}</em></li>\n'

    output += '   </ul>\n'
    output += '  </div>\n'
    output += '</li>\n'
    return output


def generate_animals_html(data):
    """Generate complete HTML cards for all animals"""
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output


def read_template(file):
    """Reads the HTML template file."""
    with open(file, 'r', encoding='utf-8') as fileobj:
        return fileobj.read()


def write_html_file(content, output_file="animals.html"):
    """Writes the HTML content to a file"""
    with open(output_file, 'w', encoding='utf-8') as fileobj:
        fileobj.write(content)


def main():
    """The main function"""
    data = load_data('animals_data.json')
    animals_string = generate_animals_html(data)
    template = read_template("animals_template.html")
    new_content_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_string)
    write_html_file(new_content_html)


if __name__ == "__main__":
    main()