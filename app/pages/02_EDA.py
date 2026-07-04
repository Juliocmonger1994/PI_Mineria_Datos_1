# -----------------------------------
# Seccion 1 - Encabezado
# -----------------------------------

import streamlit as st
import pandas as pd
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

# Consifuración

st.set_page_config(
    page_title="EDA",
    page_icon="📊",
    layout="wide"
)

# Titulo

st.title("📊 Análisis Exploratorio de Datos")

# Introduccion

st.markdown("""
En esta sección se presentan los principales resultados del Análisis Exploratorio de Datos (EDA).

El objetivo es comprender la distribución de las variables, identificar posibles valores atípicos, analizar relaciones entre atributos y descubrir patrones presentes en el conjunto de datos antes de aplicar técnicas de minería de datos.
""")

# -----------------------------------
# Seccion 2 - Carga del Dataset
# -----------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "dataset_final.csv"
)

df = pd.read_csv(DATA_PATH)

# -----------------------------------
# Seccion 3 - Variables Numéricas
# -----------------------------------

numericas = df.select_dtypes(include="number").columns.tolist()

variable = st.selectbox(
    "Seleccione una variable numérica",
    numericas
)

# -----------------------------------
# Seccion 4 - Análisis univariado de variables numéricas
# -----------------------------------

# Crear Columnas

col1, col2 = st.columns(2)

# Histograma

with col1:

    st.subheader("Distribución")

    fig, ax = plt.subplots(figsize=(7, 4))

    sns.histplot(
        data=df,
        x=variable,
        kde=True,
        color="steelblue",
        ax=ax
    )

    ax.set_xlabel(variable)
    ax.set_ylabel("Frecuencia")

    st.pyplot(fig)

# Boxplot

with col2:

    st.subheader("Valores Atípicos")

    fig, ax = plt.subplots(figsize=(7, 2.5))

    sns.boxplot(
        data=df,
        x=variable,
        color="lightcoral",
        ax=ax
    )

    ax.set_xlabel(variable)

    st.pyplot(fig)

# Agregar indicadores estadísticos

st.subheader("Resumen Estadístico")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Media", f"{df[variable].mean():.2f}")
col2.metric("Mediana", f"{df[variable].median():.2f}")
col3.metric("Desv. Estándar", f"{df[variable].std():.2f}")
col4.metric("Valores Únicos", df[variable].nunique())

# -----------------------------------
# Seccion 5 - Interpretación Automática de la Variable
# -----------------------------------

# Calcular Estadísticas

# Estadísticas de la variable seleccionada
asimetria = df[variable].skew()
faltantes = df[variable].isna().sum()

Q1 = df[variable].quantile(0.25)
Q3 = df[variable].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = (
    (df[variable] < limite_inferior) |
    (df[variable] > limite_superior)
).sum()

# Construir el texto dinamicamente

st.subheader("Interpretación")

texto = []

if abs(asimetria) < 0.5:
    texto.append(
        "• La distribución es aproximadamente simétrica."
    )

elif asimetria > 0.5:
    texto.append(
        "• La distribución presenta asimetría positiva (cola hacia la derecha)."
    )

else:
    texto.append(
        "• La distribución presenta asimetría negativa (cola hacia la izquierda)."
    )

if outliers > 0:
    texto.append(
        f"• Se detectaron {outliers} posibles valores atípicos según la regla del IQR."
    )
else:
    texto.append(
        "• No se detectaron valores atípicos mediante la regla del IQR."
    )

if faltantes > 0:
    texto.append(
        f"• La variable contiene {faltantes} valores faltantes."
    )
else:
    texto.append(
        "• La variable no presenta valores faltantes."
    )

st.info("\n\n".join(texto))


# -----------------------------------
# Seccion 6 - Análisis Bivariado
# -----------------------------------

# Matriz de Correlación

st.divider()

st.header("Relación entre Variables")

corr = df[numericas].corr()

numericas = df.select_dtypes(include="number").columns.tolist()


st.info("""
La matriz de correlación permite identificar relaciones lineales entre las variables numéricas.

Los coeficientes cercanos a **1** indican una fuerte relación positiva, los cercanos a **-1** una fuerte relación negativa y los próximos a **0** indican ausencia de relación lineal.

Este análisis resulta especialmente útil para detectar variables redundantes y fundamentar posteriormente la aplicación de técnicas de reducción de dimensionalidad como PCA.
""")

with st.expander("Ver matriz de correlación"):

    fig, ax = plt.subplots(figsize=(10,8))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        center=0,
        linewidths=.5,
        fmt=".2f",
        ax=ax
    )

    st.pyplot(fig)

# -----------------------------------
# Seccion 7 - Grafico de Dispersion Interactivo
# -----------------------------------

# Encabezado

st.divider()

st.header("Gráfico de Dispersión")

# Selectores

col_x, col_y = st.columns(2)

with col_x:
    variable_x = st.selectbox(
        "Variable del eje X",
        numericas,
        index=0,
        key="x"
    )

with col_y:
    variable_y = st.selectbox(
        "Variable del eje Y",
        numericas,
        index=1 if len(numericas) > 1 else 0,
        key="y"
    )

# Crear el grafico

fig, ax = plt.subplots(figsize=(9,6))

sns.scatterplot(
    data=df,
    x=variable_x,
    y=variable_y,
    alpha=0.7,
    ax=ax
)

ax.set_xlabel(variable_x)
ax.set_ylabel(variable_y)

st.pyplot(fig)

# Calcular la correlación del par seleccionado

correlacion = df[variable_x].corr(df[variable_y])

st.metric(
    "Correlación de Pearson",
    f"{correlacion:.3f}"
)

# Interpretacion Automatica

if abs(correlacion) >= 0.8:
    mensaje = (
        "Existe una relación lineal muy fuerte entre las variables seleccionadas."
    )

elif abs(correlacion) >= 0.6:
    mensaje = (
        "Se observa una relación lineal moderadamente fuerte entre las variables."
    )

elif abs(correlacion) >= 0.3:
    mensaje = (
        "La relación lineal entre las variables es moderada."
    )

else:
    mensaje = (
        "La relación lineal entre las variables es débil o prácticamente inexistente."
    )

st.info(mensaje)

# Separador

st.divider()

st.header("Conclusiones del Análisis Exploratorio")

# Texto de Conclusiones

st.success("""
El Análisis Exploratorio de Datos permitió comprender en profundidad las características del conjunto de datos mediante el estudio de la distribución de las variables, la identificación de valores atípicos y el análisis de las relaciones existentes entre los distintos atributos.

Las visualizaciones y herramientas interactivas incorporadas en esta aplicación facilitan la exploración individual de cada variable, el análisis de sus principales estadísticas descriptivas y la interpretación de las correlaciones presentes en el conjunto de datos.

Los resultados obtenidos durante esta etapa confirmaron que, luego del proceso de limpieza y preparación, el dataset presenta una estructura consistente y adecuada para la aplicación de técnicas multivariadas. Asimismo, el análisis exploratorio proporcionó la información necesaria para interpretar posteriormente los resultados del Análisis de Componentes Principales (PCA).
""")

# Transicion hacia PCA

st.markdown("""
### Próxima etapa

En la siguiente página se presenta el **Análisis de Componentes Principales (PCA)**, donde se analizará la estructura de las variables numéricas, la proporción de varianza explicada por cada componente principal y la utilidad del PCA como herramienta de exploración y representación del conjunto de datos.
""")
