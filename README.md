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
	source pythonVirtual/bin/activate
	Para windows(ejecutar en carpeta raiz):
	 	```
		python -m venv venv
		.\venv\Scripts\activate
		```
	3. Install dependencies: `pip install -r requirements.txt`
	4. Run the app: `python src/main.py`
	**Extras**
	Documentacion kivy: https://kivy.org/
	See `docs/instrucciones.md` for detailed setup and development instructions.

## Project Structure
	- `src/`: Código fuente Python (modelos, interfaz de usuario, utilidades, audio).
	- `kv/`: Kivy UI files for declarative layouts.
	- `assets/`: Static assets (fonts, icons, audio).
	- `data/`: Datos de tiempo de ejecución (notas, categorías, ajustes).
	- `docs/`: Documentation (instructions, architecture, changelog).
	- `tests/`: Unit tests for code quality.
appMovilNotas/
├── src/                    # Código fuente de la aplicación
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
│   ├── utils/              # Funciones de utilidad (por ejemplo, JSON, Markdown, PDF)
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
├── pendientes.md
├── vitacora.md             # Proyecto paso a paso
├── .gitignore              # Git ignore file
├── buildozer.spec          # Configuración de Buildozer para construcciones móviles
├── requirements.txt        # Python dependencies
└── LICENSE                 # License file (e.g., PRO)

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
### 1.- Archivos de Python:
	*.pyc, __pycache__/, *.pyo, *.pyd, *.egg-info/, dist/, build/, *.egg:
		- Excluye correctamente los archivos compilados de Python, los paquetes de distribución y los artefactos de compilación.
		- Asegura que no se versionen archivos Python temporales o generados.
	- .Python: Probablemente innecesario (raramente generado), pero inofensivo para incluir.
### 2.- Entornos Virtuales:
	venv/, env/, .env/, .venv/:
		- Excluye adecuadamente los directorios de entorno virtual comunes.
		- Evita comprometer grandes carpetas de dependencia, lo cual es crítico para la colaboración.
### 3.- Buildozer y Mobile Builds:
	.bin/, .gen/, buildozer/, *.apk, *.aab, *.ipa:
		- Excluye efectivamente los artefactos de compilación de Buildozerrad y los paquetes de aplicaciones móviles (Android APK, AAB, iOS IPA).
		- Se alinea con su plan para usar Buildozer para la implementación de Android/iOS.
### 4.- Caché y Archivos Temporales:
	*.cache, *.log, *.pid, *.swp, *~:
		- Cubre archivos temporales del editor/IDE, registros y archivos de intercambio.
		- Mantiene el repositorio limpio de archivos transitorios.
### 5.- Configuraciones de IDE/Editor:
	.vscode/, .idea/, *.sublime-project, *.sublime-workspace:
		- Excluye la configuración de IDE/editores comunes (VS Code, JetBrains, Sublime).
		- Evita comprometer configuraciones específicas del usuario, lo cual es bueno para la colaboración en equipo.
### 6.- Archivos específicos de OS:
	.DS_Store, Thumbs.db:
		- Excluye los archivos del sistema macOS y Windows que podrían cometerse accidentalmente.
### 7.- Datos de Tiempo de ejecución:
	data/*.json.bak, data/*.db, data/local_config.json:
		- Excluye parcialmente los archivos JSON de copia de seguridad, bases de datos y configuraciones locales en data/.
		- Se alinea con su estructura (data/notes.json, data/categories.json, data/config.json) para evitar el control de versiones de datos generados por el usuario.
### 8.- Construir y Embalaje:
	.gradle/, construir/, fuera/:
		- Excluye artefactos Gradle (relevantes para compilaciones de Android) y directorios genéricos de compilación/salida.
		- build/ se enumera dos veces (también en artefactos de Python), pero Git maneja los duplicados bien.
### 9.- Pruebas y Cobertura:
	.coverage, coverage.xml, *.cover, htmlcov/
		- Excluye los informes de cobertura de pruebas, que se generan durante las pruebas (test/folder).
		- Asegura que los artefactos de prueba no estén comprometidos.
### 10.- Varios:
	*.bak, *.tmp:
		- Captura copias de seguridad genéricas y archivos temporales, agregando una capa adicional de protección.

## Contributing
Contributions are welcome! Please read `docs/instrucciones.md` for development guidelines and submit pull requests on GitHub.

## License
PRO License (see `LICENSE`).
.\pythonVirtual\Scripts\activate
