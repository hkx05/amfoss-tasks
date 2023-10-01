from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication, QVBoxLayout, QMainWindow, QDialog
from PySide6.QtGui import QPixmap, QFont
import requests
import sys
from PySide6.QtCore import Qt

class DisplayWindow(QDialog):
    def __init__(self, captured_pokemons):
        super().__init__()
        self.setWindowTitle("Captured Pokémon")
        self.setGeometry(100, 100, 400, 400)

        self.captured_pokemons = captured_pokemons
        self.current_pokemon_index = 0

        self.pokemon_name_label = QLabel("", self)
        self.pokemon_name_label.setGeometry(20, 20, 300, 40)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pokemon_name_label.setFont(font)

        self.pokemon_image_label = QLabel(self)
        self.pokemon_image_label.setGeometry(20, 70, 250, 250)

        self.previous_button = QPushButton("Previous", self)
        self.previous_button.setGeometry(20, 330, 80, 30)
        self.previous_button.clicked.connect(self.show_previous_pokemon)

        self.next_button = QPushButton("Next", self)
        self.next_button.setGeometry(100, 330, 80, 30)
        self.next_button.clicked.connect(self.show_next_pokemon)

        self.show_pokemon()

    def show_pokemon(self):
        if self.current_pokemon_index >= 0 and self.current_pokemon_index < len(self.captured_pokemons):
            pokemon_data = self.captured_pokemons[self.current_pokemon_index]
            self.pokemon_name_label.setText(pokemon_data['name'])
            pixmap_url = pokemon_data['sprites']['front_default']
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(pixmap_url).content)
            self.pokemon_image_label.setPixmap(pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio))

    def show_previous_pokemon(self):
        self.current_pokemon_index -= 1
        if self.current_pokemon_index < 0:
            self.current_pokemon_index = len(self.captured_pokemons) - 1
        self.show_pokemon()

    def show_next_pokemon(self):
        self.current_pokemon_index += 1
        if self.current_pokemon_index >= len(self.captured_pokemons):
            self.current_pokemon_index = 0
        self.show_pokemon()

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850, 500)
        self.setWindowTitle("Pokémon Data Viewer")

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 280, 40)

        label1 = QLabel("Enter a Pokémon's name", self)
        label1.setGeometry(50, 5, 600, 70)

        search_button = QPushButton("Search", self)
        search_button.setGeometry(50, 300, 160, 43)
        search_button.clicked.connect(self.fetch_pokemon_data)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capture_pokemon)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.display_captured_pokemon)

        self.pokemon_name_label = QLabel("Name:", self)
        self.pokemon_name_label.setGeometry(350, 20, 300, 40)

        self.pokemon_image_label = QLabel(self)
        self.pokemon_image_label.setGeometry(350, 50, 250, 250)

        self.pokemon_info_label = QLabel(self)
        self.pokemon_info_label.setGeometry(350, 280, 500, 200)

        label_font = QFont()
        label_font.setPointSize(14)
        label_font.setBold(True)
        self.pokemon_name_label.setFont(label_font)
        self.pokemon_info_label.setFont(label_font)

        self.captured_pokemons = []

    def fetch_pokemon_data(self):
        pokemon_name = self.textbox.text().strip().lower()
        if pokemon_name:
            api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                self.pokemon_name_label.setText(f"Name: {data['name']}")
                pixmap_url = data['sprites']['front_default']
                pixmap = QPixmap()
                pixmap.loadFromData(requests.get(pixmap_url).content)
                self.pokemon_image_label.setPixmap(pixmap)
                abilities = [ability['ability']['name'] for ability in data['abilities']]
                types = [type['type']['name'] for type in data['types']]
                stats = [f"{stat['stat']['name']}: {stat['base_stat']}" for stat in data['stats']]
                formatted_stats = '\n'.join(stats)
                self.pokemon_info_label.setText(f"Abilities: {', '.join(abilities)}\nTypes: {', '.join(types)}\nStats:\n{formatted_stats}")
            else:
                self.pokemon_name_label.setText("Pokemon not found")
                self.pokemon_image_label.clear()
                self.pokemon_info_label.clear()
        else:
            self.pokemon_name_label.setText("Please enter a Pokemon name")
            self.pokemon_image_label.clear()
            self.pokemon_info_label.clear()

    def capture_pokemon(self):
        pokemon_name = self.textbox.text().strip().lower()
        if pokemon_name:
            api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                self.captured_pokemons.append(data)
                self.textbox.clear()
                self.pokemon_name_label.clear()
                self.pokemon_image_label.clear()
                self.pokemon_info_label.clear()
            else:
                self.pokemon_name_label.setText("Pokemon not found")
                self.pokemon_image_label.clear()
                self.pokemon_info_label.clear()
        else:
            self.pokemon_name_label.setText("Please enter a Pokemon name")
            self.pokemon_image_label.clear()
            self.pokemon_info_label.clear()

    def display_captured_pokemon(self):
        if self.captured_pokemons:
            display_window = DisplayWindow(self.captured_pokemons)
            display_window.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
