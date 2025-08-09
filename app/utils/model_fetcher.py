import requests
import os

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

if __name__ == '__main__':
    # Example usage:
    available_models = get_available_models()
    if available_models:
        print(f"Successfully fetched {len(available_models)} models.")
        
        # Example of how you might access model details
        for model in available_models[:5]: # Print first 5 models
            print(f"- {model.get('name')} (ID: {model.get('id')})")

        compatible_models = filter_openrouter_models(available_models)
        print(f"\n{len(compatible_models)} models are considered compatible.")

    else:
        print("Could not fetch models from OpenRouter.")
