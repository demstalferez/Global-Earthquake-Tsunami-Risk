"""
Componente de Introducción
===========================
Renderiza la sección de introducción y contexto del proyecto.
"""

import streamlit as st
import pandas as pd

def render_intro(df: pd.DataFrame):
    """
    Renderiza la sección de introducción con contexto del proyecto.
    
    Args:
        df: DataFrame con datos filtrados
    """
    
    # ========================================================================
    # RESUMEN EJECUTIVO
    # ========================================================================
    
    st.markdown("## 📋 Resumen Ejecutivo")
    
    st.markdown("""
    <div class="info-card">
        <h3>🎯 Objetivo del Análisis</h3>
        <p style="font-size: 1.1rem; line-height: 1.6;">
            Este panel de inteligencia analiza más de <strong>dos décadas de datos sísmicos globales</strong> 
            para responder una pregunta crítica: <strong>¿Qué factores se asocian a la generación de tsunamis?</strong>
        </p>
        <p style="font-size: 1.1rem; line-height: 1.6; margin-top: 1rem;">
            A partir de variables sísmicas, geográficas y temporales, identificamos patrones que 
            sustentan decisiones de <strong>prevención, alerta y priorización de recursos</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ========================================================================
    # HALLAZGOS CLAVE
    # ========================================================================
    
    st.markdown("## 🔍 Hallazgos Clave")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-card">
            <h4>✅ Factores Identificados</h4>
            <ul style="font-size: 1rem; line-height: 1.8;">
                <li><strong>Magnitud alta</strong> y <strong>poca profundidad</strong> (< 70 km)</li>
                <li>Ubicación en <strong>zonas de subducción</strong></li>
                <li>Concentración en el <strong>Cinturón de Fuego del Pacífico</strong></li>
                <li>Patrones geográficos consistentes</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-card">
            <h4>⚠️ Consideraciones Importantes</h4>
            <ul style="font-size: 1rem; line-height: 1.8;">
                <li>Calidad del monitoreo varía por región</li>
                <li>Sesgos temporales en los registros</li>
                <li>Correlaciones entre variables de monitoreo</li>
                <li>Limitaciones de cobertura geográfica</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # ========================================================================
    # DATOS Y ALCANCE
    # ========================================================================
    
    st.markdown("## 📊 Datos y Alcance")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>📅 Período de Análisis</h4>
            <p style="font-size: 1.5rem; font-weight: bold; color: #667eea;">
                2001 - 2022
            </p>
            <p style="color: #888;">
                22 años de datos continuos
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="info-card">
            <h4>🌍 Cobertura Global</h4>
            <p style="font-size: 1.5rem; font-weight: bold; color: #667eea;">
                {len(df):,}
            </p>
            <p style="color: #888;">
                eventos sísmicos registrados
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="info-card">
            <h4>🌊 Eventos Tsunamigénicos</h4>
            <p style="font-size: 1.5rem; font-weight: bold; color: #667eea;">
                {int(df['tsunami'].sum())}
            </p>
            <p style="color: #888;">
                {df['tsunami'].mean() * 100:.1f}% del total
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # ========================================================================
    # VARIABLES CLAVE
    # ========================================================================
    
    st.markdown("## 🔬 Variables Analizadas")
    
    with st.expander("📖 Glosario de Variables (Ver más)", expanded=False):
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Variables Sísmicas:**
            
            - **Magnitude:** Energía liberada por el terremoto (escala de Richter/momento)
            - **Depth:** Profundidad del epicentro en kilómetros
            - **Significance (sig):** Índice compuesto de severidad e impacto del evento
            
            **Variables de Intensidad:**
            
            - **CDI:** Community Decimal Intensity - intensidad reportada por la población
            - **MMI:** Modified Mercalli Intensity - intensidad instrumental medida
            """)
        
        with col2:
            st.markdown("""
            **Variables de Monitoreo:**
            
            - **nst:** Número de estaciones sísmicas que registraron el evento
            - **dmin:** Distancia angular a la estación más cercana (grados)
            - **gap:** Cobertura angular de las estaciones (menor es mejor)
            
            **Variables Geográficas:**
            
            - **Latitude/Longitude:** Coordenadas del epicentro
            - **Year/Month:** Dimensiones temporales del evento
            """)
    
    # ========================================================================
    # PREGUNTAS DE INVESTIGACIÓN
    # ========================================================================
    
    st.markdown("## ❓ Preguntas de Investigación")
    
    st.markdown("""
    <div class="info-card">
        <ol style="font-size: 1.1rem; line-height: 2;">
            <li>¿Qué características sísmicas distinguen a los terremotos que generan tsunamis?</li>
            <li>¿Existen zonas geográficas con patrones de mayor riesgo tsunamigénico?</li>
            <li>¿Cómo influyen la profundidad y magnitud en la probabilidad de tsunami?</li>
            <li>¿Qué sesgos introduce la calidad y cobertura del monitoreo sísmico?</li>
            <li>¿Cómo han evolucionado los patrones tsunamigénicos a lo largo del tiempo?</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # ========================================================================
    # METODOLOGÍA
    # ========================================================================
    
    st.markdown("## 🧪 Metodología de Análisis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Análisis Estadístico:**
        - Estadística descriptiva completa
        - Pruebas de normalidad (Shapiro-Wilk)
        - Correlaciones no paramétricas (Spearman)
        - Análisis de distribuciones
        """)
    
    with col2:
        st.markdown("""
        **Análisis Geoespacial:**
        - Mapas interactivos globales
        - Identificación de hotspots
        - Análisis temporal-espacial
        - Evaluación de calidad de monitoreo
        """)
    
    # ========================================================================
    # APLICACIONES
    # ========================================================================
    
    st.markdown("## 🎯 Aplicaciones Prácticas")
    
    applications = [
        {
            "icon": "📊",
            "title": "Paneles Operativos",
            "desc": "Vigilancia en tiempo real y priorización de recursos por zona de riesgo"
        },
        {
            "icon": "🤖",
            "title": "Modelos Predictivos",
            "desc": "Ingeniería de características para ML y sistemas de alerta temprana"
        },
        {
            "icon": "🔍",
            "title": "Evaluación de Sesgos",
            "desc": "Identificación de gaps en cobertura de monitoreo y calidad de datos"
        },
        {
            "icon": "📈",
            "title": "Análisis de Tendencias",
            "desc": "Evolución temporal de patrones y cambios en la actividad sísmica"
        }
    ]
    
    cols = st.columns(4)
    for i, app in enumerate(applications):
        with cols[i]:
            st.markdown(f"""
            <div class="info-card" style="text-align: center; height: 200px;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">{app['icon']}</div>
                <h4>{app['title']}</h4>
                <p style="font-size: 0.9rem; color: #888;">{app['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # ========================================================================
    # FUENTE DE DATOS
    # ========================================================================
    
    st.markdown("## 📚 Fuente de Datos")
    
    st.markdown("""
    <div class="info-card">
        <h4>🌐 USGS Earthquake Catalog</h4>
        <p style="font-size: 1rem; line-height: 1.6;">
            Los datos provienen del <strong>United States Geological Survey (USGS)</strong>, 
            la autoridad científica líder en monitoreo y análisis de actividad sísmica global.
        </p>
        <p style="font-size: 1rem; line-height: 1.6; margin-top: 1rem;">
            🔗 <a href="https://earthquake.usgs.gov/" target="_blank">earthquake.usgs.gov</a>
        </p>
    </div>
    """, unsafe_allow_html=True)
