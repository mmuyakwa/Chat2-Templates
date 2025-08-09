# 🚀 AI Query Assistant 🤖

Eine elegante und leistungsstarke Flask-basierte Webanwendung, die als dynamisches Interface für verschiedene KI-Modelle von OpenRouter dient. Passen Sie Ihre KI-Interaktionen mit dynamischen Prompt-Vorlagen an und genießen Sie eine saubere, responsive Benutzeroberfläche.

---

## ✨ Hauptmerkmale

-   **🎨 Modernes UI**: Eine saubere, dunkle und responsive Single-Page-Anwendung.
-   **🔄 Dynamische KI-Modelle**: Ruft die neuesten verfügbaren Modelle von der OpenRouter-API in Echtzeit ab.
-   **📂 Dynamische Prompt-Vorlagen**: Erstellt automatisch ein Auswahlmenü aus den Markdown-Dateien (`.md`) im `prompts`-Verzeichnis.
-   **🔢 Sortierte & bereinigte Prompts**: Die Prompts werden alphabetisch sortiert. Namen wie `01_Mein_Prompt.md` werden sauber als "Mein Prompt" angezeigt.
-   **✍️ Erweiterte Texteingabe**: Ein mehrzeiliges Textfeld, das mit `Cmd/Ctrl + Enter` sendet.
-   **📄 Markdown-Rendering**: Wechseln Sie zwischen rohem Markdown und einer ansprechend gerenderten HTML-Ansicht für die KI-Antworten.
-   **🎨 Syntax-Highlighting**: Codeblöcke in der gerenderten Ansicht werden mit Pygments farblich hervorgehoben.
-   **📋 In die Zwischenablage kopieren**: Kopieren Sie einfach rohes Markdown oder einzelne Code-Snippets mit einem Klick.
-   **🐳 Docker-Unterstützung**: Inklusive `Dockerfile` und `docker-compose.yaml` für eine einfache, reproduzierbare Bereitstellung.
-   **⚙️ Konfigurierbar**: Legen Sie Ihr Standard-KI-Modell und Ihre API-Schlüssel einfach über eine `.env`-Datei fest.

---

## 🏁 Erste Schritte

Folgen Sie diesen Schritten, um die Anwendung zum Laufen zu bringen.

### 1. Voraussetzungen

-   [Docker](https://www.docker.com/get-started) und [Docker Compose](https://docs.docker.com/compose/install/)
-   ODER eine lokale Python-Umgebung mit [uv](https://github.com/astral-sh/uv)

### 2. Konfiguration 🔑

Die Anwendung verwendet eine `.env`-Datei für die Konfiguration.

1.  **Beispiel kopieren:** Falls Sie keine `.env`-Datei haben, benennen Sie `.env.example` in `.env` um.
2.  **`.env`-Datei bearbeiten:**
    ```dotenv
    # Ihr geheimer API-Schlüssel von https://openrouter.ai/keys
    OPENROUTER_API_KEY=ihr_api_schlüssel_hier

    # Legt das Standardmodell fest, das beim Laden der Seite ausgewählt wird
    DEFAULT_MODEL=openai/gpt-4o-mini

    # Es wird empfohlen, den Flask Secret Key zu ändern
    SECRET_KEY=generieren_sie_einen_neuen_starken_schlüssel
    ```

### 3. Anwendung starten 🚀

Sie können die App entweder mit Docker (empfohlen) oder einer lokalen Python-Umgebung starten.

#### Option A: Mit Docker (Empfohlen)

Dies ist der einfachste Weg, um loszulegen.

```bash
docker-compose up --build
```

Die Anwendung ist dann erreichbar unter 👉 **http://localhost:5004**

#### Option B: Mit einer lokalen Python-Umgebung (`uv`)

Dies ist ideal für die aktive Entwicklung.

1.  **Virtuelle Umgebung erstellen (einmalig):**
    ```bash
    uv venv
    ```
2.  **Abhängigkeiten im "Editable"-Modus installieren:**
    Dieser Befehl installiert alle Abhängigkeiten aus der `pyproject.toml`, einschließlich Entwickler-Tools wie `ruff`. Das `-e`-Flag sorgt dafür, dass Ihre Code-Änderungen sofort wirksam werden.
    ```bash
    uv pip install -e . --all-extras
    ```
3.  **App starten:**
    ```bash
    uv run flask run
    ```

Die Anwendung ist dann erreichbar unter 👉 **http://localhost:5004**

## 🤖 CI & Automatisierung

Dieses Projekt verwendet GitHub Actions, um die Code-Qualität zu sichern und Abhängigkeiten aktuell zu halten:

-   **CI & Linting**: Bei jedem Push oder Pull Request wird automatisch der `ruff`-Linter ausgeführt, um den Code auf Stilprobleme und Fehler zu prüfen.
-   **Dependabot**: Sucht automatisch nach veralteten Abhängigkeiten und erstellt Pull Requests, um diese zu aktualisieren.
-   **Automerge**: Führt Dependabot Pull Requests automatisch zusammen, wenn alle Prüfungen (wie der Linter) erfolgreich sind.

---

## 📁 Projektstruktur

```
├── prompts/              # 📂 Fügen Sie hier Ihre .md Prompt-Vorlagen hinzu!
├── app/
│   ├── routes/           #  Flask Blueprints
│   ├── static/           # Statische Assets (aktuell ungenutzt)
│   ├── templates/        # HTML-Vorlagen
│   ├── utils/            # Hilfsmodule (Prompt-Lader, Modell-Abruf)
│   ├── app.py            # Flask Application Factory
│   └── config.py         # Konfigurationsklasse
├── .dockerignore         # 🐳 Dateien, die vom Docker-Image ausgeschlossen werden
├── .gitignore            #  Von Git ignorierte Dateien
├── docker-compose.yaml   # Docker Compose Konfiguration
├── Dockerfile            # Definiert das Docker-Image
├── pyproject.toml        # 📦 Python-Projektdefinition und Abhängigkeiten
└── README_DE.md          # 📄 Diese Datei
```

---

## 🛠️ Anpassungen

### Neue Prompts hinzufügen

Fügen Sie einfach eine neue Markdown-Datei (`.md`) zum `app/prompts/`-Verzeichnis hinzu.

-   Um die **Reihenfolge zu steuern**, stellen Sie dem Dateinamen eine Nummer voran, z.B. `01_Mein_erster_Prompt.md`.
-   Der Name im Dropdown-Menü wird automatisch bereinigt (z.B. "Mein Erster Prompt").
-   Der Inhalt der Datei wird als **System-Prompt** für die KI verwendet.
