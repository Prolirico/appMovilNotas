# Vítacora de Desarrollo - appMovilNotas

Este documento registra los pasos realizados en el desarrollo de **appMovilNotas**, una aplicación móvil de notas construida con Python y Kivy. Sirve como referencia para proyectos futuros.

## Pasos Realizados

1. **Creación del Repositorio en GitHub**  
   - Fecha: [22-05-2025]  
   - Creé un repositorio en GitHub llamado `appMovilNotas` en `https://github.com/Prolirico/appMovilNotas.git`.  
   - Configuré el repositorio con una licencia MIT (`LICENSE`) y un `README.md` inicial describiendo el proyecto.

2. **Clonación del Repositorio**  
    - Fecha: [22-05-2025]  
	- Cloné el repositorio en mi máquina local (Arch Linux) en `/home/axel/Documentos/ProyectosPersonales/`:  
     ```bash
     cd ~/Documentos/ProyectosPersonales
     git clone https://github.com/Prolirico/appMovilNotas.git
     cd appMovilNotas
     ```

3. **Definición de la Estructura del Proyecto**
	Estructura:
	src/: Código Python (modelos, UI, utilidades, audio).
	kv/: Archivos Kivy para diseño de interfaz.
	activos/: Recursos estáticos (fuentes, íconos, audio).
	datos/: Datos en tiempo de ejecución (notas, categorías, configuración).
	documentos/: Documentación (instrucciones, arquitectura).
	pruebas/: Pruebas unitarias.
	Archivos raíz: README.md, .gitignore, requisitos.txt, buildozer.spec, LICENCIA, vitacora.md.
	Documenté la estructura en docs/arquitectura.md.

4. **Configuración de .gitignore**
	INFORMACION en /appMovilNotas/README.md
	
5. **Creación de Documentación Inicial**
	- Fecha: [22-05-2025]
	Actual README.md con:
	Descripción del proyecto.
	Funciones (notas con títulos, Markdown/PDF, categorías, notas de voz, temas claro/oscuro, títulos colapsables, etiquetas, sincronización en la nube, interfaz rápida, reordenación de títulos).
	Instrumentos básicas de inicio.
	Estructura del proyecto.
	Guías para contribuir y licencia (MIT).
	Crema documentos/instrucciones.md con instrucciones detalladas de configuración y desarrollo.
	Crema docs/arquitectura.md explicando la estructura y el patrón MVC (Modelo-Ver-Controlador).
	Iniciar vitacora.md (este archivo) para registrar el progreso.
	
6. **Verificación de Python**
	- Fecha: [23-05-2025]
	Confirmado que Python 3.8+ está instalado en Arch Linux:	
    ```bash
	python --version
	```
	No instalación Kivy aún, pero plano hacerlo en el siguiente paso para comenzar a desarrollar la interfaz.

7. **Creacion entorno virtual python**
    - Fecha: [23-05-2025]
    ```bash
    python -m venv entornoVirtualParaApp
    ```
    
8. **Instalar dependencias de Kivy**
	- Fecha: [23-05-2025]
	- Para corroborar las dependencias usamos:
	```bash
	pip install kivy --no-deps --dry-run
	pip install kivymd --no-deps --dry-run
	pip install pyaudio --no-deps --dry-run
	pip install reportlab --no-deps --dry-run
	```
	Alternativamente, consulte las páginas de PyPI:
	Kivy: https://pypi.org/project/Kivy/
	KivyMD: https://pypi.org/project/kivymd/
	PyAudio: https://pypi.org/project/PyAudio/
	ReportLab: https://pypi.org/project/reportlab/
	- En el archivo requirements.txt ubicada en la carpeta raiz
	pondremos lo siguiente:
	kivy==2.3.1
	kivymd==1.2.0
	pyaudio==0.2.14
	reportlab==4.4.1
	- ¿Porque estas dependencias?
	kivy y kivymd para la interfaz de usuario móvil.
	pyaudio para la grabación de audio (src/audio/recorder.py).
	reportlab para la generación de PDF (src/utils/pdf_export.py).
	- Instalar las dependencias
	```bash
	pip install -r requirements.txt
	```
		
9. 	**Verificar instalacion de Kivy**
	- Ejecutar:
	```
	python src/main.py
	```
