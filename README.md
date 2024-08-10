# METHYL

**METHYL** is an application designed to analyze and provide information on genetic variability related to methylation metabolism. This tool allows users to explore detailed information about various genes and their variants and how these variants may impact health and well-being.

## Description

The application provides 23andme RAW data analysis on various genes involved in methylation, including functions, consequences of genetic variants, recommendations for supplements, foods, and lifestyle. The content is available in multiple languages and adapts to different user needs.

## Features

- **RAW Data Load**: Load 23andme RAWdata file to analyze your Methylation based on your genes.
- **Genetic Data Visualization**: Access detailed information about various genes and their variants.
- **Multilingual Support**: Available in multiple languages  ([EN](https://github.com/KanYoso/METHYL/blob/main/README.md), [ES](https://github.com/KanYoso/METHYL/blob/main/README.ES.md)).
- **Personalized Recommendations**: Information on supplements, foods, and lifestyle based on genetic variants.
- **Recommended Tests**: Information on recommended clinical tests.

## Installation

To run the application, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/KanYoso/METHYL.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd METHYL
    ```

3. **Install dependencies**:

    Make sure you have Python 3.x installed. Then, install the dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:

    ```bash
    streamlit run  app.py
    ```

## Usage

Once the application is running, access the interface through your web browser at the address provided by the application. You can change the language. Upload your 23andme RAW data file. Explore genetic information by entering gene identifiers and access recommendations based on genetic variants.

## Project Structure

- `app.py`: The main file to run the application.
- `data.json`: JSON file containing multilingual genetic information.
- `requirements.txt`: File with the dependencies required for the project.

## Example Data

Here is an example of how a segment of the `data.json` file is structured:

```json
{
  "rs6311": {
    "gen": {
      "es": "HTR2A",
      "en": "HTR2A"
    },
    "funcion": {
      "es": "Receptor de serotonina",
      "en": "Serotonin receptor"
    },
    "consecuencias": {
      "es": "Depresión, ansiedad",
      "en": "Depression, anxiety"
    },
    "suplementos": {
      "es": "5-HTP, hierba de San Juan",
      "en": "5-HTP, St. John's Wort"
    },
    "evitar_suplementos": {
      "es": "Alcohol",
      "en": "Alcohol"
    },
    "comida": {
      "es": "Alimentos ricos en triptófano, como pavo y plátanos",
      "en": "Foods rich in tryptophan, like turkey and bananas"
    },
    "evitar_comida": {
      "es": "Alimentos procesados con alto contenido de azúcar",
      "en": "Processed foods high in sugar"
    },
    "estilo_vida": {
      "es": "Ejercicio regular, técnicas de manejo del estrés",
      "en": "Regular exercise, stress management techniques"
    },
    "evitar_medicacion": {
      "es": "Antidepresivos que afectan el sistema serotoninérgico",
      "en": "Antidepressants affecting the serotonin system"
    },
    "pruebas": {
      "es": "Nivel de serotonina: 101-283 ng/mL",
      "en": "Serotonin level: 101-283 ng/mL"
    },
    "normal": "GG",
    "heterocigoto": "AG",
    "mutante": "AA"
  }
}
```
## Contributing

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. **Fork the repository**.
2. **Create a branch** for your changes:

    ```bash
    git checkout -b your-branch-name
    ```

3. **Commit your changes**:

    ```bash
    git commit -am 'Add new feature'
    ```

4. **Push your changes**:

    ```bash
    git push origin your-branch-name
    ```

5. **Create a pull request** in the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please contact [kanyoso92@gmail.com](mailto:kanyoso92@gmail.com).
