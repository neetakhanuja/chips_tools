import json

# Define a class to represent a Game
class Game:
    def __init__(self, title, year, platform):
        self.title = title
        self.year = year
        self.platform = platform

    def __str__(self):
        return f"Title: {self.title}, Year: {self.year}, Platform: {self.platform['name']} ({self.platform['launch_year']})"

# Define a class to represent the Game Library
class GameLibrary:
    def __init__(self, games):
        self.games = [Game(game["title"], game["year"], game["platform"]) for game in games]

    def __str__(self):
        return "\n".join(str(game) for game in self.games)

# Load the JSON file
with open("data/test_data.json", "r") as file:
    data = json.load(file)

# Convert JSON data to a GameLibrary object
game_library = GameLibrary(data["games"])

# Print the game library
print(game_library)
