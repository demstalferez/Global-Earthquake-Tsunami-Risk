#!/bin/bash

# ============================================================================
# Script de Inicialización del Panel de Inteligencia Sísmico
# ============================================================================
# Este script verifica las dependencias y lanza la aplicación Streamlit
# Autor: Sistema de Análisis Sísmico
# ============================================================================

echo "🌊 Panel de Inteligencia: Riesgo Global de Terremotos y Tsunamis"
echo "=================================================================="
echo ""

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# ============================================================================
# 1. VERIFICAR PYTHON
# ============================================================================

echo "🔍 Verificando instalación de Python..."

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 no está instalado${NC}"
    echo "Por favor instala Python 3.8 o superior desde https://www.python.org/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✅ Python $PYTHON_VERSION encontrado${NC}"
echo ""

# ============================================================================
# 2. VERIFICAR ARCHIVO DE DATOS
# ============================================================================

echo "🔍 Verificando archivo de datos..."

DATA_FILE="../data/earthquake_data_tsunami.csv"

if [ ! -f "$DATA_FILE" ]; then
    echo -e "${RED}❌ Archivo de datos no encontrado: $DATA_FILE${NC}"
    echo "Por favor asegúrate de que el archivo CSV esté en la carpeta data/"
    exit 1
fi

echo -e "${GREEN}✅ Archivo de datos encontrado${NC}"
echo ""

# ============================================================================
# 3. VERIFICAR/CREAR ENTORNO VIRTUAL
# ============================================================================

echo "🔍 Verificando entorno virtual..."

if [ ! -d "venv" ]; then
    echo -e "${YELLOW}⚠️  Entorno virtual no encontrado. Creando...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}✅ Entorno virtual creado${NC}"
else
    echo -e "${GREEN}✅ Entorno virtual encontrado${NC}"
fi

echo ""

# ============================================================================
# 4. ACTIVAR ENTORNO VIRTUAL
# ============================================================================

echo "🔄 Activando entorno virtual..."

source venv/bin/activate

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Entorno virtual activado${NC}"
else
    echo -e "${RED}❌ Error al activar entorno virtual${NC}"
    exit 1
fi

echo ""

# ============================================================================
# 5. INSTALAR/ACTUALIZAR DEPENDENCIAS
# ============================================================================

echo "📦 Verificando dependencias..."

if [ ! -f "venv/.dependencies_installed" ]; then
    echo -e "${YELLOW}⚠️  Instalando dependencias (esto puede tomar unos minutos)...${NC}"
    pip install --upgrade pip
    pip install -r requirements.txt
    
    if [ $? -eq 0 ]; then
        touch venv/.dependencies_installed
        echo -e "${GREEN}✅ Dependencias instaladas correctamente${NC}"
    else
        echo -e "${RED}❌ Error al instalar dependencias${NC}"
        exit 1
    fi
else
    echo -e "${GREEN}✅ Dependencias ya instaladas${NC}"
fi

echo ""

# ============================================================================
# 6. LANZAR APLICACIÓN
# ============================================================================

echo "🚀 Lanzando Panel de Inteligencia Sísmico..."
echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}  🌐 La aplicación se abrirá en: http://localhost:8501${NC}"
echo -e "${GREEN}  ⌨️  Presiona Ctrl+C para detener el servidor${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

sleep 2

streamlit run app.py

# ============================================================================
# 7. CLEANUP AL SALIR
# ============================================================================

echo ""
echo "👋 Cerrando aplicación..."
deactivate
echo -e "${GREEN}✅ Hasta pronto!${NC}"
