@echo off
echo ========================================
echo Iniciando o app de Análise de Imagens Médicas
echo ========================================
cd /d "%~dp0"
if not exist venv (
    echo Criando ambiente virtual...
    python -m venv venv
)
call venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
pause
