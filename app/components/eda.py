"""
Componente de Análisis Exploratorio (EDA)
==========================================
Renderiza la sección completa de análisis exploratorio con visualizaciones interactivas.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from typing import Dict, Any

def render_eda_section(df: pd.DataFrame):
    """
    Renderiza la sección completa de EDA con múltiples subsecciones.
    
    Args:
        df: DataFrame con datos filtrados
    """
    
    st.markdown("## 📊 Análisis Exploratorio de Datos (EDA)")
    
    st.markdown("""
    <div class="info-card">
        <p style="font-size: 1.1rem;">
            Exploración profunda de patrones sísmicos, distribuciones estadísticas 
            y relaciones entre variables. Los análisis incluyen visualizaciones interactivas, 
            pruebas estadísticas y mapas geoespaciales.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ========================================================================
    # SUBTABS PARA ORGANIZAR EL EDA
    # ========================================================================
    
    eda_tab1, eda_tab2, eda_tab3, eda_tab4, eda_tab5 = st.tabs([
        "📈 Distribuciones",
        "🔗 Correlaciones",
        "🗺️ Análisis Geoespacial",
        "⏱️ Análisis Temporal",
        "🎯 Análisis Multivariable"
    ])
    
    # ========================================================================
    # TAB 1: DISTRIBUCIONES
    # ========================================================================
    
    with eda_tab1:
        render_distributions(df)
    
    # ========================================================================
    # TAB 2: CORRELACIONES
    # ========================================================================
    
    with eda_tab2:
        render_correlations(df)
    
    # ========================================================================
    # TAB 3: ANÁLISIS GEOESPACIAL
    # ========================================================================
    
    with eda_tab3:
        render_geospatial(df)
    
    # ========================================================================
    # TAB 4: ANÁLISIS TEMPORAL
    # ========================================================================
    
    with eda_tab4:
        render_temporal(df)
    
    # ========================================================================
    # TAB 5: ANÁLISIS MULTIVARIABLE
    # ========================================================================
    
    with eda_tab5:
        render_multivariate(df)

# ============================================================================
# FUNCIONES DE RENDERIZADO POR SUBSECCIÓN
# ============================================================================

def render_distributions(df: pd.DataFrame):
    """Renderiza análisis de distribuciones."""
    
    st.markdown("### 📊 Distribuciones de Variables")
    
    st.markdown("""
    <div class="info-card">
        <p>Análisis de las distribuciones de las principales variables sísmicas, 
        incluyendo pruebas de normalidad y estadísticas descriptivas.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Variable selector
    variables = ['magnitude', 'depth', 'sig', 'nst', 'dmin', 'gap', 'cdi', 'mmi']
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        selected_var = st.selectbox(
            "Selecciona Variable",
            options=variables,
            format_func=lambda x: x.replace('_', ' ').title()
        )
    
    with col2:
        st.markdown(f"**Variable seleccionada:** `{selected_var}`")
    
    # Crear visualización de distribución
    col1, col2 = st.columns(2)
    
    with col1:
        # Histograma
        fig_hist = px.histogram(
            df,
            x=selected_var,
            nbins=50,
            title=f'Distribución de {selected_var.title()}',
            labels={selected_var: selected_var.title()},
            color_discrete_sequence=['#667eea']
        )
        
        fig_hist.update_layout(
            template='plotly_dark',
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Box plot por tsunami
        fig_box = px.box(
            df,
            x='tsunami',
            y=selected_var,
            color='tsunami',
            title=f'{selected_var.title()} por Estado de Tsunami',
            labels={
                selected_var: selected_var.title(),
                'tsunami': 'Tsunami'
            },
            color_discrete_map={0: 'lightblue', 1: 'red'}
        )
        
        fig_box.update_layout(
            template='plotly_dark',
            height=400
        )
        
        st.plotly_chart(fig_box, use_container_width=True)
    
    # Estadísticas descriptivas
    st.markdown("#### 📋 Estadísticas Descriptivas")
    
    col1, col2, col3 = st.columns(3)
    
    stats_data = df[selected_var].describe()
    
    with col1:
        st.metric("Media", f"{stats_data['mean']:.2f}")
        st.metric("Mediana", f"{stats_data['50%']:.2f}")
    
    with col2:
        st.metric("Desv. Estándar", f"{stats_data['std']:.2f}")
        st.metric("Mínimo", f"{stats_data['min']:.2f}")
    
    with col3:
        st.metric("Máximo", f"{stats_data['max']:.2f}")
        st.metric("Q3 - Q1", f"{stats_data['75%'] - stats_data['25%']:.2f}")
    
    # Test de normalidad
    with st.expander("🔬 Test de Normalidad (Shapiro-Wilk)"):
        sample_size = min(5000, len(df))
        sample_data = df[selected_var].dropna().sample(sample_size)
        stat, p_value = stats.shapiro(sample_data)
        
        is_normal = p_value > 0.05
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Estadístico", f"{stat:.4f}")
            st.metric("P-valor", f"{p_value:.4e}")
        
        with col2:
            if is_normal:
                st.success("✅ La variable parece seguir una distribución normal")
            else:
                st.warning("⚠️ La variable NO sigue una distribución normal")
        
        st.markdown(f"""
        **Interpretación:** {'Con p-valor > 0.05, no rechazamos la hipótesis de normalidad.' 
        if is_normal else 
        'Con p-valor < 0.05, rechazamos la hipótesis de normalidad. Se recomienda usar métodos no paramétricos.'}
        """)


def render_correlations(df: pd.DataFrame):
    """Renderiza análisis de correlaciones."""
    
    st.markdown("### 🔗 Análisis de Correlaciones")
    
    st.markdown("""
    <div class="info-card">
        <p>Matriz de correlación de Spearman (no paramétrica) para identificar 
        relaciones entre variables. Ideal cuando las variables no siguen distribución normal.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Selección de variables para correlación
    numeric_cols = ['magnitude', 'depth', 'sig', 'nst', 'dmin', 'gap', 
                   'cdi', 'mmi', 'Year', 'Month', 'tsunami']
    
    available_cols = [col for col in numeric_cols if col in df.columns]
    
    # Calcular matriz de correlación
    corr_matrix = df[available_cols].corr(method='spearman')
    
    # Heatmap de correlación
    fig_corr = px.imshow(
        corr_matrix,
        labels=dict(color="Correlación de Spearman"),
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        color_continuous_scale='RdBu_r',
        zmin=-1,
        zmax=1,
        title='Matriz de Correlación de Spearman',
        aspect='auto'
    )
    
    fig_corr.update_layout(
        template='plotly_dark',
        height=700
    )
    
    st.plotly_chart(fig_corr, use_container_width=True)
    
    # Correlaciones más fuertes
    st.markdown("#### 🎯 Correlaciones Más Relevantes")
    
    # Obtener pares de correlación más fuertes
    corr_pairs = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            corr_pairs.append({
                'Variable 1': corr_matrix.columns[i],
                'Variable 2': corr_matrix.columns[j],
                'Correlación': corr_matrix.iloc[i, j]
            })
    
    corr_df = pd.DataFrame(corr_pairs)
    corr_df = corr_df.sort_values('Correlación', ascending=False, key=abs)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔴 Correlaciones Positivas Fuertes**")
        positive_corr = corr_df[corr_df['Correlación'] > 0].head(5)
        st.dataframe(positive_corr, hide_index=True, use_container_width=True)
    
    with col2:
        st.markdown("**🔵 Correlaciones Negativas Fuertes**")
        negative_corr = corr_df[corr_df['Correlación'] < 0].head(5)
        st.dataframe(negative_corr, hide_index=True, use_container_width=True)
    
    # Interpretación
    with st.expander("📖 Interpretación de Correlaciones"):
        st.markdown("""
        **Guía de interpretación:**
        
        - **|r| > 0.7:** Correlación fuerte
        - **0.4 < |r| < 0.7:** Correlación moderada
        - **|r| < 0.4:** Correlación débil
        
        **Hallazgos clave del análisis:**
        
        - ✅ **`nst` vs `dmin` (negativa):** Mayor cobertura de estaciones implica menor distancia
        - ✅ **`sig` vs `magnitude` (positiva):** La magnitud es el principal factor de significancia
        - ✅ **`sig` vs `cdi`/`mmi` (moderada):** Mayor severidad se correlaciona con mayor intensidad percibida
        - ⚠️ **Multicolinealidad:** Considerar eliminar variables altamente correlacionadas en modelos predictivos
        """)


def render_geospatial(df: pd.DataFrame):
    """Renderiza análisis geoespacial."""
    
    st.markdown("### 🗺️ Análisis Geoespacial")
    
    st.markdown("""
    <div class="info-card">
        <p>Mapas interactivos que revelan patrones geográficos de actividad sísmica 
        y eventos tsunamigénicos a nivel global.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Selector de tipo de mapa
    map_type = st.radio(
        "Selecciona el tipo de visualización:",
        options=[
            '🌍 Distribución Global por Magnitud',
            '🌊 Tsunamis vs Profundidad',
            '🔥 Ring of Fire - Zonas de Alto Riesgo',
            '🎯 Calidad del Monitoreo Sísmico'
        ],
        horizontal=False
    )
    
    if map_type == '🌍 Distribución Global por Magnitud':
        render_global_magnitude_map(df)
    
    elif map_type == '🌊 Tsunamis vs Profundidad':
        render_tsunami_depth_map(df)
    
    elif map_type == '🔥 Ring of Fire - Zonas de Alto Riesgo':
        render_ring_of_fire_map(df)
    
    elif map_type == '🎯 Calidad del Monitoreo Sísmico':
        render_monitoring_quality_map(df)


def render_global_magnitude_map(df: pd.DataFrame):
    """Mapa global de terremotos por magnitud."""
    
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        color='magnitude',
        size='sig',
        hover_data=['depth', 'tsunami', 'Year'],
        projection='natural earth',
        title='Distribución Global de Terremotos por Magnitud',
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=600,
        geo=dict(
            showland=True,
            landcolor='rgb(50, 50, 50)',
            showcountries=True,
            countrycolor='rgb(100, 100, 100)',
            showocean=True,
            oceancolor='rgb(20, 20, 20)'
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_tsunami_depth_map(df: pd.DataFrame):
    """Mapa de tsunamis vs profundidad."""
    
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        color='tsunami',
        size='depth',
        hover_data=['magnitude', 'sig', 'Year'],
        color_discrete_map={0: 'lightblue', 1: 'red'},
        title='🌊 Eventos Tsunamigénicos vs Profundidad del Epicentro',
        labels={'tsunami': 'Tsunami', 'depth': 'Profundidad (km)'}
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=600,
        geo=dict(
            showland=True,
            landcolor='rgb(50, 50, 50)',
            showcountries=True,
            countrycolor='rgb(100, 100, 100)',
            showocean=True,
            oceancolor='rgb(20, 20, 20)'
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Análisis de profundidad
    col1, col2 = st.columns(2)
    
    with col1:
        shallow_tsunami = df[(df['depth'] < 70) & (df['tsunami'] == 1)]
        st.metric(
            "Tsunamis Superficiales (< 70km)",
            f"{len(shallow_tsunami)}",
            f"{len(shallow_tsunami) / df['tsunami'].sum() * 100:.1f}% del total"
        )
    
    with col2:
        deep_tsunami = df[(df['depth'] >= 70) & (df['tsunami'] == 1)]
        st.metric(
            "Tsunamis Profundos (≥ 70km)",
            f"{len(deep_tsunami)}",
            f"{len(deep_tsunami) / df['tsunami'].sum() * 100:.1f}% del total"
        )


def render_ring_of_fire_map(df: pd.DataFrame):
    """Mapa del Ring of Fire."""
    
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        color='magnitude',
        size='sig',
        symbol='tsunami',
        hover_data=['depth', 'Year'],
        color_continuous_scale='Plasma',
        symbol_map={0: 'circle', 1: 'diamond'},
        title='🔥 Cinturón de Fuego del Pacífico: Hotspots Tsunamigénicos',
        labels={'magnitude': 'Magnitud', 'sig': 'Significancia'}
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=600,
        geo=dict(
            showland=True,
            landcolor='rgb(50, 50, 50)',
            showcountries=True,
            countrycolor='rgb(100, 100, 100)',
            showocean=True,
            oceancolor='rgb(20, 20, 20)',
            projection_type='orthographic'
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_monitoring_quality_map(df: pd.DataFrame):
    """Mapa de calidad del monitoreo."""
    
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        color='nst',
        size='dmin',
        hover_data=['magnitude', 'gap', 'tsunami'],
        color_continuous_scale='RdYlGn',
        title='🎯 Cobertura de Monitoreo: Estaciones vs Distancia',
        labels={'nst': 'Núm. Estaciones', 'dmin': 'Distancia Mín. (°)'}
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=600,
        geo=dict(
            showland=True,
            landcolor='rgb(50, 50, 50)',
            showcountries=True,
            countrycolor='rgb(100, 100, 100)',
            showocean=True,
            oceancolor='rgb(20, 20, 20)'
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_temporal(df: pd.DataFrame):
    """Renderiza análisis temporal."""
    
    st.markdown("### ⏱️ Análisis Temporal")
    
    st.markdown("""
    <div class="info-card">
        <p>Evolución de patrones sísmicos a lo largo del tiempo (2001-2022).</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Evolución anual
    yearly_stats = df.groupby(['Year', 'tsunami']).size().reset_index(name='count')
    
    fig_year = px.bar(
        yearly_stats,
        x='Year',
        y='count',
        color='tsunami',
        title='📅 Evolución Anual de Eventos Sísmicos',
        labels={'count': 'Número de Eventos', 'tsunami': 'Tsunami'},
        color_discrete_map={0: 'lightblue', 1: 'red'},
        barmode='stack'
    )
    
    fig_year.update_layout(
        template='plotly_dark',
        height=500
    )
    
    st.plotly_chart(fig_year, use_container_width=True)
    
    # Distribución mensual
    monthly_stats = df.groupby(['Month', 'tsunami']).size().reset_index(name='count')
    
    fig_month = px.bar(
        monthly_stats,
        x='Month',
        y='count',
        color='tsunami',
        title='📊 Distribución Mensual de Eventos',
        labels={'count': 'Número de Eventos', 'Month': 'Mes', 'tsunami': 'Tsunami'},
        color_discrete_map={0: 'lightblue', 1: 'red'},
        barmode='group'
    )
    
    fig_month.update_layout(
        template='plotly_dark',
        height=400
    )
    
    st.plotly_chart(fig_month, use_container_width=True)


def render_multivariate(df: pd.DataFrame):
    """Renderiza análisis multivariable."""
    
    st.markdown("### 🎯 Análisis Multivariable")
    
    st.markdown("""
    <div class="info-card">
        <p>Relaciones complejas entre múltiples variables simultáneamente.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Scatter 3D
    fig_3d = px.scatter_3d(
        df.sample(min(1000, len(df))),
        x='magnitude',
        y='depth',
        z='sig',
        color='tsunami',
        size='sig',
        hover_data=['latitude', 'longitude', 'Year'],
        color_discrete_map={0: 'lightblue', 1: 'red'},
        title='🌊 Análisis 3D: Magnitud, Profundidad y Significancia vs Tsunami',
        labels={
            'magnitude': 'Magnitud',
            'depth': 'Profundidad (km)',
            'sig': 'Significancia'
        }
    )
    
    fig_3d.update_layout(
        template='plotly_dark',
        height=700
    )
    
    st.plotly_chart(fig_3d, use_container_width=True)
    
    # Histograma comparativo
    col1, col2 = st.columns(2)
    
    with col1:
        fig_hist = go.Figure()
        fig_hist.add_trace(go.Histogram(
            x=df[df['tsunami'] == 1]['magnitude'],
            name='Con Tsunami',
            marker_color='red',
            opacity=0.7
        ))
        fig_hist.add_trace(go.Histogram(
            x=df[df['tsunami'] == 0]['magnitude'],
            name='Sin Tsunami',
            marker_color='lightblue',
            opacity=0.7
        ))
        
        fig_hist.update_layout(
            title='Comparación de Magnitudes',
            barmode='overlay',
            template='plotly_dark',
            height=400
        )
        
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        fig_depth = go.Figure()
        fig_depth.add_trace(go.Histogram(
            x=df[df['tsunami'] == 1]['depth'],
            name='Con Tsunami',
            marker_color='red',
            opacity=0.7
        ))
        fig_depth.add_trace(go.Histogram(
            x=df[df['tsunami'] == 0]['depth'],
            name='Sin Tsunami',
            marker_color='lightblue',
            opacity=0.7
        ))
        
        fig_depth.update_layout(
            title='Comparación de Profundidades',
            barmode='overlay',
            template='plotly_dark',
            height=400
        )
        
        st.plotly_chart(fig_depth, use_container_width=True)
