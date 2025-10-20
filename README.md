# 🩺 Análise de Imagens Médicas com IA (Gemini + Streamlit + Agno)
Aplicação interativa que utiliza **Modelos Multimodais (M-LLMs)** do Google Gemini para realizar **análises automáticas de imagens médicas** (raio-X, tomografias, ultrassons etc.), oferecendo achados, diagnósticos e referências médicas complementares.
> ⚠️ **Aviso:** Este projeto é para fins educacionais e de demonstração.  
> Nenhum resultado substitui a avaliação de profissionais de saúde qualificados.

## 🚀 Funcionalidades
- Upload e visualização de imagens médicas  
- Pré-processamento automático (Pillow)  
- Análise diagnóstica via **Gemini**  
- Pesquisa médica complementar com **Tavily**  
- Interface intuitiva feita com **Streamlit**  
- Compatível com **Windows, Linux e macOS**

## 🧩 Tecnologias
| Biblioteca | Função |
|-------------|--------|
| **Streamlit** | Interface web |
| **Agno** | Framework para agentes multimodais |
| **Google Gemini API** | Análise de imagem e texto |
| **Tavily API** | Pesquisa de literatura médica |
| **Pillow (PIL)** | Manipulação de imagem |
| **dotenv** | Carregar chaves de API com segurança |

## 🧰 Instalação (Windows)
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/bomcabelo/analise_imagens_medicas.git
cd analise_imagens_medicas
```
### 2️⃣ Criar ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```
### 4️⃣ Configurar variáveis de ambiente
Copie o arquivo `.env.example` e renomeie para `.env`, preenchendo suas chaves:
```env
GOOGLE_API_KEY=AIzaSy...sua_chave...
TAVILY_API_KEY=tvly-...sua_chave...
```
## 💻 Execução
### Método 1 — Manual
```bash
streamlit run app08.py
```
### Método 2 — Automático
Clique duas vezes em **`run.bat`** ou execute:
```bash
setup.bat
```

## 🧪 Teste rápido
1. Envie uma imagem médica (ex: raio-X de tórax).  
2. Clique em **“🔍 Analisar imagem”**.  
3. O app exibirá:  
   - Tipo e qualidade da imagem  
   - Achados relevantes  
   - Diagnóstico e explicação leiga  
   - Referências médicas

## 🧱 Estrutura do projeto
| Arquivo | Descrição |
|----------|------------|
| `app08.py` | Código principal Streamlit |
| `requirements.txt` | Lista de dependências |
| `.env.example` | Modelo de variáveis de ambiente |
| `run.bat` | Executa o app |
| `setup.bat` | Cria ambiente e instala dependências |
| `README.md` | Documentação completa |

## 🧾 Licença
Distribuído sob a licença **MIT**.  
Sinta-se livre para usar, modificar e compartilhar, mantendo a atribuição ao autor.

## 👤 Autor
**Anderson da Silva Rodrigues**  
Analista Judiciário – Tribunal de Justiça do Tocantins  
Pós-graduando em Ciência de Dados – Data Science Academy  
GitHub: [@bomcabelo](https://github.com/bomcabelo)
