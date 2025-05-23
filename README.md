# appMovilNotas
## Requerimientos
Nombrar el título de las notas.
Escribir notas en dos modos: Markdown (con exportación a PDF) o texto normal.
Categorizar notas en carpetas con nombre, emoji y color personalizables.
Agregar notas de voz.
Implementar modo claro y oscuro.
Permitir títulos dentro de una nota, con contenido indentado (2 espacios) que se agrupe bajo el título y sea comprimible si el título comienza con *.
## Que hice?
1.- Escoger DirectoryStructure/Project Structure
    notes-mobile/
    ├── src/                    # Source code for the app
    │   ├── main.py             # Entry point (Kivy app initialization)
    │   ├── models/             # Data models (Note, Category, CollapsibleSection)
    │   │   ├── note.py
    │   │   ├── category.py
    │   │   └── section.py
    │   ├── ui/                 # UI components and logic
    │   │   ├── widgets/        # Custom Kivy widgets (e.g., collapsible section)
    │   │   │   ├── note_widget.py
    │   │   │   └── category_widget.py
    │   │   └── screens/        # Screen layouts (e.g., main screen, note view)
    │   │       ├── main_screen.py
    │   │       └── note_screen.py
    │   ├── utils/              # Utility functions (e.g., JSON, Markdown, PDF)
    │   │   ├── storage.py
    │   │   ├── markdown_parser.py
    │   │   └── pdf_export.py
    │   └── audio/              # Audio recording/playback logic
    │       └── recorder.py
    ├── kv/                     # Kivy UI files (declarative UI)
    │   ├── notes.kv            # Main UI layout
    │   ├── note_widget.kv      # Note widget UI
    │   └── category_widget.kv  # Category widget UI
    ├── assets/                 # Static assets (images, fonts, audio)
    │   ├── fonts/              # Custom fonts for emojis
    │   ├── icons/              # Icons for UI
    │   └── audio/              # Temporary audio files (voice notes)
    ├── data/                   # Runtime data (notes, categories)
    │   ├── notes.json
    │   ├── categories.json
    │   └── config.json         # App settings (e.g., theme)
    ├── docs/                   # Documentation
    │   ├── instrucciones.md    # Existing instructions
    │   ├── README.md           # Project overview
    │   └── architecture.md     # App architecture and design
    ├── tests/                  # Unit tests
    │   ├── test_storage.py
    │   ├── test_markdown.py
    │   └── test_audio.py
    ├── .gitignore              # Git ignore file
    ├── buildozer.spec          # Buildozer config for mobile builds
    ├── requirements.txt        # Python dependencies
    └── LICENSE                 # License file (e.g., MIT)
    ***Explicacion del DirectoryStructure***
    src/: Contains all Python code, split into models (data), ui (Kivy widgets/screens), utils (helpers), and audio (voice notes).
    kv/: Stores Kivy’s declarative UI files to separate presentation from logic.
    assets/: Holds static files like fonts (for emojis) and icons.
    data/: Stores runtime JSON files for notes, categories, and settings.
    docs/: Centralizes documentation, including your instrucciones.md.
    tests/: For unit tests to ensure code quality.
    requirements.txt: Lists dependencies (e.g., kivy, markdown).
    buildozer.spec: Configures mobile builds.
    .gitignore: Excludes .venv/, data/, *.pyc, __pycache__/, and Buildozer build artifacts.
2.- 
