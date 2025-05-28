import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Constants
API_URL = "https://api.api-ninjas.com/v1/animals?name={}"
API_KEY = os.getenv("API_NINJAS_KEY")


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
       ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
          ...
        }
    },
    """
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
