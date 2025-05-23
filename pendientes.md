Pendientes - appMovilNotas
Este documento lista las tareas pendientes para el desarrollo de appMovilNotas, una aplicación móvil de notas construida con Python y Kivy. Las tareas están organizadas por categoría y prioridad para guiar el desarrollo.

1. **Configuración del Entorno de Desarrollo**
	<input type="checkbox" disabled> Instalar Kivy y dependencias
	Instalar Kivy y las dependencias listadas en requirements.txt en el entorno virtual.
	Crear el entorno virtual en el directorio raíz del proyecto: python -m venv .venv.
	Activar el entorno virtual: source .venv/bin/activate (en Linux).
	Instalar dependencias: pip install -r requirements.txt.
	Verificar la instalación ejecutando un script Kivy de prueba (por ejemplo, un "Hello World" en src/main.py).
	<input type="checkbox" disabled> Configurar Buildozer para compilación móvil
	Configurar buildozer.spec para compilar la aplicación en Android (y opcionalmente iOS).
	Instalar Buildozer: pip install buildozer.
	Actualizar buildozer.spec con el nombre de la aplicación, paquete, versión, y permisos (por ejemplo, grabación de audio, almacenamiento).
	Probar una compilación inicial para Android: buildozer android debug.
	Documentar cualquier problema de compilación en docs/instrucciones.md.
	
2. **Desarrollo del Modelo de Datos**
	<input type="checkbox" disabled> Implementar modelos de datos en src/models/
	Completar las clases en src/models/note.py, src/models/category.py, y src/models/section.py.
	Definir la clase Note con atributos para título, contenido (Markdown o texto plano), etiquetas, y referencia a una categoría.
	Definir la clase Category con atributos para nombre, emoji, y color.
	Definir la clase Section para soportar títulos colapsables dentro de una nota (título con * y contenido indentado).
	Asegurar que los modelos sean serializables a JSON para almacenamiento en data/notes.json y data/categories.json.
	<input type="checkbox" disabled> Configurar almacenamiento en src/utils/storage.py
	Implementar funciones para leer/escribir datos en data/notes.json, data/categories.json, y data/config.json.
	Crear funciones para guardar y cargar notas, categorías, y configuraciones (por ejemplo, tema claro/oscuro).
	Implementar manejo de errores para archivos corruptos o faltantes.
	Asegurar que los datos se actualicen correctamente al crear, editar o eliminar notas/categorías.
	
3. **Desarrollo de la Interfaz de Usuario**
	<input type="checkbox" disabled> Implementar pantallas principales en src/ui/screens/
	Desarrollar la lógica de las pantallas en src/ui/screens/main_screen.py y src/ui/screens/note_screen.py.
	En main_screen.py, crear una pantalla que muestre una lista de categorías y notas, con botones para crear nuevas notas/categorías.
	En note_screen.py, crear una pantalla para ver/editar una nota, con soporte para título, contenido, y etiquetas.
	Vincular las pantallas con los archivos Kivy en kv/notes.kv.
	<input type="checkbox" disabled> Implementar widgets personalizados en src/ui/widgets/
	Completar la lógica de los widgets en src/ui/widgets/category_widget.py y src/ui/widgets/note_widget.py.
	En category_widget.py, implementar un widget que muestre el nombre, emoji, y color de una categoría, con opción de selección.
	En note_widget.py, implementar un widget que muestre el título y un resumen del contenido, con opción de abrir la nota completa.
	Vincular los widgets con sus respectivos archivos .kv (kv/category_widget.kv, kv/note_widget.kv).
	<input type="checkbox" disabled> Soporte para títulos colapsables
	Implementar la funcionalidad de títulos colapsables en src/ui/widgets/note_widget.py y kv/note_widget.kv.
	Detectar títulos marcados con * y contenido indentado (2 espacios) en el contenido de la nota.
	Mostrar los títulos como elementos colapsables (por ejemplo, usando Accordion de Kivy).
	Permitir al usuario ocultar/mostrar el contenido de cada título.
	<input type="checkbox" disabled> Implementar reordenación de títulos por arrastre
	Añadir soporte para reordenar títulos dentro de una nota mediante arrastre.
	Usar gestos de arrastre en note_widget.py para permitir reordenar secciones.
	Actualizar el modelo de datos (src/models/section.py) y el almacenamiento (src/utils/storage.py) al cambiar el orden.
	<input type="checkbox" disabled> Implementar temas claro y oscuro
	Añadir soporte para alternar entre temas claro y oscuro en data/config.json.
	Crear un selector de temas en la interfaz (por ejemplo, un botón en main_screen.py).
	Definir estilos para ambos temas en los archivos .kv (colores de fondo, texto, botones).
	Guardar la preferencia del tema en data/config.json y cargarla al iniciar la app.

4. **Funcionalidades de Notas**
	<input type="checkbox" disabled> Soporte para Markdown en src/utils/markdown_parser.py
	Implementar un analizador de Markdown para renderizar notas en formato enriquecido.
	Convertir texto Markdown a widgets Kivy (por ejemplo, texto con formato, listas, enlaces).
	Asegurar que los títulos colapsables (* con indentación) se procesen correctamente.
	Probar el renderizado con diferentes tipos de Markdown (encabezados, listas, negritas, cursivas).
	<input type="checkbox" disabled> Exportación a PDF en src/utils/pdf_export.py
	Implementar la exportación de notas a PDF.
	Usar una librería como reportlab o weasyprint para generar PDFs desde Markdown o texto plano.
	Incluir el título de la nota y el contenido formateado en el PDF.
	Añadir un botón en note_screen.py para exportar la nota actual a PDF.
	<input type="checkbox" disabled> Soporte para etiquetas personalizables
	Añadir funcionalidad para asignar etiquetas a notas en src/models/note.py y src/ui/screens/note_screen.py.
	Permitir al usuario crear etiquetas con texto, color, y emoji.
	Mostrar etiquetas en la interfaz de la nota y permitir filtrar notas por etiquetas en main_screen.py.
	Guardar las etiquetas en data/notes.json.

5. **Funcionalidades de Audio**
	<input type="checkbox" disabled> Implementar grabación y reproducción de notas de voz en src/audio/recorder.py
	Añadir soporte para grabar y reproducir notas de voz.
	Usar una librería como pyaudio o sounddevice para grabar audio.
	Guardar los archivos de audio en assets/audio/ con nombres únicos (por ejemplo, basados en el ID de la nota).
	Añadir botones en note_screen.py para grabar y reproducir audio.
	Asociar los archivos de audio con las notas en data/notes.json.

6. **Sincronización en la Nube**
	<input type="checkbox" disabled> Implementar sincronización con correo electrónico
	Añadir funcionalidad para respaldar notas en la nube usando correo electrónico.
	Configurar una librería como smtplib para enviar correos con archivos adjuntos (data/notes.json, data/categories.json).
	Crear una pantalla o sección en main_screen.py para configurar la cuenta de correo (servidor SMTP, usuario, contraseña).
	Implementar funciones en src/utils/storage.py para enviar y recuperar datos desde el correo.
	Asegurar que los datos sean seguros (por ejemplo, encriptar archivos antes de enviarlos).

7. **Pruebas y Calidad**
	<input type="checkbox" disabled> Escribir pruebas unitarias en tests/
	Completar las pruebas en test_storage.py, test_markdown.py, y test_audio.py.
	En test_storage.py, probar funciones de lectura/escritura de JSON en src/utils/storage.py.
	En test_markdown.py, probar el analizador de Markdown en src/utils/markdown_parser.py.
	En test_audio.py, probar la grabación y reproducción en src/audio/recorder.py.
	Añadir nuevas pruebas para los modelos (note.py, category.py, section.py) y widgets (note_widget.py, category_widget.py).
	<input type="checkbox" disabled> Configurar cobertura de pruebas
	Configurar una herramienta como pytest-cov para medir la cobertura de pruebas.
	Actualizar requirements.txt con las dependencias necesarias.
	Ejecutar pruebas con cobertura: pytest --cov=src tests/.
	Generar un informe de cobertura y verificar que cubra al menos el 80% del código.

8. **Documentación y Finalización**
	<input type="checkbox" disabled> Actualizar documentación en docs/
	Completar y actualizar los archivos de documentación.
	En docs/instrucciones.md, añadir instrucciones detalladas para compilar con Buildozer y ejecutar pruebas.
	En docs/architecture.md, documentar cualquier cambio en el diseño (por ejemplo, cómo se implementaron los títulos colapsables o la sincronización).
	Crear un archivo docs/changelog.md para registrar los cambios realizados en cada versión.
	<input type="checkbox" disabled> Revisar y finalizar README.md
	Actualizar README.md con cualquier cambio en las funciones o instrucciones de configuración.
	Asegurar que la sección de características refleje el estado final de la app.
	Añadir capturas de pantalla o un video corto de la app en acción (guardar en assets/ y enlazar en README.md).
	<input type="checkbox" disabled> Actualizar vitacora.md
	Registrar cada paso completado en vitacora.md con fechas y detalles.
	Incluir problemas encontrados y cómo se resolvieron.
	Mantener el formato consistente con los pasos ya documentados.

9. **Despliegue**
	<input type="checkbox" disabled> Probar la aplicación en un dispositivo móvil
	Compilar y probar la aplicación en un dispositivo Android (y opcionalmente iOS).
	Usar Buildozer para generar un APK: buildozer android debug deploy run.
	Probar todas las funciones (crear notas, grabar audio, cambiar temas, etc.) en el dispositivo.
	Corregir cualquier problema de rendimiento o compatibilidad (por ejemplo, tamaños de fuente, permisos).
	<input type="checkbox" disabled> Preparar para distribución
	Preparar la aplicación para su distribución en tiendas de aplicaciones (Google Play, App Store).
	Crear íconos y recursos gráficos en assets/icons/ según los requisitos de las tiendas.
	Generar un APK/AAB firmado para Android y, si aplica, un IPA para iOS.
	Investigar los requisitos de publicación en Google Play y documentarlos en docs/instrucciones.md.

**Prioridades**
	Configuración del entorno: Completar la instalación de Kivy y Buildozer para comenzar el desarrollo.
	Modelos y almacenamiento: Implementar los modelos de datos y el sistema de almacenamiento para soportar las notas y categorías.
	Interfaz básica: Desarrollar las pantallas y widgets principales para tener una app funcional.
	Funcionalidades clave: Añadir soporte para Markdown, PDF, audio, y etiquetas.
	Sincronización y temas: Implementar la sincronización en la nube y los temas claro/oscuro.
	Pruebas y documentación: Escribir pruebas y actualizar la documentación.
	Despliegue: Probar en dispositivos móviles y preparar para distribución.

**Instrucciones para usar este archivo**
	Marca cada tarea completada con [x] en el archivo pendientes.md.
	Añade nuevas tareas si surgen durante el desarrollo.
	Actualiza vitacora.md con los detalles de cada tarea completada (fecha, descripción, problemas encontrados).
	Revisa las prioridades periódicamente para ajustar el enfoque según el progreso.
