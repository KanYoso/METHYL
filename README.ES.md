# METHYL

**METHYL** es una aplicación diseñada para analizar y proporcionar información sobre la variabilidad genética relacionada con el metabolismo de la metilación. Esta herramienta permite a los usuarios explorar información detallada sobre diversos genes y sus variantes, y cómo estas variantes pueden impactar la salud y el bienestar.

## Descripción

La aplicación proporciona análisis de datos RAW de 23andme sobre varios genes involucrados en la metilación, incluyendo funciones, consecuencias de variantes genéticas, recomendaciones de suplementos, alimentos y estilo de vida. El contenido está disponible en varios idiomas y se adapta a las diferentes necesidades del usuario.

## Funcionalidades

- **Carga de Datos RAW**: Carga el archivo RAW de 23andme para analizar la metilación basada en tus genes.
- **Visualización de Datos Genéticos**: Accede a información detallada sobre varios genes y sus variantes.
- **Soporte Multilingüe**: Disponible en varios idiomas ([EN](https://github.com/KanYoso/METHYL/README.md), [ES](https://github.com/KanYoso/METHYL/README.ES.md)).
- **Recomendaciones Personalizadas**: Información sobre suplementos, alimentos y estilo de vida basada en variantes genéticas.
- **Pruebas Recomendadas**: Información sobre pruebas clínicas recomendadas.

## Instalación

Para ejecutar la aplicación, sigue estos pasos:

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/KanYoso/METHYL.git
    ```

2. **Navega al directorio del proyecto**:

    ```bash
    cd METHYL
    ```

3. **Instala las dependencias**:

    Asegúrate de tener Python 3.x instalado. Luego, instala las dependencias usando pip:

    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecuta la aplicación**:

    ```bash
    streamlit run app.py
    ```

## Uso

Una vez que la aplicación esté en funcionamiento, accede a la interfaz a través de tu navegador web en la dirección proporcionada por la aplicación. Puedes cambiar el idioma. Sube tu archivo de datos RAW de 23andme. Explora la información genética ingresando identificadores de genes y accede a recomendaciones basadas en variantes genéticas.

## Estructura del Proyecto

- `app.py`: Archivo principal para ejecutar la aplicación.
- `data.json`: Archivo JSON que contiene información genética multilingüe.
- `requirements.txt`: Archivo con las dependencias requeridas para el proyecto.

## Contribuir

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama para tus cambios:

```bash
    git checkout -b nombre-de-tu-rama
   ```
3. Realiza un commit de tus cambios:

```bash
    git commit -am 'Añadir nueva funcionalidad'
   ```
4. Sube tus cambios:

```bash
    git push origin nombre-de-tu-rama
   ```
5. Crea un pull request en el repositorio original.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

##Contacto

Para preguntas o sugerencias, por favor contacta a [kanyoso92@gmail.com](mailto:kanyoso92@gmail.com).
