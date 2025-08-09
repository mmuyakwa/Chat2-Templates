#!/bin/bash
# Schritt 1: Erstelle eine Python Virtual Environment mit uv im Subfolder .venv
uv venv .venv
# Schritt 2: Aktiviere die virtuelle Umgebung
source .venv/bin/activate
# Schritt 3: Installiere die Pakete mit uv
uv pip install wheel python-dotenv autopep8

# Schritt 4: Installiere die erforderlichen Python-Pakete
# Wenn eine requirements.txt-Datei vorhanden ist, installiere die darin aufgelisteten Pakete
if [ -f requirements.txt ]; then
    uv pip install -r requirements.txt
fi

# Gib eine Nachricht aus, die darauf hinweist, dass das Skript abgeschlossen ist
echo "Entwicklungsumgebung wurde eingerichtet."

echo $PWD >location.txt
