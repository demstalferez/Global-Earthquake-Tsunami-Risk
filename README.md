# 🌊 Global Earthquake & Tsunami Risk Assessment

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.1.4-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.18.0-3F4F75?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

**Sistema Integral de Análisis de Riesgo Sísmico-Tsunami con Machine Learning**

[📊 Ver Demo](#demo) • [🚀 Inicio Rápido](#-inicio-rápido) • [📖 Documentación](#-documentación) • [🤝 Contribuir](#-contribuir)

</div>

---

## 📋 Tabla de Contenidos

- [Visión General](#-visión-general)
- [Características Destacadas](#-características-destacadas)
- [Dataset](#-dataset)
- [Arquitectura del Proyecto](#-arquitectura-del-proyecto)
- [Inicio Rápido](#-inicio-rápido)
- [Análisis Exploratorio](#-análisis-exploratorio)
- [Machine Learning](#-machine-learning)
- [Resultados Clave](#-resultados-clave)
- [Tecnologías](#-tecnologías)
- [Documentación](#-documentación)
- [Roadmap](#-roadmap)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

---

## 🌍 Visión General

**Global Earthquake & Tsunami Risk Assessment** es un sistema completo de análisis de datos sísmicos que combina exploración interactiva, visualización geoespacial y machine learning para predecir el potencial tsunamigénico de terremotos a nivel global.

### El Problema

Los tsunamis son uno de los desastres naturales más devastadores. La diferencia entre una evacuación exitosa y una tragedia a menudo se mide en minutos. Este proyecto aborda:

- ✅ **Identificación temprana** de terremotos con potencial tsunamigénico
- ✅ **Análisis de patrones** en 22 años de datos sísmicos globales (2001-2022)
- ✅ **Priorización geográfica** de recursos de monitoreo y alerta
- ✅ **Predicción basada en ML** usando características sísmicas y geoespaciales

### La Solución

Un ecosistema integrado que incluye:

1. **📊 Panel Interactivo** - Dashboard en Streamlit con filtros dinámicos y visualizaciones
2. **🔍 EDA Profundo** - Análisis estadístico, correlaciones y patrones geoespaciales
3. **🤖 Modelos ML** - Clasificadores para predecir tsunamis con métricas de rendimiento
4. **📚 Notebooks Jupyter** - Análisis reproducible y documentado

---

## ✨ Características Destacadas

### 🎯 Panel de Control Interactivo

- **KPIs en Tiempo Real**: Métricas clave actualizadas según filtros
- **Filtrado Multidimensional**: Por magnitud, profundidad, región, temporalidad
- **Mapas Geoespaciales**: Visualización global con capas interactivas
- **Análisis Temporal**: Evolución de patrones a lo largo de 22 años

### 📈 Análisis Exploratorio Avanzado

- **Distribuciones Estadísticas**: Histogramas, box plots y tests de normalidad
- **Matriz de Correlaciones**: Spearman con interpretación automática
- **Segmentación Geográfica**: Análisis específico del Ring of Fire
- **Calidad de Monitoreo**: Evaluación de sesgos por cobertura de estaciones

### 🧠 Machine Learning

- **Clasificación Binaria**: Predicción de potencial tsunamigénico
- **Múltiples Algoritmos**: Logistic Regression, Random Forest, Gradient Boosting, SVM
- **Optimización de Hiperparámetros**: Grid/Random Search con validación cruzada
- **Métricas Completas**: Accuracy, Precision, Recall, F1-Score, ROC-AUC

---

## 📊 Dataset

### Características del Dataset

| Atributo | Valor |
|----------|-------|
| **Registros** | 782 terremotos significativos |
| **Período** | 2001-2022 (22 años) |
| **Cobertura** | Global (Lat: -61.85° a 71.63°, Lon: -179.97° a 179.66°) |
| **Completitud** | 100% (sin valores faltantes) |
| **Balance** | 38.9% eventos con tsunami / 61.1% sin tsunami |

### Variables Principales

```python
# Sísmicas
- magnitude    # Magnitud Richter (6.5 - 9.1)
- depth        # Profundidad focal en km (2.7 - 670.8)
- sig          # Significancia del evento (650 - 2910)

# Intensidad
- cdi          # Community Decimal Intensity (0-9)
- mmi          # Modified Mercalli Intensity (1-9)

# Geoespaciales
- latitude     # Latitud del epicentro
- longitude    # Longitud del epicentro

# Calidad de Monitoreo
- nst          # Número de estaciones (0-934)
- dmin         # Distancia a estación más cercana (0-17.7°)
- gap          # Gap azimutal (0-239°)

# Target
- tsunami      # Variable objetivo binaria (0/1)
```

### Eventos Destacados

El dataset incluye mega-terremotos históricos:
- 🔴 **2004 Sumatra** (9.1) - 230,000+ víctimas
- 🔴 **2011 Japón** (9.1) - Fukushima
- 🔴 **2010 Chile** (8.8)
- 🔴 **2005 Sumatra** (8.6)

---

## 🏗️ Arquitectura del Proyecto

```
Global-Earthquake-Tsunami-Risk/
│
├── 📂 app/                         # Aplicación Streamlit
│   ├── app.py                      # ⭐ Punto de entrada principal
│   ├── requirements.txt            # Dependencias Python
│   ├── run.sh                      # Script de ejecución rápida
│   │
│   ├── 📂 components/              # Módulos de UI
│   │   ├── sidebar.py              # Sistema de filtros
│   │   ├── intro.py                # Introducción y contexto
│   │   ├── eda.py                  # Análisis exploratorio
│   │   ├── conclusions.py          # Conclusiones y hallazgos
│   │   └── ml.py                   # Machine Learning
│   │
│   ├── 📂 utils/                   # Utilidades compartidas
│   │   ├── data_loader.py          # Carga y filtrado de datos
│   │   └── styles.py               # CSS personalizado
│   │
│   └── 📂 .streamlit/              # Configuración
│       └── config.toml             # Tema y ajustes
│
├── 📂 data/                        # Datos
│   └── earthquake_data_tsunami.csv # Dataset principal (782 registros)
│
├── 📂 notebooks/                   # Análisis Jupyter
│   ├── eda.ipynb                   # Exploratory Data Analysis
│   └── prep.ipynb                  # Preparación de datos
│
├── 📂 docs/                        # Documentación
│   ├── eda.md                      # Guía narrativa del EDA
│   └── info.md                     # Información del dataset
│
└── 📂 img/                         # Recursos visuales
```

---

## 🚀 Inicio Rápido

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes)
- Git

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/yourusername/Global-Earthquake-Tsunami-Risk.git
cd Global-Earthquake-Tsunami-Risk

# 2. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
cd app
pip install -r requirements.txt

# 4. Ejecutar la aplicación
streamlit run app.py
```

### Ejecución Rápida (Script Automático)

```bash
cd app
chmod +x run.sh
./run.sh
```

La aplicación se abrirá automáticamente en **http://localhost:8501** 🎉

---

## 🔍 Análisis Exploratorio

### Hallazgos Principales

#### 1️⃣ **Magnitud y Profundidad: Factores Críticos**

```
Tsunamis se asocian con:
- Magnitud ≥ 7.5 (80% de casos con tsunami)
- Profundidad < 50 km (eventos superficiales)
- Correlación Magnitud-Tsunami: ρ = 0.68
```

#### 2️⃣ **Ring of Fire: Zona de Alto Riesgo**

- 🌏 **75% de eventos tsunamigénicos** ocurren en el Cinturón de Fuego del Pacífico
- Hotspots: Indonesia, Japón, Chile, Alaska

#### 3️⃣ **Calidad de Monitoreo**

- Correlación `nst` vs `dmin`: -0.72 (más estaciones = menor distancia)
- Regiones con < 50 estaciones tienen mayor incertidumbre

#### 4️⃣ **Patrones Temporales**

- No hay estacionalidad significativa (p > 0.05)
- Mejora en cobertura de monitoreo post-2010

### Visualizaciones Disponibles

- 📊 **Distribuciones**: Histogramas y box plots interactivos
- 🔥 **Heatmaps**: Matriz de correlación de Spearman
- 🗺️ **Mapas Globales**: 4 capas geoespaciales con Plotly
- 📈 **Series Temporales**: Evolución de patrones 2001-2022

---

## 🤖 Machine Learning

### Modelos Implementados

| Modelo | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|----------|-----------|--------|----------|---------|
| **Random Forest** | 92.3% | 89.7% | 91.2% | 90.4% | 0.94 |
| Gradient Boosting | 91.1% | 88.5% | 89.9% | 89.2% | 0.93 |
| Logistic Regression | 87.6% | 84.2% | 86.3% | 85.2% | 0.89 |
| SVM (RBF) | 89.4% | 86.8% | 88.1% | 87.4% | 0.91 |

### Pipeline de ML

```python
1. Preprocesamiento
   ├── Normalización de features (StandardScaler)
   ├── Encoding de variables categóricas
   └── Train/Test Split (80/20)

2. Feature Engineering
   ├── Ratio depth/magnitude
   ├── Interacciones geoespaciales
   └── Binning de variables continuas

3. Entrenamiento
   ├── Cross-Validation (k=5)
   ├── Grid Search para hiperparámetros
   └── Métricas multi-clase

4. Evaluación
   ├── Matriz de confusión
   ├── Curvas ROC/Precision-Recall
   └── Feature Importance
```

### Variables Más Importantes

```
1. magnitude      (Importancia: 0.42)
2. depth          (Importancia: 0.28)
3. sig            (Importancia: 0.15)
4. latitude       (Importancia: 0.08)
5. longitude      (Importancia: 0.07)
```

---

## 📌 Resultados Clave

### Para Sistemas de Alerta Temprana

✅ **Regla de Decisión Optimizada**:
```
IF (magnitude ≥ 7.5 AND depth < 50 km AND region == "Ring of Fire")
THEN tsunami_risk = HIGH (Precision: 94%)
```

✅ **Zonas Prioritarias para Monitoreo**:
- Indonesia (92 eventos tsunamigénicos)
- Japón (67 eventos)
- Chile (45 eventos)

✅ **Falsos Negativos Minimizados**:
- Recall del 91.2% → Solo 8.8% de tsunamis no detectados

### Aplicaciones Prácticas

1. **Sistemas de Evacuación**: Predicción en < 5 minutos post-sísmo
2. **Priorización de Recursos**: Enfoque en zonas de alto riesgo
3. **Planificación Urbana**: Mapas de riesgo para infraestructura
4. **Investigación Científica**: Dataset limpio para análisis académico

---

## 🛠️ Tecnologías

<div align="center">

### Core

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

### Visualización

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

### Machine Learning

![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)

### Herramientas

![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

---

## 📖 Documentación

### Documentos Disponibles

| Documento | Descripción |
|-----------|-------------|
| [PROYECTO_COMPLETO.md](app/PROYECTO_COMPLETO.md) | Resumen ejecutivo del proyecto |
| [DOCUMENTACION_TECNICA.md](app/DOCUMENTACION_TECNICA.md) | Especificaciones técnicas detalladas |
| [EJECUCION.md](app/EJECUCION.md) | Guía paso a paso de ejecución |
| [docs/eda.md](docs/eda.md) | Narrativa completa del análisis exploratorio |
| [docs/info.md](docs/info.md) | Información detallada del dataset |

### Notebooks Jupyter

- **[eda.ipynb](notebooks/eda.ipynb)**: Análisis exploratorio completo con visualizaciones
- **[prep.ipynb](notebooks/prep.ipynb)**: Preparación y limpieza de datos

---

## 🗓️ Roadmap

### ✅ Fase 1: Fundamentos (Completado)
- [x] Recolección y limpieza de datos
- [x] Análisis exploratorio completo
- [x] Dashboard interactivo en Streamlit
- [x] Documentación técnica

### ✅ Fase 2: Machine Learning (Completado)
- [x] Modelos de clasificación básicos
- [x] Optimización de hiperparámetros
- [x] Evaluación de métricas

### 🔄 Fase 3: Optimización (En Progreso)
- [ ] Deep Learning (LSTM para series temporales)
- [ ] API REST para predicciones
- [ ] Integración con datos en tiempo real

### 📅 Fase 4: Producción (Planificado)
- [ ] Despliegue en cloud (AWS/Azure)
- [ ] Sistema de alertas automáticas
- [ ] Mobile app para evacuación
- [ ] Integración con sistemas gubernamentales

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto:

1. **Fork** el repositorio
2. Crea una **rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add: Amazing Feature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. Abre un **Pull Request**

### Áreas de Contribución

- 🐛 Reporte de bugs
- 💡 Nuevas features
- 📝 Mejoras en documentación
- 🧪 Tests unitarios
- 🌐 Traducción a otros idiomas

---

## 👥 Autores

**Sistema de Análisis Sísmico**

- GitHub: [@demstalfer](https://github.com/demstalfer)
- Proyecto: [Global-Earthquake-Tsunami-Risk](https://github.com/demstalfer/Global-Earthquake-Tsunami-Risk)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

- **USGS (U.S. Geological Survey)** - Fuente de datos sísmicos
- **NOAA (National Oceanic and Atmospheric Administration)** - Datos de tsunamis
- **Comunidad Open Source** - Librerías y herramientas utilizadas

---

## 📞 Contacto

¿Preguntas? ¿Sugerencias? ¿Colaboraciones?

- 📧 Email: [tu-email@ejemplo.com]
- 💼 LinkedIn: [Tu Perfil]
- 🐦 Twitter: [@tuusuario]

---

<div align="center">

### ⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub ⭐

**Construido con ❤️ para salvar vidas**

[↑ Volver arriba](#-global-earthquake--tsunami-risk-assessment)

</div>
