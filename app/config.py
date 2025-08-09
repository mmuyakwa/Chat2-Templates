import os

class Config:
    """
    Application configuration class.
    Loads settings from environment variables.
    """
    # --- General Config ---
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-should-really-change-this')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')

    # --- API Keys ---
    OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')

    # --- Application-Specific Settings ---
    DEFAULT_MODEL = os.environ.get('DEFAULT_MODEL', 'openrouter/auto')
    # Path to the prompts directory.
    # For Docker, this is the root 'prompts' dir inside the container.
    # For local dev, it's overridden by PROMPTS_PATH in the .env file.
    PROMPTS_DIR = os.environ.get('PROMPTS_PATH', 'prompts')
    DATA_DIR = os.environ.get('DATA_DIR', 'app/data')
    
    # --- Network Scanner ---
    DEFAULT_NETWORK_RANGE = os.environ.get('DEFAULT_NETWORK_RANGE', '192.168.1.0/24')