"""
Panel de Inteligencia: Riesgo Global de Terremotos y Tsunamis
==============================================================
Aplicación principal de Streamlit para análisis interactivo de datos sísmicos.

Autor: Sistema de Análisis Sísmico
Fecha: 2025
"""

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

# Importar módulos personalizados
from components.sidebar import render_sidebar
from components.intro import render_intro
from components.eda import render_eda_section
from components.conclusions import render_conclusions
from components.ml import render_ml_section
from utils.data_loader import load_data, get_filtered_data
from utils.styles import apply_custom_css

# ============================================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================================

st.set_page_config(
    page_title="🌊 Panel Sísmico Global",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yourusername/Global-Earthquake-Tsunami-Risk',
        'Report a bug': 'https://github.com/yourusername/Global-Earthquake-Tsunami-Risk/issues',
        'About': """
        ## Panel de Inteligencia: Riesgo Global de Terremotos y Tsunamis
        
        Esta aplicación analiza más de dos décadas de datos sísmicos globales
        para identificar patrones y factores asociados a la generación de tsunamis.
        
        **Fuente de datos:** USGS Earthquake Catalog (2001-2022)
        """
    }
)

# ============================================================================
# INICIALIZACIÓN DE ESTADO DE SESIÓN
# ============================================================================

def init_session_state():
    """
    Inicializa variables de estado de la sesión de Streamlit.
    Útil para mantener configuraciones entre reruns.
    """
    if 'data_loaded' not in st.session_state:
        st.session_state.data_loaded = False
    if 'current_section' not in st.session_state:
        st.session_state.current_section = 'Introducción'

# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que orquesta toda la aplicación.
    Gestiona la carga de datos, aplicación de estilos y renderizado de secciones.
    """
    # Inicializar estado
    init_session_state()
    
    # Aplicar estilos CSS personalizados
    apply_custom_css()
    
    # ========================================================================
    # CABECERA PRINCIPAL
    # ========================================================================
    
    st.markdown("""
        <div class="main-header">
            <h1>🌊 Panel de Inteligencia: Riesgo Global de Terremotos y Tsunamis</h1>
            <p class="subtitle">Análisis Exploratorio Interactivo | 2001-2022 | USGS Data</p>
        </div>
    """, unsafe_allow_html=True)
    
    # ========================================================================
    # CARGA DE DATOS
    # ========================================================================
    
    try:
        with st.spinner('🔄 Cargando datos sísmicos...'):
            df = load_data()
            st.session_state.data_loaded = True
            
    except Exception as e:
        st.error(f"❌ Error al cargar los datos: {str(e)}")
        st.stop()
    
    # ========================================================================
    # SIDEBAR CON FILTROS
    # ========================================================================
    
    filters = render_sidebar(df)
    
    # Aplicar filtros a los datos
    df_filtered = get_filtered_data(df, filters)
    
    # ========================================================================
    # MÉTRICAS RÁPIDAS (KPIs)
    # ========================================================================
    
    st.markdown("---")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="📊 Total Eventos",
            value=f"{len(df_filtered):,}",
            delta=f"{len(df_filtered) - len(df):,}" if len(df_filtered) != len(df) else None
        )
    
    with col2:
        tsunami_count = df_filtered['tsunami'].sum()
        tsunami_pct = (tsunami_count / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
        st.metric(
            label="🌊 Tsunamis",
            value=f"{int(tsunami_count):,}",
            delta=f"{tsunami_pct:.1f}%"
        )
    
    with col3:
        avg_mag = df_filtered['magnitude'].mean()
        st.metric(
            label="📈 Magnitud Promedio",
            value=f"{avg_mag:.2f}",
            delta=f"{avg_mag - df['magnitude'].mean():.2f}" if len(df_filtered) != len(df) else None
        )
    
    with col4:
        avg_depth = df_filtered['depth'].mean()
        st.metric(
            label="🌍 Profundidad Promedio",
            value=f"{avg_depth:.0f} km",
            delta=f"{avg_depth - df['depth'].mean():.0f}" if len(df_filtered) != len(df) else None
        )
    
    with col5:
        max_sig = df_filtered['sig'].max()
        st.metric(
            label="⚡ Significancia Máx.",
            value=f"{int(max_sig):,}",
            delta=f"{int(max_sig - df['sig'].max()):,}" if len(df_filtered) != len(df) else None
        )
    
    st.markdown("---")
    
    # ========================================================================
    # NAVEGACIÓN POR SECCIONES
    # ========================================================================
    
    # Tabs principales
    tab1, tab2, tab3, tab4 = st.tabs([
        "📖 Introducción & Contexto",
        "📊 Análisis Exploratorio (EDA)",
        "📌 Conclusiones & Recomendaciones",
        "🤖 Machine Learning (Próximamente)"
    ])
    
    with tab1:
        render_intro(df_filtered)
    
    with tab2:
        render_eda_section(df_filtered)
    
    with tab3:
        render_conclusions(df_filtered)
    
    with tab4:
        render_ml_section(df_filtered)
    
    # ========================================================================
    # FOOTER
    # ========================================================================
    
    st.markdown("---")
    st.markdown("""
        <div class="footer">
            <p>
                🔬 Desarrollado con Streamlit | 
                📊 Datos: USGS Earthquake Catalog | 
                📅 Periodo: 2001-2022 |
                💻 <a href="https://github.com/yourusername/Global-Earthquake-Tsunami-Risk" target="_blank">GitHub</a>
            </p>
        </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    main()
