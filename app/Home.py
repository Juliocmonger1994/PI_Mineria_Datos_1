import streamlit as st

# ---------------------------------------------------------
# Configuración de la página
# ---------------------------------------------------------

st.set_page_config(
    page_title="Proyecto Integrador - Minería de Datos I",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Encabezado
# ---------------------------------------------------------

st.title("📊 Proyecto Integrador - Minería de Datos I")

st.subheader("Análisis Exploratorio de Datos de Usuarios de Plataformas de Streaming")

st.markdown("---")

# ---------------------------------------------------------
# Presentación
# ---------------------------------------------------------

st.markdown("""
Bienvenido a la aplicación desarrollada para el **Proyecto Integrador de la asignatura Minería de Datos I**.

En este trabajo se realizó un proceso completo de minería de datos sobre un conjunto de información correspondiente a usuarios de plataformas de streaming.

La aplicación resume los principales resultados obtenidos durante las distintas etapas del proyecto y permite explorar de manera interactiva los análisis realizados.
""")

# ---------------------------------------------------------
# Objetivo
# ---------------------------------------------------------

st.info("""
**Objetivo del proyecto**

Analizar un conjunto de datos de usuarios de plataformas de streaming mediante técnicas de inspección, preparación de datos, análisis exploratorio y reducción de dimensionalidad, con el propósito de identificar patrones relevantes y comunicar los resultados de forma clara e interactiva.
""")

# ---------------------------------------------------------
# Contenido de la aplicación
# ---------------------------------------------------------

st.markdown("## 📌 Contenido")

st.markdown("""
Desde el menú lateral podrá acceder a las siguientes secciones:

- 📂 **Dataset**
    - Descripción del conjunto de datos.
    - Variables analizadas.
    - Estadísticas generales.

- 📊 **Análisis Exploratorio (EDA)**
    - Distribuciones.
    - Variables numéricas.
    - Variables categóricas.
    - Relaciones entre variables.

- 📉 **PCA**
    - Escalamiento.
    - Componentes principales.
    - Varianza explicada.

- 📝 **Conclusiones**
    - Principales hallazgos.
    - Limitaciones.
    - Mejoras futuras.
""")

# ---------------------------------------------------------
# Descripción del Dataset
# ---------------------------------------------------------

st.markdown("## 📂 Dataset analizado")

st.write("""
El proyecto se desarrolló utilizando un conjunto de datos correspondiente a usuarios
de plataformas de streaming.

Durante el proceso de minería de datos se realizaron tareas de inspección,
limpieza, preparación, análisis exploratorio y reducción de dimensionalidad,
con el objetivo de comprender mejor la estructura del dataset e identificar
patrones relevantes.
""")

# ---------------------------------------------------------
# Flujo de Trabajo
# ---------------------------------------------------------

st.markdown("## 🔄 Flujo de trabajo")

st.markdown("""
1. 🔎 Inspección inicial del dataset

2. 🧹 Limpieza y preparación de datos

3. 📊 Análisis Exploratorio (EDA)

4. 📉 Escalamiento y PCA

5. 📝 Conclusiones
""")

# ---------------------------------------------------------
# Tecnologías Utilizadas
# ---------------------------------------------------------

st.markdown("## 🛠️ Tecnologías utilizadas")

st.markdown("""
- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- Streamlit
""")

# ---------------------------------------------------------
# Próximas Páginas
# ---------------------------------------------------------

st.success("""
Utilice el menú lateral para navegar entre las distintas etapas del proyecto.

📂 Dataset

📊 Análisis Exploratorio

📉 PCA

📝 Conclusiones
""")