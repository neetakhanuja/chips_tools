import json

# Load and validate the JSON file to check if everything is correct
try:
    with open("data/nkhanuja_cc1.json", "r") as file:
        data = json.load(file)
    print("✅ JSON is correctly formatted!")

    # Print a summary of level data
    for level in data["level_pack"]["levels"]:
        print(f"\n🔹 Level {level['level_number']}:")
        print(f"   - Time Limit: {level['time']} seconds")
        print(f"   - Chips Required: {level['chip_count']}")
        print(f"   - Password: {level['optional_fields']['password']}")
        print(f"   - Monsters at: {level['optional_fields']['monsters']}")
except json.JSONDecodeError as e:
    print(f"❌ JSON Error: {e}")
except KeyError as k:
    print(f"❌ Key Error: Missing key {k}")
