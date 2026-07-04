# Configuración

import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Conclusiones",
    page_icon="✅",
    layout="wide"
)

# Titulo
st.title("✅ Conclusiones del Proyecto")

# Introduccion

st.markdown("""
Esta sección sintetiza los principales resultados obtenidos durante el desarrollo del Proyecto Integrador de Minería de Datos I.

A lo largo del proyecto se aplicó un proceso completo de inspección, limpieza, preparación, análisis exploratorio y Análisis de Componentes Principales (PCA), permitiendo transformar un conjunto de datos inicial en un dataset consistente y apto para su análisis.

Las conclusiones presentadas integran los principales hallazgos obtenidos en cada etapa del proyecto y resumen los aportes más relevantes del proceso de minería de datos desarrollado.
""")

# Carga del Dataset

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "dataset_final.csv"
)

df = pd.read_csv(DATA_PATH)

# Resumen del Proyecto

st.divider()

st.header("Resumen del Proyecto")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Registros",
    f"{df.shape[0]}"
)

col2.metric(
    "Variables",
    f"{df.shape[1]}"
)

col3.metric(
    "Variables Numéricas",
    f"{df.select_dtypes(include='number').shape[1]}"
)

col4.metric(
    "Valores Faltantes",
    f"{df.isna().sum().sum()}"
)

# Principales hallazgos

st.divider()

st.header("Principales Hallazgos")

st.success("""
• Se realizó un proceso completo de inspección, limpieza y preparación del conjunto de datos, mejorando significativamente su calidad.

• Se corrigieron registros duplicados, valores inconsistentes, categorías equivalentes y valores faltantes mediante criterios estadísticos apropiados.

• El Análisis Exploratorio de Datos permitió comprender la distribución de las variables, identificar valores atípicos plausibles y analizar las relaciones existentes entre los distintos atributos.

• El Análisis de Componentes Principales permitió estudiar la estructura de las variables numéricas y comprender cómo se distribuye la variabilidad del conjunto de datos.

• El análisis mostró que fue necesario conservar las tres componentes principales para representar completamente la información disponible, por lo que el PCA resultó especialmente útil como herramienta de exploración e interpretación.

• La aplicación desarrollada en Streamlit integra todas las etapas del proyecto mediante una interfaz interactiva que facilita la exploración y comunicación de los resultados obtenidos.
""")

# Limitaciones

st.divider()

st.header("Limitaciones")

st.warning("""
• Los resultados obtenidos dependen de la calidad y representatividad del conjunto de datos analizado.

• Algunas variables presentaban valores faltantes e inconsistencias que debieron corregirse durante la etapa de preparación de datos.

• El PCA considera únicamente relaciones lineales entre las variables numéricas y su interpretación depende del análisis conjunto de las cargas factoriales.

• Los resultados obtenidos corresponden exclusivamente al conjunto de datos analizado y no deben generalizarse sin una validación adicional sobre nuevos datos.
""")

# Trabajo Futuro

st.divider()

st.header("Trabajo Futuro")

st.info("""
Como continuación de este proyecto podrían desarrollarse las siguientes líneas de trabajo:

• Incorporar nuevas variables que permitan caracterizar con mayor profundidad el comportamiento de los usuarios.

• Implementar modelos supervisados de clasificación o regresión utilizando el dataset preparado durante este proyecto.

• Comparar el PCA con otras técnicas de reducción de dimensionalidad y agrupamiento, como t-SNE, UMAP o algoritmos de clustering.

• Ampliar la aplicación desarrollada en Streamlit incorporando nuevas visualizaciones interactivas y métricas descriptivas.

• Publicar la aplicación mediante Streamlit Community Cloud para facilitar su acceso y difusión.
""")

# Conclusion final

st.divider()

st.header("Conclusión Final")

st.markdown("""
El desarrollo de este Proyecto Integrador permitió aplicar de manera práctica las principales etapas del proceso de minería de datos, desde la inspección inicial del conjunto de datos hasta su preparación, análisis exploratorio y estudio mediante Análisis de Componentes Principales.

La calidad del análisis alcanzado fue posible gracias a un proceso sistemático de limpieza y preparación de los datos, que permitió corregir inconsistencias, normalizar variables e imputar valores faltantes utilizando criterios metodológicamente adecuados.

El Análisis Exploratorio proporcionó una comprensión detallada de la estructura del conjunto de datos, mientras que el PCA permitió estudiar la relación existente entre las variables numéricas y representar la información en un nuevo espacio de componentes principales, favoreciendo su interpretación.

Finalmente, la aplicación desarrollada en Streamlit integra todas las etapas del proyecto en una única interfaz interactiva, facilitando la exploración, visualización y comunicación de los resultados obtenidos. En conjunto, el proyecto evidencia la importancia de una adecuada preparación de los datos como fundamento para obtener análisis confiables y conclusiones consistentes dentro del proceso de minería de datos.
""")