import streamlit as st
import pandas as pd
import random
import time
import streamlit.components.v1 as components
from PIL import Image


# ======================================================
# CONFIGURACIÓN GENERAL
# ======================================================

APP_TITLE = "SimuGen BioCode X"
APP_SUBTITLE = "Simulador interactivo para aprender bioinformática, genómica y análisis de secuencias"
APP_LOGO = "SGX"
PROFESSOR_NAME = "Profesor Geno"

APP_VERSION = "Versión 1.0"
LAST_UPDATE = "Última actualización: 7 de julio de 2026"
APP_STATUS = "Estado del proyecto: versión educativa funcional"

ICON_PATH = "assets/icon_dna.png"
SIDEBAR_LOGO_PATH = "assets/sidebar_logo.png"

try:
    APP_ICON = Image.open(ICON_PATH)
except Exception:
    APP_ICON = "🧬"

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide"
)


# ======================================================
# ESTILOS VISUALES
# ======================================================

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f4fbff 0%, #fff8e7 100%);
    }

    .block-container {
        padding-top: 2rem;
        max-width: 1200px;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #e0f2fe, #fef9c3);
    }

    .sidebar-title {
        text-align: center;
        font-weight: 800;
        color: #0f172a;
        font-size: 18px;
        margin-top: 8px;
        margin-bottom: 10px;
    }

    .sidebar-subtitle {
        text-align: center;
        color: #334155;
        font-size: 13px;
        margin-bottom: 18px;
        line-height: 1.4;
    }

    .hero {
        background: linear-gradient(120deg, #3b82f6, #14b8a6);
        padding: 35px;
        border-radius: 28px;
        color: white;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        margin-bottom: 30px;
    }

    .brand-row {
        display: flex;
        align-items: center;
        gap: 18px;
        margin-bottom: 10px;
    }

    .brand-logo {
        width: 78px;
        height: 78px;
        border-radius: 22px;
        background: white;
        color: #0f766e;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        font-weight: 900;
        box-shadow: 0 8px 20px rgba(0,0,0,0.18);
        border: 3px solid rgba(255,255,255,0.85);
    }

    .brand-text h1 {
        margin: 0;
        font-size: 50px;
    }

    .brand-text p {
        margin: 4px 0;
        font-size: 19px;
        line-height: 1.5;
    }

    .hero p {
        font-size: 20px;
        line-height: 1.6;
    }

    .theme-banner {
        background: white;
        color: #0f172a;
        padding: 14px 22px;
        border-radius: 18px;
        border-left: 8px solid #14b8a6;
        box-shadow: 0 5px 18px rgba(0,0,0,0.08);
        margin-bottom: 22px;
        font-weight: bold;
        text-align: center;
    }

    .classroom {
        background: #f2d6a2;
        border-radius: 28px;
        padding: 25px;
        margin-bottom: 28px;
        border: 6px solid #8b5e34;
        position: relative;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.12);
    }

    .board {
        background: #183d2f;
        color: #f8f8f8;
        border: 8px solid #7a4f22;
        border-radius: 12px;
        padding: 28px;
        min-height: 190px;
        font-family: 'Courier New', monospace;
        position: relative;
        overflow: hidden;
        box-shadow: inset 0 0 18px rgba(0,0,0,0.6);
    }

    .board h2 {
        font-family: Arial, sans-serif;
        font-size: 32px;
        margin-bottom: 18px;
        color: #ffffff;
    }

    .board p {
        font-size: 18px;
        line-height: 1.7;
    }

    .chalk {
        width: 75px;
        height: 10px;
        background: #ffffff;
        border-radius: 10px;
        position: absolute;
        bottom: 28px;
        left: 35px;
        box-shadow: 0 0 8px rgba(255,255,255,0.8);
    }

    .chalk.active {
        animation: chalkMove 2.3s infinite alternate ease-in-out;
    }

    @keyframes chalkMove {
        from { left: 35px; transform: rotate(0deg); }
        to { left: 78%; transform: rotate(8deg); }
    }

    .teacher {
        font-size: 90px;
        text-align: center;
        margin-top: 18px;
        animation: teacherFloat 2s infinite alternate ease-in-out;
    }

    @keyframes teacherFloat {
        from { transform: translateY(0px); }
        to { transform: translateY(-8px); }
    }

    .teacher-name {
        text-align: center;
        font-weight: bold;
        color: #1e293b;
        font-size: 17px;
    }

    .module-card {
        background: white;
        border-radius: 22px;
        padding: 24px;
        margin: 16px 0;
        border-left: 10px solid #14b8a6;
        box-shadow: 0 5px 18px rgba(0,0,0,0.08);
        line-height: 1.7;
    }

    .module-card h3 {
        color: #0f766e;
        margin-bottom: 10px;
    }

    .image-card {
        background: linear-gradient(135deg, #dbeafe, #ccfbf1);
        padding: 28px;
        border-radius: 22px;
        text-align: center;
        font-size: 68px;
        margin-bottom: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        min-height: 190px;
    }

    .image-card h3 {
        font-size: 22px;
        color: #0f172a;
    }

    .interpretation {
        background: #ecfeff;
        border-left: 8px solid #0891b2;
        padding: 20px;
        border-radius: 16px;
        margin-top: 18px;
        font-size: 17px;
        line-height: 1.7;
        color: #0f172a;
    }

    .genobox {
        background: linear-gradient(135deg, #fef3c7, #dbeafe);
        border-radius: 22px;
        padding: 24px;
        margin-bottom: 28px;
        border: 3px solid #38bdf8;
        box-shadow: 0 6px 20px rgba(0,0,0,0.10);
    }

    .genobox h3 {
        color: #075985;
        margin-bottom: 8px;
    }

    .game-card {
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        border-radius: 25px;
        padding: 25px;
        border: 4px solid #f59e0b;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        margin-bottom: 20px;
    }

    .score-box {
        background: #dcfce7;
        border: 3px solid #22c55e;
        padding: 18px;
        border-radius: 18px;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 18px;
    }

    .footer {
        background: #0f172a;
        color: white;
        padding: 32px;
        border-radius: 25px;
        margin: 55px auto 0 auto;
        font-size: 15px;
        text-align: center;
        max-width: 900px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.18);
    }

    .footer h4 {
        color: #67e8f9;
        text-align: center;
        font-size: 28px;
        margin-bottom: 16px;
    }

    .footer p {
        text-align: center;
        line-height: 1.7;
        margin-bottom: 10px;
    }

    .footer b {
        color: #bae6fd;
    }

    .footer-meta {
        margin-top: 22px;
        padding-top: 18px;
        border-top: 1px solid rgba(255,255,255,0.25);
        color: #e2e8f0;
        font-size: 14px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# ======================================================
# FUNCIONES VISUALES
# ======================================================

def clave_widget(texto):
    return "".join(c for c in texto if c.isalnum())


def aplicar_tema(menu_actual):
    temas = {
        "Inicio del aula": {
            "fondo": "linear-gradient(135deg, #f0f9ff 0%, #ecfeff 45%, #fff7ed 100%)",
            "hero": "linear-gradient(120deg, #3b82f6, #14b8a6)",
            "acento": "#14b8a6",
            "titulo": "Tema general del aula"
        },
        "1. Transcripción ADN a ARN": {
            "fondo": "linear-gradient(135deg, #ecfdf5 0%, #d1fae5 50%, #f0fdf4 100%)",
            "hero": "linear-gradient(120deg, #059669, #10b981)",
            "acento": "#059669",
            "titulo": "Tema verde: flujo ADN → ARN"
        },
        "2. Traducción ARN a proteína": {
            "fondo": "linear-gradient(135deg, #f5f3ff 0%, #ede9fe 50%, #faf5ff 100%)",
            "hero": "linear-gradient(120deg, #7c3aed, #a855f7)",
            "acento": "#7c3aed",
            "titulo": "Tema morado: ARN → proteína"
        },
        "3. Mutación puntual": {
            "fondo": "linear-gradient(135deg, #fff7ed 0%, #fed7aa 50%, #fee2e2 100%)",
            "hero": "linear-gradient(120deg, #ea580c, #ef4444)",
            "acento": "#ea580c",
            "titulo": "Tema naranja: cambio genético"
        },
        "4. Ensamble de fragmentos": {
            "fondo": "linear-gradient(135deg, #fffbeb 0%, #fef3c7 50%, #fef9c3 100%)",
            "hero": "linear-gradient(120deg, #d97706, #f59e0b)",
            "acento": "#d97706",
            "titulo": "Tema amarillo: reconstrucción de secuencias"
        },
        "5. Alineamiento global": {
            "fondo": "linear-gradient(135deg, #eff6ff 0%, #dbeafe 50%, #e0f2fe 100%)",
            "hero": "linear-gradient(120deg, #2563eb, #0284c7)",
            "acento": "#2563eb",
            "titulo": "Tema azul: comparación de secuencias"
        },
        "6. Filogenia UPGMA": {
            "fondo": "linear-gradient(135deg, #f0fdf4 0%, #dcfce7 50%, #ecfccb 100%)",
            "hero": "linear-gradient(120deg, #166534, #65a30d)",
            "acento": "#166534",
            "titulo": "Tema bosque: relaciones evolutivas"
        },
        "7. Modelado estructural": {
            "fondo": "linear-gradient(135deg, #fdf2f8 0%, #fae8ff 50%, #eef2ff 100%)",
            "hero": "linear-gradient(120deg, #be185d, #7c3aed)",
            "acento": "#be185d",
            "titulo": "Tema magenta: proteína 3D"
        },
        "Juego: Misión Bioinformática": {
            "fondo": "linear-gradient(135deg, #fff7ed 0%, #fef3c7 50%, #dcfce7 100%)",
            "hero": "linear-gradient(120deg, #f97316, #22c55e)",
            "acento": "#f97316",
            "titulo": "Tema aventura: reto del ahorcado genómico"
        },
        "Autoevaluación de 20 preguntas": {
            "fondo": "linear-gradient(135deg, #f8fafc 0%, #e0e7ff 50%, #f1f5f9 100%)",
            "hero": "linear-gradient(120deg, #4f46e5, #64748b)",
            "acento": "#4f46e5",
            "titulo": "Tema evaluación: comprobar aprendizajes"
        },
        "Ayuda guiada": {
            "fondo": "linear-gradient(135deg, #ecfeff 0%, #cffafe 50%, #f0f9ff 100%)",
            "hero": "linear-gradient(120deg, #0891b2, #0ea5e9)",
            "acento": "#0891b2",
            "titulo": "Tema ayuda: orientación paso a paso"
        },
        "Sobre el proyecto": {
            "fondo": "linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #f1f5f9 100%)",
            "hero": "linear-gradient(120deg, #334155, #0f766e)",
            "acento": "#334155",
            "titulo": "Tema institucional: información del proyecto"
        }
    }

    tema = temas.get(menu_actual, temas["Inicio del aula"])

    st.markdown(f"""
    <style>
        .stApp {{
            background: {tema["fondo"]} !important;
        }}

        .hero {{
            background: {tema["hero"]} !important;
        }}

        .module-card {{
            border-left: 10px solid {tema["acento"]} !important;
        }}

        .image-card {{
            border: 3px solid {tema["acento"]};
        }}

        .theme-banner {{
            border-left: 8px solid {tema["acento"]} !important;
        }}
    </style>

    <div class="theme-banner">
        {tema["titulo"]}
    </div>
    """, unsafe_allow_html=True)


def aula_virtual(titulo, texto_pizarra, chalk_active=False):
    clase_tiza = "chalk active" if chalk_active else "chalk"

    st.markdown(f"""
    <div class="classroom">
        <div class="board">
            <h2>{titulo}</h2>
            <p>{texto_pizarra}</p>
            <div class="{clase_tiza}"></div>
        </div>
        <div class="teacher">👨🏿‍🏫</div>
        <p class="teacher-name">{PROFESSOR_NAME}: aprendamos bioinformática paso a paso</p>
    </div>
    """, unsafe_allow_html=True)


def footer():
    footer_html = (
        f'<div class="footer">'
        f'<h4>{APP_TITLE}</h4>'
        f'<p><b>Desarrollado por:</b> Bernny José Alberto Toribio</p>'
        f'<p><b>Propósito:</b> Recurso educativo interactivo para la enseñanza introductoria de la bioinformática y la genómica.</p>'
        f'<p><b>Contacto:</b> bernnyjat17@gmail.com</p>'
        f'<p><b>Sobre el proyecto:</b> {APP_TITLE} adapta procesos bioinformáticos reales a una experiencia didáctica, visual y accesible para estudiantes principiantes.</p>'
        f'<p><b>Nota:</b> Esta plataforma no sustituye herramientas profesionales como BLAST, Clustal Omega, Galaxy, NCBI o RCSB PDB.</p>'
        f'<p class="footer-meta"><b>{APP_VERSION}</b> &nbsp; | &nbsp; <b>{LAST_UPDATE}</b> &nbsp; | &nbsp; <b>{APP_STATUS}</b></p>'
        f'</div>'
    )

    st.markdown(footer_html, unsafe_allow_html=True)


def imagen_modulo(emoji, titulo):
    st.markdown(f"""
    <div class="image-card">
        <div>{emoji}</div>
        <h3>{titulo}</h3>
    </div>
    """, unsafe_allow_html=True)


def interpretacion(texto):
    st.markdown(f"""
    <div class="interpretation">
        <b>Interpretación educativa:</b><br>
        {texto}
    </div>
    """, unsafe_allow_html=True)


# ======================================================
# PROFESOR GENO
# ======================================================

def responder_profesor_geno(pregunta):
    pregunta = pregunta.lower().strip()

    if pregunta == "":
        return "Escribe una duda para que el Profesor Geno pueda ayudarte.", False

    if any(palabra in pregunta for palabra in ["transcripcion", "transcripción", "adn a arn", "arn mensajero"]):
        return (
            "La transcripción es el proceso mediante el cual la información del ADN se copia en una molécula de ARN mensajero. "
            "En este simulador se representa de forma sencilla cambiando la timina, representada por T, por uracilo, representado por U. "
            "Por ejemplo, si el ADN es ATG, el ARN producido será AUG.",
            True
        )

    elif any(palabra in pregunta for palabra in ["traduccion", "traducción", "proteina", "proteína", "codon", "codón", "aminoacido", "aminoácido"]):
        return (
            "La traducción ocurre cuando el ARN mensajero se lee en grupos de tres bases llamados codones. "
            "Cada codón indica un aminoácido específico. Por ejemplo, AUG codifica para metionina y suele funcionar como señal de inicio.",
            True
        )

    elif any(palabra in pregunta for palabra in ["mutacion", "mutación", "puntual", "silenciosa", "sin sentido", "cambio de sentido"]):
        return (
            "Una mutación puntual ocurre cuando cambia una sola base del ADN. Ese cambio puede no afectar la proteína, "
            "puede cambiar un aminoácido o puede generar un codón de parada.",
            True
        )

    elif any(palabra in pregunta for palabra in ["ensamble", "fragmento", "fragmentos", "solapamiento", "unir"]):
        return (
            "El ensamble de fragmentos consiste en reconstruir una secuencia más larga a partir de fragmentos pequeños de ADN. "
            "El simulador busca coincidencias entre el final de un fragmento y el inicio de otro para unirlos.",
            True
        )

    elif any(palabra in pregunta for palabra in ["alineamiento", "needleman", "wunsch", "gap", "matriz", "puntuacion", "puntuación"]):
        return (
            "El alineamiento global compara dos secuencias completas usando una matriz de puntuación. "
            "Needleman-Wunsch asigna puntos por coincidencias y penaliza diferencias o gaps.",
            True
        )

    elif any(palabra in pregunta for palabra in ["filogenia", "upgma", "arbol", "árbol", "distancia genetica", "distancia genética"]):
        return (
            "La filogenia estudia las relaciones evolutivas entre organismos o secuencias. "
            "En este simulador se usa UPGMA, que agrupa primero a los organismos con menor distancia genética.",
            True
        )

    elif any(palabra in pregunta for palabra in ["modelado", "estructura", "estructural", "3d", "3dmol", "proteina 3d", "proteína 3d"]):
        return (
            "El modelado estructural permite observar proteínas en tres dimensiones. "
            "Una mutación puede cambiar propiedades como carga, polaridad o tamaño del aminoácido, afectando la estabilidad o el plegamiento.",
            True
        )

    elif any(palabra in pregunta for palabra in ["bioinformatica", "bioinformática", "para que sirve", "qué es", "que es"]):
        return (
            "La bioinformática utiliza herramientas computacionales para analizar información biológica, como secuencias de ADN, ARN o proteínas.",
            True
        )

    elif any(palabra in pregunta for palabra in ["juego", "puntos", "mision", "misión", "desafio", "desafío", "ahorcado"]):
        return (
            "El juego del ahorcado genómico permite practicar vocabulario de bioinformática respondiendo preguntas y descubriendo palabras ocultas.",
            True
        )

    else:
        return (
            "Disculpa, pero no te entiendo o mi programación no me permite responder eso todavía. "
            "Puedes preguntarme sobre transcripción, traducción, mutaciones, ensamble, alineamiento, filogenia, modelado estructural, bioinformática o el juego.",
            False
        )


def barra_preguntas_profesor_geno():
    st.markdown(f"""
    <div class="genobox">
        <h3>Pregúntale al {PROFESSOR_NAME}</h3>
        <p>
        Escribe una duda sobre la clase. El profesor puede responder preguntas sobre transcripción, traducción, mutaciones,
        ensamble, alineamiento, filogenia, modelado estructural y bioinformática básica.
        </p>
    </div>
    """, unsafe_allow_html=True)

    pregunta = st.text_input(
        "Escribe tu pregunta aquí:",
        placeholder="Ejemplo: ¿Qué es una mutación puntual?"
    )

    if st.button("Preguntar al profesor"):
        respuesta, reconocida = responder_profesor_geno(pregunta)
        st.session_state["respuesta_profesor"] = respuesta
        st.session_state["pregunta_reconocida"] = reconocida
        st.session_state["chalk_active"] = reconocida


def mostrar_respuesta_profesor():
    if "respuesta_profesor" in st.session_state:
        if st.session_state.get("pregunta_reconocida", False):
            st.success(st.session_state["respuesta_profesor"])
        else:
            st.warning(st.session_state["respuesta_profesor"])

    st.session_state["chalk_active"] = False


# ======================================================
# FUNCIONES BIOLÓGICAS
# ======================================================

def limpiar_secuencia(seq):
    return seq.upper().replace(" ", "").replace("\n", "").replace("\t", "")


def validar_adn(seq):
    return len(seq) > 0 and all(base in "ATCG" for base in seq)


def validar_arn(seq):
    return len(seq) > 0 and all(base in "AUCG" for base in seq)


def porcentaje_identidad(aln1, aln2):
    coincidencias = sum(1 for a, b in zip(aln1, aln2) if a == b)
    return round((coincidencias / len(aln1)) * 100, 2) if aln1 else 0


codigo_genetico = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "STOP", "UAG": "STOP",
    "UGU": "Cys", "UGC": "Cys", "UGA": "STOP", "UGG": "Trp",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}


def traducir_arn(arn):
    proteina = []
    codones = []

    for i in range(0, len(arn) - 2, 3):
        codon = arn[i:i + 3]
        aminoacido = codigo_genetico.get(codon, "?")
        codones.append((codon, aminoacido))

        if aminoacido == "STOP":
            proteina.append("STOP")
            break
        else:
            proteina.append(aminoacido)

    return proteina, codones


def overlap(a, b, min_len=2):
    mejor = 0
    for i in range(min_len, min(len(a), len(b)) + 1):
        if a[-i:] == b[:i]:
            mejor = i
    return mejor


def ensamblar_fragmentos(fragmentos, min_overlap=2):
    fragmentos = fragmentos[:]
    pasos = []

    while len(fragmentos) > 1:
        mejor_i, mejor_j, mejor_ov = None, None, 0
        mejor_merge = ""

        for i in range(len(fragmentos)):
            for j in range(len(fragmentos)):
                if i != j:
                    ov = overlap(fragmentos[i], fragmentos[j], min_overlap)
                    if ov > mejor_ov:
                        mejor_i, mejor_j, mejor_ov = i, j, ov
                        mejor_merge = fragmentos[i] + fragmentos[j][ov:]

        if mejor_ov == 0:
            break

        pasos.append({
            "Fragmento A": fragmentos[mejor_i],
            "Fragmento B": fragmentos[mejor_j],
            "Solapamiento": mejor_ov,
            "Resultado unido": mejor_merge
        })

        nuevos = []
        for k, frag in enumerate(fragmentos):
            if k not in [mejor_i, mejor_j]:
                nuevos.append(frag)

        nuevos.append(mejor_merge)
        fragmentos = nuevos

    return fragmentos, pasos


def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    n = len(seq1)
    m = len(seq2)

    matriz = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        matriz[i][0] = matriz[i - 1][0] + gap

    for j in range(1, m + 1):
        matriz[0][j] = matriz[0][j - 1] + gap

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diagonal = matriz[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            arriba = matriz[i - 1][j] + gap
            izquierda = matriz[i][j - 1] + gap
            matriz[i][j] = max(diagonal, arriba, izquierda)

    alineada1 = ""
    alineada2 = ""
    i, j = n, m

    while i > 0 or j > 0:
        puntaje_actual = matriz[i][j]

        if i > 0 and j > 0:
            puntaje_diag = matriz[i - 1][j - 1]
            valor = match if seq1[i - 1] == seq2[j - 1] else mismatch

            if puntaje_actual == puntaje_diag + valor:
                alineada1 = seq1[i - 1] + alineada1
                alineada2 = seq2[j - 1] + alineada2
                i -= 1
                j -= 1
                continue

        if i > 0 and puntaje_actual == matriz[i - 1][j] + gap:
            alineada1 = seq1[i - 1] + alineada1
            alineada2 = "-" + alineada2
            i -= 1
        else:
            alineada1 = "-" + alineada1
            alineada2 = seq2[j - 1] + alineada2
            j -= 1

    return matriz, alineada1, alineada2, matriz[n][m]


def matriz_a_dataframe(matriz, seq1, seq2):
    columnas = ["Inicio"] + [f"{base}{i+1}" for i, base in enumerate(seq2)]
    indices = ["Inicio"] + [f"{base}{i+1}" for i, base in enumerate(seq1)]
    return pd.DataFrame(matriz, index=indices, columns=columnas)


def construir_upgma(labels, distancias_originales):
    clusters = {
        label: {
            "members": [label],
            "height": 0,
            "newick": label
        }
        for label in labels
    }

    nodos = {}
    aristas = []
    pasos = []
    contador = 1

    def distancia_cluster(c1, c2):
        valores = []
        for a in clusters[c1]["members"]:
            for b in clusters[c2]["members"]:
                clave = tuple(sorted([a, b]))
                valores.append(distancias_originales[clave])
        return sum(valores) / len(valores)

    while len(clusters) > 1:
        claves = list(clusters.keys())
        mejor_par = None
        mejor_distancia = float("inf")

        for i in range(len(claves)):
            for j in range(i + 1, len(claves)):
                d = distancia_cluster(claves[i], claves[j])
                if d < mejor_distancia:
                    mejor_distancia = d
                    mejor_par = (claves[i], claves[j])

        a, b = mejor_par
        nuevo = f"N{contador}"
        altura = mejor_distancia / 2

        rama_a = max(altura - clusters[a]["height"], 0)
        rama_b = max(altura - clusters[b]["height"], 0)

        newick = f"({clusters[a]['newick']}:{rama_a:.2f},{clusters[b]['newick']}:{rama_b:.2f})"

        pasos.append({
            "Paso": contador,
            "Clúster unido": f"{a} + {b}",
            "Distancia genética": round(mejor_distancia, 3),
            "Altura del nodo": round(altura, 3)
        })

        nodos[nuevo] = f"U{contador}\\nDist: {mejor_distancia:.2f}"
        aristas.append((nuevo, a))
        aristas.append((nuevo, b))

        nuevos_miembros = clusters[a]["members"] + clusters[b]["members"]

        del clusters[a]
        del clusters[b]

        clusters[nuevo] = {
            "members": nuevos_miembros,
            "height": altura,
            "newick": newick
        }

        contador += 1

    raiz = list(clusters.keys())[0]
    newick_final = clusters[raiz]["newick"] + ";"

    dot = 'digraph G { rankdir=TB; node [shape=box, style="rounded,filled", fillcolor="#ecfeff"];\n'

    for label in labels:
        dot += f'"{label}" [label="{label}", fillcolor="#dcfce7"];\n'

    for nodo, etiqueta in nodos.items():
        dot += f'"{nodo}" [label="{etiqueta}", fillcolor="#dbeafe"];\n'

    for padre, hijo in aristas:
        dot += f'"{padre}" -> "{hijo}";\n'

    dot += "}"

    return pasos, newick_final, dot


def evaluar_mutacion_proteica(original, nueva):
    grupos = {
        "Ala": "hidrofóbico", "Val": "hidrofóbico", "Leu": "hidrofóbico", "Ile": "hidrofóbico", "Phe": "hidrofóbico",
        "Ser": "polar", "Thr": "polar", "Asn": "polar", "Gln": "polar", "Tyr": "polar",
        "Lys": "positivo", "Arg": "positivo", "His": "positivo",
        "Asp": "negativo", "Glu": "negativo",
        "Gly": "especial", "Pro": "especial", "Cys": "especial", "Met": "hidrofóbico", "Trp": "hidrofóbico"
    }

    grupo_original = grupos.get(original, "desconocido")
    grupo_nuevo = grupos.get(nueva, "desconocido")

    if original == nueva:
        return "sin cambio", "No se observa cambio porque el aminoácido original y el nuevo son iguales."

    if grupo_original == grupo_nuevo:
        return "impacto bajo", (
            "El cambio ocurre entre aminoácidos con propiedades químicas parecidas. "
            "Por eso, el efecto estructural esperado podría ser bajo en esta simulación didáctica."
        )

    if {grupo_original, grupo_nuevo} in [
        {"positivo", "negativo"},
        {"hidrofóbico", "polar"},
        {"hidrofóbico", "positivo"},
        {"hidrofóbico", "negativo"}
    ]:
        return "impacto alto", (
            "El cambio ocurre entre aminoácidos con propiedades químicas muy diferentes. "
            "Esto podría alterar interacciones internas, estabilidad o plegamiento de la proteína."
        )

    return "impacto moderado", (
        "El cambio modifica las propiedades del aminoácido, pero el posible efecto dependería "
        "de la posición dentro de la proteína y de sus interacciones con otros residuos."
    )


def visor_3dmol(pdb_id, posicion):
    html = f"""
    <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
    <div id="viewer" style="height: 430px; width: 100%; position: relative; border-radius: 18px; overflow: hidden;"></div>

    <script>
        let viewer = $3Dmol.createViewer("viewer", {{
            backgroundColor: "white"
        }});

        $3Dmol.download("pdb:{pdb_id}", viewer, {{}}, function() {{
            viewer.setStyle({{}}, {{cartoon: {{color: "spectrum"}}}});
            viewer.setStyle({{resi: {posicion}}}, {{stick: {{colorscheme: "magentaCarbon", radius: 0.35}}}});
            viewer.zoomTo();
            viewer.render();
        }});
    </script>
    """

    components.html(html, height=450)


# ======================================================
# JUEGO DEL AHORCADO GENÓMICO
# ======================================================

BANCO_PALABRAS_AHORCADO = [
    {"palabra": "ADN", "pista": "Molécula que almacena la información genética."},
    {"palabra": "ARN", "pista": "Molécula que participa en la expresión de la información genética."},
    {"palabra": "GEN", "pista": "Unidad básica de información hereditaria."},
    {"palabra": "BASE", "pista": "Componente químico representado por letras como A, T, C, G o U."},
    {"palabra": "CODON", "pista": "Grupo de tres bases que codifica un aminoácido."},
    {"palabra": "GENOMA", "pista": "Conjunto completo del material genético de un organismo."},
    {"palabra": "BLAST", "pista": "Herramienta usada para comparar secuencias biológicas."},
    {"palabra": "PDB", "pista": "Base de datos donde se encuentran estructuras de proteínas."},
    {"palabra": "EXON", "pista": "Región de un gen que puede quedar presente en el ARN maduro."},
    {"palabra": "INTRON", "pista": "Región que suele eliminarse durante el procesamiento del ARN."},
    {"palabra": "GAP", "pista": "Espacio introducido durante un alineamiento de secuencias."},
    {"palabra": "MUTACION", "pista": "Cambio en la secuencia genética."},
    {"palabra": "ENSAMBLE", "pista": "Proceso de unir fragmentos para reconstruir una secuencia."},
    {"palabra": "PROTEINA", "pista": "Molécula formada por aminoácidos."},
    {"palabra": "RIBOSOMA", "pista": "Estructura celular donde ocurre la traducción."},
    {"palabra": "SECUENCIA", "pista": "Orden de bases o aminoácidos en una molécula biológica."},
    {"palabra": "UPGMA", "pista": "Algoritmo usado para construir árboles filogenéticos."},
    {"palabra": "FILOGENIA", "pista": "Estudio de las relaciones evolutivas."},
    {"palabra": "HOMOLOGIA", "pista": "Similitud entre secuencias por origen común."},
    {"palabra": "MOLECULA", "pista": "Estructura formada por átomos unidos químicamente."}
]

PREGUNTAS_AHORCADO = [
    {
        "pregunta": "¿Qué molécula se produce durante la transcripción?",
        "opciones": ["ADN", "ARN mensajero", "Proteína"],
        "correcta": "ARN mensajero",
        "retro": "La transcripción copia la información del ADN en ARN mensajero."
    },
    {
        "pregunta": "¿Qué base del ADN se reemplaza por uracilo en el ARN?",
        "opciones": ["Timina", "Adenina", "Guanina"],
        "correcta": "Timina",
        "retro": "En el ARN no se usa timina; se utiliza uracilo."
    },
    {
        "pregunta": "¿Cuántas bases forman un codón?",
        "opciones": ["2", "3", "4"],
        "correcta": "3",
        "retro": "Un codón está formado por tres bases nitrogenadas."
    },
    {
        "pregunta": "¿Qué codón suele funcionar como inicio de la traducción?",
        "opciones": ["AUG", "UAA", "UGA"],
        "correcta": "AUG",
        "retro": "AUG suele funcionar como codón de inicio y codifica para metionina."
    },
    {
        "pregunta": "¿Qué indica un codón STOP?",
        "opciones": ["Inicio de traducción", "Fin de traducción", "Un gap"],
        "correcta": "Fin de traducción",
        "retro": "Un codón STOP indica que la traducción debe detenerse."
    },
    {
        "pregunta": "¿Qué es una mutación puntual?",
        "opciones": ["Cambio de una base", "Unión de fragmentos", "Construcción de árbol"],
        "correcta": "Cambio de una base",
        "retro": "Una mutación puntual ocurre cuando cambia una sola base."
    },
    {
        "pregunta": "¿Qué es una mutación silenciosa?",
        "opciones": ["No cambia la proteína", "Genera siempre STOP", "Elimina el ADN"],
        "correcta": "No cambia la proteína",
        "retro": "Una mutación silenciosa no modifica el aminoácido final."
    },
    {
        "pregunta": "¿Qué busca el ensamblaje de fragmentos?",
        "opciones": ["Reconstruir una secuencia", "Traducir ARN", "Crear proteínas 3D"],
        "correcta": "Reconstruir una secuencia",
        "retro": "El ensamblaje intenta unir fragmentos pequeños para reconstruir una secuencia mayor."
    },
    {
        "pregunta": "¿Qué es un solapamiento?",
        "opciones": ["Región compartida entre fragmentos", "Una proteína", "Una base de ARN"],
        "correcta": "Región compartida entre fragmentos",
        "retro": "El solapamiento permite unir fragmentos que comparten partes de su secuencia."
    },
    {
        "pregunta": "¿Qué algoritmo se utiliza en el alineamiento global del simulador?",
        "opciones": ["Needleman-Wunsch", "UPGMA", "Traducción"],
        "correcta": "Needleman-Wunsch",
        "retro": "Needleman-Wunsch se utiliza para alinear dos secuencias completas."
    },
    {
        "pregunta": "¿Qué representa un gap en un alineamiento?",
        "opciones": ["Un espacio insertado", "Un codón", "Una proteína"],
        "correcta": "Un espacio insertado",
        "retro": "Un gap es un espacio usado para ajustar secuencias durante el alineamiento."
    },
    {
        "pregunta": "¿Qué indica una puntuación alta en un alineamiento?",
        "opciones": ["Mayor similitud", "Menor relación", "Error automático"],
        "correcta": "Mayor similitud",
        "retro": "Una puntuación alta suele indicar mayor similitud entre secuencias."
    },
    {
        "pregunta": "¿Para qué sirve UPGMA?",
        "opciones": ["Construir árboles filogenéticos", "Traducir ARN", "Eliminar mutaciones"],
        "correcta": "Construir árboles filogenéticos",
        "retro": "UPGMA agrupa organismos o secuencias según sus distancias genéticas."
    },
    {
        "pregunta": "En filogenia, una menor distancia genética indica:",
        "opciones": ["Mayor similitud", "Ausencia de ADN", "Mayor error"],
        "correcta": "Mayor similitud",
        "retro": "Mientras menor sea la distancia genética, mayor suele ser la similitud."
    },
    {
        "pregunta": "¿Qué permite observar el modelado estructural?",
        "opciones": ["La forma tridimensional de una proteína", "La edad del organismo", "El número de estudiantes"],
        "correcta": "La forma tridimensional de una proteína",
        "retro": "El modelado estructural permite visualizar proteínas en tres dimensiones."
    },
    {
        "pregunta": "Una mutación en una proteína puede afectar:",
        "opciones": ["Su estabilidad o plegamiento", "El color del navegador", "La velocidad de internet"],
        "correcta": "Su estabilidad o plegamiento",
        "retro": "Una mutación puede cambiar propiedades químicas y afectar la estructura de una proteína."
    },
    {
        "pregunta": "¿Qué base aparece en ARN pero no en ADN?",
        "opciones": ["Uracilo", "Timina", "Guanina"],
        "correcta": "Uracilo",
        "retro": "El ARN utiliza uracilo en lugar de timina."
    },
    {
        "pregunta": "¿Qué base aparece en ADN pero no en ARN?",
        "opciones": ["Timina", "Uracilo", "Adenina"],
        "correcta": "Timina",
        "retro": "El ADN utiliza timina, mientras que el ARN utiliza uracilo."
    },
    {
        "pregunta": "¿Qué herramienta se usa comúnmente para buscar similitud entre secuencias?",
        "opciones": ["BLAST", "PowerPoint", "Excel"],
        "correcta": "BLAST",
        "retro": "BLAST permite comparar secuencias con bases de datos biológicas."
    },
    {
        "pregunta": "¿Qué representa PDB en bioinformática estructural?",
        "opciones": ["Base de datos de estructuras", "Un tipo de codón", "Una mutación silenciosa"],
        "correcta": "Base de datos de estructuras",
        "retro": "PDB almacena estructuras tridimensionales de proteínas y otras macromoléculas."
    }
]


def seleccionar_pregunta_ahorcado():
    st.session_state.ahorcado_pregunta = random.choice(PREGUNTAS_AHORCADO)
    st.session_state.ahorcado_turno += 1
    st.session_state.ahorcado_puede_adivinar = False


def iniciar_ahorcado():
    st.session_state.ahorcado_activo = True
    st.session_state.ahorcado_ganado = False
    st.session_state.ahorcado_perdido = False
    st.session_state.ahorcado_motivo_perdida = ""
    st.session_state.ahorcado_palabras = random.sample(BANCO_PALABRAS_AHORCADO, 3)
    st.session_state.ahorcado_indice = 0
    st.session_state.ahorcado_inicio = time.time()
    st.session_state.ahorcado_turno = 0
    preparar_palabra_ahorcado()
    st.session_state.ahorcado_mensaje = "El reto inició. Responde correctamente para intentar adivinar letras."


def preparar_palabra_ahorcado():
    palabra_actual = st.session_state.ahorcado_palabras[st.session_state.ahorcado_indice]["palabra"]
    st.session_state.ahorcado_reveladas = ["_"] * len(palabra_actual)
    st.session_state.ahorcado_posicion = 0
    st.session_state.ahorcado_errores = 0
    st.session_state.ahorcado_puede_adivinar = False
    seleccionar_pregunta_ahorcado()


def dibujo_ahorcado_html(errores):
    cabeza = '<circle cx="150" cy="85" r="22" stroke="black" stroke-width="5" fill="white" />' if errores >= 1 else ""
    cuerpo = '<line x1="150" y1="107" x2="150" y2="175" stroke="black" stroke-width="5" stroke-linecap="round"/>' if errores >= 2 else ""
    brazo1 = '<line x1="150" y1="130" x2="110" y2="155" stroke="black" stroke-width="5" stroke-linecap="round"/>' if errores >= 3 else ""
    brazo2 = '<line x1="150" y1="130" x2="190" y2="155" stroke="black" stroke-width="5" stroke-linecap="round"/>' if errores >= 4 else ""
    pierna1 = '<line x1="150" y1="175" x2="115" y2="225" stroke="black" stroke-width="5" stroke-linecap="round"/>' if errores >= 5 else ""
    pierna2 = '<line x1="150" y1="175" x2="185" y2="225" stroke="black" stroke-width="5" stroke-linecap="round"/>' if errores >= 6 else ""

    html = f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0;">
        <div style="
            background:white;
            border-radius:20px;
            padding:15px;
            box-shadow:0 6px 18px rgba(0,0,0,0.10);
            text-align:center;
            font-family:Arial, sans-serif;
        ">
            <svg width="280" height="260" viewBox="0 0 280 260">
                <line x1="40" y1="240" x2="220" y2="240" stroke="black" stroke-width="5" stroke-linecap="round"/>
                <line x1="70" y1="240" x2="70" y2="30" stroke="black" stroke-width="5" stroke-linecap="round"/>
                <line x1="70" y1="30" x2="150" y2="30" stroke="black" stroke-width="5" stroke-linecap="round"/>
                <line x1="150" y1="30" x2="150" y2="62" stroke="black" stroke-width="5" stroke-linecap="round"/>
                {cabeza}
                {cuerpo}
                {brazo1}
                {brazo2}
                {pierna1}
                {pierna2}
            </svg>

            <p style="
                font-weight:700;
                color:#0f172a;
                font-size:18px;
                margin-top:5px;
            ">
                Errores: {errores}/6
            </p>
        </div>
    </body>
    </html>
    """

    components.html(html, height=350)


def tiempo_restante_ahorcado():
    transcurrido = int(time.time() - st.session_state.ahorcado_inicio)
    restante = max(0, 900 - transcurrido)
    return restante


def mostrar_cronometro_ahorcado(segundos):
    minutos = segundos // 60
    seg = segundos % 60

    components.html(f"""
    <div style="
        background:#0f172a;
        color:white;
        padding:18px;
        border-radius:18px;
        text-align:center;
        font-size:26px;
        font-weight:800;
        margin-bottom:18px;">
        Tiempo restante: <span id="timer">{minutos:02d}:{seg:02d}</span>
    </div>

    <script>
        let segundos = {segundos};
        const timer = document.getElementById("timer");

        function actualizar() {{
            if (segundos <= 0) {{
                timer.innerHTML = "00:00";
                setTimeout(function() {{
                    window.parent.location.reload();
                }}, 1200);
                return;
            }}

            segundos -= 1;
            let m = Math.floor(segundos / 60);
            let s = segundos % 60;
            timer.innerHTML = String(m).padStart(2, "0") + ":" + String(s).padStart(2, "0");
        }}

        setInterval(actualizar, 1000);
    </script>
    """, height=80)


def mostrar_game_over_ahorcado():
    motivo = st.session_state.get("ahorcado_motivo_perdida", "")

    if motivo == "tiempo":
        mensaje_motivo = "Se agotó el tiempo disponible para completar el reto."
    elif motivo == "muneco":
        mensaje_motivo = "El muñeco del ahorcado se completó por acumulación de errores."
    else:
        mensaje_motivo = "El reto terminó antes de completarse."

    palabra_actual = "No disponible"

    if "ahorcado_palabras" in st.session_state and "ahorcado_indice" in st.session_state:
        indice = min(
            st.session_state.ahorcado_indice,
            len(st.session_state.ahorcado_palabras) - 1
        )
        palabra_actual = st.session_state.ahorcado_palabras[indice]["palabra"]

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #fee2e2, #fecaca);
        border: 4px solid #dc2626;
        border-radius: 25px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 8px 22px rgba(0,0,0,0.15);
        margin-bottom: 25px;
    ">
        <h1 style="color:#991b1b; font-size:48px; margin-bottom:10px;">GAME OVER</h1>
        <h3 style="color:#7f1d1d;">{mensaje_motivo}</h3>
        <p style="font-size:20px; color:#111827;">
            La palabra que estabas intentando descubrir era:
            <b>{palabra_actual}</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="interpretation">
        <b>Retroalimentación:</b><br>
        Debes repasar los conceptos básicos de bioinformática trabajados en el simulador:
        transcripción, traducción, mutaciones, ensamblaje, alineamiento, filogenia y modelado estructural.
        Recuerda que cada respuesta correcta te permite intentar descubrir una letra, pero cada error acerca más el muñeco al final.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Intentar de nuevo"):
        iniciar_ahorcado()
        st.rerun()


# ======================================================
# EJEMPLOS DE SIMULADORES
# ======================================================

EJEMPLOS = {
    "transcripcion": {
        "Ejemplo 1: Secuencia básica": "ATGTTTCAA",
        "Ejemplo 2: Secuencia con varios codones": "ATGAAACCC",
        "Ejemplo 3: Secuencia más larga": "ATGCGTACCTAA"
    },
    "traduccion": {
        "Ejemplo 1: Traducción con STOP": "AUGUUUCAAUGA",
        "Ejemplo 2: Inicio y parada rápida": "AUGGCCUAA",
        "Ejemplo 3: Proteína más larga": "AUGAAACCCGGGUAG"
    },
    "mutacion": {
        "Ejemplo 1: Posible mutación sin sentido": {
            "adn": "ATGAAA",
            "posicion": 4,
            "nueva_base": "T"
        },
        "Ejemplo 2: Cambio de sentido": {
            "adn": "ATGGCT",
            "posicion": 5,
            "nueva_base": "A"
        },
        "Ejemplo 3: Mutación silenciosa probable": {
            "adn": "ATGTTT",
            "posicion": 6,
            "nueva_base": "C"
        }
    },
    "ensamble": {
        "Ejemplo 1: Ensamble sencillo": "ATGCA\nGCATT\nATTGA",
        "Ejemplo 2: Fragmentos de un gen": "GATTACA\nTACAGGA\nGGATTC",
        "Ejemplo 3: Ensamble con mayor solapamiento": "AACCGG\nCCGGTT\nGGTTAA"
    },
    "alineamiento": {
        "Ejemplo 1: Secuencias parecidas": {
            "seq1": "ATGCA",
            "seq2": "ATCCA",
            "match": 1,
            "mismatch": -1,
            "gap": -2
        },
        "Ejemplo 2: Con inserción o gap": {
            "seq1": "ATGCAA",
            "seq2": "ATGCA",
            "match": 1,
            "mismatch": -1,
            "gap": -2
        },
        "Ejemplo 3: Menor similitud": {
            "seq1": "ATGCGT",
            "seq2": "TACGCA",
            "match": 1,
            "mismatch": -1,
            "gap": -2
        }
    },
    "filogenia": {
        "Ejemplo 1: Humano, chimpancé y ratón": {
            "org1": "Humano",
            "org2": "Chimpancé",
            "org3": "Ratón",
            "d12": 2.0,
            "d13": 8.0,
            "d23": 9.0
        },
        "Ejemplo 2: Tres bacterias": {
            "org1": "Bacteria A",
            "org2": "Bacteria B",
            "org3": "Bacteria C",
            "d12": 4.0,
            "d13": 10.0,
            "d23": 7.0
        },
        "Ejemplo 3: Plantas cercanas": {
            "org1": "Planta 1",
            "org2": "Planta 2",
            "org3": "Planta 3",
            "d12": 3.0,
            "d13": 6.0,
            "d23": 5.0
        }
    },
    "estructura": {
        "Ejemplo 1: Crambina": {
            "pdb_id": "1CRN",
            "posicion": 10,
            "original": "Ala",
            "nueva": "Val"
        },
        "Ejemplo 2: Mioglobina": {
            "pdb_id": "1MBN",
            "posicion": 64,
            "original": "His",
            "nueva": "Gly"
        },
        "Ejemplo 3: Hemoglobina": {
            "pdb_id": "4HHB",
            "posicion": 6,
            "original": "Glu",
            "nueva": "Val"
        }
    }
}


# ======================================================
# MENÚ LATERAL
# ======================================================

with st.sidebar:
    try:
        st.image(SIDEBAR_LOGO_PATH, use_container_width=True)
    except Exception:
        st.markdown("<h1 style='text-align:center;'>SGX</h1>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="sidebar-title">{APP_TITLE}</div>
    <div class="sidebar-subtitle">
        Aula interactiva de bioinformática y genómica
    </div>
    """, unsafe_allow_html=True)

    menu = st.radio(
        "Selecciona un espacio del aula",
        [
            "Inicio del aula",
            "1. Transcripción ADN a ARN",
            "2. Traducción ARN a proteína",
            "3. Mutación puntual",
            "4. Ensamble de fragmentos",
            "5. Alineamiento global",
            "6. Filogenia UPGMA",
            "7. Modelado estructural",
            "Juego: Misión Bioinformática",
            "Autoevaluación de 20 preguntas",
            "Ayuda guiada",
            "Sobre el proyecto"
        ]
    )

aplicar_tema(menu)

st.markdown(f"""
<div class="hero">
    <div class="brand-row">
        <div class="brand-logo">{APP_LOGO}</div>
        <div class="brand-text">
            <h1>{APP_TITLE}</h1>
            <p>{APP_SUBTITLE}</p>
        </div>
    </div>
    <p>
    Aprende transcripción, traducción, mutaciones, ensamblaje, alineamiento, filogenia y modelado estructural
    mediante simuladores interactivos, ejemplos guiados y actividades de evaluación.
    </p>
</div>
""", unsafe_allow_html=True)

barra_preguntas_profesor_geno()
chalk_on = st.session_state.get("chalk_active", False)


# ======================================================
# INICIO
# ======================================================

if menu == "Inicio del aula":
    aula_virtual(
        "Bienvenido al aula de SimuGen BioCode X",
        "Hoy aprenderemos cómo la bioinformática permite analizar secuencias biológicas usando simuladores sencillos.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    col1, col2, col3 = st.columns(3)

    with col1:
        imagen_modulo("🧬", "ADN y ARN")
        st.write("Explora cómo se transforma la información genética durante la transcripción.")

    with col2:
        imagen_modulo("🧪", "Proteínas")
        st.write("Observa cómo los codones del ARN se convierten en aminoácidos.")

    with col3:
        imagen_modulo("📊", "Algoritmos")
        st.write("Comprende cómo se comparan secuencias mediante matrices de puntuación.")

    st.markdown(f"""
    <div class="module-card">
        <h3>¿Qué es {APP_TITLE}?</h3>
        <p>
        {APP_TITLE} es una plataforma didáctica que convierte procesos bioinformáticos complejos 
        en simulaciones pequeñas, visuales y fáciles de comprender. Su diseño está inspirado en 
        un aula virtual, donde el usuario aprende como si estuviera recibiendo una clase guiada.
        </p>
        <p>
        El propósito no es reemplazar herramientas profesionales, sino ayudar a que un estudiante 
        principiante entienda la lógica básica de los análisis de secuencias biológicas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    footer()


# ======================================================
# TRANSCRIPCIÓN
# ======================================================

elif menu == "1. Transcripción ADN a ARN":
    aula_virtual(
        "Clase 1: Transcripción",
        "En la transcripción, la información del ADN se copia en ARN mensajero. La T se cambia por U.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    imagen_modulo("DNA ➜ RNA", "Transcripción de ADN a ARN")

    st.markdown("""
    <div class="module-card">
        <h3>¿Qué aprenderás aquí?</h3>
        <p>
        Este simulador muestra cómo una secuencia de ADN puede convertirse en ARN mensajero. 
        Es una representación sencilla de un proceso biológico esencial.
        </p>
    </div>
    """, unsafe_allow_html=True)

    ejemplo_trans = st.selectbox(
        "Elige un ejemplo para probar:",
        list(EJEMPLOS["transcripcion"].keys())
    )

    adn = st.text_input(
        "Escribe una secuencia de ADN:",
        EJEMPLOS["transcripcion"][ejemplo_trans],
        key=f"trans_{clave_widget(ejemplo_trans)}"
    )

    adn = limpiar_secuencia(adn)

    if st.button("Simular transcripción"):
        if validar_adn(adn):
            arn = adn.replace("T", "U")
            st.success(f"ARN mensajero producido: {arn}")

            df = pd.DataFrame({
                "ADN original": list(adn),
                "ARN transcrito": list(arn)
            })

            st.table(df)

            interpretacion(
                "El simulador reemplazó cada timina del ADN por uracilo, porque el ARN utiliza U en lugar de T. "
                "Esta simulación representa una idea biológica fundamental: la información genética puede copiarse de una molécula a otra."
            )
        else:
            st.error("Secuencia no válida. Usa solamente las bases A, T, C y G.")

    footer()


# ======================================================
# TRADUCCIÓN
# ======================================================

elif menu == "2. Traducción ARN a proteína":
    aula_virtual(
        "Clase 2: Traducción",
        "El ARN se lee en grupos de tres bases llamados codones. Cada codón representa un aminoácido.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    imagen_modulo("RNA ➜ Proteína", "Traducción de ARN a proteína")

    st.markdown("""
    <div class="module-card">
        <h3>¿Qué aprenderás aquí?</h3>
        <p>
        Este módulo permite observar cómo una secuencia de ARN mensajero se transforma en una cadena de aminoácidos.
        </p>
    </div>
    """, unsafe_allow_html=True)

    ejemplo_trad = st.selectbox(
        "Elige un ejemplo para probar:",
        list(EJEMPLOS["traduccion"].keys())
    )

    arn = st.text_input(
        "Escribe una secuencia de ARN:",
        EJEMPLOS["traduccion"][ejemplo_trad],
        key=f"trad_{clave_widget(ejemplo_trad)}"
    )

    arn = limpiar_secuencia(arn)

    if st.button("Simular traducción"):
        if validar_arn(arn):
            proteina, codones = traducir_arn(arn)

            st.success("Proteína obtenida:")
            st.write(" - ".join(proteina))

            st.subheader("Lectura de codones")
            st.table(pd.DataFrame(codones, columns=["Codón", "Aminoácido"]))

            if len(arn) % 3 != 0:
                st.warning("La secuencia no es múltiplo de 3. Las bases finales incompletas no fueron traducidas.")

            interpretacion(
                "El simulador leyó el ARN en grupos de tres bases. Cada triplete fue interpretado como un codón "
                "y se transformó en su aminoácido correspondiente. Si aparece un codón STOP, la traducción se detiene."
            )
        else:
            st.error("Secuencia no válida. Usa solamente las bases A, U, C y G.")

    footer()


# ======================================================
# MUTACIÓN PUNTUAL
# ======================================================

elif menu == "3. Mutación puntual":
    aula_virtual(
        "Clase 3: Mutaciones",
        "Una mutación puntual ocurre cuando cambia una sola base. Ese pequeño cambio puede modificar una proteína.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    imagen_modulo("ADN alterado", "Mutación puntual")

    st.markdown("""
    <div class="module-card">
        <h3>¿Qué aprenderás aquí?</h3>
        <p>
        Este módulo permite simular qué sucede cuando una base del ADN cambia por otra.
        </p>
    </div>
    """, unsafe_allow_html=True)

    ejemplo_mut = st.selectbox(
        "Elige un ejemplo para probar:",
        list(EJEMPLOS["mutacion"].keys())
    )

    datos_mut = EJEMPLOS["mutacion"][ejemplo_mut]

    adn = st.text_input(
        "Secuencia original de ADN:",
        datos_mut["adn"],
        key=f"mut_adn_{clave_widget(ejemplo_mut)}"
    )

    adn = limpiar_secuencia(adn)

    if validar_adn(adn):
        posicion = st.number_input(
            "Posición de la base que deseas cambiar:",
            min_value=1,
            max_value=len(adn),
            value=min(datos_mut["posicion"], len(adn)),
            key=f"mut_pos_{clave_widget(ejemplo_mut)}"
        )

        bases = ["A", "T", "C", "G"]

        nueva_base = st.selectbox(
            "Nueva base:",
            bases,
            index=bases.index(datos_mut["nueva_base"]),
            key=f"mut_base_{clave_widget(ejemplo_mut)}"
        )

        if st.button("Aplicar mutación"):
            lista = list(adn)
            base_original = lista[posicion - 1]
            lista[posicion - 1] = nueva_base
            adn_mutado = "".join(lista)

            arn_original = adn.replace("T", "U")
            arn_mutado = adn_mutado.replace("T", "U")

            proteina_original, _ = traducir_arn(arn_original)
            proteina_mutada, _ = traducir_arn(arn_mutado)

            df = pd.DataFrame({
                "Elemento": ["ADN", "ARN", "Proteína"],
                "Original": [adn, arn_original, " - ".join(proteina_original)],
                "Mutado": [adn_mutado, arn_mutado, " - ".join(proteina_mutada)]
            })

            st.table(df)
            st.write(f"Base cambiada en la posición {posicion}: `{base_original}` → `{nueva_base}`")

            if proteina_original == proteina_mutada:
                st.success("Tipo de efecto: mutación silenciosa. La proteína no cambió.")
                tipo = "silenciosa"
            elif "STOP" in proteina_mutada and "STOP" not in proteina_original:
                st.error("Tipo de efecto: mutación sin sentido. Se generó un codón de parada.")
                tipo = "sin sentido"
            else:
                st.warning("Tipo de efecto: mutación de cambio de sentido. Cambió al menos un aminoácido.")
                tipo = "cambio de sentido"

            interpretacion(
                f"La mutación aplicada fue clasificada como una mutación {tipo}. "
                "Esto demuestra que un solo cambio en la secuencia de ADN puede tener consecuencias distintas."
            )
    else:
        st.error("Secuencia no válida. Usa solamente las bases A, T, C y G.")

    footer()


# ======================================================
# ENSAMBLE
# ======================================================

elif menu == "4. Ensamble de fragmentos":
    aula_virtual(
        "Clase 4: Ensamble de fragmentos",
        "Cuando tenemos fragmentos pequeños de ADN, podemos unirlos si comparten regiones solapadas.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    imagen_modulo("Fragmentos de ADN", "Ensamble simple de fragmentos")

    st.markdown("""
    <div class="module-card">
        <h3>¿Qué aprenderás aquí?</h3>
        <p>
        Este simulador muestra una versión reducida del ensamblaje de secuencias.
        </p>
    </div>
    """, unsafe_allow_html=True)

    ejemplo_ens = st.selectbox(
        "Elige un ejemplo para probar:",
        list(EJEMPLOS["ensamble"].keys())
    )

    entrada = st.text_area(
        "Escribe los fragmentos de ADN, uno por línea:",
        EJEMPLOS["ensamble"][ejemplo_ens],
        key=f"ens_{clave_widget(ejemplo_ens)}"
    )

    min_overlap = st.slider("Tamaño mínimo del solapamiento:", 2, 5, 2)

    if st.button("Simular ensamblaje"):
        fragmentos = [limpiar_secuencia(f) for f in entrada.splitlines() if f.strip()]

        if all(validar_adn(f) for f in fragmentos) and len(fragmentos) >= 2:
            resultado, pasos = ensamblar_fragmentos(fragmentos, min_overlap)

            if pasos:
                st.table(pd.DataFrame(pasos))
            else:
                st.warning("No se encontraron solapamientos suficientes entre los fragmentos.")

            st.subheader("Resultado final")
            st.success(" / ".join(resultado))

            interpretacion(
                "El simulador buscó regiones compartidas entre el final de un fragmento y el inicio de otro. "
                "Cuando encontró un solapamiento suficiente, unió ambos fragmentos para formar una secuencia más larga."
            )
        else:
            st.error("Debes introducir al menos dos fragmentos válidos de ADN usando A, T, C y G.")

    footer()


# ======================================================
# ALINEAMIENTO GLOBAL
# ======================================================

elif menu == "5. Alineamiento global":
    aula_virtual(
        "Clase 5: Alineamiento global",
        "Needleman-Wunsch compara dos secuencias completas usando una matriz de puntuación.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    imagen_modulo("Matriz de comparación", "Alineamiento global de secuencias")

    st.markdown("""
    <div class="module-card">
        <h3>¿Qué aprenderás aquí?</h3>
        <p>
        Este módulo utiliza el algoritmo Needleman-Wunsch para comparar dos secuencias completas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    ejemplo_aln = st.selectbox(
        "Elige un ejemplo para probar:",
        list(EJEMPLOS["alineamiento"].keys())
    )

    datos_aln = EJEMPLOS["alineamiento"][ejemplo_aln]

    col1, col2 = st.columns(2)

    with col1:
        seq1 = st.text_input(
            "Secuencia 1:",
            datos_aln["seq1"],
            key=f"aln_seq1_{clave_widget(ejemplo_aln)}"
        )

    with col2:
        seq2 = st.text_input(
            "Secuencia 2:",
            datos_aln["seq2"],
            key=f"aln_seq2_{clave_widget(ejemplo_aln)}"
        )

    seq1 = limpiar_secuencia(seq1)
    seq2 = limpiar_secuencia(seq2)

    st.subheader("Parámetros de puntuación")

    col3, col4, col5 = st.columns(3)

    with col3:
        match = st.number_input(
            "Coincidencia",
            value=float(datos_aln["match"]),
            step=0.5,
            format="%.2f",
            key=f"aln_match_{clave_widget(ejemplo_aln)}"
        )

    with col4:
        mismatch = st.number_input(
            "Diferencia",
            value=float(datos_aln["mismatch"]),
            step=0.5,
            format="%.2f",
            key=f"aln_mismatch_{clave_widget(ejemplo_aln)}"
        )

    with col5:
        gap = st.number_input(
            "Gap",
            value=float(datos_aln["gap"]),
            step=0.5,
            format="%.2f",
            key=f"aln_gap_{clave_widget(ejemplo_aln)}"
        )

    if st.button("Simular alineamiento"):
        if validar_adn(seq1) and validar_adn(seq2):
            matriz, aln1, aln2, score = needleman_wunsch(seq1, seq2, match, mismatch, gap)

            st.subheader("Matriz de puntuación")
            df_matriz = matriz_a_dataframe(matriz, seq1, seq2)
            st.dataframe(df_matriz, use_container_width=True)

            st.subheader("Alineamiento obtenido")
            st.code(aln1)
            st.code(aln2)

            identidad = porcentaje_identidad(aln1, aln2)

            st.success(f"Puntuación final del alineamiento: {score}")
            st.info(f"Porcentaje de identidad aproximado: {identidad}%")

            interpretacion(
                "El algoritmo construyó una matriz comparando cada posición de una secuencia con cada posición de la otra. "
                "Las coincidencias aumentan la puntuación, mientras que las diferencias y los gaps la reducen."
            )
        else:
            st.error("Ambas secuencias deben ser válidas. Usa solamente A, T, C y G.")

    footer()


# ======================================================
# FILOGENIA UPGMA
# ======================================================

elif menu == "6. Filogenia UPGMA":
    aula_virtual(
        "Clase 6: Filogenia UPGMA",
        "La filogenia permite representar relaciones evolutivas usando distancias genéticas.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    imagen_modulo("Árbol evolutivo", "Árbol filogenético dinámico")

    st.markdown("""
    <div class="module-card">
        <h3>¿Qué aprenderás aquí?</h3>
        <p>
        Este simulador utiliza una versión didáctica del algoritmo UPGMA. El usuario introduce distancias genéticas 
        entre organismos y el sistema agrupa primero a los organismos más parecidos.
        </p>
    </div>
    """, unsafe_allow_html=True)

    ejemplo_fil = st.selectbox(
        "Elige un ejemplo para probar:",
        list(EJEMPLOS["filogenia"].keys())
    )

    datos_fil = EJEMPLOS["filogenia"][ejemplo_fil]

    st.subheader("Organismos o secuencias")

    col1, col2, col3 = st.columns(3)

    with col1:
        org1 = st.text_input(
            "Organismo A",
            datos_fil["org1"],
            key=f"fil_org1_{clave_widget(ejemplo_fil)}"
        )

    with col2:
        org2 = st.text_input(
            "Organismo B",
            datos_fil["org2"],
            key=f"fil_org2_{clave_widget(ejemplo_fil)}"
        )

    with col3:
        org3 = st.text_input(
            "Organismo C",
            datos_fil["org3"],
            key=f"fil_org3_{clave_widget(ejemplo_fil)}"
        )

    st.subheader("Distancias genéticas")

    d12 = st.number_input(
        f"Distancia entre {org1} y {org2}",
        min_value=0.0,
        value=datos_fil["d12"],
        key=f"fil_d12_{clave_widget(ejemplo_fil)}"
    )

    d13 = st.number_input(
        f"Distancia entre {org1} y {org3}",
        min_value=0.0,
        value=datos_fil["d13"],
        key=f"fil_d13_{clave_widget(ejemplo_fil)}"
    )

    d23 = st.number_input(
        f"Distancia entre {org2} y {org3}",
        min_value=0.0,
        value=datos_fil["d23"],
        key=f"fil_d23_{clave_widget(ejemplo_fil)}"
    )

    if st.button("Construir árbol UPGMA"):
        labels = [org1, org2, org3]

        distancias = {
            tuple(sorted([org1, org2])): d12,
            tuple(sorted([org1, org3])): d13,
            tuple(sorted([org2, org3])): d23
        }

        pasos, newick, dot = construir_upgma(labels, distancias)

        st.subheader("Pasos del agrupamiento")
        st.table(pd.DataFrame(pasos))

        st.subheader("Árbol filogenético visual")
        st.graphviz_chart(dot)

        st.subheader("Formato Newick")
        st.code(newick)

        interpretacion(
            "El algoritmo agrupó primero los organismos con menor distancia genética, porque se consideran más similares. "
            "Después comparó ese grupo con el organismo restante para construir el árbol completo."
        )

    footer()


# ======================================================
# MODELADO ESTRUCTURAL
# ======================================================

elif menu == "7. Modelado estructural":
    aula_virtual(
        "Clase 7: Modelado estructural",
        "Una mutación puede modificar propiedades de una proteína y afectar su estructura tridimensional.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    imagen_modulo("Proteína 3D", "Visualizador estructural de proteína")

    st.markdown("""
    <div class="module-card">
        <h3>¿Qué aprenderás aquí?</h3>
        <p>
        Este módulo utiliza un visor molecular basado en 3Dmol.js para observar una proteína en tres dimensiones. 
        También permite simular una mutación puntual a nivel de aminoácidos y estimar su posible impacto estructural.
        </p>
    </div>
    """, unsafe_allow_html=True)

    ejemplo_est = st.selectbox(
        "Elige un ejemplo para probar:",
        list(EJEMPLOS["estructura"].keys())
    )

    datos_est = EJEMPLOS["estructura"][ejemplo_est]

    st.subheader("Proteína a visualizar")

    pdb_id = st.text_input(
        "Código PDB",
        datos_est["pdb_id"],
        key=f"est_pdb_{clave_widget(ejemplo_est)}"
    )

    posicion = st.number_input(
        "Residuo o posición simulada de la mutación",
        min_value=1,
        value=datos_est["posicion"],
        key=f"est_pos_{clave_widget(ejemplo_est)}"
    )

    aminoacidos = [
        "Ala", "Val", "Leu", "Ile", "Phe", "Ser", "Thr", "Asn", "Gln",
        "Lys", "Arg", "His", "Asp", "Glu", "Gly", "Pro", "Cys", "Met", "Trp", "Tyr"
    ]

    col1, col2 = st.columns(2)

    with col1:
        original = st.selectbox(
            "Aminoácido original",
            aminoacidos,
            index=aminoacidos.index(datos_est["original"]),
            key=f"est_original_{clave_widget(ejemplo_est)}"
        )

    with col2:
        nueva = st.selectbox(
            "Aminoácido mutado",
            aminoacidos,
            index=aminoacidos.index(datos_est["nueva"]),
            key=f"est_nueva_{clave_widget(ejemplo_est)}"
        )

    if st.button("Simular mutación estructural"):
        st.subheader("Visualización 3D de la proteína")

        visor_3dmol(pdb_id, posicion)

        impacto, explicacion = evaluar_mutacion_proteica(original, nueva)

        st.subheader("Resultado de la simulación")

        st.write(f"Mutación simulada: **{original}{posicion}{nueva}**")
        st.write(f"Impacto estimado: **{impacto.upper()}**")

        interpretacion(
            explicacion + " El residuo seleccionado se resalta en la estructura para relacionar la mutación con una posición espacial de la proteína."
        )

    st.info("Nota: el visor 3D necesita conexión a internet para cargar la estructura desde la base de datos PDB.")

    footer()


# ======================================================
# JUEGO: AHORCADO GENÓMICO
# ======================================================

elif menu == "Juego: Misión Bioinformática":
    aula_virtual(
        "Reto del Ahorcado Genómico",
        "Responde preguntas de bioinformática, adivina letras y descubre tres palabras antes de que se acabe el tiempo.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    st.markdown("""
    <div class="game-card">
        <h2>Reto del Ahorcado Genómico</h2>
        <p>
        En este reto deberás descubrir <b>3 palabras bioinformáticas</b> en un máximo de <b>15 minutos</b>.
        Para intentar adivinar cada letra, primero debes responder correctamente una pregunta.
        Si fallas una pregunta o una letra, el muñeco del ahorcado se irá completando.
        Si el muñeco se completa o se acaba el tiempo, aparecerá el mensaje de <b>GAME OVER</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.get("ahorcado_perdido", False):
        mostrar_game_over_ahorcado()
        footer()

    elif st.session_state.get("ahorcado_ganado", False):
        st.balloons()
        st.success("¡Muy bien! Descubriste las 3 palabras antes de que terminara el tiempo.")
        st.markdown("""
        <div class="interpretation">
            <b>Retroalimentación:</b><br>
            Lograste relacionar conceptos de bioinformática con sus definiciones y aplicaste razonamiento para descubrir las palabras.
            Este tipo de juego refuerza vocabulario científico, atención, memoria y comprensión conceptual.
        </div>
        """, unsafe_allow_html=True)

        if st.button("Intentar de nuevo"):
            iniciar_ahorcado()
            st.rerun()

        footer()

    elif not st.session_state.get("ahorcado_activo", False):
        st.info("Presiona el botón para iniciar el reto. El cronómetro comenzará inmediatamente.")

        if st.button("Empezar juego"):
            iniciar_ahorcado()
            st.rerun()

        footer()

    else:
        restante = tiempo_restante_ahorcado()

        if restante <= 0:
            st.session_state.ahorcado_perdido = True
            st.session_state.ahorcado_activo = False
            st.session_state.ahorcado_motivo_perdida = "tiempo"
            st.rerun()

        mostrar_cronometro_ahorcado(restante)

        palabra_info = st.session_state.ahorcado_palabras[st.session_state.ahorcado_indice]
        palabra = palabra_info["palabra"]
        reveladas = st.session_state.ahorcado_reveladas
        posicion = st.session_state.ahorcado_posicion
        errores = st.session_state.ahorcado_errores

        st.markdown(f"""
        <div class="score-box">
            Palabra {st.session_state.ahorcado_indice + 1} de 3 |
            Letras: {len(palabra)} |
            Errores: {errores}/6
        </div>
        """, unsafe_allow_html=True)

        col_dibujo, col_juego = st.columns([1, 2])

        with col_dibujo:
            dibujo_ahorcado_html(errores)

        with col_juego:
            st.subheader("Palabra oculta")
            st.markdown(
                f"<div style='font-size:42px;letter-spacing:12px;font-weight:900;color:#0f172a;background:white;padding:20px;border-radius:18px;text-align:center;'>{' '.join(reveladas)}</div>",
                unsafe_allow_html=True
            )

            st.write(f"Vas por la letra número **{posicion + 1}** de **{len(palabra)}**.")

            if st.button("Pistas"):
                st.info(f"Pista: {palabra_info['pista']}")

            st.write(st.session_state.ahorcado_mensaje)

            pregunta = st.session_state.ahorcado_pregunta

            st.markdown("### Pregunta para ganar oportunidad")
            respuesta = st.radio(
                pregunta["pregunta"],
                pregunta["opciones"],
                index=None,
                key=f"pregunta_ahorcado_{st.session_state.ahorcado_turno}"
            )

            if st.button("Responder pregunta"):
                if respuesta is None:
                    st.warning("Selecciona una respuesta antes de continuar.")
                elif respuesta == pregunta["correcta"]:
                    st.session_state.ahorcado_puede_adivinar = True
                    st.session_state.ahorcado_mensaje = "Respuesta correcta. Ahora puedes intentar adivinar la letra."
                    st.success(pregunta["retro"])
                else:
                    st.session_state.ahorcado_errores += 1
                    st.session_state.ahorcado_mensaje = f"Respuesta incorrecta. {pregunta['retro']}"

                    if st.session_state.ahorcado_errores >= 6:
                        st.session_state.ahorcado_perdido = True
                        st.session_state.ahorcado_activo = False
                        st.session_state.ahorcado_motivo_perdida = "muneco"
                    else:
                        seleccionar_pregunta_ahorcado()

                    st.rerun()

            if st.session_state.get("ahorcado_puede_adivinar", False):
                letra = st.text_input(
                    "Escribe la letra que crees que corresponde:",
                    max_chars=1,
                    key=f"letra_ahorcado_{st.session_state.ahorcado_turno}_{posicion}"
                )

                if st.button("Adivinar letra"):
                    letra = letra.upper().strip()

                    if letra == "":
                        st.warning("Debes escribir una letra.")
                    elif not letra.isalpha():
                        st.warning("Escribe solamente una letra.")
                    else:
                        letra_correcta = palabra[posicion]

                        if letra == letra_correcta:
                            st.session_state.ahorcado_reveladas[posicion] = letra
                            st.session_state.ahorcado_posicion += 1

                            if st.session_state.ahorcado_posicion >= len(palabra):
                                st.success(f"¡Correcto! Descubriste la palabra: {palabra}")

                                st.session_state.ahorcado_indice += 1

                                if st.session_state.ahorcado_indice >= 3:
                                    st.session_state.ahorcado_ganado = True
                                    st.session_state.ahorcado_activo = False
                                else:
                                    preparar_palabra_ahorcado()
                                    st.session_state.ahorcado_mensaje = "Muy bien. Pasaste a la siguiente palabra."

                                st.rerun()

                            else:
                                st.session_state.ahorcado_mensaje = "Letra correcta. Sigue respondiendo preguntas para descubrir la palabra."
                                seleccionar_pregunta_ahorcado()
                                st.rerun()

                        else:
                            st.session_state.ahorcado_errores += 1
                            st.session_state.ahorcado_mensaje = f"Letra incorrecta. La letra correcta no era {letra}."

                            if st.session_state.ahorcado_errores >= 6:
                                st.session_state.ahorcado_perdido = True
                                st.session_state.ahorcado_activo = False
                                st.session_state.ahorcado_motivo_perdida = "muneco"
                            else:
                                seleccionar_pregunta_ahorcado()

                            st.rerun()

        footer()


# ======================================================
# AUTOEVALUACIÓN
# ======================================================

elif menu == "Autoevaluación de 20 preguntas":
    aula_virtual(
        "Autoevaluación",
        "Esta prueba permite comprobar qué tanto comprendiste después de usar los simuladores.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    st.markdown("""
    <div class="module-card">
        <h3>Descripción de la autoevaluación</h3>
        <p>
        Esta sección contiene 20 preguntas de selección múltiple relacionadas con los módulos del simulador: 
        transcripción, traducción, mutaciones, ensamble, alineamiento, filogenia y modelado estructural.
        </p>
        <p>
        Ninguna respuesta aparece marcada al inicio. El usuario debe seleccionar una opción por pregunta. 
        Al finalizar, el sistema muestra la puntuación y una retroalimentación indicando cuáles respuestas fueron correctas 
        y cuáles deben repasarse.
        </p>
    </div>
    """, unsafe_allow_html=True)

    preguntas = [
        {
            "pregunta": "1. ¿Qué molécula se produce durante la transcripción?",
            "opciones": ["ADN", "ARN mensajero", "Proteína"],
            "correcta": "ARN mensajero",
            "explicacion": "La transcripción copia la información del ADN en ARN mensajero."
        },
        {
            "pregunta": "2. ¿Qué base del ADN se reemplaza por uracilo en ARN?",
            "opciones": ["Timina", "Adenina", "Guanina"],
            "correcta": "Timina",
            "explicacion": "En ARN no se usa timina; se usa uracilo."
        },
        {
            "pregunta": "3. ¿Qué bases se utilizan en el ADN?",
            "opciones": ["A, T, C, G", "A, U, C, G", "A, B, C, D"],
            "correcta": "A, T, C, G",
            "explicacion": "El ADN contiene adenina, timina, citosina y guanina."
        },
        {
            "pregunta": "4. ¿Qué bases se utilizan en el ARN?",
            "opciones": ["A, U, C, G", "A, T, C, G", "A, R, N, D"],
            "correcta": "A, U, C, G",
            "explicacion": "El ARN contiene adenina, uracilo, citosina y guanina."
        },
        {
            "pregunta": "5. ¿Cuántas bases forman un codón?",
            "opciones": ["2", "3", "4"],
            "correcta": "3",
            "explicacion": "Un codón está formado por tres bases nitrogenadas."
        },
        {
            "pregunta": "6. ¿Qué codón suele funcionar como inicio de la traducción?",
            "opciones": ["AUG", "UAA", "CCC"],
            "correcta": "AUG",
            "explicacion": "AUG suele funcionar como codón de inicio y codifica para metionina."
        },
        {
            "pregunta": "7. ¿Qué significa STOP en la traducción?",
            "opciones": ["Fin de la traducción", "Inicio de ADN", "Un gap"],
            "correcta": "Fin de la traducción",
            "explicacion": "Un codón STOP indica que la traducción debe detenerse."
        },
        {
            "pregunta": "8. ¿Qué es una mutación puntual?",
            "opciones": ["Cambio de una base", "Destrucción del ribosoma", "Unión de proteínas"],
            "correcta": "Cambio de una base",
            "explicacion": "Una mutación puntual ocurre cuando cambia una sola base."
        },
        {
            "pregunta": "9. ¿Qué es una mutación silenciosa?",
            "opciones": ["No cambia la proteína", "Siempre mata la célula", "Elimina todo el ADN"],
            "correcta": "No cambia la proteína",
            "explicacion": "Una mutación silenciosa no modifica el aminoácido final."
        },
        {
            "pregunta": "10. ¿Qué es una mutación sin sentido?",
            "opciones": ["Genera un codón de parada", "No cambia nada", "Une fragmentos"],
            "correcta": "Genera un codón de parada",
            "explicacion": "Una mutación sin sentido produce un codón STOP prematuro."
        },
        {
            "pregunta": "11. ¿Qué busca el ensamblaje de fragmentos?",
            "opciones": ["Reconstruir una secuencia", "Traducir ARN", "Crear gaps"],
            "correcta": "Reconstruir una secuencia",
            "explicacion": "El ensamblaje intenta unir fragmentos pequeños para reconstruir una secuencia mayor."
        },
        {
            "pregunta": "12. ¿Qué es un solapamiento?",
            "opciones": ["Región compartida entre fragmentos", "Una proteína", "Una base prohibida"],
            "correcta": "Región compartida entre fragmentos",
            "explicacion": "El solapamiento permite unir fragmentos que comparten partes de su secuencia."
        },
        {
            "pregunta": "13. ¿Qué algoritmo se usa en el alineamiento global de este simulador?",
            "opciones": ["Needleman-Wunsch", "UPGMA", "BLASTX"],
            "correcta": "Needleman-Wunsch",
            "explicacion": "Needleman-Wunsch se utiliza para realizar alineamiento global."
        },
        {
            "pregunta": "14. ¿Qué representa un gap?",
            "opciones": ["Un espacio insertado", "Un aminoácido", "Una base de ARN"],
            "correcta": "Un espacio insertado",
            "explicacion": "Un gap es un espacio usado para ajustar secuencias durante el alineamiento."
        },
        {
            "pregunta": "15. ¿Qué indica una puntuación alta en un alineamiento?",
            "opciones": ["Mayor similitud", "Menor relación", "Error obligatorio"],
            "correcta": "Mayor similitud",
            "explicacion": "Una puntuación alta suele indicar mayor similitud entre las secuencias."
        },
        {
            "pregunta": "16. ¿Para qué sirve UPGMA?",
            "opciones": ["Construir árboles filogenéticos", "Traducir ARN", "Eliminar mutaciones"],
            "correcta": "Construir árboles filogenéticos",
            "explicacion": "UPGMA agrupa organismos o secuencias según sus distancias genéticas."
        },
        {
            "pregunta": "17. En filogenia, una menor distancia genética indica:",
            "opciones": ["Mayor similitud", "Menor relación", "Ausencia de ADN"],
            "correcta": "Mayor similitud",
            "explicacion": "Mientras menor es la distancia genética, mayor suele ser la similitud entre organismos o secuencias."
        },
        {
            "pregunta": "18. ¿Qué permite observar el modelado estructural?",
            "opciones": ["La forma tridimensional de una proteína", "La cantidad de estudiantes", "El tamaño de una bacteria"],
            "correcta": "La forma tridimensional de una proteína",
            "explicacion": "El modelado estructural permite visualizar proteínas en tres dimensiones."
        },
        {
            "pregunta": "19. Una mutación en una proteína puede afectar:",
            "opciones": ["Su estabilidad o plegamiento", "El color del monitor", "La velocidad de internet"],
            "correcta": "Su estabilidad o plegamiento",
            "explicacion": "Una mutación puede cambiar propiedades químicas y afectar la estructura o función de una proteína."
        },
        {
            "pregunta": "20. ¿Cuál es el propósito principal de SimuGen BioCode X?",
            "opciones": ["Enseñar conceptos bioinformáticos de forma didáctica", "Reemplazar todas las herramientas profesionales", "Hacer diagnósticos médicos"],
            "correcta": "Enseñar conceptos bioinformáticos de forma didáctica",
            "explicacion": "SimuGen BioCode X es una herramienta educativa, no una plataforma profesional de diagnóstico."
        }
    ]

    respuestas_usuario = {}
    faltantes = []

    for i, item in enumerate(preguntas):
        respuesta = st.radio(
            item["pregunta"],
            item["opciones"],
            index=None,
            key=f"autoevaluacion_{i}"
        )
        respuestas_usuario[i] = respuesta

    if st.button("Calificar autoevaluación"):
        puntaje = 0
        retroalimentacion = []

        for i, item in enumerate(preguntas):
            respuesta = respuestas_usuario[i]

            if respuesta is None:
                faltantes.append(i + 1)
            elif respuesta == item["correcta"]:
                puntaje += 1
                retroalimentacion.append({
                    "Pregunta": i + 1,
                    "Resultado": "Correcta",
                    "Tu respuesta": respuesta,
                    "Respuesta correcta": item["correcta"],
                    "Retroalimentación": item["explicacion"]
                })
            else:
                retroalimentacion.append({
                    "Pregunta": i + 1,
                    "Resultado": "Incorrecta",
                    "Tu respuesta": respuesta,
                    "Respuesta correcta": item["correcta"],
                    "Retroalimentación": item["explicacion"]
                })

        if faltantes:
            st.warning(f"Debes responder todas las preguntas. Te faltan las preguntas: {faltantes}")
        else:
            st.success(f"Tu puntuación fue: {puntaje}/20")

            porcentaje = (puntaje / 20) * 100

            if porcentaje >= 90:
                st.balloons()
                st.write("Excelente. Demuestras un dominio muy alto de los conceptos trabajados.")
            elif porcentaje >= 70:
                st.write("Muy bien. Comprendiste la mayoría de los contenidos, aunque puedes reforzar algunos detalles.")
            elif porcentaje >= 50:
                st.warning("Resultado aceptable. Conviene repasar los módulos donde fallaste.")
            else:
                st.error("Debes repasar los conceptos básicos. Vuelve a practicar con los simuladores.")

            st.subheader("Retroalimentación pregunta por pregunta")
            df_retro = pd.DataFrame(retroalimentacion)
            st.dataframe(df_retro, use_container_width=True)

    footer()


# ======================================================
# AYUDA GUIADA
# ======================================================

elif menu == "Ayuda guiada":
    aula_virtual(
        "Ayuda guiada",
        "Esta sección explica cómo usar cada simulador, qué datos escribir y cómo interpretar los resultados.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    st.markdown("""
    <div class="module-card">
        <h3>¿Para qué sirve esta ayuda guiada?</h3>
        <p>
        Esta sección orienta al usuario paso a paso para utilizar correctamente cada espacio del simulador.
        Aquí se explica qué hace cada módulo, qué tipo de datos se deben escribir, qué botones se deben presionar
        y cómo interpretar los resultados obtenidos.
        </p>
        <p>
        La plataforma está diseñada para estudiantes que están comenzando a estudiar bioinformática, por eso los ejemplos
        son pequeños, visuales y fáciles de modificar.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Recomendación general: usa primero los ejemplos que ya trae el simulador. Después modifica las secuencias poco a poco para observar cómo cambian los resultados."
    )

    with st.expander("1. Pasos generales para usar la plataforma", expanded=True):
        st.markdown("""
        **Sigue estos pasos:**

        1. Ve al menú lateral izquierdo.
        2. Selecciona el módulo que deseas trabajar.
        3. Lee primero la explicación del aula virtual.
        4. Observa el ejemplo que aparece cargado.
        5. Modifica los datos si deseas probar otra situación.
        6. Presiona el botón de simulación.
        7. Revisa la tabla, matriz, resultado o visualización generada.
        8. Lee la interpretación educativa para comprender qué significa el resultado.

        **Importante:** cada módulo trabaja con datos pequeños porque el objetivo es enseñar el proceso, no reemplazar herramientas profesionales.
        """)

    with st.expander("2. Módulo de Transcripción ADN a ARN"):
        st.markdown("""
        **Objetivo del módulo:**  
        Mostrar cómo una secuencia de ADN se transforma en ARN mensajero.

        **Qué debes escribir:**  
        Una secuencia de ADN usando solamente estas letras:

        `A, T, C, G`

        **Ejemplo válido:**  
        `ATGTTTCAA`

        **Qué hace el simulador:**  
        Cambia cada `T` del ADN por `U`, porque el ARN usa uracilo en lugar de timina.

        **Resultado esperado:**  
        Si escribes:

        `ATGTTTCAA`

        el simulador produce:

        `AUGUUUCAA`

        **Cómo interpretar el resultado:**  
        El resultado representa una versión simplificada de la transcripción, donde la información genética pasa de ADN a ARN.
        """)

    with st.expander("3. Módulo de Traducción ARN a proteína"):
        st.markdown("""
        **Objetivo del módulo:**  
        Explicar cómo el ARN mensajero puede leerse para formar una cadena de aminoácidos.

        **Qué debes escribir:**  
        Una secuencia de ARN usando solamente estas letras:

        `A, U, C, G`

        **Ejemplo válido:**  
        `AUGUUUCAAUGA`

        **Qué hace el simulador:**  
        Lee el ARN en grupos de tres bases llamados **codones**.  
        Cada codón se convierte en un aminoácido.

        **Ejemplo:**  
        `AUG` → Metionina  
        `UUU` → Fenilalanina  
        `UGA` → STOP

        **Cómo interpretar el resultado:**  
        El simulador muestra cómo una secuencia de ARN puede convertirse en una proteína.  
        Si aparece un codón `STOP`, la traducción se detiene.
        """)

    with st.expander("4. Módulo de Mutación puntual"):
        st.markdown("""
        **Objetivo del módulo:**  
        Mostrar qué puede ocurrir cuando cambia una sola base del ADN.

        **Qué debes hacer:**

        1. Escribe una secuencia de ADN.
        2. Selecciona la posición de la base que deseas cambiar.
        3. Elige la nueva base.
        4. Presiona el botón **Aplicar mutación**.

        **Tipos de resultados posibles:**

        - **Mutación silenciosa:** cambia el ADN, pero no cambia la proteína.
        - **Mutación de cambio de sentido:** cambia un aminoácido.
        - **Mutación sin sentido:** aparece un codón STOP antes de tiempo.

        **Cómo interpretar el resultado:**  
        El simulador compara la secuencia original con la mutada para mostrar si el cambio fue importante o no.
        """)

    with st.expander("5. Módulo de Ensamble de fragmentos"):
        st.markdown("""
        **Objetivo del módulo:**  
        Simular cómo se pueden unir fragmentos pequeños de ADN para reconstruir una secuencia más larga.

        **Qué debes escribir:**  
        Varios fragmentos de ADN, uno debajo del otro.

        **Ejemplo válido:**

        ```text
        ATGCA
        GCATT
        ATTGA
        ```

        **Qué hace el simulador:**  
        Busca regiones repetidas o compartidas entre los fragmentos.  
        A esas regiones se les llama **solapamientos**.

        **Cómo interpretar el resultado:**  
        Si dos fragmentos tienen una parte en común, el simulador los une para formar una secuencia más larga.
        Esto representa una versión simplificada del ensamblaje genómico.
        """)

    with st.expander("6. Módulo de Alineamiento global"):
        st.markdown("""
        **Objetivo del módulo:**  
        Comparar dos secuencias completas de ADN usando el algoritmo Needleman-Wunsch.

        **Qué debes escribir:**  
        Dos secuencias de ADN usando:

        `A, T, C, G`

        **Ejemplo:**

        Secuencia 1: `ATGCA`  
        Secuencia 2: `ATCCA`

        **Parámetros que puedes modificar:**

        - **Coincidencia:** puntos cuando dos bases son iguales.
        - **Diferencia:** penalización cuando dos bases son distintas.
        - **Gap:** penalización por insertar un espacio.

        **Qué muestra el simulador:**

        - Una matriz de puntuación.
        - El alineamiento final.
        - La puntuación obtenida.
        - El porcentaje aproximado de identidad.

        **Cómo interpretar el resultado:**  
        Una puntuación alta indica que las secuencias son más parecidas.  
        Los gaps ayudan a ajustar las secuencias cuando hay inserciones o eliminaciones.
        """)

    with st.expander("7. Módulo de Filogenia UPGMA"):
        st.markdown("""
        **Objetivo del módulo:**  
        Construir un árbol filogenético sencillo a partir de distancias genéticas.

        **Qué debes escribir:**  
        Tres nombres de organismos o secuencias y sus distancias entre sí.

        **Ejemplo:**

        - Humano – Chimpancé: 2
        - Humano – Ratón: 8
        - Chimpancé – Ratón: 9

        **Qué hace el simulador:**  
        Agrupa primero los organismos que tienen menor distancia genética.

        **Qué significa menor distancia genética:**  
        Significa que los organismos o secuencias son más parecidos entre sí.

        **Cómo interpretar el árbol:**  
        Los organismos que aparecen unidos primero son los más cercanos evolutivamente.
        """)

    with st.expander("8. Módulo de Modelado estructural"):
        st.markdown("""
        **Objetivo del módulo:**  
        Observar una proteína en tres dimensiones y simular el posible efecto de una mutación.

        **Qué debes hacer:**

        1. Selecciona un ejemplo de proteína.
        2. Observa el código PDB.
        3. Elige una posición de aminoácido.
        4. Selecciona el aminoácido original y el aminoácido mutado.
        5. Presiona **Simular mutación estructural**.

        **Qué significa PDB:**  
        Es una base de datos donde se almacenan estructuras tridimensionales de proteínas.

        **Cómo interpretar el resultado:**  
        El simulador estima si el cambio puede tener impacto bajo, moderado o alto según las propiedades químicas del aminoácido.
        """)

    with st.expander("9. Juego: Reto del Ahorcado Genómico"):
        st.markdown("""
        **Objetivo del juego:**  
        Reforzar vocabulario bioinformático mediante un reto de palabras ocultas.

        **Cómo se juega:**

        1. Presiona **Empezar juego**.
        2. El cronómetro comienza a correr.
        3. Debes descubrir 3 palabras bioinformáticas.
        4. Para intentar adivinar una letra, primero debes responder una pregunta correctamente.
        5. Si respondes mal, el muñeco del ahorcado avanza.
        6. Si escribes una letra incorrecta, también se suma un error.
        7. Si completas las 3 palabras antes de que termine el tiempo, ganas.
        8. Si se acaba el tiempo o se completa el muñeco, aparece **GAME OVER**.

        **Botón de pistas:**  
        El botón **Pistas** muestra una ayuda relacionada con la palabra oculta.

        **Qué se aprende con el juego:**  
        Vocabulario científico, relación entre conceptos y memoria de términos bioinformáticos.
        """)

    with st.expander("10. Autoevaluación de 20 preguntas"):
        st.markdown("""
        **Objetivo de la autoevaluación:**  
        Comprobar si el usuario comprendió los contenidos trabajados en los simuladores.

        **Cómo funciona:**

        1. Lee cada pregunta.
        2. Selecciona una sola respuesta.
        3. Ninguna respuesta aparece marcada al inicio.
        4. Al terminar, presiona **Calificar autoevaluación**.
        5. El sistema muestra tu puntuación.
        6. También indica qué preguntas acertaste y cuáles fallaste.

        **Cómo interpretar la retroalimentación:**

        - Si sacas una puntuación alta, dominas la mayoría de los contenidos.
        - Si fallas varias preguntas, revisa nuevamente los módulos relacionados.
        - La retroalimentación te indica cuál era la respuesta correcta y por qué.
        """)

    with st.expander("11. Errores comunes y cómo solucionarlos"):
        st.markdown("""
        **Error 1: La secuencia no es válida**  
        Ocurre cuando escribes letras diferentes a las permitidas.

        - Para ADN usa: `A, T, C, G`
        - Para ARN usa: `A, U, C, G`

        **Error 2: La traducción no toma todas las bases**  
        Puede ocurrir cuando la secuencia de ARN no tiene una cantidad de bases múltiplo de 3.

        **Error 3: El alineamiento no da el resultado esperado**  
        Revisa los valores de coincidencia, diferencia y gap.  
        Cambiar esos parámetros modifica la matriz y la puntuación final.

        **Error 4: El visor 3D no carga**  
        El módulo de modelado estructural necesita conexión a internet para cargar la proteína desde PDB.

        **Error 5: El juego no avanza**  
        Debes responder correctamente una pregunta antes de poder intentar adivinar una letra.
        """)

    with st.expander("12. Recomendaciones para aprender mejor"):
        st.markdown("""
        - Empieza con los ejemplos que ya aparecen en cada módulo.
        - Cambia solo una cosa a la vez para observar el efecto.
        - Compara los resultados antes y después de modificar una secuencia.
        - Lee siempre la interpretación educativa.
        - Usa la autoevaluación al final para comprobar tu aprendizaje.
        - Usa el juego como repaso de vocabulario.
        - No uses secuencias muy largas, porque esta plataforma es didáctica y trabaja a pequeña escala.
        """)

    st.success(
        "Con esta guía, el usuario puede aprender a usar cada simulador paso a paso y comprender mejor los resultados."
    )

    footer()


# ======================================================
# SOBRE EL PROYECTO
# ======================================================

elif menu == "Sobre el proyecto":
    aula_virtual(
        "Sobre SimuGen BioCode X",
        "Este proyecto fue creado como una propuesta individual para enseñar bioinformática de manera interactiva.",
        chalk_active=chalk_on
    )

    mostrar_respuesta_profesor()

    st.markdown(f"""
    <div class="module-card">
        <h3>Información general</h3>
        <p><b>Nombre del proyecto:</b> {APP_TITLE}: Simulador interactivo para el aprendizaje de la bioinformática y la genómica.</p>
        <p><b>Desarrollador:</b> Bernny José Alberto Toribio.</p>
        <p><b>Tipo de recurso:</b> Simulador web educativo.</p>
        <p><b>Público objetivo:</b> Estudiantes de secundaria y primeros niveles universitarios.</p>
    </div>

    <div class="module-card">
        <h3>Justificación pedagógica</h3>
        <p>
        La bioinformática puede resultar difícil para estudiantes principiantes porque combina biología, matemática, 
        programación y análisis de datos. Por esa razón, {APP_TITLE} transforma conceptos complejos en simulaciones 
        pequeñas, visuales y guiadas.
        </p>
    </div>

    <div class="module-card">
        <h3>Limitaciones</h3>
        <p>
        Este simulador trabaja con secuencias cortas y modelos simplificados. Por tanto, no debe utilizarse para análisis 
        profesionales o diagnósticos reales. Su finalidad es exclusivamente educativa.
        </p>
    </div>
    """, unsafe_allow_html=True)

    footer()