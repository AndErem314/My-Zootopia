import data_fetcher


def serialize_animal(species):
    """Serialize a single animal object to HTML card format."""
    output = []
    output.append('<li class="cards__item">')
    output.append(f'  <div class="card__title">{species.get("name", "Unknown")}</div>')
    output.append('  <div class="card__text">')
    output.append('   <ul>')

    diet = species.get("characteristics", {}).get("diet")
    if diet:
        output.append(f'    <li><strong>Diet:</strong> {diet}</li>')

    locations = species.get("locations", [])
    if locations:
        output.append(f'    <li><strong>Location:</strong> {locations[0]}</li>')

    animal_type = species.get("characteristics", {}).get("type")
    if animal_type:
        output.append(f'    <li><strong>Type:</strong> {animal_type}</li>')

    scientific_name = species.get("taxonomy", {}).get("scientific_name")
    if scientific_name:
        output.append(f'    <li><strong>Latin name:</strong> <em>{scientific_name}</em></li>')

    output.append('   </ul>')
    output.append('  </div>')
    output.append('</li>')
    return '\n'.join(output)


def generate_animals_html(data):
    """Generate HTML cards for all animals."""
    if isinstance(data, dict) and data.get('error'):
        return f'<div class="error">{data["message"]}</div>'
    return ''.join(serialize_animal(animal) for animal in data)


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
    animal_name = input("Enter an animal name: ").strip()
    data = data_fetcher.fetch_data(animal_name)
    animals_html = generate_animals_html(data)
    template = read_template("animals_template.html")
    new_content_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)
    write_html_file(new_content_html)


if __name__ == "__main__":
    main()