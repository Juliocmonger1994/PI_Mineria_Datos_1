# Configuracion de la pagina

import streamlit as st
import pandas as pd
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(
    page_title="PCA",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Análisis de Componentes Principales (PCA)")

# Introduccion

st.markdown("""
En esta sección se presenta el **Análisis de Componentes Principales (PCA)** aplicado al conjunto de datos.

El objetivo es estudiar la estructura de las variables numéricas mediante una transformación a un nuevo espacio de componentes principales, evaluando cuánta información puede resumirse en un menor número de dimensiones y facilitando la interpretación de los datos.
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

# Seleccion de Variable Numerica

numericas = df.select_dtypes(include="number")

# Escalamiento

scaler = StandardScaler()

datos_escalados = scaler.fit_transform(numericas)

# Aplicacion del PCA

pca = PCA()

componentes = pca.fit_transform(datos_escalados)

# Calcular la Varianza Explicada

varianza = pca.explained_variance_ratio_

varianza_acumulada = varianza.cumsum()

# Crear un DataFrame

df_varianza = pd.DataFrame({
    "Componente": [
        f"PC{i+1}"
        for i in range(len(varianza))
    ],
    "Varianza Explicada": varianza,
    "Varianza Acumulada": varianza_acumulada
})

# Mostrar la Tabla

st.subheader("Varianza Explicada")

st.dataframe(
    df_varianza.style.format({
        "Varianza Explicada":"{:.2%}",
        "Varianza Acumulada":"{:.2%}"
    }),
    use_container_width=True
)

# Grafico de Barras

fig, ax = plt.subplots(figsize=(10,5))

ax.bar(
    df_varianza["Componente"],
    df_varianza["Varianza Explicada"]
)

ax.set_ylabel("Varianza Explicada")

ax.set_xlabel("Componentes Principales")

ax.set_title("Varianza Explicada por cada Componente")

st.pyplot(fig)

# Graficos de Varianza Acumulada

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(
    range(1, len(varianza)+1),
    varianza_acumulada,
    marker="o"
)

ax.set_ylim(0,1.05)

ax.set_xlabel("Número de Componentes")

ax.set_ylabel("Varianza Acumulada")

ax.grid(True)

st.pyplot(fig)

# Intrerpretacion Automatica

componentes_80 = (
    (varianza_acumulada >= 0.80)
    .argmax() + 1
)

st.info(f"""
Los primeros **{componentes_80} componentes principales**
permiten alcanzar al menos el **80 %** de la varianza acumulada.

En este conjunto de datos fue necesario conservar las **tres componentes principales** para representar completamente la información original, por lo que el PCA resultó útil principalmente como herramienta de análisis e interpretación, más que como una técnica de reducción significativa de dimensionalidad.
""")

# CREAR LA MATRIZ DE LOADINGS

st.divider()

st.header("Contribución de las Variables")

loadings = pd.DataFrame(
    pca.components_.T,
    index=numericas.columns,
    columns=[f"PC{i+1}" for i in range(len(numericas.columns))]
)

# Mostrar los primeros dos componentes

st.subheader("Cargas de los Componentes Principales")

st.dataframe(
    loadings[["PC1", "PC2"]].style.format("{:.3f}"),
    use_container_width=True
)

# Resaltar las variebles mas influyentes

pc1 = loadings["PC1"].abs().sort_values(ascending=False)
pc2 = loadings["PC2"].abs().sort_values(ascending=False)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Variables más influyentes en PC1")
    st.write(pc1.head(3))

with col2:
    st.subheader("Variables más influyentes en PC2")
    st.write(pc2.head(3))

# Interpretacion

st.info("""
Las cargas (loadings) indican cuánto contribuye cada variable original a la formación de cada componente principal.

Valores absolutos elevados representan una mayor influencia sobre el componente correspondiente. Este análisis permite interpretar qué información resume cada componente y comprender cómo se distribuye la variabilidad entre las variables originales.
""")



# Crear el DataFrame

componentes = pca.fit_transform(datos_escalados)

st.divider()

st.header("Proyección de las Observaciones")

df_pca = pd.DataFrame(
    componentes,
    columns=[f"PC{i+1}" for i in range(componentes.shape[1])]
)

# Crear el grafico

fig, ax = plt.subplots(figsize=(10,6))

sns.scatterplot(
    data=df_pca,
    x="PC1",
    y="PC2",
    alpha=0.7,
    s=60,
    ax=ax
)

ax.set_xlabel("Primer Componente Principal (PC1)")
ax.set_ylabel("Segundo Componente Principal (PC2)")

ax.set_title("Proyección de las Observaciones")

st.pyplot(fig)

# Informacion Adicional

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Varianza explicada por PC1",
        f"{varianza[0]:.2%}"
    )

with col2:
    st.metric(
        "Varianza explicada por PC2",
        f"{varianza[1]:.2%}"
    )

# Interpretación

st.info("""
La proyección sobre los dos primeros componentes principales permite visualizar las observaciones en un espacio bidimensional y explorar la estructura general del conjunto de datos.

Si bien PC1 y PC2 concentran una proporción importante de la variabilidad, todavía existe información relevante representada por la tercera componente principal. Por este motivo, la proyección constituye una herramienta útil para la exploración visual, aunque no reemplaza completamente la información contenida en las variables originales.
""")

st.divider()

st.header("Conclusiones del PCA")

st.success("""
El Análisis de Componentes Principales permitió estudiar la estructura interna de las variables numéricas y analizar cómo se distribuye la variabilidad del conjunto de datos entre las distintas componentes principales.

Los resultados mostraron que ninguna componente domina claramente a las demás, por lo que fue necesario conservar las tres componentes para representar completamente la información disponible. En consecuencia, el PCA resultó especialmente útil como herramienta de exploración e interpretación de los datos, aunque no permitió una reducción significativa de la dimensionalidad.
""")

st.markdown("""
### Próxima etapa

En la última sección se presentan las conclusiones generales del proyecto, integrando los resultados obtenidos durante la limpieza de datos, el análisis exploratorio y el Análisis de Componentes Principales.
""")