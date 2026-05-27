import streamlit as st
import base64
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Loreto Campos Carrasco | Portafolio EnviroTech",
    page_icon="🌿",
    layout="centered"
)

# Función auxiliar para convertir una imagen local a base64 para HTML
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode()
        return encoded_string
    except FileNotFoundError:
        return None

# Definir rutas de imágenes locales
path_perfil = "Screenshot_20260524_150650_ChatGPT.jpg"
path_logo_darwin = "logo.png"
path_logo_biocore = "logo_biocore.png"

# Convertir imágenes de logos a base64 para uso en HTML
encoded_logo_darwin = get_base64_image(path_logo_darwin)
encoded_logo_biocore = get_base64_image(path_logo_biocore)

# CSS Personalizado para elevar la estética (Estilo Card / Premium)
st.markdown("""
    <style>
    /* Fondo y tipografía general */
    .main {
        background-color: #f9fbfd;
    }
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        color: #1e293b;
    }
    
    /* Foto de perfil circular */
    .profile-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        width: 180px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        object-fit: cover;
    }
    
    /* Subtítulo destacado */
    .subtitle {
        text-align: center;
        font-size: 24px;
        font-weight: 300;
        color: #6366f1; /* Tono morado/indigo premium */
        margin-top: 10px;
        margin-bottom: 20px;
    }
    
    /* Texto de biografía */
    .bio-text {
        text-align: justify;
        font-size: 16px;
        color: #475569;
        line-height: 1.6;
    }
    
    /* Contenedor de proyectos (Cards) */
    .project-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);
        transition: transform 0.2s, box-shadow 0.2s;
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }
    
    /* Links de los proyectos */
    .project-link {
        text-decoration: none;
        color: inherit;
    }
    
    /* Logos de proyectos */
    .project-logo {
        max-height: 80px;
        margin-bottom: 15px;
        object-fit: contain;
    }
    </style>
""", unsafe_allow_html=True)

# --- SECCIÓN PRINCIPAL / PERFIL ---

# Mostrar la foto de perfil principal usando st.image para manejo local nativo
col_p1, col_p2, col_p3 = st.columns([1,2,1])
with col_p2:
    try:
        # Cargar la imagen usando PIL para flexibilidad
        img_perfil = Image.open(path_perfil)
        # st.image aplica la clase profile-img CSS automáticamente
        st.image(img_perfil, use_column_width=True)
    except FileNotFoundError:
        st.warning("⚠️ Imagen de perfil no encontrada. Asegúrate de que 'Screenshot_20260524_150650_ChatGPT.jpg' esté en el repositorio.")

st.markdown("<h1 style='text-align: center;'>Loreto Campos Carrasco</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Bióloga & Desarrolladora EnviroTech</div>", unsafe_allow_html=True)

st.markdown("""
<div class='bio-text'>
    Titulada con Distinción Máxima. Combino la gestión ambiental bajo normativa 
    con el desarrollo de soluciones de datos en R y Python para automatizar el 
    monitoreo y mitigar riesgos normativos. Creadora de soluciones inteligentes.
</div>
""", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# --- SECCIÓN DE PROYECTOS (GRID) ---
st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Plataformas y Soluciones</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Proyecto 1: DarwinCheck (Actualizado con imagen base64 y nuevo link)
    if encoded_logo_darwin:
        st.markdown(f"""
        <a href="https://darwin-check.streamlit.app/" target="_blank" class="project-link">
            <div class="project-card">
                <img src="data:image/png;base64,{encoded_logo_darwin}" class="project-logo" alt="Logo DarwinCheck">
                <h3>DarwinCheck</h3>
                <p style='color: #64748b; font-size: 14px;'>Auditoría Ecológica Inteligente</p>
            </div>
        </a>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Logo DarwinCheck no encontrado.")

with col2:
    # Proyecto 2: BioCore Intelligence (Actualizado con imagen base64 y nuevo link)
    if encoded_logo_biocore:
        st.markdown(f"""
        <a href="https://biocoreintelligence.streamlit.app/" target="_blank" class="project-link">
            <div class="project-card">
                <img src="data:image/png;base64,{encoded_logo_biocore}" class="project-logo" alt="Logo BioCore">
                <h3>BioCore Intelligence</h3>
                <p style='color: #64748b; font-size: 14px;'>Vigilancia Ambiental de Alto Nivel</p>
            </div>
        </a>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Logo BioCore no encontrado.")
