Animal Facts Explorer 🐾

A Python project that fetches and displays animal facts using the API Ninjas API.

📌 Project Description

This project lets users search for animals (e.g., "Fox," "Tiger") and displays their:

Scientific name
Diet
Habitat
Taxonomy
in a clean HTML format.

🚀 Installation

# Clone the repository

# Set up environment:

- Create a .env file:

API_NINJAS_KEY=your_api_key_here

- Get a free API key from API Ninjas.

# Install dependencies:

pip install -r requirements.txt

🛠 Usage

1. Run the Script


python animals_web_generator.py

Enter an animal name when prompted (e.g., "Fox").

2. Output

Generates an animals.html file with facts.

Example output for "Fox":

<li class="cards__item">
  <div class="card__title">Red Fox</div>
  <div class="card__text">
    <ul>
      <li><strong>Diet:</strong> Omnivore</li>
      <li><strong>Location:</strong> North America</li>
      <li><strong>Latin name:</strong> <em>Vulpes vulpes</em></li>
    </ul>
  </div>
</li>

3. Error Handling

Invalid animal name: Shows The animal "XYZ" doesn't exist.

API errors: Displays Failed to connect to the API: [error].

📜 License

MIT License. See LICENSE.