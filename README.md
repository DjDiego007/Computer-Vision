Proyecto: Sistema de Inteligencia Artificial para el Hogar
📝 Descripción
Este proyecto implementa un sistema de Visión Artificial diseñado para la automatización de un hogar inteligente. El software es capaz de detectar rostros en tiempo real a través de una cámara web (externa o integrada) y ejecutar acciones simuladas como el ajuste de iluminación y activación de sistemas multimedia basándose en la presencia del usuario.

🚀 Tecnologías Utilizadas
Python 3.x: Lenguaje principal de desarrollo.

OpenCV: Librería de visión artificial para el procesamiento de imágenes y detección facial.

Haar Cascade Classifiers: Algoritmo de machine learning para la identificación de rasgos faciales.

Entornos Virtuales (venv): Para la gestión aislada de dependencias.

🛠️ Metodología
Captura de Video: Procesamiento de frames en tiempo real desde hardware externo.

Preprocesamiento: Conversión de imágenes a escala de grises para optimizar la velocidad de detección.

Algoritmo de Detección: Implementación de detectMultiScale para localizar coordenadas espaciales del rostro.

Lógica de Automatización: Triggering de eventos (mensajes de consola) que simulan la activación de dispositivos IoT en el hogar.

📊 Resultados
El sistema demuestra una precisión sólida en diferentes condiciones de iluminación, logrando:

Identificación inmediata del usuario.

Feedback visual mediante rectángulos de seguimiento (Bounding Boxes).

Generación automática de evidencia fotográfica (evidencia_rostro.jpg).

📦 Instalación y Uso
Clonar el repositorio.

Activar el entorno virtual:

Bash
.\venv\Scripts\activate
Instalar dependencias:

Bash
pip install -r requirements.txt
Ejecutar la aplicación:

Bash
python hogar_inteligente.py
Desarrollado por: Diego (DjDiego007)
Roadmap: DevSecOps Engineer