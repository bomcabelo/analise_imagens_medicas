import os
import tempfile
import logging
from PIL import Image as PILImage
from agno.agent import Agent
from agno.models.google import Gemini
from agno.media import Image as AgnoImage
from agno.tools.tavily import TavilyTools
from textwrap import dedent
import streamlit as st
from dotenv import load_dotenv

# Configuração inicial
load_dotenv()
logging.basicConfig(level=logging.INFO)

# Configurações do Streamlit
st.set_page_config(page_title="Análise de Imagens Médicas", layout="centered", page_icon="🩺")
st.title("🩺 Análise de Imagens Médicas")
st.markdown(
    """
    Carregue uma **imagem médica** (raio-X, ressonância, tomografia, ultrassom, etc.)
    e nosso agente de IA a analisará, fornecendo resultados detalhados, diagnósticos e insights.  
    ⚠️ **Importante:** Sempre consulte profissionais de saúde qualificados.
    """
)

# Verifica chaves de API
if not os.environ.get("GOOGLE_API_KEY"):
    st.error("❌ Defina sua chave de API do Google (GOOGLE_API_KEY) no arquivo .env")
    st.stop()
if not os.environ.get("TAVILY_API_KEY"):
    st.warning("⚠️ TAVILY_API_KEY não definida. A pesquisa médica será limitada.")

# Escolha do modelo
st.sidebar.header("Configuração do Modelo")
id_model = st.sidebar.selectbox(
    "Escolha o modelo Gemini",
    ("gemini-2.0-flash", "gemini-2.5-flash-preview-05-20"),
)

# Função de pré-processamento
def preprocess_img(img_path):
    """Redimensiona e salva a imagem em um diretório temporário"""
    image = PILImage.open(img_path)
    width, height = image.size
    aspect_ratio = width / height
    img_width = 600
    img_height = int(img_width / aspect_ratio)
    resized_img = image.resize((img_width, img_height))

    temp_path = os.path.join(tempfile.gettempdir(), "temp_img.png")
    resized_img.save(temp_path)
    return temp_path, resized_img

# Formatação da resposta
def format_res(res):
    res = res.strip().replace("```", "")
    if "</think>" in res:
        res = res.split("</think>")[-1].strip()
    return res

# Prompts e agentes
prompt_analysis = """
Você é um especialista em diagnóstico por imagem.
Analise a imagem e responda em português conforme a estrutura:

### 1. Tipo de imagem e região
### 2. Achados relevantes
### 3. Avaliação diagnóstica
### 4. Explicação em linguagem leiga
"""

med_agent = Agent(
    name="Medical Image Agent",
    role="Especialista em imagens médicas",
    model=Gemini(id=id_model),
    markdown=True,
)

prompt_search_template = """Com base na seguinte análise, realize uma pesquisa médica:
Resultado da análise: "{}"
"""

research_agent = Agent(
    name="Researcher Agent",
    role="Pesquisador médico",
    instructions=dedent(
        """Você busca informações complementares sobre achados da imagem médica.
        Forneça fontes confiáveis (PubMed, WHO, etc.) com links e resumos."""
    ),
    model=Gemini(id=id_model),
    tools=[TavilyTools()],
)

# Pipeline de análise
def process_img_pipeline(agno_img):
    if agno_img is None:
        return "Erro: Nenhuma imagem fornecida."
    res = med_agent.run(prompt_analysis, images=[agno_img])
    analysis = res.content
    prompt_search = prompt_search_template.format(analysis)
    res_search = research_agent.run(prompt_search)
    return f"### 📋 Análise:\n{format_res(analysis)}\n\n---\n\n### 📚 Pesquisa:\n{format_res(res_search.content)}"

# Interface de upload
st.sidebar.header("📁 Enviar imagem")
uploaded_img = st.sidebar.file_uploader("Envie a imagem médica", type=["jpg", "jpeg", "png", "bmp", "gif"])

if uploaded_img is not None:
    st.image(uploaded_img, caption="Imagem enviada", use_container_width=True)

    if st.sidebar.button("🔍 Analisar imagem"):
        with st.spinner("Analisando imagem..."):
            temp_file = os.path.join(tempfile.gettempdir(), uploaded_img.name)
            with open(temp_file, "wb") as f:
                f.write(uploaded_img.getbuffer())

            temp_path, _ = preprocess_img(temp_file)
            agno_img = AgnoImage(filepath=temp_path)
            result = process_img_pipeline(agno_img)
            st.markdown(result, unsafe_allow_html=True)

            # Limpeza segura
            for path in [temp_file, temp_path]:
                try:
                    if os.path.exists(path):
                        os.remove(path)
                except Exception as e:
                    logging.warning(f"Não foi possível remover {path}: {e}")
else:
    st.warning("⚠️ Carregue uma imagem médica para iniciar a análise.")
