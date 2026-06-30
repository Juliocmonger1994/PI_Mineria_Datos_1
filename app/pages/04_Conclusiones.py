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
Esta sección resume los principales resultados obtenidos durante el desarrollo del Proyecto Integrador de Minería de Datos I.

A partir del proceso de inspección, preparación, análisis exploratorio y reducción de dimensionalidad mediante PCA, fue posible comprender las características del conjunto de datos e identificar los patrones más relevantes para su interpretación.
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
• Se realizó un proceso completo de inspección y preparación del conjunto de datos.

• El análisis exploratorio permitió estudiar la distribución de las variables, detectar posibles valores atípicos y analizar las relaciones entre los atributos.

• La matriz de correlación facilitó la identificación de variables relacionadas, aportando evidencia para la aplicación del PCA.

• El Análisis de Componentes Principales permitió reducir la dimensionalidad del conjunto de datos conservando una elevada proporción de la variabilidad original.

• La aplicación desarrollada integra todas las etapas del proceso de minería de datos mediante una interfaz interactiva que facilita la exploración y comprensión de los resultados.
""")

# Limitaciones

st.divider()

st.header("Limitaciones")

st.warning("""
• Los resultados obtenidos dependen de la calidad del conjunto de datos analizado.

• El PCA considera únicamente relaciones lineales entre las variables numéricas.

• La interpretación de los componentes principales requiere analizar conjuntamente las cargas de las variables originales.

• Los resultados corresponden exclusivamente al dataset utilizado en este proyecto y no deben generalizarse sin un análisis adicional.
""")

# Trabajo Futuro

st.divider()

st.header("Trabajo Futuro")

st.info("""
Como continuación de este proyecto podrían desarrollarse las siguientes líneas de trabajo:

• Incorporar nuevos registros para ampliar el conjunto de datos.

• Evaluar otras técnicas de reducción de dimensionalidad.

• Implementar modelos de aprendizaje automático utilizando el dataset procesado.

• Comparar el desempeño de diferentes algoritmos de minería de datos.

• Desplegar la aplicación utilizando Streamlit Community Cloud para facilitar su acceso.
""")

# Conclusion final

st.divider()

st.header("Conclusión Final")

st.markdown("""
El desarrollo de este Proyecto Integrador permitió aplicar de manera práctica las principales etapas del proceso de minería de datos, desde la inspección inicial del conjunto de datos hasta la reducción de dimensionalidad mediante Análisis de Componentes Principales.

La combinación de las notebooks desarrolladas y la aplicación interactiva en Streamlit favorece la reproducibilidad del análisis y la comunicación clara de los resultados, integrando herramientas de programación, análisis estadístico y visualización de datos en un único entorno.

En conjunto, el proyecto constituye una solución completa para la exploración, comprensión e interpretación del conjunto de datos analizado, evidenciando la importancia de un proceso sistemático en la obtención de conocimiento a partir de los datos.
""")