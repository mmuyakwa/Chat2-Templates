# 🚀 AI Query Assistant 🤖

A sleek and powerful Flask-based web application that serves as a dynamic interface for various AI models from OpenRouter. Customize your AI interactions with dynamic prompt templates and enjoy a clean, responsive UI.

---

## ✨ Key Features

-   **🎨 Modern UI**: A clean, dark-themed, and responsive single-page application.
-   **🔄 Dynamic AI Models**: Fetches the latest available models from the OpenRouter API in real-time.
-   **📂 Dynamic Prompt Templates**: Automatically creates a selection menu from Markdown (`.md`) files in the `prompts` directory.
-   **🔢 Sorted & Cleaned Prompts**: Prompts are sorted alphabetically. Naming like `01_My_Prompt.md` is displayed cleanly as "My Prompt".
-   **✍️ Advanced Text Input**: A multi-line textarea that sends with `Cmd/Ctrl + Enter`.
-   **📄 Markdown Rendering**: Toggle between raw Markdown and a beautifully rendered HTML view for AI responses.
-   **🎨 Syntax Highlighting**: Code blocks in the rendered view are highlighted using Pygments.
-   **📋 Copy-to-Clipboard**: Easily copy raw Markdown or individual code snippets with a single click.
-   **🐳 Dockerized**: Comes with a multi-stage `Dockerfile` and `docker-compose.yaml` for easy, reproducible deployment.
-   **⚙️ Configurable**: Easily set your default AI model and API keys via an `.env` file.

---

## 🏁 Getting Started

Follow these steps to get the application up and running.

### 1. Prerequisites

-   [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)
-   OR a local Python environment with [uv](https://github.com/astral-sh/uv)

### 2. Configuration 🔑

The application uses an `.env` file for configuration.

1.  **Copy the Example:** If you don't have a `.env` file, rename `.env.example` to `.env`.
2.  **Edit `.env`:**
    ```dotenv
    # Your secret key from https://openrouter.ai/keys
    OPENROUTER_API_KEY=your_api_key_here

    # Set the default model to be selected on page load
    DEFAULT_MODEL=openai/gpt-4o-mini

    # It's recommended to change the Flask secret key
    SECRET_KEY=generate_a_new_strong_secret_key
    ```

### 3. Running the Application 🚀

You can run the app using either Docker (recommended) or a local Python environment.

#### Option A: With Docker (Recommended)

This is the easiest way to get started.

```bash
docker-compose up --build
```

The application will be available at 👉 **http://localhost:5004**

#### Option B: With a Local Python Environment (`uv`)

This is ideal for active development.

1.  **Create a virtual environment (once):**
    ```bash
    uv venv
    ```
2.  **Install dependencies in editable mode:**
    This command installs all dependencies from `pyproject.toml`, including development tools like `ruff`. The `-e` flag means your code changes are reflected immediately.
    ```bash
    uv pip install -e . --all-extras
    ```
3.  **Run the App:**
    ```bash
    uv run flask run
    ```

The application will be available at 👉 **http://localhost:5004**

## 🤖 CI & Automation

This project uses GitHub Actions to maintain code quality and keep dependencies up to date:

-   **CI & Linting**: On every push or pull request, a workflow automatically runs the `ruff` linter to check for code style issues and errors.
-   **Dependabot**: Automatically scans for outdated dependencies and creates pull requests to update them.
-   **Automerge**: Automatically merges Dependabot pull requests if all checks (like the linter) pass successfully.

---

## 📁 Project Structure

```
├── prompts/              # 📂 Add your .md prompt templates here!
├── app/
│   ├── routes/           #  Flask blueprints
│   ├── static/           # Static assets (currently unused)
│   ├── templates/        # HTML templates
│   ├── utils/            # Helper modules (prompt loader, model fetcher)
│   ├── app.py            # Flask application factory
│   └── config.py         # Configuration class
├── .dockerignore         # 🐳 Files to exclude from the Docker image
├── .gitignore            #  Git ignored files
├── docker-compose.yaml   # Docker Compose setup
├── Dockerfile            # Defines the Docker image
├── pyproject.toml        # 📦 Python project definition and dependencies
└── README.md             # 📄 This file
```

---

## 🛠️ How to Customize

### Adding New Prompts

Simply add a new Markdown file (`.md`) to the `app/prompts/` directory.

-   To **control the order**, prefix the filename with a number, e.g., `01_My_First_Prompt.md`.
-   The name in the dropdown will be automatically cleaned up (e.g., "My First Prompt").
-   The content of the file will be used as the **system prompt** for the AI.