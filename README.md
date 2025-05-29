**_Animal Facts Explorer 🐾**_

A Python project that fetches and displays animal facts using the API Ninjas API.

**📌 Project Description**

This project lets users search for animals (e.g., "Fox," "Tiger") and displays following info in a clean HTML format:

* Scientific name
* Diet
* Habitat
* Taxonomy

🚀 **Installation**

- Clone the repository

- Set up environment:

- Create a .env file:

API_NINJAS_KEY=<your_api_key_here>

- Get a free API key from API Ninjas.

- Install dependencies:

_pip install -r requirements.txt_

🛠 **Usage**

1. Run the Script

_python animals_web_generator.py_

Enter an animal name when prompted (e.g., "Fox").

2. Output

Generates an animals.html file with facts.

3. Error Handling

Invalid animal name: Shows The animal "XYZ" doesn't exist.

API errors: Displays Failed to connect to the API: [error].

📜 **License**

MIT License. See LICENSE.