# appMovilNotas

A mobile notes application built with Python and Kivy, allowing users to create, categorize, and manage notes with Markdown support, voice notes, and customizable themes.

## Features
- Create notes with custom titles.
- Write notes in Markdown (with PDF export) or plain text.
- Organize notes in folders with custom names, emojis, and colors.
- Record and play voice notes.
- Switch between light and dark themes.
- Support collapsible titles within notes (marked with `*`, content indented by 2 spaces).

## Getting Started
1. Clone the repository: `git clone https://github.com/Prolirico/appMovilNotas.git`
2. Set up a virtual environment: `python -m venv .venv && source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `python src/main.py`

See `docs/instrucciones.md` for detailed setup and development instructions.

## Project Structure
- `src/`: Python source code (models, UI, utilities, audio).
- `kv/`: Kivy UI files for declarative layouts.
- `assets/`: Static assets (fonts, icons, audio).
- `data/`: Runtime data (notes, categories, settings).
- `docs/`: Documentation (instructions, architecture, changelog).
- `tests/`: Unit tests for code quality.
appMovilNotas/
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
│   ├── instrucciones.md    # Setup and development instructions
│   ├── architecture.md     # App architecture and design
│   └── changelog.md        # Project updates and changes
├── tests/                  # Unit tests
│   ├── test_storage.py
│   ├── test_markdown.py
│   └── test_audio.py
├── README.md               # Project overview (moved to root)
├── .gitignore              # Git ignore file
├── buildozer.spec          # Buildozer config for mobile builds
├── requirements.txt        # Python dependencies
└── LICENSE                 # License file (e.g., MIT)

## Requerimientos
- **Crear notas con títulos personalizados**: Permitir a los usuarios asignar un título único a cada nota para identificarla fácilmente.
- **Escribir notas en formato Markdown (con exportación a PDF) o texto plano**: Soportar dos modos de escritura: Markdown para formato 
enriquecido con opción de exportar a PDF, y texto plano para simplicidad.
- **Organizar notas en carpetas con nombres, emojis y colores personalizables**: Crear categorías (como "libros") con nombres, emojis y
colores definidos por el usuario para agrupar notas relacionadas.
- **Etiquetar notas con etiquetas personalizables**: Asignar etiquetas a notas, con opciones de color y emoji, para organizarlas dentro de
categorías y facilitar su búsqueda.
- **Grabar y reproducir notas de voz**: Permitir grabar audios como notas y reproducirlos desde la app.
- **Interfaz rápida y fácil de usar**: Diseñar una interfaz intuitiva que minimice pasos para crear, editar y buscar notas, optimizando la 
experiencia del usuario.
- **Sincronización con correo electrónico para respaldo en la nube**: Sincronizar notas con una cuenta de correo para almacenarlas en la nube 
y recuperarlas en caso de pérdida del dispositivo.
- **Soporte para títulos colapsables dentro de las notas**: Permitir que los títulos marcados con `*` (con contenido indentado por 2 espacios)
sean colapsables para ocultar/mostrar información y facilitar la navegación en notas largas.
- **Reorganizar títulos mediante arrastre**: Habilitar la reordenación de títulos dentro de una nota arrastrándolos, para ajustar su posición
sin editar manualmente.
- **Alternar entre temas claro y oscuro**: Ofrecer modos claro y oscuro para personalizar la apariencia de la app según las preferencias del
usuario.

## Exclusiones(.gitignore)
Archivos de Python:
*.pyc, __pycache__/, *.pyo, *.pyd: Archivos compilados de Python que se generan automáticamente.
*.egg-info/, dist/, build/: Carpetas generadas al empaquetar o instalar paquetes Python.
Entornos virtuales:
venv/, env/, .venv/, .env/: Ignora entornos virtuales locales para dependencias.
Buildozer y compilaciones móviles:
.bin/, .gen/, buildozer/: Carpetas generadas por Buildozer durante la compilación.
*.apk, *.aab, *.ipa: Archivos de salida para Android/iOS.
Cachés y temporales:
*.cache, *.log, *.swp, *~: Archivos temporales o de respaldo generados por editores o procesos.
.DS_Store, Thumbs.db: Archivos específicos de macOS y Windows.
Configuraciones de editores:
.vscode/, .idea/: Ignora configuraciones de Visual Studio Code, IntelliJ, u otros IDEs.
Datos sensibles o generados:
data/*.json.bak: Ignora respaldos de archivos JSON.
data/*.db, data/local_config.json: Ignora bases de datos locales o configuraciones específicas del usuario (ajusta según necesites).
Pruebas y cobertura:
.coverage, coverage.xml, htmlcov/: Ignora archivos generados por herramientas de cobertura de pruebas.

## Contributing
Contributions are welcome! Please read `docs/instrucciones.md` for development guidelines and submit pull requests on GitHub.

## License
MIT License (see `LICENSE`).
