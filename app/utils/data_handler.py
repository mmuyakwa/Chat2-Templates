import json
import os

DATA_DIRECTORY = "app/data"

def ensure_data_directory():
    """Ensures the data directory exists."""
    if not os.path.exists(DATA_DIRECTORY):
        os.makedirs(DATA_DIRECTORY)

def save_data(filename, data):
    """
    Saves data to a JSON file.

    Args:
        filename (str): The name of the file (e.g., 'ideas.json').
        data (dict or list): The data to save.

    Returns:
        bool: True if successful, False otherwise.
    """
    ensure_data_directory()
    filepath = os.path.join(DATA_DIRECTORY, filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError) as e:
        print(f"Error saving data to {filepath}: {e}")
        return False

def load_data(filename):
    """
    Loads data from a JSON file.

    Args:
        filename (str): The name of the file (e.g., 'ideas.json').

    Returns:
        dict or list: The loaded data, or an empty dictionary if the file doesn't exist or is invalid.
    """
    ensure_data_directory()
    filepath = os.path.join(DATA_DIRECTORY, filename)
    if not os.path.exists(filepath):
        return {}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading data from {filepath}: {e}")
        return {}

if __name__ == '__main__':
    # Example usage:
    
    # 1. Save some sample data
    ideas_data = {
        "ideas": [
            {"id": 1, "title": "Multi-Dashboard App", "description": "A cool app with many dashboards."},
            {"id": 2, "title": "AI-Powered Code Generator", "description": "Generate code from natural language."}
        ]
    }
    print("Saving sample ideas data...")
    save_success = save_data("ideas.json", ideas_data)
    if save_success:
        print("Data saved successfully.")

    # 2. Load the data back
    print("\nLoading ideas data...")
    loaded_ideas = load_data("ideas.json")
    if loaded_ideas:
        print("Loaded data:")
        print(json.dumps(loaded_ideas, indent=2))
    else:
        print("Could not load data.")

    # 3. Example with a different dataset
    stocks_data = {"portfolios": [{"name": "Tech Growth", "stocks": ["AAPL", "GOOGL", "MSFT"]}]}
    save_data("stocks.json", stocks_data)
    loaded_stocks = load_data("stocks.json")
    print("\nLoaded stocks data:")
    print(json.dumps(loaded_stocks, indent=2))
