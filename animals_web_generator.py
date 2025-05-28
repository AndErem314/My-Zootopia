import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Constants
API_URL = "https://api.api-ninjas.com/v1/animals?name={}"
API_KEY = os.getenv("API_NINJAS_KEY")


def load_data_from_api(animal_name):
    """Loads animal data from API for the given name"""
    if not API_KEY:
        raise ValueError("API key not found. Please set API_NINJAS_KEY in .env file")

    try:
        response = requests.get(
            API_URL.format(animal_name),
            headers={'X-Api-Key': API_KEY},
            timeout=10
        )
        if response.status_code == requests.codes.ok:
            data = response.json()
            if not data:
                return {
                    'error': True,
                    'message': f'The animal "{animal_name}" doesn\'t exist.',
                    'animal_name': animal_name
                }
            return data
        return {
            'error': True,
            'message': f'API request failed (Status: {response.status_code}).',
            'animal_name': animal_name
        }

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


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
    data = load_data_from_api(animal_name)
    animals_html = generate_animals_html(data)
    template = read_template("animals_template.html")
    new_content_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)
    write_html_file(new_content_html)


if __name__ == "__main__":
    main()