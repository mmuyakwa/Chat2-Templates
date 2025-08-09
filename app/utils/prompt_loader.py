import os
import re

def load_prompts(prompts_directory):
    """
    Loads all markdown prompts from a given directory path.
    This function is now independent of Flask.
    """
    prompts = {}
    if not prompts_directory or not os.path.exists(prompts_directory):
        print(f"Warning: Prompts directory not found at '{prompts_directory}'")
        return prompts

    # Get a sorted list of filenames
    sorted_filenames = sorted(os.listdir(prompts_directory))

    for filename in sorted_filenames:
        if filename.endswith(".md"):
            filepath = os.path.join(prompts_directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                prompt_name = os.path.splitext(filename)[0]
                cleaned_name = re.sub(r'^\d{2}_', '', prompt_name)
                prompts[cleaned_name] = f.read()
                
    return prompts