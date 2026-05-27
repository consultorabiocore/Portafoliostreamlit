# ============================================================================ #
#          DarwinCheck Vol.1 - Auditoría Taxonómica y Geográfica             #
#               Versión Python/Streamlit (MIGRACIÓN DESDE R)                 #
# ============================================================================ #

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import json
from io import BytesIO
import warnings

warnings.filterwarnings('ignore')
# ==================== IMPORTAR MÓDULOS ====================
from modules.config import *
from modules.utils import (
    safe_val, normalizar_texto, limpiar_dataframe, fmt_entero, fmt_decimal,
    fmt_coordenada, detectar_encabezado, formatar_hora, gms_a_decimal,
    registrar_log
)
from modules.taxonomia import gestor_taxonomia
from modules.coordenadas import validador
from modules.ecologia import calc_ecologico
from modules.graficos import gen_graficos
from modules.excel_io import gestor_excel
# ==================== CONFIGURACIÓN STREAMLIT ====================
st.set_page_config(
    page_title="DarwinCheck Vol.1",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS
st.markdown("""
    <style>
    .metric-card { background: linear-gradient(135deg, #27ae60 0%, #1e8449 100%);
                   color: white; padding: 20px; border-radius: 10px; 
