"""
Componente Sidebar
==================
Renderiza el menú lateral con filtros interactivos.
"""

import streamlit as st
import pandas as pd
from typing import Dict, Any

def render_sidebar(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Renderiza el sidebar con todos los controles de filtrado.
    
    Args:
        df: DataFrame original con todos los datos
        
    Returns:
        Dict con los filtros seleccionados por el usuario
    """
    
    with st.sidebar:
        # Logo y título del sidebar
        st.markdown("""
            <div style="text-align: center; padding: 1rem 0;">
                <h2>🎛️ Panel de Control</h2>
                <p style="color: #888; font-size: 0.9rem;">
                    Ajusta los filtros para explorar los datos
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # ====================================================================
        # SECCIÓN: FILTROS TEMPORALES
        # ====================================================================
        
        st.markdown("### 📅 Filtros Temporales")
        
        # Filtro de rango de años
        year_min = int(df['Year'].min())
        year_max = int(df['Year'].max())
        
        year_range = st.slider(
            "Rango de Años",
            min_value=year_min,
            max_value=year_max,
            value=(year_min, year_max),
            help="Selecciona el período de análisis"
        )
        
        # Filtro de meses
        all_months = list(range(1, 13))
        month_names = {
            1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
            5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
            9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
        }
        
        selected_months_display = st.multiselect(
            "Meses del Año",
            options=all_months,
            default=all_months,
            format_func=lambda x: month_names[x],
            help="Selecciona uno o más meses"
        )
        
        st.markdown("---")
        
        # ====================================================================
        # SECCIÓN: FILTROS SÍSMICOS
        # ====================================================================
        
        st.markdown("### 🌍 Filtros Sísmicos")
        
        # Filtro de magnitud
        mag_min = float(df['magnitude'].min())
        mag_max = float(df['magnitude'].max())
        
        magnitude_range = st.slider(
            "Magnitud",
            min_value=mag_min,
            max_value=mag_max,
            value=(mag_min, mag_max),
            step=0.1,
            help="Filtra por rango de magnitud del terremoto"
        )
        
        # Filtro de profundidad
        depth_min = float(df['depth'].min())
        depth_max = float(df['depth'].max())
        
        depth_range = st.slider(
            "Profundidad (km)",
            min_value=depth_min,
            max_value=min(depth_max, 700.0),  # Limitar para mejor UX
            value=(depth_min, min(depth_max, 700.0)),
            step=10.0,
            help="Filtra por profundidad del epicentro"
        )
        
        st.markdown("---")
        
        # ====================================================================
        # SECCIÓN: FILTROS DE TSUNAMI
        # ====================================================================
        
        st.markdown("### 🌊 Filtros de Tsunami")
        
        tsunami_filter = st.radio(
            "Estado de Tsunami",
            options=['Todos', 'Solo con Tsunami', 'Solo sin Tsunami'],
            help="Filtra eventos según generación de tsunami"
        )
        
        st.markdown("---")
        
        # ====================================================================
        # SECCIÓN: FILTROS GEOGRÁFICOS
        # ====================================================================
        
        st.markdown("### 🗺️ Filtros Geográficos")
        
        region_filter = st.radio(
            "Región",
            options=['Todas', 'Solo Ring of Fire', 'Fuera Ring of Fire'],
            help="Filtra por ubicación geográfica"
        )
        
        st.markdown("---")
        
        # ====================================================================
        # SECCIÓN: OPCIONES DE VISUALIZACIÓN
        # ====================================================================
        
        st.markdown("### ⚙️ Opciones de Visualización")
        
        show_advanced = st.checkbox(
            "Mostrar análisis avanzados",
            value=True,
            help="Incluye correlaciones, distribuciones y pruebas estadísticas"
        )
        
        chart_theme = st.selectbox(
            "Tema de Gráficos",
            options=['plotly_dark', 'plotly', 'seaborn', 'ggplot2'],
            index=0,
            help="Selecciona el estilo visual de los gráficos"
        )
        
        st.markdown("---")
        
        # ====================================================================
        # SECCIÓN: INFORMACIÓN Y AYUDA
        # ====================================================================
        
        with st.expander("ℹ️ Información del Dataset"):
            total_events = len(df)
            tsunami_events = int(df['tsunami'].sum())
            
            st.markdown(f"""
            **Estadísticas Globales:**
            - 📊 Total de eventos: **{total_events:,}**
            - 🌊 Eventos con tsunami: **{tsunami_events:,}**
            - 📈 Tasa de tsunami: **{tsunami_events/total_events*100:.2f}%**
            - 📅 Período: **{year_min} - {year_max}**
            - 🌍 Magnitud máxima: **{df['magnitude'].max():.1f}**
            """)
        
        with st.expander("❓ Ayuda"):
            st.markdown("""
            **Cómo usar este panel:**
            
            1. **Filtros Temporales:** Ajusta el período de análisis
            2. **Filtros Sísmicos:** Define rangos de magnitud y profundidad
            3. **Filtros de Tsunami:** Enfoca en eventos específicos
            4. **Filtros Geográficos:** Analiza regiones específicas
            
            💡 **Tip:** Los filtros se aplican automáticamente
            """)
        
        # ====================================================================
        # BOTÓN DE RESET
        # ====================================================================
        
        st.markdown("---")
        
        if st.button("🔄 Restablecer Filtros", use_container_width=True):
            st.rerun()
    
    # ========================================================================
    # RETORNAR DICCIONARIO DE FILTROS
    # ========================================================================
    
    return {
        'year_range': year_range,
        'months': selected_months_display,
        'magnitude_range': magnitude_range,
        'depth_range': depth_range,
        'tsunami_filter': tsunami_filter,
        'region_filter': region_filter,
        'show_advanced': show_advanced,
        'chart_theme': chart_theme
    }
