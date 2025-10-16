"""
Módulo de Carga y Filtrado de Datos
====================================
Funciones para cargar, validar y filtrar datos sísmicos.
"""

import pandas as pd
import streamlit as st
from pathlib import Path
from typing import Dict, Any

# ============================================================================
# CONSTANTES
# ============================================================================

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "earthquake_data_tsunami.csv"

# ============================================================================
# CARGA DE DATOS
# ============================================================================

@st.cache_data(ttl=3600)  # Cache por 1 hora
def load_data() -> pd.DataFrame:
    """
    Carga y prepara el dataset de terremotos.
    
    Returns:
        pd.DataFrame: DataFrame con datos sísmicos procesados
        
    Raises:
        FileNotFoundError: Si el archivo de datos no existe
        ValueError: Si los datos no tienen el formato esperado
    """
    try:
        # Cargar datos
        df = pd.read_csv(DATA_PATH)
        
        # Validar columnas requeridas
        required_cols = ['magnitude', 'depth', 'latitude', 'longitude', 
                        'tsunami', 'Year', 'Month', 'sig']
        
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Faltan columnas requeridas: {missing_cols}")
        
        # Crear columnas derivadas útiles
        df['shallow'] = (df['depth'] < 70).astype(int)
        df['high_magnitude'] = (df['magnitude'] >= 7.0).astype(int)
        df['ring_of_fire'] = ((df['latitude'].abs() > 10) & 
                              ((df['longitude'].between(120, -60)) | 
                               (df['longitude'].between(-180, -60)))).astype(int)
        
        # Crear categorías de magnitud
        df['mag_category'] = pd.cut(
            df['magnitude'],
            bins=[0, 6.5, 7.0, 7.5, 10],
            labels=['Moderado', 'Alto', 'Muy Alto', 'Extremo']
        )
        
        # Crear categorías de profundidad
        df['depth_category'] = pd.cut(
            df['depth'],
            bins=[-1, 70, 300, 700],
            labels=['Superficial (<70km)', 'Intermedio (70-300km)', 'Profundo (>300km)']
        )
        
        # Limpiar valores nulos en columnas críticas
        df['cdi'] = df['cdi'].fillna(0)
        df['mmi'] = df['mmi'].fillna(0)
        
        return df
        
    except FileNotFoundError:
        raise FileNotFoundError(
            f"No se encontró el archivo de datos en: {DATA_PATH}\n"
            "Verifica que el archivo earthquake_data_tsunami.csv esté en la carpeta data/"
        )
    except Exception as e:
        raise Exception(f"Error al cargar los datos: {str(e)}")

# ============================================================================
# FILTRADO DE DATOS
# ============================================================================

def get_filtered_data(df: pd.DataFrame, filters: Dict[str, Any]) -> pd.DataFrame:
    """
    Aplica filtros al DataFrame según las selecciones del usuario.
    
    Args:
        df: DataFrame original
        filters: Diccionario con configuraciones de filtros
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    df_filtered = df.copy()
    
    # Filtro por rango de años
    if 'year_range' in filters:
        year_min, year_max = filters['year_range']
        df_filtered = df_filtered[
            (df_filtered['Year'] >= year_min) & 
            (df_filtered['Year'] <= year_max)
        ]
    
    # Filtro por rango de magnitud
    if 'magnitude_range' in filters:
        mag_min, mag_max = filters['magnitude_range']
        df_filtered = df_filtered[
            (df_filtered['magnitude'] >= mag_min) & 
            (df_filtered['magnitude'] <= mag_max)
        ]
    
    # Filtro por rango de profundidad
    if 'depth_range' in filters:
        depth_min, depth_max = filters['depth_range']
        df_filtered = df_filtered[
            (df_filtered['depth'] >= depth_min) & 
            (df_filtered['depth'] <= depth_max)
        ]
    
    # Filtro por tsunami
    if 'tsunami_filter' in filters:
        if filters['tsunami_filter'] == 'Solo con Tsunami':
            df_filtered = df_filtered[df_filtered['tsunami'] == 1]
        elif filters['tsunami_filter'] == 'Solo sin Tsunami':
            df_filtered = df_filtered[df_filtered['tsunami'] == 0]
        # Si es 'Todos', no se filtra
    
    # Filtro por región (Ring of Fire)
    if 'region_filter' in filters:
        if filters['region_filter'] == 'Solo Ring of Fire':
            df_filtered = df_filtered[df_filtered['ring_of_fire'] == 1]
        elif filters['region_filter'] == 'Fuera Ring of Fire':
            df_filtered = df_filtered[df_filtered['ring_of_fire'] == 0]
    
    # Filtro por meses
    if 'months' in filters and filters['months']:
        df_filtered = df_filtered[df_filtered['Month'].isin(filters['months'])]
    
    return df_filtered

# ============================================================================
# ESTADÍSTICAS DE DATOS
# ============================================================================

def get_data_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Genera un resumen estadístico del DataFrame.
    
    Args:
        df: DataFrame a resumir
        
    Returns:
        Dict con estadísticas clave
    """
    return {
        'total_events': len(df),
        'tsunami_events': int(df['tsunami'].sum()),
        'tsunami_rate': float(df['tsunami'].mean() * 100),
        'avg_magnitude': float(df['magnitude'].mean()),
        'max_magnitude': float(df['magnitude'].max()),
        'avg_depth': float(df['depth'].mean()),
        'years_covered': int(df['Year'].max() - df['Year'].min() + 1),
        'countries_affected': df[['latitude', 'longitude']].drop_duplicates().shape[0]
    }
