# Guía de Ejecución del Panel de Inteligencia Sísmico

## 🚀 Inicio Rápido

### Opción 1: Ejecución Directa

```bash
# Navegar a la carpeta app
cd app

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
streamlit run app.py
```

### Opción 2: Con Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En macOS/Linux:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
cd app
streamlit run app.py
```

## 🔧 Configuración

### Variables de Entorno (opcional)

Crear archivo `.streamlit/config.toml` en la carpeta `app/`:

```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#1e1e1e"
textColor = "#fafafa"
font = "sans serif"

[server]
port = 8501
headless = false
enableCORS = false
enableXsrfProtection = true
maxUploadSize = 200

[browser]
gatherUsageStats = false
```

## 📊 Navegación del Panel

### Menú Lateral (Sidebar)
- **Filtros Temporales**: Ajusta el período de análisis
- **Filtros Sísmicos**: Define rangos de magnitud y profundidad
- **Filtros de Tsunami**: Enfócate en eventos específicos
- **Filtros Geográficos**: Analiza regiones específicas

### Secciones Principales
1. **Introducción & Contexto**: Resumen ejecutivo y objetivos
2. **Análisis Exploratorio (EDA)**: Visualizaciones y estadísticas
3. **Conclusiones & Recomendaciones**: Insights accionables
4. **Machine Learning**: Roadmap y demo interactiva

## 🐛 Solución de Problemas

### Error: "No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### Error: "FileNotFoundError: earthquake_data_tsunami.csv"
Verificar que el archivo CSV esté en `data/earthquake_data_tsunami.csv`

### Puerto 8501 ocupado
```bash
streamlit run app.py --server.port 8502
```

### Problemas de memoria con datasets grandes
Ajustar el tamaño de muestra en visualizaciones (ver `eda.py`)

## 💡 Tips de Uso

1. **Filtros**: Los filtros se aplican automáticamente sin necesidad de botón "Aplicar"
2. **Rendimiento**: Reducir rango de años para mejorar velocidad
3. **Exportación**: Usar botón de descarga de Plotly en gráficos interactivos
4. **Fullscreen**: Click en "⤢" en las esquinas de los gráficos

## 📝 Notas

- La aplicación usa caching para optimizar el rendimiento
- Los datos se cargan una vez al iniciar y se filtran en memoria
- Las visualizaciones son completamente interactivas (zoom, pan, hover)
