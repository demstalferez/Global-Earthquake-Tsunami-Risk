# Panel de Inteligencia: Riesgo Global de Terremotos y Tsunamis

## 🌊 Descripción

Panel interactivo desarrollado en Streamlit para el análisis exploratorio de datos sísmicos globales (2001-2022) con enfoque en la identificación de factores asociados a la generación de tsunamis.

## 🚀 Características

- 📊 **Análisis Exploratorio Completo**: Distribuciones, correlaciones y estadísticas descriptivas
- 🗺️ **Visualizaciones Geoespaciales**: Mapas interactivos globales con múltiples capas
- ⏱️ **Análisis Temporal**: Evolución de patrones a lo largo de 22 años
- 🎯 **Sistema de Filtros**: Controles interactivos para exploración personalizada
- 📌 **Conclusiones y Recomendaciones**: Insights accionables para sistemas de alerta
- 🤖 **Roadmap ML**: Preparación para modelos predictivos

## 📂 Estructura del Proyecto

```
app/
├── app.py                      # Aplicación principal
├── components/                 # Componentes modulares
│   ├── __init__.py
│   ├── sidebar.py             # Menú lateral con filtros
│   ├── intro.py               # Sección de introducción
│   ├── eda.py                 # Análisis exploratorio completo
│   ├── conclusions.py         # Conclusiones y recomendaciones
│   └── ml.py                  # Sección de Machine Learning
├── utils/                     # Utilidades
│   ├── __init__.py
│   ├── data_loader.py         # Carga y filtrado de datos
│   └── styles.py              # CSS personalizado
└── requirements.txt           # Dependencias
```

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/yourusername/Global-Earthquake-Tsunami-Risk.git
cd Global-Earthquake-Tsunami-Risk
```

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
cd app
pip install -r requirements.txt
```

## 🚀 Ejecución

Desde la carpeta `app/`, ejecutar:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`

## 📊 Datos

Los datos provienen del catálogo de terremotos del USGS (United States Geological Survey):
- **Período**: 2001-2022
- **Eventos**: ~800 terremotos de magnitud ≥ 6.5
- **Variables**: Magnitud, profundidad, ubicación, tsunami, significancia, calidad de monitoreo

## 🎨 Características Técnicas

### Arquitectura

- **Framework**: Streamlit (Python)
- **Visualizaciones**: Plotly Express & Plotly Graph Objects
- **Análisis Estadístico**: SciPy, NumPy, Pandas
- **Diseño**: CSS personalizado con tema oscuro
- **Responsividad**: Diseño adaptativo multi-dispositivo

### Componentes Modulares

```python
# Estructura modular para fácil mantenimiento
from components.sidebar import render_sidebar
from components.eda import render_eda_section
from utils.data_loader import load_data, get_filtered_data
from utils.styles import apply_custom_css
```

### Caching Inteligente

```python
@st.cache_data(ttl=3600)  # Cache de 1 hora
def load_data() -> pd.DataFrame:
    # Carga optimizada de datos
```

## 🔍 Funcionalidades Principales

### 1. Filtros Interactivos

- **Temporales**: Rango de años, meses específicos
- **Sísmicos**: Magnitud, profundidad
- **Geográficos**: Ring of Fire, regiones personalizadas
- **Estado**: Con/sin tsunami

### 2. Análisis Exploratorio (EDA)

- **Distribuciones**: Histogramas, box plots, pruebas de normalidad
- **Correlaciones**: Matriz de Spearman con heatmap interactivo
- **Mapas Geoespaciales**: 
  - Distribución global por magnitud
  - Tsunamis vs profundidad
  - Ring of Fire y zonas de alto riesgo
  - Calidad del monitoreo sísmico
- **Análisis Temporal**: Evolución anual y mensual
- **Multivariable**: Scatter 3D, histogramas comparativos

### 3. Conclusiones

- Hallazgos principales del análisis
- Recomendaciones para sistemas de alerta
- Estrategias de modelado predictivo
- Mejoras en infraestructura de monitoreo

### 4. Machine Learning (Próximamente)

- Roadmap de desarrollo
- Arquitectura propuesta
- Demo interactiva con simulación
- Recursos y documentación

## 📈 Métricas y KPIs

El panel incluye métricas clave en tiempo real:

- 📊 **Total de Eventos**: Conteo de terremotos filtrados
- 🌊 **Tsunamis**: Número y porcentaje de eventos tsunamigénicos
- 📈 **Magnitud Promedio**: Media de magnitudes en la selección
- 🌍 **Profundidad Promedio**: Media de profundidades
- ⚡ **Significancia Máxima**: Evento más significativo

## 🎯 Casos de Uso

1. **Investigación Científica**: Análisis de patrones sísmicos globales
2. **Sistemas de Alerta**: Diseño de umbrales y niveles de alerta
3. **Gestión de Riesgos**: Identificación de zonas de alto riesgo
4. **Educación**: Herramienta didáctica para sismología
5. **Política Pública**: Priorización de inversiones en monitoreo

## 🧪 Próximos Desarrollos

- [ ] Modelo predictivo de tsunamis (Random Forest / XGBoost)
- [ ] API REST para predicciones en tiempo real
- [ ] Integración con datos en vivo del USGS
- [ ] Alertas automáticas por email/SMS
- [ ] Análisis de series temporales (ARIMA/LSTM)
- [ ] Exportación de reportes en PDF

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 📧 Contacto

- **Autor**: Tu Nombre
- **Email**: your.email@example.com
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Proyecto**: [Global-Earthquake-Tsunami-Risk](https://github.com/yourusername/Global-Earthquake-Tsunami-Risk)

## 🙏 Agradecimientos

- **USGS** por proporcionar los datos sísmicos
- **Streamlit** por el framework de desarrollo
- **Plotly** por las visualizaciones interactivas
- Comunidad de código abierto

---

**⚠️ Disclaimer**: Este panel es una herramienta de análisis y no debe usarse como único sistema de alerta de tsunamis. Para alertas oficiales, consulte siempre las autoridades locales y el [NOAA Tsunami Warning Center](https://www.tsunami.gov/).
