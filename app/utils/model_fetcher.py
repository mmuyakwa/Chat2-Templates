import requests

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/models"

def get_available_models():
    """
    Fetches the list of available models from the OpenRouter API.

    Returns:
        list: A list of model dictionaries, or an empty list if the request fails.
    """
    try:
        response = requests.get(OPENROUTER_API_URL)
        response.raise_for_status()  # Raise an exception for bad status codes
        models_data = response.json()
        return models_data.get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching models from OpenRouter: {e}")
        return []
