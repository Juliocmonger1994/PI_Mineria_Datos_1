import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# Configuración de la página
# ---------------------------------------------------------

st.set_page_config(
    page_title="Dataset",
    page_icon="📂",
    layout="wide"
)

# Titulo

st.title("📂 Dataset")

st.markdown("""
En esta sección se presenta una descripción general del conjunto de datos utilizado
durante el Proyecto Integrador.

Se muestran sus principales características estructurales con el propósito de
proporcionar una visión inicial antes de avanzar hacia el análisis exploratorio
y la aplicación de técnicas de minería de datos.
""")

st.markdown("---")

# Cargar el Dataset

from pathlib import Path

# ---------------------------------------------------------
# Carga del dataset
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

DATASET = BASE_DIR / "data" / "processed" / "dataset_final.csv"

if DATASET.exists():
    df = pd.read_csv(DATASET)
else:
    st.error(f"No se encontró el archivo:\n{DATASET}")
    st.stop()

# ---------------------------------------------------------
# Indicadores del dataset
# ---------------------------------------------------------

st.markdown("## 📊 Información general")

num_registros = df.shape[0]
num_variables = df.shape[1]

num_numericas = df.select_dtypes(include="number").shape[1]

num_categoricas = df.select_dtypes(exclude="number").shape[1]

# Cantidad total de valores faltantes
valores_faltantes = df.isna().sum().sum()

# Cantidad total de celdas del dataset
total_celdas = df.shape[0] * df.shape[1]

# Porcentaje de calidad del dataset
calidad = ((total_celdas - valores_faltantes) / total_celdas) * 100

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    st.metric("📄 Registros", num_registros)

with col2:
    st.metric("🧩 Variables", num_variables)

with col3:
    st.metric("🔢 Numéricas", num_numericas)

with col4:
    st.metric("🏷️ Categóricas", num_categoricas)

with col5:
    st.metric("🚨 Valores faltantes", valores_faltantes)

with col6:
    st.metric("✅ Calidad", f"{calidad:.2f}%")

# Vista Previa

st.markdown("---")

st.markdown("## 👀 Vista previa del dataset")

cantidad_filas = st.selectbox(
    "Seleccione la cantidad de filas a visualizar:",
    [5, 10, 20, 50]
)

st.dataframe(
    df.head(cantidad_filas),
    use_container_width=True
)

# Información de Variables

st.markdown("---")

st.markdown("## 📝 Variables del dataset")

tipos = pd.DataFrame({
    "Variable": df.columns,
    "Tipo de dato": df.dtypes.astype(str)
})

st.dataframe(tipos, use_container_width=True)

# Estadísticas Descriptivas
st.markdown("---")

st.markdown("## 📈 Estadísticas descriptivas")

st.dataframe(df.describe())

# Valores Faltantes

st.markdown("---")

st.markdown("## 🚨 Valores faltantes")

faltantes = df.isna().sum()

faltantes = faltantes[faltantes > 0]

if faltantes.empty:

    st.success("No se encontraron valores faltantes en el dataset.")

else:

    st.dataframe(faltantes)

