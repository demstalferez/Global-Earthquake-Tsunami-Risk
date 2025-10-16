# Documentación Técnica del Panel de Inteligencia Sísmico

## 📐 Arquitectura del Sistema

### Estructura Modular

El panel está diseñado con una arquitectura modular para facilitar el mantenimiento, escalabilidad y colaboración:

```
app/
├── app.py                     # Orquestador principal
├── components/                # Módulos de UI
│   ├── sidebar.py            # Controles de filtrado
│   ├── intro.py              # Presentación y contexto
│   ├── eda.py                # Análisis exploratorio
│   ├── conclusions.py        # Hallazgos y recomendaciones
│   └── ml.py                 # Machine Learning (futuro)
├── utils/                    # Utilidades compartidas
│   ├── data_loader.py        # Gestión de datos
│   └── styles.py             # Estilos CSS
└── .streamlit/               # Configuración
    └── config.toml           # Tema y ajustes
```

### Flujo de Datos

```
CSV File → load_data() → DataFrame → Filters → Filtered DataFrame → Visualizations
                ↓
            Cache (1h TTL)
                ↓
        Feature Engineering
                ↓
        Derived Columns
```

## 🔧 Componentes Principales

### 1. `app.py` - Aplicación Principal

**Responsabilidades:**
- Inicialización de la aplicación
- Gestión del estado de sesión
- Coordinación de componentes
- Renderizado del layout principal

**Funciones Clave:**
```python
def init_session_state()  # Inicializa variables de sesión
def main()                # Función principal de orquestación
```

### 2. `utils/data_loader.py` - Carga de Datos

**Responsabilidades:**
- Carga optimizada del CSV
- Validación de datos
- Feature engineering
- Filtrado dinámico

**Funciones Clave:**
```python
@st.cache_data(ttl=3600)
def load_data() -> pd.DataFrame
    # Carga y prepara dataset
    # Returns: DataFrame con columnas derivadas

def get_filtered_data(df, filters) -> pd.DataFrame
    # Aplica filtros del usuario
    # Returns: DataFrame filtrado

def get_data_summary(df) -> Dict
    # Genera estadísticas de resumen
    # Returns: Diccionario con métricas
```

**Features Derivadas:**
- `shallow`: Binario para profundidad < 70 km
- `high_magnitude`: Binario para magnitud ≥ 7.0
- `ring_of_fire`: Pertenencia al Cinturón de Fuego
- `mag_category`: Categorías de magnitud
- `depth_category`: Categorías de profundidad

### 3. `utils/styles.py` - Estilos CSS

**Responsabilidades:**
- Tema visual personalizado
- Animaciones CSS
- Componentes responsivos
- Consistencia de diseño

**Clases CSS Disponibles:**
```css
.info-card        # Tarjeta informativa estándar
.warning-card     # Alerta/precaución
.danger-card      # Peligro/crítico
.success-card     # Éxito/confirmación
.main-header      # Cabecera principal
```

### 4. `components/sidebar.py` - Menú Lateral

**Responsabilidades:**
- Renderizar controles de filtrado
- Gestión de estado de filtros
- Información contextual

**Filtros Implementados:**
- Temporales: Años, meses
- Sísmicos: Magnitud, profundidad
- Tsunami: Con/sin/todos
- Geográficos: Regiones
- Visualización: Tema, opciones

**Return Type:**
```python
Dict[str, Any] = {
    'year_range': Tuple[int, int],
    'months': List[int],
    'magnitude_range': Tuple[float, float],
    'depth_range': Tuple[float, float],
    'tsunami_filter': str,
    'region_filter': str,
    'show_advanced': bool,
    'chart_theme': str
}
```

### 5. `components/eda.py` - Análisis Exploratorio

**Responsabilidades:**
- Visualizaciones estadísticas
- Mapas geoespaciales
- Análisis de correlaciones
- Pruebas estadísticas

**Subsecciones:**
1. **Distribuciones**: Histogramas, box plots, tests de normalidad
2. **Correlaciones**: Matriz de Spearman, análisis de pares
3. **Geoespacial**: 4 tipos de mapas interactivos
4. **Temporal**: Evolución anual y mensual
5. **Multivariable**: Scatter 3D, comparaciones

**Funciones Clave:**
```python
def render_eda_section(df)         # Renderiza sección completa
def render_distributions(df)       # Análisis de distribuciones
def render_correlations(df)        # Matriz de correlación
def render_geospatial(df)          # Mapas interactivos
def render_temporal(df)            # Series temporales
def render_multivariate(df)        # Análisis multivariable
```

### 6. `components/conclusions.py` - Conclusiones

**Responsabilidades:**
- Síntesis de hallazgos
- Recomendaciones estratégicas
- Próximos pasos
- Roadmap de desarrollo

**Subsecciones:**
- Hallazgos principales
- Recomendaciones para alertas
- Estrategias de modelado
- Mejoras en monitoreo

### 7. `components/ml.py` - Machine Learning

**Responsabilidades:**
- Roadmap de desarrollo ML
- Arquitectura propuesta
- Demo interactiva (simulación)
- Recursos y documentación

**Estado Actual:** Planificación y diseño

## 📊 Optimizaciones de Rendimiento

### Caching

```python
@st.cache_data(ttl=3600)  # Cache de 1 hora
def load_data():
    # Los datos se cargan una vez y se cachean
    # Invalidación automática después de 1 hora
```

**Beneficios:**
- Carga instantánea en navegación
- Reducción de I/O de disco
- Mejor experiencia de usuario

### Sampling en Visualizaciones

Para datasets grandes, las visualizaciones complejas usan muestreo:

```python
# Scatter 3D con máximo 1000 puntos
df.sample(min(1000, len(df)))
```

### Lazy Loading

Los componentes se renderizan solo cuando son visibles (tabs).

## 🔐 Seguridad y Validación

### Validación de Datos

```python
# Verificación de columnas requeridas
required_cols = ['magnitude', 'depth', 'latitude', 'longitude', ...]
missing_cols = [col for col in required_cols if col not in df.columns]
if missing_cols:
    raise ValueError(f"Faltan columnas: {missing_cols}")
```

### Sanitización de Inputs

- Todos los filtros tienen rangos válidos
- No se permite entrada de código arbitrario
- Validación de tipos de datos

### XSRF Protection

Habilitado en configuración:
```toml
[server]
enableXsrfProtection = true
```

## 🧪 Testing (Planificado)

### Unit Tests

```python
# tests/test_data_loader.py
def test_load_data():
    df = load_data()
    assert 'magnitude' in df.columns
    assert len(df) > 0
    assert df['tsunami'].isin([0, 1]).all()

def test_get_filtered_data():
    df = load_data()
    filters = {'year_range': (2010, 2020)}
    filtered = get_filtered_data(df, filters)
    assert filtered['Year'].min() >= 2010
    assert filtered['Year'].max() <= 2020
```

### Integration Tests

```python
# tests/test_integration.py
def test_full_pipeline():
    # Cargar → Filtrar → Visualizar
    pass
```

## 📈 Métricas de Rendimiento

### Tiempos de Carga Objetivo

- Carga inicial: < 3 segundos
- Cambio de filtros: < 1 segundo
- Renderizado de gráficos: < 2 segundos
- Cambio de tabs: < 0.5 segundos

### Uso de Memoria

- Datos base: ~10-50 MB
- Visualizaciones: ~50-100 MB
- Total estimado: < 200 MB

## 🔄 Actualización de Datos

### Flujo Actual (Manual)

1. Descargar nuevos datos del USGS
2. Reemplazar CSV en `data/`
3. Reiniciar aplicación (cache se invalida)

### Flujo Futuro (Automático)

```python
# Propuesta para integración con API USGS
@st.cache_data(ttl=3600)
def fetch_latest_data():
    # Llamada a USGS API
    # Merge con datos históricos
    # Update incremental
    pass
```

## 🎨 Personalización

### Modificar Tema

Editar `app/.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#TU_COLOR"
backgroundColor = "#TU_COLOR"
# ...
```

### Agregar Nuevas Visualizaciones

```python
# En components/eda.py
def render_new_analysis(df: pd.DataFrame):
    st.markdown("### Mi Nuevo Análisis")
    # Tu código aquí
    
# En render_eda_section():
with new_tab:
    render_new_analysis(df)
```

### Agregar Nuevos Filtros

```python
# En components/sidebar.py
new_filter = st.selectbox("Nuevo Filtro", options=[...])

# Return en diccionario:
return {
    # ... filtros existentes
    'new_filter': new_filter
}
```

## 🐛 Debugging

### Activar Modo Debug

```bash
streamlit run app.py --logger.level=debug
```

### Ver Estado de Sesión

```python
# Agregar temporalmente en app.py
st.write(st.session_state)
```

### Profiling

```python
import cProfile
import pstats

with cProfile.Profile() as pr:
    # Tu código
    
stats = pstats.Stats(pr)
stats.sort_stats('cumtime')
stats.print_stats(10)
```

## 📝 Contribución al Código

### Convenciones

- **Docstrings**: Todas las funciones públicas
- **Type Hints**: Uso obligatorio
- **Comentarios**: Secciones claras con separadores `===`
- **Naming**: snake_case para funciones, PascalCase para clases

### Pre-commit Checklist

- [ ] Código documentado
- [ ] Type hints agregados
- [ ] Sin hardcoded paths
- [ ] Funciona con datos de ejemplo
- [ ] README actualizado si es necesario

## 🚀 Despliegue

### Streamlit Cloud

```bash
# 1. Push a GitHub
git push origin main

# 2. Conectar en streamlit.io
# 3. Seleccionar repo y app.py
# 4. Deploy automático
```

### Docker (Futuro)

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 📞 Soporte

Para preguntas técnicas:
- Revisar esta documentación
- Consultar README.md
- Abrir issue en GitHub
- Contactar al equipo de desarrollo

---

**Última actualización:** 2025  
**Mantenido por:** Sistema de Análisis Sísmico
