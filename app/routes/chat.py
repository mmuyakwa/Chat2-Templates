import requests
import markdown
from flask import Blueprint, render_template, current_app, request, jsonify
from app.extensions import socketio
from app.utils.prompt_loader import load_prompts
from app.utils.model_fetcher import get_available_models

chat_bp = Blueprint('chat_bp', __name__, template_folder='../../templates')

@chat_bp.route('/')
def chat_interface():
    """Renders the main chat interface."""
    # Get the prompts path from the current app's configuration
    prompts_path = current_app.config.get('PROMPTS_DIR')
    prompts = load_prompts(prompts_path)
    
    all_models = get_available_models()
    default_model = current_app.config.get('DEFAULT_MODEL', 'openrouter/auto')
    
    return render_template('chat_interface.html', 
                           prompts=prompts, 
                           models=all_models,
                           default_model=default_model)

@chat_bp.route('/render_markdown', methods=['POST'])
def render_markdown_route():
    """Renders markdown text to HTML on the server with syntax highlighting."""
    markdown_text = request.json.get('text', '')
    # Enable extensions for tables, fenced code blocks, and code highlighting
    html = markdown.markdown(
        markdown_text, 
        extensions=[
            'markdown.extensions.tables', 
            'markdown.extensions.fenced_code',
            'codehilite'
        ]
    )
    return jsonify({'html': html})

def call_openrouter_api(model, system_prompt, user_message):
    """Calls the OpenRouter API with a system and user message."""
    api_key = current_app.config['OPENROUTER_API_KEY']
    if not api_key:
        return "Error: OPENROUTER_API_KEY is not set."

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={"model": model, "messages": messages}
        )
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        print(f"API Error: {e}")
        return f"Error: Could not get a response from the AI. Details: {e}"

@socketio.on('send_message')
def handle_send_message(json_data):
    """Handles incoming chat messages."""
    user_message = json_data.get('message', '')
    system_prompt = json_data.get('system_prompt', 'You are a helpful assistant.') # Default prompt
    model = json_data.get('model', 'openrouter/auto')
    sid = request.sid
    
    print(f"SID {sid}: Received message for model {model}")
    
    app = current_app._get_current_object()

    def background_task():
        with app.app_context():
            response_message = call_openrouter_api(model, system_prompt, user_message)
            socketio.emit('ai_response', {'response': response_message}, to=sid)

    socketio.start_background_task(background_task)