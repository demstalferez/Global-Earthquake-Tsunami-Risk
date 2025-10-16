# Guía Narrativa del EDA: Riesgo Global de Terremotos y Tsunamis

Una historia sobre dónde, cuándo y por qué algunos terremotos se convierten en tsunamis, contada con datos.

---

## 1. Resumen Ejecutivo

Este análisis exploratorio (EDA) estudia más de dos décadas de terremotos globales para responder una pregunta clave: ¿qué factores se asocian a la generación de tsunamis? A partir de variables sísmicas, geográficas y temporales, identificamos patrones que sustentan decisiones de prevención, alerta y priorización de recursos.

Hallazgos clave:
- Los tsunamis se asocian más a terremotos de **magnitud alta y poca profundidad**.
- La **ubicación geográfica** (especialmente el Cinturón de Fuego del Pacífico) concentra la mayoría de eventos tsunamigénicos.
- La **calidad del monitoreo** (número de estaciones y distancia) varía por región y tiempo, afectando la confiabilidad de registros.
- Existen **correlaciones fuertes** entre variables de calidad de datos (por ejemplo, `nst` vs `dmin`) y **moderadas** entre significancia (`sig`) e intensidad percibida (`cdi`/`mmi`).

Aplicaciones:
- Diseño de **paneles operativos** para vigilancia y priorización por zona.
- **Ingeniería de características** para modelos predictivos de ocurrencia de tsunamis.
- Evaluación de **sesgos** por cobertura de monitoreo y cambios temporales.

---

## 2. Objetivo y Preguntas de Negocio

Objetivo: Comprender los determinantes geográficos, sísmicos y temporales de eventos tsunamigénicos para soportar decisiones de prevención, respuesta y modelado.

Preguntas guía:
1. ¿Qué rasgos sísmicos distinguen a los terremotos que generan tsunamis?
2. ¿Existen zonas geográficas con patrones de mayor riesgo?
3. ¿Cómo influye la profundidad y magnitud en la probabilidad de tsunami?
4. ¿Qué sesgos o limitaciones introduce la calidad del monitoreo?
5. ¿Cómo han cambiado los patrones con el tiempo?

---

## 3. Datos y Alcance

- Fuente: `data/earthquake_data_tsunami.csv`
- Periodo: 2001–2022
- Granularidad: Evento sísmico
- Variables clave: `magnitude`, `depth`, `latitude`, `longitude`, `sig`, `cdi`, `mmi`, `nst`, `dmin`, `gap`, `Year`, `Month`, `tsunami`

Glosario rápido (no técnico):
- Magnitud: energía liberada por el terremoto.
- Profundidad: qué tan profundo fue el epicentro (km).
- Intensidad (cdi/mmi): qué tanto se sintió/medió en superficie.
- Significancia (sig): severidad/impacto general del evento.
- Tsunami: 1 si hubo potencial/ocurrencia, 0 si no.

---

## 4. Metodología de Análisis

- Estadística descriptiva y distribución de variables (histogramas + prueba Shapiro-Wilk).
- Correlación no paramétrica (**Spearman**) para robustez ante no-normalidad.
- Análisis geoespacial interactivo (Plotly) con 5 mapas focales:
  1) Tsunamis vs Profundidad
  2) Zonas de Alto Riesgo (Ring of Fire)
  3) Evolución Temporal (2001–2022)
  4) Calidad del Monitoreo (nst vs dmin)
  5) Significancia vs Impacto (sig vs cdi/mmi)

Referencias visuales:
- Matriz Spearman: `img/corrspearman.png` (si está disponible)
- Mapas: ver notebook `notebooks/eda.ipynb`

---

## 5. Hallazgos Principales

### 5.1 Distribuciones y normalidad
- La mayoría de variables no siguen distribución normal (Shapiro-Wilk), justificando el uso de Spearman.
- `magnitude` se concentra entre 6.5 y 7.5; `depth` muestra cola larga con valores profundos.
- `sig`, `cdi` y `mmi` son asimétricas: conviene considerar transformaciones en modelado.

### 5.2 Correlaciones (Spearman)

Principales relaciones observadas:
- Fuerte: `nst` vs `dmin` (negativa) → mayor cobertura, menor distancia a la estación más cercana.
- Fuerte: `sig` vs `magnitude` (positiva) → la magnitud explica gran parte de la significancia.
- Moderadas: `sig` vs `cdi` y `sig` vs `mmi` → mayor severidad, mayor intensidad sentida/medida.
- Temporales: `Year` correlaciona con `nst` y `dmin` → cambios en las redes de monitoreo.

Implicaciones:
- Evitar multicolinealidad: considerar elegir entre `nst` y `dmin`.
- `sig` añade información, pero parte está ya en `magnitude`.

> Ver Heatmap: `img/corrspearman.png`

### 5.3 Geografía del riesgo (mapas)

1) Tsunamis vs Profundidad: los eventos superficiales (< 70 km) cerca de márgenes de placas tienen mayor probabilidad de tsunami.
2) Ring of Fire: Japón, Indonesia, Chile, Alaska y Tonga concentran la mayoría de eventos tsunamigénicos.
3) Temporalidad: variaciones 2001–2022 sugieren cambios de cobertura y/o reporte.
4) Monitoreo: regiones con **bajo `nst` y alto `dmin`** podrían subreportar.
5) Significancia vs Impacto: identifica eventos de alta `sig` sin tsunami (posibles falsos positivos) y eventos de menor `sig` pero con tsunami (casos interesantes).

---

## 6. Conclusiones

- El riesgo tsunamigénico no depende solo de magnitud: la **profundidad** y el **contexto geográfico** son determinantes.
- La **calidad y cobertura del monitoreo** introducen sesgos espaciales y temporales; deben considerarse en cualquier modelo.
- La combinación de rasgos geográficos (lat/lon) con sísmicos (mag/depth) es prometedora para un **modelo predictivo**.

---

## 7. Recomendaciones para un Panel de Inteligencia

Métricas clave:
- Conteos de eventos por región/mes/año
- Tasa de tsunamis por rango de profundidad y magnitud
- Mapa de calor de hotspots tsunamigénicos
- Indicadores de calidad: `nst`, `dmin`, `gap` por región

Visualizaciones sugeridas:
- Mapa interactivo global con filtros por año, magnitud, profundidad y estado de tsunami.
- Barras apiladas: tasa de tsunami por bins de magnitud y profundidad.
- Línea temporal: evolución anual de eventos y tasa de tsunami.
- Panel de calidad de datos: cobertura de estaciones vs distancia mínima.

Alertas/umbrales (operativo):
- Profundidad < 70 km y magnitud ≥ 7.0 en zonas de subducción → alerta alta.
- `dmin` alto y `nst` bajo en regiones críticas → bandera de baja confiabilidad.

---

## 8. Ingeniería de Características (para modelado)

Sugerencias:
- `shallow` = 1 si `depth` < 70 km
- `mag_bin` y `depth_bin` (discretizaciones informativas)
- `monitoring_quality` = f(`nst`, `dmin`, `gap`)
- Features geográficas: pertenencia a "Ring of Fire" o zonas de subducción
- Interacciones: `magnitude × shallow`, `latitude/longitude` agrupadas por región

---

## 9. Riesgos, Sesgos y Limitaciones

- Subreporte en zonas con baja cobertura (`nst` bajo, `dmin` alto)
- Cambios metodológicos a lo largo del tiempo (`Year`) que afectan comparabilidad
- Variables correlacionadas que pueden inflar importancia si no se controlan
- Ausencia de variables oceanográficas (batimetría, distancia a costa) que mejorarían el contexto

---

## 10. Próximos Pasos

1. Enriquecer datos con capas geográficas (placas tectónicas, distancia a costa, batimetría).
2. Validar hipótesis de profundidad y zonas de subducción con fuentes externas.
3. Prototipar un modelo base (logístico/árboles) con validación temporal.
4. Diseñar el panel interactivo con filtros y alertas de umbral.

---

## 11. Glosario

- CDI/MMI: medidas de intensidad sentida/instrumental.
- `nst`: número de estaciones que registraron el evento.
- `dmin`: distancia angular a la estación más cercana.
- `gap`: cobertura angular de estaciones (menor es mejor).
- Spearman: correlación por rangos, robusta a no-normalidad.

---

## 12. Referencias

- Notebook: `notebooks/eda.ipynb`
- Imagen correlaciones: `img/corrspearman.png`
- Datos: `data/earthquake_data_tsunami.csv`
