"""
Módulo de Estilos CSS
======================
Define y aplica estilos personalizados para la aplicación Streamlit.
"""

import streamlit as st

def apply_custom_css():
    """
    Aplica estilos CSS personalizados a la aplicación.
    Incluye temas oscuros/claros, animaciones y componentes responsivos.
    """
    
    custom_css = """
    <style>
    /* ====================================================================
       VARIABLES CSS (Tema Principal)
       ==================================================================== */
    :root {
        --primary-color: #1f77b4;
        --secondary-color: #ff7f0e;
        --danger-color: #d62728;
        --success-color: #2ca02c;
        --background-dark: #0e1117;
        --background-light: #ffffff;
        --text-primary: #fafafa;
        --text-secondary: #b0b0b0;
        --card-background: #1e1e1e;
        --border-color: #333333;
    }
    
    /* ====================================================================
       RESET Y CONFIGURACIÓN GLOBAL
       ==================================================================== */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* ====================================================================
       CABECERA PRINCIPAL
       ==================================================================== */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        animation: fadeInDown 0.8s ease-in-out;
    }
    
    .main-header h1 {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .main-header .subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        font-weight: 300;
        margin-top: 0.5rem;
    }
    
    /* ====================================================================
       ANIMACIONES
       ==================================================================== */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* ====================================================================
       TARJETAS Y CONTENEDORES
       ==================================================================== */
    .info-card {
        background: var(--card-background);
        border-left: 4px solid var(--primary-color);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: fadeIn 0.6s ease-in-out;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    .warning-card {
        background: rgba(255, 193, 7, 0.1);
        border-left: 4px solid #ffc107;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .danger-card {
        background: rgba(220, 53, 69, 0.1);
        border-left: 4px solid #dc3545;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .success-card {
        background: rgba(40, 167, 69, 0.1);
        border-left: 4px solid #28a745;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    /* ====================================================================
       MÉTRICAS PERSONALIZADAS
       ==================================================================== */
    div[data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary-color);
    }
    
    div[data-testid="stMetricDelta"] {
        font-size: 1rem;
    }
    
    /* ====================================================================
       SIDEBAR PERSONALIZADA
       ==================================================================== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e1e1e 0%, #2d2d2d 100%);
        border-right: 2px solid var(--border-color);
    }
    
    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }
    
    /* ====================================================================
       BOTONES
       ==================================================================== */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    
    /* ====================================================================
       TABS
       ==================================================================== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: var(--card-background);
        border-radius: 10px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        background: transparent;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 255, 255, 0.05);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* ====================================================================
       SELECTORES Y SLIDERS
       ==================================================================== */
    .stSelectbox, .stMultiSelect {
        animation: slideInLeft 0.5s ease-in-out;
    }
    
    .stSlider {
        padding: 1rem 0;
    }
    
    /* ====================================================================
       TABLAS
       ==================================================================== */
    .dataframe {
        border: none !important;
        border-radius: 10px;
        overflow: hidden;
    }
    
    .dataframe th {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        padding: 1rem;
        text-align: left;
    }
    
    .dataframe td {
        padding: 0.75rem;
        border-bottom: 1px solid var(--border-color);
    }
    
    .dataframe tr:hover {
        background: rgba(255, 255, 255, 0.05);
    }
    
    /* ====================================================================
       GRÁFICOS PLOTLY
       ==================================================================== */
    .js-plotly-plot {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* ====================================================================
       EXPANDERS
       ==================================================================== */
    .streamlit-expanderHeader {
        background: var(--card-background);
        border-radius: 8px;
        font-weight: 600;
        font-size: 1.1rem;
        padding: 1rem;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(255, 255, 255, 0.05);
    }
    
    /* ====================================================================
       FOOTER
       ==================================================================== */
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: var(--text-secondary);
        font-size: 0.9rem;
        margin-top: 3rem;
        border-top: 1px solid var(--border-color);
    }
    
    .footer a {
        color: var(--primary-color);
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .footer a:hover {
        color: var(--secondary-color);
        text-decoration: underline;
    }
    
    /* ====================================================================
       RESPONSIVIDAD
       ==================================================================== */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 1.8rem;
        }
        
        .main-header .subtitle {
            font-size: 0.9rem;
        }
        
        .info-card {
            padding: 1rem;
        }
    }
    
    /* ====================================================================
       SPINNER DE CARGA
       ==================================================================== */
    .stSpinner > div {
        border-top-color: var(--primary-color) !important;
    }
    
    /* ====================================================================
       SCROLLBAR PERSONALIZADA
       ==================================================================== */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--background-dark);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    </style>
    """
    
    st.markdown(custom_css, unsafe_allow_html=True)
