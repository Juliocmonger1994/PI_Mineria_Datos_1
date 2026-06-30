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

El objetivo es reducir la dimensionalidad del dataset, conservando la mayor cantidad posible de información y facilitando la identificación de patrones entre las variables numéricas.
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
explican al menos el **80 %** de la variabilidad del conjunto
de datos.

Esto indica que es posible representar la información
original utilizando un número menor de variables, reduciendo
la dimensionalidad sin perder una parte importante de la
información.
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
Las cargas (loadings) indican la contribución de cada variable original en la construcción de los componentes principales.

Las variables con valores absolutos más elevados son las que tienen mayor influencia en cada componente y permiten interpretar qué información resume cada uno de ellos.
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
La proyección sobre los dos primeros componentes principales permite representar cada observación del conjunto de datos en un espacio bidimensional.

Como PC1 y PC2 concentran la mayor parte de la variabilidad del dataset, este gráfico facilita la identificación de patrones generales, agrupamientos y posibles valores atípicos sin necesidad de visualizar todas las variables originales simultáneamente.
""")

