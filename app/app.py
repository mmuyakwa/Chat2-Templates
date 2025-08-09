import os
from flask import Flask, render_template
from dotenv import load_dotenv

def create_app():
    """
    Creates and configures the Flask application.
    """
    # Load environment variables
    load_dotenv()

    # Initialize Flask App
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('app.config.Config')

    # Initialize extensions
    from .extensions import socketio
    socketio.init_app(app)

    # Import and register blueprints
    from .routes.chat import chat_bp
    app.register_blueprint(chat_bp)

    # Register the main index route to redirect to chat
    @app.route('/')
    def index():
        """Redirect to the main chat interface."""
        return redirect(url_for('chat_bp.chat_interface'))

    return app

if __name__ == '__main__':
    # This block is for direct execution, e.g., `python app/app.py`
    # For development, `flask run` is preferred.
    app = create_app()
    from app.extensions import socketio
    socketio.run(app, debug=app.config['DEBUG'], host='0.0.0.0', port=5000)