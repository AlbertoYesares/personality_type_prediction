# PREDICCIÓN DE TIPO DE PERSONALIDAD DE UNA PERSONA

## Introducción

El concepto de las "16 personalidades" proviene del indicador de tipo Myers-Briggs (MBTI), que es una teoría desarrollada por Isabel Briggs Myers y su madre, Katharine Cook Briggs, basada en las teorías del psiquiatra Carl Jung. Este modelo clasifica la personalidad en 16 tipos distintos, que resultan de combinar cuatro pares de preferencias:

- **Extraversión (E) - Introversión (I)**: Indica dónde las personas obtienen su energía: de la interacción con el mundo externo (E) o del mundo interno de ideas y reflexiones (I).
- **Sensación (S) - Intuición (N)**: Describe cómo las personas procesan información. Los tipos "S" se centran en detalles concretos y realidades prácticas, mientras que los tipos "N" se enfocan en patrones y posibilidades futuras.
- **Pensamiento (T) - Sentimiento (F)**: Define cómo las personas toman decisiones. Los "T" prefieren decisiones lógicas y objetivas, mientras que los "F" priorizan valores y consideraciones personales.
- **Juicio (J) - Percepción (P)**: Indica cómo las personas manejan el mundo externo: con estructura y planificación (J) o de manera abierta y flexible (P).

Cada tipo de personalidad es representado por una combinación de estas cuatro letras (por ejemplo, INTJ, ENFP, ESTJ), lo cual da un total de 16 combinaciones posibles. Este modelo de MBTI se utiliza en diversos ámbitos, como desarrollo personal, orientación vocacional y el ámbito laboral para mejorar la dinámica de equipo.

### Descripción de las columnas del dataset

- **Age**: Edad de la persona.
- **Gender**: Género de la persona (Male/Female).
- **Education**: Nivel educativo (0 para no licenciados, 1 para licenciados).
- **Introversion Score**: Puntaje de introversión, un indicador de la preferencia de la persona hacia la introversión.
- **Sensing Score**: Puntaje de sensación, que mide la inclinación hacia la observación de hechos concretos y detalles.
- **Thinking Score**: Puntaje de pensamiento, que evalúa la preferencia por tomar decisiones de manera lógica y objetiva.
- **Judging Score**: Puntaje de juicio, que indica la tendencia a estructurar y planificar la vida.
- **Interest**: Área de interés principal de la persona (Unknown, Arts, Others, Technology, Sports).
- **Personality**: Tipo de personalidad resultante según el modelo MBTI.

## Contenido del Proyecto

- **notebooks**: Directorio que contiene todas las notebooks de Jupyter (.ipynb) utilizadas para realizar pruebas.
- **data**: Directorio que contiene los archivos de datos necesarios para el entrenamiento del modelo de Machine Learning (.csv).
- **README.md**: El archivo que estás leyendo actualmente, que documenta la estructura y uso del proyecto.
- **app**: Directorio que contiene:
  - **models**: Carpeta donde se almacenan los modelos entrenados. Debido a restricciones de tamaño, esta carpeta no está en el repositorio, pero puedes descargarla en un archivo comprimido desde Google Drive. [Descargar modelos](https://drive.google.com/file/d/1tqWEJhnKWT2vr2-n6kSAAZXQCYU5qD48/view?usp=sharing)
  - **app.py**: Archivo que contiene el código principal de la aplicación desarrollada con Gradio.
  - **Dockerfile**: Archivo Docker que contiene las instrucciones para construir la imagen Docker del proyecto.
  - **requirements.txt**: Archivo que especifica las dependencias necesarias para ejecutar el proyecto.

## Descargar Archivos Grandes

Para utilizar el modelo entrenado, es necesario descargar los archivos de modelos grandes que están almacenados externamente debido a restricciones de tamaño de GitHub. Puedes descargarlos desde el siguiente enlace:

- [Descargar carpeta comprimida con modelos entrenados](https://drive.google.com/file/d/1tqWEJhnKWT2vr2-n6kSAAZXQCYU5qD48/view?usp=sharing)

Una vez descargado el archivo, descomprímelo y colócalo dentro del directorio `app/models` para que la aplicación pueda acceder a los modelos entrenados.

## Uso y Requisitos

Para ejecutar este proyecto, necesitas cumplir con los siguientes requisitos:

1. **Docker**: Si aún no lo tienes instalado, puedes obtener Docker siguiendo [este enlace de instalación](https://docs.docker.com/get-docker/).

### Configuración de la Imagen Docker

El archivo Dockerfile del proyecto está configurado para:

- Utilizar una imagen base oficial de Python.
- Instalar todas las dependencias necesarias listadas en `requirements.txt`.
- Copiar el código fuente al contenedor.
- Configurar y ejecutar el servidor de la API de predicción cuando se inicia el contenedor.

### Iniciar la Aplicación

Sigue estos pasos para construir y ejecutar la aplicación:

1. **Construir la Imagen Docker (En la Terminal de Docker)**:

   ```bash
   docker build --no-cache -t gradio-app .

2. **Ejecutar el Contenedor (En la Terminal de Docker)**:

   ```bash
   docker run -p 7860:7860 gradio-app
3. **Abrir la Aplicación**:

   Una vez que el contenedor esté ejecutándose, abre en enlace que aparecerá en la terminal de Docker para acceder a la aplicación de Gradio.

4. **Realiza una Predicción**:

   Ingresa los datos solicitados en la aplicación, y el algoritmo te proporcionará una predicción del tipo de personalidad según el modelo MBTI.
