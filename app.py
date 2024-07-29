import streamlit as st
import pandas as pd
import json
from datetime import datetime

# Título de la aplicación
st.title("Methylation Panel")
st.write("Developed by @KanYoso [GitHub](https://github.com/KanYoso/MethylationPannel)")

# Selección de idioma
language = st.selectbox("Choose language / Elige idioma", ["English", "Español"])

# Traducción de texto
translations = {
    "English": {
        "description": "The purpose of this application is to provide a detailed analysis of the methylation panel based on 23andMe genetic data. The results are shown with color coding for different genotypes and provide additional information about each analyzed gene.",
        "upload": "Upload 23andMe file",
        "results": "Methylation Panel Results",
        "legend": "Legend",
        "legend_red": "**Red**: Homozygous mutant (+/+)",
        "legend_yellow": "**Yellow**: Heterozygous (+/-)",
        "legend_green": "**Green**: Normal (-/-)",
        "not_found": "Variants not found in the 23andMe file but present in the dictionary"
    },
    "Español": {
        "description": "El objetivo de esta aplicación es proporcionar un análisis detallado del panel de metilación basado en los datos genéticos de 23andMe. Los resultados se muestran con codificación de colores para diferentes genotipos y proporcionan información adicional sobre cada gen analizado.",
        "upload": "Cargar archivo de 23andMe",
        "results": "Resultados del Panel de Metilación",
        "legend": "Leyenda",
        "legend_red": "**Rojo**: Homocigoto mutante (+/+)",
        "legend_yellow": "**Amarillo**: Heterocigoto (+/-)",
        "legend_green": "**Verde**: Normal (-/-)",
        "not_found": "Variantes no encontradas en el archivo de 23andMe pero presentes en el diccionario"
    }
}

# Selección de idioma
lang_code = "en" if language == "English" else "es"
trans = translations[language]

# Descripción del objetivo del programa
st.write(trans["description"])

# Cargar el archivo de diccionario de SNP
def load_snp_dict():
    with open('SNPMethylDict.txt', 'r', encoding='utf-8') as file:
        snp_dict = json.load(file)
    return snp_dict

# Parsear archivo de 23andMe
def parse_23andme(file):
    snps = {}
    for line in file:
        if isinstance(line, bytes):
            line = line.decode('utf-8')
        if line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) >= 4:
            rsid = parts[0]
            genotype = parts[3]
            snps[rsid] = genotype
    return snps

# Función para clasificar genotipos
def classify_genotype(rsid, genotype, snp_dict):
    if rsid in snp_dict:
        normal = snp_dict[rsid]['normal']
        heterocigoto = snp_dict[rsid]['heterocigoto']
        mutante = snp_dict[rsid]['mutante']
        
        if genotype in normal:
            return "-/-", "Verde"  # Normal
        elif genotype in heterocigoto:
            return "+/-", "Amarillo"  # Heterocigoto
        elif genotype in mutante:
            return "+/+", "Rojo"  # Mutante
    return "Desconocido", "Blanco"

# Cargar archivo de 23andMe
uploaded_file = st.file_uploader(trans["upload"], type="txt")
if uploaded_file is not None:
    snp_dict = load_snp_dict()
    snps = parse_23andme(uploaded_file)
    
    # Preparar datos para la tabla
    data = []
    not_found = []

    for rsid, info in snp_dict.items():
        if rsid in snps:
            genotype = snps[rsid]
            gene_info = info
            genotype_status, color = classify_genotype(rsid, genotype, snp_dict)
            data.append({
                'Gen': gene_info['gen'][lang_code],
                'RSID': rsid,
                'Genotipo': genotype,
                'Status': genotype_status,
                'Función': gene_info['funcion'][lang_code],
                'Consecuencias': gene_info['consecuencias'][lang_code],
                'Suplementos': gene_info['suplementos'][lang_code],
                'Evitar Suplementos': gene_info['evitar_suplementos'][lang_code],
                'Comida': gene_info['comida'][lang_code],
                'Evitar Comida': gene_info['evitar_comida'][lang_code],
                'Estilo de Vida': gene_info['estilo_vida'][lang_code],
                'Evitar Medicación': gene_info['evitar_medicacion'][lang_code],
                'Pruebas': gene_info['pruebas'][lang_code],
                'Color': color
            })
        else:
            not_found.append(rsid)
    
    # Mostrar tabla de resultados
    df = pd.DataFrame(data)
    st.write(f"### {trans['results']}")

    def color_rows(row):
        color = 'background-color: '
        if row.Color == 'Rojo':
            color += 'red'
        elif row.Color == 'Amarillo':
            color += 'yellow'
        else:
            color += 'green'
        return [color] * len(row)

    st.dataframe(df.style.apply(color_rows, axis=1))

    # Leyenda
    st.write(f"### {trans['legend']}")
    st.markdown(f"""
    - {trans['legend_red']}
    - {trans['legend_yellow']}
    - {trans['legend_green']}
    """)

    # Variantes no encontradas
    if not_found:
        st.write(f"### {trans['not_found']}")
        st.write(", ".join(not_found))
