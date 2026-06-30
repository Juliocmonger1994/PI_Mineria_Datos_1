# Proyecto Integrador – Minería de Datos I

## Tecnicatura Universitaria en Inteligencia Artificial

Este proyecto fue desarrollado como trabajo integrador de la asignatura **Minería de Datos I**, con el objetivo de aplicar de forma práctica las principales etapas del proceso de minería de datos sobre un conjunto de datos real.

Durante el desarrollo se llevó a cabo un flujo de trabajo completo que incluyó la inspección inicial del dataset, la limpieza y preparación de los datos, el análisis exploratorio (EDA), el escalamiento de variables, la aplicación del Análisis de Componentes Principales (PCA) y la construcción de una aplicación interactiva mediante **Streamlit** para comunicar los resultados obtenidos.

El proyecto fue desarrollado íntegramente en Python utilizando herramientas ampliamente empleadas en Ciencia de Datos, priorizando la reproducibilidad, la claridad metodológica y la interpretación de los resultados.

---

# Objetivos

## Objetivo General

Aplicar un proceso completo de minería de datos sobre un conjunto de datos real, utilizando técnicas de preparación, exploración, análisis estadístico y reducción de dimensionalidad, complementado con una aplicación interactiva para la visualización de los resultados.

## Objetivos Específicos

* Inspeccionar y comprender la estructura del conjunto de datos.
* Realizar el proceso de limpieza y preparación de los datos.
* Analizar las variables mediante técnicas de Análisis Exploratorio de Datos (EDA).
* Identificar relaciones entre variables utilizando matrices de correlación y gráficos estadísticos.
* Aplicar técnicas de escalamiento para preparar los datos antes del análisis multivariado.
* Implementar el Análisis de Componentes Principales (PCA) para reducir la dimensionalidad del conjunto de datos.
* Interpretar los componentes principales y la varianza explicada.
* Desarrollar una aplicación interactiva con Streamlit que permita explorar los resultados de forma dinámica.
* Documentar todo el proceso de manera reproducible y organizada mediante notebooks y un repositorio en GitHub.

---

# Estructura del Proyecto

El repositorio se encuentra organizado siguiendo una estructura orientada a facilitar la reproducibilidad del análisis y la separación de cada etapa del proyecto.

```text
PI_MINERIA_DATOS_1/
│
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 01_Dataset.py
│       ├── 02_EDA.py
│       ├── 03_PCA.py
│       └── 04_Conclusiones.py
│
├── data/
│   ├── raw/
│   └── processed/
│       └── dataset_final.csv
│
├── logs/
│
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
│
├── reports/
│
├── README.md
└── requirements.txt
```

## Descripción de la estructura

| Carpeta / Archivo    | Descripción                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------- |
| **app/**             | Aplicación desarrollada con Streamlit para la visualización interactiva del proyecto.         |
| **data/raw/**        | Conjunto de datos original utilizado en el análisis.                                          |
| **data/processed/**  | Dataset procesado y utilizado durante las distintas etapas del proyecto.                      |
| **logs/**            | Carpeta destinada al almacenamiento de registros generados durante la ejecución del proyecto. |
| **notebooks/**       | Notebooks desarrolladas para cada etapa del proceso de minería de datos.                      |
| **reports/**         | Carpeta reservada para informes y documentación complementaria.                               |
| **README.md**        | Documento principal con la descripción del proyecto y las instrucciones de uso.               |
| **requirements.txt** | Archivo con las dependencias necesarias para ejecutar el proyecto.                            |

---

# Desarrollo del Proyecto

El proyecto se desarrolló siguiendo las principales etapas del proceso de minería de datos, desde la comprensión del conjunto de datos hasta la comunicación de los resultados mediante una aplicación interactiva.

| Etapa                              | Notebook                        | Descripción                                                                                                                                                             |
| ---------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Inspección del Dataset**      | `01_inspeccion_inicial.ipynb`   | Análisis inicial de la estructura del conjunto de datos, identificación de variables, tipos de datos, valores faltantes y evaluación general de la calidad del dataset. |
| **2. Limpieza y Preparación**      | `02_calidad_y_limpieza.ipynb` | Tratamiento de valores faltantes, estandarización de variables, transformación de datos y generación del dataset procesado utilizado en las etapas posteriores.         |
| **3. Análisis Exploratorio (EDA)** | `03_eda.ipynb`                  | Estudio de la distribución de las variables, análisis estadístico descriptivo, detección de valores atípicos y análisis de correlaciones mediante visualizaciones.      |
| **4. Escalamiento y PCA**          | `04_pca.ipynb`     | Escalamiento de las variables numéricas y aplicación del Análisis de Componentes Principales (PCA) para reducir la dimensionalidad y analizar la varianza explicada.    |
| **5. Conclusiones**                | `05_conclusiones.ipynb`         | Síntesis de los resultados obtenidos, interpretación del análisis realizado y principales conclusiones del proyecto.                                                    |

---

# Aplicación Interactiva

Como complemento de las notebooks, se desarrolló una aplicación utilizando **Streamlit** con el propósito de presentar los resultados del análisis de manera interactiva.

La aplicación permite recorrer las distintas etapas del proyecto mediante una interfaz organizada en páginas independientes:

| Página             | Descripción                                                                                                                                                                  |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **🏠 Home**        | Presentación del proyecto, objetivos, flujo de trabajo y tecnologías utilizadas.                                                                                             |
| **📄 Dataset**     | Exploración del conjunto de datos, métricas generales, calidad del dataset, estadísticas descriptivas y vista previa interactiva.                                            |
| **📊 EDA**         | Visualización interactiva de histogramas, boxplots, correlaciones, gráficos de dispersión e interpretación de los principales resultados del análisis exploratorio.          |
| **📈 PCA**         | Presentación de la varianza explicada, componentes principales, cargas (loadings), proyección de las observaciones e interpretación del Análisis de Componentes Principales. |
| **✅ Conclusiones** | Resumen de los principales resultados, hallazgos, limitaciones y conclusiones finales del proyecto.                                                                          |

---

# Tecnologías Utilizadas

El proyecto fue desarrollado utilizando las siguientes herramientas y bibliotecas:

* **Python 3**
* **Jupyter Notebook**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Streamlit**
* **Git**
* **GitHub**

---

# Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/USUARIO/PI_MINERIA_DATOS_1.git
```

2. Acceder a la carpeta del proyecto:

```bash
cd PI_MINERIA_DATOS_1
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

# Ejecución de la Aplicación

Una vez instaladas las dependencias, ejecutar el siguiente comando desde la carpeta raíz del proyecto:

```bash
streamlit run app/Home.py
```

La aplicación se abrirá automáticamente en el navegador predeterminado.

---

# Resultados Obtenidos

Durante el desarrollo del proyecto se logró:

* Implementar un proceso completo de minería de datos sobre un conjunto de datos real.
* Preparar y limpiar el dataset para su posterior análisis.
* Realizar un Análisis Exploratorio de Datos (EDA) mediante estadísticas descriptivas y visualizaciones interactivas.
* Analizar las relaciones entre variables utilizando matrices de correlación y gráficos de dispersión.
* Aplicar el Análisis de Componentes Principales (PCA) para reducir la dimensionalidad del conjunto de datos conservando la mayor parte de la información.
* Desarrollar una aplicación interactiva con Streamlit que permite explorar e interpretar los resultados de manera clara e intuitiva.
* Organizar el proyecto siguiendo buenas prácticas de documentación y reproducibilidad.

---

# Autor

**Julio César Monge Roldán**

Proyecto desarrollado como Trabajo Integrador para la asignatura **Minería de Datos I** de la **Tecnicatura Superior en Base de Datos e Inteligencia Artificial**.
